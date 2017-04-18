import itertools
import os


def _sanitize(q):
    return q.replace('[', '_').replace(']', '')


def generate(api_items, duplicate_api_items, dupe_info):
    content = ''

    # sort api_items by path alphabetically
    for name in sorted(list(api_items.keys()),
                       key=lambda i: api_items[i]['path']):
        item = api_items[name]

        query = '&'.join('{0}=<arg>'.format(q) for q in item['query_params'])

        if query:
            query = '?' + query

        # We expect to have a method but it is not guaranteed
        if item['method'] is None:
            method = 'MULTIPLE'
        else:
            method = item['method']

        content += '{:<8} {}{}\n'.format(method, item['path'], query)

    return ('listing.txt', content)

