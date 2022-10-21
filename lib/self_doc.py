import json
import os
import sys
import traceback

# https://click.palletsprojects.com/en/8.1.x/


def get_template(template_filename, template_directory):
    filename = os.path.join(template_directory, template_filename)
    try:
        with open(filename, 'r', encoding='utf-8') as file_handler:
            content = file_handler.read()
        return content
    except BaseException:
        print('Test read failed: %s' % (filename))
        print(traceback.format_exc())
        sys.exit(1)


def get_keywords(template):
    keywords = []
    for line in template.split('\n'):
        if line.startswith('DOC_TEMPLATE:'):
            keywords.append(
                dict(
                    result=line.split(':')[1],
                    filename=line.split(':')[2]
                )
            )
    return keywords


def get_template_names():
    templates = []
    templates_directory = './doc/templates'
    for template_filename in os.listdir(templates_directory):
        templates.append(template_filename)
    return templates


def match_templates(results):
    templates = []
    templates_directory = './doc/templates'
    for template_filename in os.listdir(templates_directory):
        print('Checking template: %s' % (template_filename))
        template = get_template(template_filename, templates_directory)
        keywords = get_keywords(template)
        if len(keywords) == 0:
            print('- MATCH (no keywords)')
            templates.append(
                dict(
                    filename=template_filename,
                    template=template,
                    keywords=keywords
                )
            )
        if len(keywords) > 0:
            match = True
            for k in keywords:
                if k['result'] not in results:
                    print('- NOK %s' % (k['result']))
                    match = False
                else:
                    print('- OK %s' % (k['result']))

            if match:
                print('- MATCH')
                templates.append(
                    dict(
                        filename=template_filename,
                        template=template,
                        keywords=keywords
                    )
                )

    return templates


def replace_keywords(template, results_directory):
    new_content = ''
    for line in template['template'].split('\n'):
        if line.startswith('DOC_TEMPLATE:'):
            result_dir = line.split(':')[1]
            result_filename = line.split(':')[2]

            filename = os.path.join(results_directory, result_dir)
            filename = os.path.join(filename, 'result')
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

            command = '# %s' % (content['command'])
            command = command.replace('python3 iserver.py', 'iserver')
            command = command.replace('python.exe .\\iserver.py', 'iserver')
            if '--help' not in command:
                command = command.replace(' --', '\n    --')
            new_content = '%s\n%s' % (new_content, command)

            filename = os.path.join(results_directory, result_dir)
            filename = os.path.join(filename, result_filename)
            try:
                with open(filename, 'r', encoding='utf8', errors='ignore') as file_handler:
                    content = file_handler.read()
                    content = content.encode("ascii", "ignore")
                    content = content.decode()
            except BaseException:
                print('Failed to read file: %s' % (filename))
                print(traceback.format_exc())
                sys.exit(1)

            content = content.lstrip('\n')
            content = content.rstrip('\n')
            new_content = '%s\n%s' % (new_content, content)
        else:
            if new_content == '':
                new_content = line
            else:
                new_content = '%s\n%s' % (new_content, line)

    return new_content


def generate_docs(directory, verbose, dry_run):
    """Run test"""

    if not os.path.isdir(directory):
        print('Directory not found: %s' % (directory))
        sys.exit(1)

    results = []
    for result_directory in os.listdir(directory):
        directory_name = os.path.join(directory, result_directory)
        result_filename = os.path.join(directory_name, 'result')
        if os.path.isfile(result_filename):
            try:
                with open(result_filename, 'r', encoding='utf-8') as file_handler:
                    content = json.loads(file_handler.read())

                if content['success']:
                    results.append(result_directory)
            except BaseException:
                print('[WARNING] Failed to open result file: %s' % (result_filename))
    results = sorted(results)
    all_templates = get_template_names()

    # Example: ['scale_cp_help.help', 'scale_cp_negative.wrong_cluster_name', 'scale_cp_up.dryrun', 'scale_cp_up.run', 'scale_cp_down.dryrun']
    templates = match_templates(results)
    templates = sorted(templates, key=lambda i: i['filename'])

    print('\nMatching Templates:')
    for template in templates:
        print('- %s' % (template['filename']))

        new_content = replace_keywords(template, directory)
        doc_filename = os.path.join('./doc/features', template['filename'])
        with open(doc_filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(str(new_content))

    if len(templates) < len(all_templates):
        print('\nFailed Templates:')
        for all_template in all_templates:
            found = False
            for template in templates:
                if template['filename'] == all_template:
                    found = True
                    break

            if not found:
                print('- %s' % (all_template))

    print('\nSummary')
    print('All templates: %s' % (len(all_templates)))
    print('Matching templates: %s' % (len(templates)))
