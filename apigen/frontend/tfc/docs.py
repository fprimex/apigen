#!/usr/bin/env python3

import html.parser
import itertools
import os
import inspect
import re
import shutil
import subprocess
import urllib.parse
import sys

from bs4 import BeautifulSoup
import inflection
import requests
import plac

import apigen


api_actions = [
    'admin',
    'apply',
    'cancel',
    'create',
    'destroy',
    'discard',
    'factor',
    'impersonate',
    'lock',
    'show',
    'unimpersonate',
    'unlock',
    'update',
    'upload',
    ]

api_url = 'https://www.terraform.io/cloud-docs/api-docs'

categories = {
    'admin': 'admin',
    'private_registry': 'private-registry',
}

skippages = [
    'changelog',
    'stability-policy',
    'admin',
    'policy-sets',
]

skipfiles = [
]


def get_docs(apidocs):
    html_parser = html.parser.HTMLParser()

    if os.path.isdir(apidocs):
        shutil.rmtree(apidocs)

    apidocs_orig = os.path.abspath(f'{apidocs}_orig')

    if not os.path.isdir(apidocs_orig):
        os.makedirs(apidocs_orig)

    os.chdir(apidocs_orig)

    req = requests.get(api_url)
    content = req.content
    soup = BeautifulSoup(content, "html.parser")
    docs = set([dl['href'].removeprefix('/cloud-docs/api-docs/').removesuffix('/')
                   for dl in soup('a', href=re.compile('^/cloud-docs/api-docs/[^_][^#]+$'))])

    docs_list = []
    for link in sorted(list(docs)):
        categories = os.path.dirname(link)
        if categories:
            if not os.path.isdir(categories):
                os.makedirs(categories)

        if link in skippages:
            continue

        docs_list.append(link)
        if os.path.isfile(link):
            print(f'{link} already present')
            continue


        req = requests.get(api_url + '/' + link)
        text = BeautifulSoup(req.content, "html.parser")

        pretty_text = text.prettify()
        if not pretty_text:
            # In the case of prettify killing the whole page
            pretty_text = text
        pretty = (pretty_text)

        print(link)
        with open(link, 'w', encoding="utf-8") as fout:
            fout.write(pretty)

    os.chdir('..')

    shutil.copytree(apidocs_orig, apidocs)

    return docs_list


def parse_docs(apidocs, doc_files):

    def code_pre_docanchor(tag):
        class_ = tag.attrs.get('class', ())
        return tag.name == 'code' or tag.name == 'pre' or tag.name == 'a'

    os.chdir(apidocs)

    api_items = {}
    duplicate_api_items = {}

    last_doc_anchor = ''
    for doc_file in doc_files:
        if '.orig' in doc_file or '.swp' in doc_file or doc_file in skipfiles:
            continue

        print(doc_file)
        with open(doc_file) as doc:
            soup = BeautifulSoup(doc, "html.parser")

        items = soup.find_all(code_pre_docanchor)
        for tag in items:
            if tag.name == 'a' and 'href' in tag:
                last_doc_anchor = tag['href']
                continue

            text = tag.get_text()
            match = re.match(
                r'\s*(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) (.*)', text)
            if match:
                cat = os.path.basename(doc_file.split('_')[0])
                page = doc_file.replace(cat + '_', '')
                docpage = api_url + '/' + page

                is_singular = False
                api_item = {}
                api_item['docfile'] = doc_file
                api_item['docpage'] = docpage + last_doc_anchor
                api_item['path_params'] = []
                api_item['opt_path_params'] = []
                api_item['opt_path'] = ''
                api_item['query_params'] = []

                api_item['method'] = match.group(1)
                path = match.group(2)

                if 'archivist' in path:
                    continue

                # parse into a url object for easily accessing the parts of the url
                url = urllib.parse.urlsplit(path)

                api_item['path'] = url.path

                # Split the path and remove the first (always empty) item and
                # /api/v2 or /api/services
                param_indexes = []
                path_parts = url.path.split('/')

                if path_parts[-1].startswith(':') or api_item['method'] == 'POST':
                    # Getting a single object
                    # e.g. GET /api/v2/tickets/{id}.json
                    is_singular = True

                if path_parts[0] == '':
                    del path_parts[0]

                make_next_singular = False
                path_parts.reverse()
                for i, path_part in enumerate(path_parts):
                    part, ext = os.path.splitext(path_part)
                    path_parts[i] = part

                    if part.startswith(':'):
                        api_item['path'] = api_item['path'].replace(part, '{' + part[1:] + '}')
                        api_item['path_params'].append(part[1:])
                        param_indexes.append(i)
                        make_next_singular = True
                        continue

                    if make_next_singular:
                        make_next_singular = False
                        path_parts[i] = inflection.singularize(path_parts[i])

                path_len = len(path_parts)

                for i in param_indexes[::-1]:
                    del path_parts[i]

                expanded_parts = []
                [expanded_parts.extend(part.split('_')) for part in path_parts]
                has_action = True in [
                    action in expanded_parts for action in api_actions]

                query_params = urllib.parse.parse_qsl(url.query)
                for query_items in query_params:
                    api_item['query_params'].append(query_items[0])

                path_parts.reverse()
                name = '_'.join(path_parts)
                if is_singular:
                    name = inflection.singularize(name)

                if not has_action:
                    if api_item['method'] == 'DELETE':
                        name = name + '_delete'
                    elif api_item['method'] == 'PUT':
                        name = name + '_update'
                    elif api_item['method'] == 'POST':
                        name = name + '_create'
                    elif api_item['method'] == 'GET' and is_singular:
                        name = name + '_show'
                    elif (
                            api_item['method'] == 'GET' and
                            (len(api_item['path_params']) == 0 or
                             len(api_item['path_params']) == 1)
                        ):
                        name = name + '_list'

                api_item['path_params'].reverse()
                api_item['query_params'].reverse()

                if '-' in name:
                  continue

                if name in api_items:
                    if name not in duplicate_api_items:
                        duplicate_api_items[name] = []
                    duplicate_api_items[name].append(api_item)
                    continue

                print(f'  {name}')
                api_items[name] = api_item

                continue

    should_keep = resolve_duplicates(api_items, duplicate_api_items)

    os.chdir('..')
    return api_items, duplicate_api_items, should_keep

def resolve_duplicates(api_items, duplicate_api_items):
    dupe_info = ''
    names = list(duplicate_api_items.keys())
    names.sort()

    for name in names:
        for dupe in duplicate_api_items[name]:
            item = api_items[name]

            same_path = dupe['path'] == item['path']
            same_method = dupe['method'] == item['method']
            same_path_params = False not in [i == j for i, j in
                    itertools.zip_longest(dupe['path_params'],
                            item['path_params'])]
            same_query_params = False not in [i == j for i, j in
                    itertools.zip_longest(
                    sorted(dupe['query_params']),
                    sorted(item['query_params']))]

            if (same_path and same_method and
                same_path_params and same_query_params):
                # Everything is the same, so discard this duplicate
                dupe_info += \
                    "    # Duplicate API endpoint discarded:\n"\
                    "    # {} from\n"\
                    "    # {}\n\n".format(
                        name, dupe['docpage'])

            elif same_path and same_path_params and same_query_params:
                # Only the method differs, so indicate that method is ambiguous
                item['method'] = None

            elif same_path and same_method and same_path_params:
                # Only the query parameters differ, so we combine
                # the query parameters.
                item['query_params'] = list(
                    set(item['query_params'].copy() +
                        dupe['query_params']))

            elif same_method and not (same_path_params and same_path):
                # The path or path parameters differ, so we either do not have
                # a dupe, or have optional or ambiguous arguments. There may be
                # query parameter differences, which will all be consolidated
                # as optional parameters.

                # Common parameters are all required
                required = set(dupe['path_params']) & set(item['path_params'])

                # Optional parameters are only in one endpoint
                optional = list((
                    set(dupe['path_params']) | set(item['path_params'])) -
                    required)

                if (len(set(item['path_params']) - required) == 0 and
                        len(optional) > 0):
                    # The item is the base function and the dupe has the optional
                    # arguments. Just need to add the optional arguments
                    item['opt_path_params'] = optional
                    item['opt_path'] = dupe['path']

                    # Consolidate query parameters between the two
                    item['query_params'] = list(
                        set(item['query_params'].copy() +
                            dupe['query_params']))

                elif (len(set(dupe['path_params']) - required) == 0 and
                        len(optional) > 0):
                    # The dupe is the base function and the item has the
                    # optional arguments. Need to swap the dupe with the
                    # item and then add the optional arguments

                    # Consolidate query parameters between the two
                    dupe['query_params'] = list(
                        set(dupe['query_params'].copy() +
                            item['query_params']))

                    # Now swap
                    item_path = item['path']
                    api_items[name] = dupe
                    api_items[name]['opt_path_params'] = optional
                    api_items[name]['opt_path'] = item_path
                else:
                    # this is ambiguous. If the parameters are in the same place,
                    # then they're actually interchangeable, and we just need a
                    # better name for them.
                    handled = False
                    new_path = ''
                    new_path_params = []

                    # compare each of the path parts to see specifically what is
                    # different.
                    for i, j in itertools.zip_longest(
                            item['path'].split('/'), dupe['path'].split('/')):
                        if i == j:
                            # everything is the same up to here. keep building a
                            # new, common path.
                            if i:
                                new_path += '/' + i
                        else:
                            # the paths are different. look at how they are
                            # different.
                            ipart, iext = os.path.splitext(i)
                            jpart, jext = os.path.splitext(j)
                            if ipart == jpart and iext != jext:
                                # These are legit dupes that only differ by
                                # the extension at the end.
                                dupe_info += \
                                    "    # Duplicate API endpoint differs "\
                                    "only by extension:\n"\
                                    "    # {} from\n"\
                                    "    # {}\n\n".format(
                                        name, dupe['docpage'])
                                handled = True

                            elif (ipart.startswith('{') and jpart.startswith('{') and
                                    iext != jext):
                                # The parameters are different, but in the same
                                # place and have a different extension. So this
                                # actually needs a new method.
                                # e.g. /thing/{id} vs /thing/{name}.json
                                ihandled = False
                                jhandled = False

                                new_name = name + '_by_' + ipart.strip('{}')
                                if new_name not in api_items:
                                    api_items[new_name] = item
                                    del api_items[name]
                                    ihandled = True

                                new_name = name + '_by_' + jpart.strip('{}')
                                if new_name not in api_items:
                                    api_items[new_name] = dupe
                                    jhandled = True

                                handled = ihandled and jhandled

                            elif (ipart.startswith('{') and jpart.startswith('{') and
                                    iext == jext):
                                # The parameters are in the same place and have the
                                # same extension. Combine these parameters as they
                                # are basically interchangeable.
                                # e.g. /thing/{id} vs /thing/{name} becomes
                                #      /thing/{id_or_name}
                                new_param = i.strip('{}' + iext) \
                                    + '_or_' + j.strip('{}' + jext)
                                new_path_params.append(new_param)
                                new_path += '/{' + new_param + '}' + iext
                                item['path'] = new_path
                                item['path_params'] = new_path_params
                                handled = True

                                # Consolidate query parameters between the two
                                item['query_params'] = list(
                                    set(item['query_params'].copy() +
                                        dupe['query_params']))

                            elif ipart != jpart:
                                # This is not actually a dupe. The generated
                                # names of these two methods are the same, but
                                # actually point to two different paths. The
                                # names need to be differentiated.

                                # The shorter path will become the 'fixed' one
                                # by adding the prefix of the docpage. E.g.
                                # core_, hc_, nps_
                                if len(item['path']) > len(dupe['path']):
                                    fixed_name = dupe['docfile'].split('_')[0] + "_" + name
                                    api_items[fixed_name] = dupe.copy()
                                else:
                                    fixed_name = item['docfile'].split('_')[0] + "_" + name
                                    api_items[fixed_name] = item.copy()
                                    api_items[name] = dupe.copy()

                                handled = True
                                break

                    if not handled:
                        dupe_info += \
                            "    # Duplicate ambiguous API endpoint:\n"\
                            "    # {} from\n"\
                            "    # {}\n\n".format(name, dupe['docpage'])

            else:
                dupe_info += "\n"
                dupe_info += \
                    "    # Duplicate API endpoint that differs:\n"\
                    "    #  {} from\n"\
                    "    #  {}\n".format(name, dupe['docpage'])
                dupe_info += \
                    "    # Original definition located here:\n"\
                    "    #  {} from\n"\
                    "    #  {}\n".format(name, item['docpage'])
                dupe_info += '    # {}\n'.format(name)
                dupe_info += '    #    Path: {}\n'.format(dupe['path'])
                dupe_info += '    #    Method: {}\n'.format(dupe['method'])
                dupe_info += '    #    Parameters:\n'
                for param in dupe['path_params']:
                    dupe_info += '    #        {}\n'.format(param)
                dupe_info += '    #    Query Parameters:\n'
                for param in dupe['query_params']:
                    dupe_info += '    #        {}\n'.format(param)
                dupe_info += '    # Original definition:\n'
                dupe_info += '    #    Path: {}\n'.format(item['path'])
                dupe_info += '    #    Method: {}\n'.format(item['method'])
                dupe_info += '    #    Parameters:\n'
                for param in item['path_params']:
                    dupe_info += '    #        {}\n'.format(param)
                dupe_info += '    #    Query Parameters:\n'
                for param in item['query_params']:
                    dupe_info += '    #        {}\n'.format(param)
                dupe_info += "\n"

    if dupe_info:
        return dupe_info

