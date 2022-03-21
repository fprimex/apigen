import itertools


def _sanitize(q):
    return q.replace('[', '_').replace(']', '')


def generate(api_items, duplicate_api_items, dupe_info):
    content = ''

    if dupe_info:
        content += dupe_info 

    for name in sorted(list(api_items.keys())):
        item = api_items[name]

        # Sorting the parameters alphabetically should prevent needless differences
        # when small changes are made in different locations, so the order will be
        # the same regardless as to which parameter is found first.
        item['opt_path_params'].sort()
        item['query_params'].sort()

        path_fmt_args = ', '.join([p + '=' + p for p in item['path_params']])

        argspec = ', '.join(item['path_params'])

        if item['method']:
            if item['method'] in ['POST', 'PUT']:
                if argspec:
                    argspec += ', '
                argspec += 'data'
        else:
            if argspec:
                argspec = 'method, ' + argspec + ', data=None'
            else:
                argspec = 'method, data=None'

        if item['opt_path_params']:
            if argspec:
                argspec += ', '
            argspec += '=None, '.join(item['opt_path_params']) + '=None'

        if item['query_params']:
            if argspec:
                argspec += ', '
            argspec += '=None, '.join(
                [_sanitize(q) for q in item['query_params']]) + '=None'

        if argspec:
            argspec += ', '
        argspec += '**kwargs'

        content += '    def {}(self, {}):\n'.format(name, argspec)
        content += '        "{}"\n'.format(item['docpage'])
        content += '        api_path = "{}"\n'.format(item['path'])

        if item['path_params']:
            content += '        api_path = api_path.format({})\n'.format(
                path_fmt_args)

        if item['opt_path']:
            opt_test = ' and '.join(item['opt_path_params'])
            if path_fmt_args:
                path_fmt_args += ', '
            path_fmt_args = path_fmt_args + \
                ', '.join([p + '=' + p for p in item['opt_path_params']])
            content += '        if {}:\n'.format(opt_test)
            content += '            api_opt_path = "{}"\n'.format(item['opt_path'])
            content += '            api_path = api_opt_path.format({})\n'.format(
                path_fmt_args)

        if item['query_params']:
            content += '        api_query = {}\n'
            content += '        if "query" in kwargs.keys():\n'
            content += '            api_query.update(kwargs["query"])\n'
            content += '            del kwargs["query"]\n'

        for q in item['query_params']:
            content += '        if {}:\n'.format(_sanitize(q))
            content += '            api_query.update({\n'
            content += '                "{}": {},\n'.format(q, _sanitize(q))
            content += '            })\n'

        content += '        return self.call(api_path'

        if item['query_params']:
            content += ', query=api_query'

        if item['method']:
            if item['method'] != 'GET':
                content += ', method="{}"'.format(item['method'])

            if item['method'] in ['POST', 'PUT']:
                content += ', data=data'
        else:
            content += ', method=method, data=data'

        content += ', **kwargs)\n\n'

    return ('zdesk_api.py', content)

