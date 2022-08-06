import os
import os.path
import sys


def _sanitize(q):
    return q.replace('[', '_').replace(']', '')


def generate(program, api_items, duplicate_api_items, dupe_info):
    md_dir = 'doc'

    if not os.path.isdir(md_dir):
        os.makedirs(md_dir)

    # name = admin_user_actions_grant_admin
    for name in sorted(list(api_items.keys())):
        # doc/tfh_admin_user_actions_grant_admin.md
        doc_file = f'{md_dir}/{program}_{name}.md'

        item = api_items[name]

        # tfh admin user_actions_grant_admin
        cmd = item['docfile'].replace('/', ' ')

        if os.path.isfile(doc_file):
            os.unlink(doc_file)

        # Sorting the parameters alphabetically should prevent needless differences
        # when small changes are made in different locations, so the order will be
        # the same regardless as to which parameter is found first.
        item['opt_path_params'].sort()
        item['query_params'].sort()

        content = ''
        doc_content = ''

        content += '# {}\n'.format(item['docpage'])
        content += 'zdesk_%s () {\n' % name.replace(' ', '_')
        content += '  method={}\n'.format(item['method'])

        doc_content += '## `zdesk %s`\n\n' % name.replace('_', '-')
        doc_content += '%s\n\n' % item['path'].replace('/api/v2', '')
        doc_content += '### Synopsis\n\n'
        doc_content += '    zdesk %s [ ... ]\n\n' % name.replace('_', '-')
        doc_content += '### Description\n\n'
        doc_content += '%s\n\n' % item['docpage']

        if item['path_params'] or item['opt_path_params']:
            content += '  url="$(echo "{}" | sed \\\n'.format(item['path'])

            doc_content += '### Positional parameters\n\n'
  
            shifts = "\n"
            for p in item['path_params']:
                content += '    -e "s/{%s}"/"$1"/ \\\n' % p
                shifts += "  shift\n"

                doc_content += '* `%s`\n\n' % p.upper()
                #doc_content_pos += 'some param docs?\n\n'

            content += '  )"'
            content += shifts

            if item['opt_path']:
                opt_test = ' && '.join([ '[ -n "{}" ]'.format(opt) for opt in item['opt_path_params']])
                content += '  if {}; then\n'.format(opt_test)
                content += '    url="$(echo "{}" | sed \\ \n'.format(item['opt_path'])

                shifts = "\n"
                for p in item['path_params']:
                    content += '    -e "{%s}" "$1" \\ \n' % p
                    shifts += "  shift\n"

                    doc_content += '* `%s`\n\n' % p.upper()
                    #doc_content += 'some param docs?\n\n'

                content += '     )"'
                content += shifts
                content += '  fi\n'
        else:
            content += '  url={}\n'.format(item['path'])

        if item['query_params']:
            doc_content += '### Options\n\n'

        for q in item['query_params']:
            content += '  [ -n "$1" ] && query="$query&{}=$1"\n'.format(_sanitize(q))
            content += '  shift\n'

            doc_content += '* `-%s OPTION`\n\n' % _sanitize(q).replace('_', '-')
            #doc_content += 'some option docs?\n\n'


        content += '}'

        with open(os.path.join('cmd', 'zdesk_%s.sh' % name.replace(' ', '_')), 'w') as f:
            f.write(content)

        with open(os.path.join('doc', 'zdesk_%s.md' % name.replace(' ', '_')), 'w') as f:
            f.write(doc_content)

    for name in sorted(list(api_items.keys())):
        name_parts = name.split(' ')[::-1]
        fname = name_parts.pop()
        while name_parts:
            fpath = os.path.join('doc', 'zdesk_' + fname.replace(' ', '_') + '.md')
            if not os.path.isfile(fpath):
                with open(fpath, "w") as f:
                    f.write("## `zdesk %s`\n" % fname.replace('_', '-'))
            fname = fname + ' ' + name_parts.pop()

    sys.exit()
    #return ('zd.sh', content)
