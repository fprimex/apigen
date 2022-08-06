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

from apigen import resolve_duplicates


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

        # workspaces
        # admin/users
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
                is_singular = False
                api_item = {}
                api_item['docfile'] = doc_file
                api_item['docpage'] = api_url + '/' + doc_file + last_doc_anchor
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
                    # GET  /admin/workspaces/:id
                    # POST /admin/users/:id/actions/unsuspend
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

                for i in param_indexes[::-1]:
                    del path_parts[i]

                expanded_parts = []
                for part in path_parts:
                    expanded_parts.extend(part.split('_'))

                has_action = True in [action in expanded_parts for action in api_actions]

                query_params = urllib.parse.parse_qsl(url.query)
                for query_items in query_params:
                    api_item['query_params'].append(query_items[0])

                path_parts.reverse()
                cmd = ' '.join(path_parts)
                api_item['cmd'] = cmd
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

                if name in api_items:
                    if name not in duplicate_api_items:
                        duplicate_api_items[name] = []
                    duplicate_api_items[name].append(api_item)
                    continue

                print(f'  {name}')
                api_items[name] = api_item

    should_keep = resolve_duplicates(api_items, duplicate_api_items)

    os.chdir('..')
    return api_items, duplicate_api_items, should_keep

