import os
import os.path
import re
import shutil
import sys


def _sanitize(q):
    return q.replace('[', '_').replace(']', '')


def generate(api_items, duplicate_api_items, dupe_info, program=None):
    if api_items['service'] == 'Zendesk':
        program = 'zdesk'
    elif api_items['service'] == 'Terraform Cloud and Enterprise':
        program = 'tfh'

    md_dir  = 'doc'
    cmd_dir = 'cmd'

    if os.path.isdir(md_dir):
        shutil.rmtree(md_dir)

    if os.path.isdir(cmd_dir):
        shutil.rmtree(cmd_dir)

    os.makedirs(md_dir)
    os.makedirs(cmd_dir)

    cmd_items = {}
    for name in list(api_items.keys()):
        cmd_name = ' '.join(api_items[name]['name_parts']).replace('_', '-')
        cmd_items[cmd_name] = api_items[name]
        cmd_items[cmd_name]['name'] = name

    for cmd_name in sorted(list(cmd_items.keys())):
        print(cmd_name)
        item = cmd_items[cmd_name]
        name = item['name']
        fname = '_'.join( [i.replace('_', '-') for i in item['name_parts']] )

        # doc/tfh_admin_user_actions_grant_admin.md
        doc_file = f'{md_dir}/{program}_{fname}.md'

        # tfh admin user_actions_grant_admin
        cmd = item['docfile'].replace('/', ' ')

        if os.path.isfile(doc_file):
            os.unlink(doc_file)

        # Sorting the parameters alphabetically should prevent needless differences
        # when small changes are made in different locations, so the order will be
        # the same regardless as to which parameter is found first.
        item['opt_path_params'].sort()
        item['query_params'].sort()

        doc_content = ''

        path_upper = re.sub('{[-_a-zA-Z0-9]+}',
                            lambda m: m.group(0).upper(), item['path'])

        doc_content += f'## `{program} {cmd_name}`\n\n'
        doc_content += f'{path_upper.replace("/api/v2", "")}\n\n'
        doc_content += f'### Synopsis\n\n'
        doc_content += f'    {program} {cmd_name} [ ... ]\n\n'
        doc_content += f'### REST endpoint\n\n'
        doc_content += f'    {item["method"]} https://{{HOSTNAME}}{path_upper}\n\n'
        doc_content += f'### Description\n\n'
        doc_content += f'{item["docpage"]}\n\n'

        if item['path_params'] or item['opt_path_params']:
            doc_content += '### Positional parameters\n\n'
  
            for p in item['path_params']:
                doc_content += f'* `{p.upper()}`\n\n'

            if item['opt_path']:
                opt_test = ' && '.join([ '[ -n "{}" ]'.format(opt) for opt in item['opt_path_params']])

                for p in item['path_params']:
                    doc_content += '* `{p.upper()}`\n\n'

        if item['query_params']:
            doc_content += '### Options\n\n'

        for q in item['query_params']:
            doc_content += '* `-%s OPTION`\n\n' % _sanitize(q).replace('_', '-')

        md_filename = f'{program}_{fname}.md'
        with open(os.path.join(md_dir, md_filename), 'w') as f:
            f.write(doc_content)

    with open(os.path.join(md_dir, f'{program}.md'), 'w') as f:
        f.write(f'## `{program}`\n\n')
        f.write(f'Command line interface for {api_items["service"]}\n\n')
        f.write( '### Synopsis\n\n')
        f.write(f'    {program} SUBCOMMAND [ ... ]\n\n')
        f.write( '### Description\n\n')

        if 'description' in api_items:
            f.write(api_items['description'])

        if 'options' in api_items:
            f.write(api_items['options'])

    for cmd_name in sorted(list(cmd_items.keys())):
        item = cmd_items[cmd_name]
        name_parts = item['name_parts'][::-1]
        fname = name_parts.pop().replace('_', '-')
        while name_parts:
            md_filename = f'{program}_{fname.replace(" ", "_")}.md'
            fpath = os.path.join('doc', md_filename)
            if not os.path.isfile(fpath):
                with open(fpath, "w") as f:
                    f.write(f'## `{program} {fname}`\n\n')
                    f.write(f'Run {fname} subcommands\n\n')
                    f.write(f'### Synopsis\n\n')
                    f.write(f'    {program} {fname} COMMAND[ ... ]\n\n')
                    f.write(f'')
                    f.write(f'### Description\n\n')
                    f.write(f'Run {fname} subcommands\n\n')

            fname = fname + ' ' + name_parts.pop().replace('_', '-')

    sys.exit()
    #return ('zd.sh', content)
