import itertools
import re

FUNC_TPL = 'func (c *Client) {0}(i *{0}Input, ro *RequestOptions) ([]byte, error) {{\n'

NOINPUT_FUNC_TPL = 'func (c *Client) {0}(ro *RequestOptions) ([]byte, error) {{\n'

CHECK_TPL = """\tif i.{0} == "" {{
\t\treturn nil, errors.New("Missing required field '{0}'")
\t}}

"""

FUNC_BODY_TPL = """\tresp, err := c.Request("{}", path, ro)
\treturn handle(resp, ro, err)
}}
"""

def _sanitize(q):
    return q.replace('[', '_').replace(']', '')

def hump(w):
    acronyms = ('id')
    humped = []
    for l in w.split('_'):
        if l in acronyms:
            humped.append(l.upper() or '_')
        else:
            humped.append(l.capitalize() or '_')
    return ''.join(humped)

def generate(api_items, duplicate_api_items, dupe_info):
    content = ''

    for name in sorted(list(api_items.keys())):
        item = api_items[name]

        if not item['method']:
            print("Method for endpoint {} is required for Go backend. Skipping".format(
                    name))
            continue

        # Sorting the parameters alphabetically should prevent needless
        # differences when small changes are made in different locations, so
        # the order will be the same regardless as to which parameter is found
        # first.
        item['opt_path_params'].sort()

        camel_name = hump(name)
        camel_params = [hump(p) for p in item['path_params']]
        camel_opt_params = [hump(p) for p in item['opt_path_params']]

        if camel_params or camel_opt_params:
            content += 'type {}Input struct {{\n'.format(camel_name)

            for p in camel_params:
                content += '{} string\n'.format(p)

            for p in camel_opt_params:
                content += '{} string\n'.format(p)

            content += '}\n\n'

            content += FUNC_TPL.format(camel_name)
        else:
            content += NOINPUT_FUNC_TPL.format(camel_name)

        for p in camel_params:
           content += CHECK_TPL.format(p)

        if item['path_params']:
            input_params = 'i.'
        else:
            input_params = ''

        input_params += ', i.'.join(camel_params)
        api_path = '"{}"'.format(re.sub(r'{[a-z_]*}', '%s', item['path']))


        if item['path_params']:
            content += '\tapi_path := {}\n'.format(api_path)
            content += "\tpath := fmt.Sprintf(api_path, {})\n".format(input_params)
        else:
            content += '\tpath := {}\n'.format(api_path)

        if item['opt_path']:
            opt_test = ' '.join(['i.{} != ""'.format(p) for p in camel_opt_params])
            #opt_test = 'i.{} != nil'.format(camel_opt_params.pop())
            #opt_test = opt_test + ' != nil && i.'.join(camel_opt_params)
            input_params = ', '.join(['i.{}'.format(p) for p in camel_opt_params])
            content += '\tif {} {{\n'.format(opt_test)
            content += '\t\tapi_opt_path := "{}"\n'.format(item['opt_path'])
            content += "\t\tpath = fmt.Sprintf(api_opt_path, {})\n".format(input_params)
            content += '}\n'

        content += FUNC_BODY_TPL.format(item['method'])

    return ('zdesk_api.go', content)

