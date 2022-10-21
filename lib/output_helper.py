import json
import os
import traceback

RUN_ID = None


class OutputHelper():
    def __init__(self, silent=False, verbose=False, debug=False):
        self.flags = {}
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug
        self.output = ''
        self.stream = None
        self.set_stream()

        self.output_directory = '/tmp/iserver/'
        if RUN_ID is not None:
            self.output_directory = os.path.join(self.output_directory, RUN_ID)

        self.default_filename = os.path.join(self.output_directory, 'iserver.output.default')
        self.verbose_filename = os.path.join(self.output_directory, 'iserver.output.verbose')
        self.debug_filename = os.path.join(self.output_directory, 'iserver.output.debug')
        self.json_filename = os.path.join(self.output_directory, 'iserver.output.json')
        self.devel_filename = os.path.join(self.output_directory, 'devel.debug')

    def run_id(self, my_run_id):
        global RUN_ID
        RUN_ID = my_run_id

    def initialize(self, max_dirs=1000):
        try:
            if not os.path.isdir(self.output_directory):
                os.makedirs(self.output_directory, exist_ok=True)

        except BaseException:
            print(traceback.format_exc())

    def is_output(self):
        for filename in [self.default_filename, self.verbose_filename, self.debug_filename]:
            if os.path.isfile(filename):
                return True
        return False

    def json_output(self, output):
        try:
            self.append(self.json_filename, json.dumps(output, indent=4))
        except BaseException:
            pass

    def clean(self):
        try:
            for filename in [self.default_filename, self.verbose_filename, self.debug_filename]:
                if os.path.isfile(filename):
                    os.remove(filename)
        except BaseException:
            pass

    def print(self, output):
        if not self.flags['silent']:
            self.output = '%s\n%s' % (self.output, output)

    def print_stream(self, output, stream):
        if stream == 'output':
            self.print(output)

        if stream == 'debug':
            self.debug(output)

        if stream == 'info':
            self.info(output)

        if stream == 'default':
            self.default(output)

    def set_stream(self):
        if self.flags['silent']:
            self.stream = None
            return

        if self.flags['verbose']:
            self.stream = 'info'
            return

        if self.flags['debug']:
            self.stream = 'debug'
            return

        self.stream = 'default'

    def set_flags(self, silent, verbose, debug):
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug
        self.set_stream()

    def append(self, filename, output):
        try:
            with open(filename, 'a', encoding='utf-8') as file_handler:
                file_handler.write('%s\n' % (output))
        except BaseException:
            pass

    def traceback(self, output):
        ''' Always print '''
        print(output)
        self.append(self.default_filename, output)
        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def error(self, output):
        ''' Always print '''
        output = '[ERROR] %s' % (output)
        print(output)
        self.append(self.default_filename, output)
        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def files_only(self, output):
        self.append(self.default_filename, output)
        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def default(self, output, underline=False):
        ''' Unless silent is set '''
        if underline:
            output = '%s\n%s' % (output, "".join(('-',) * len(output)))

        if not self.flags['silent']:
            print(output)

        self.append(self.default_filename, output)
        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def debug(self, output, underline=False):
        ''' When debug flag set '''
        if underline:
            output = '%s\n%s' % (output, "".join(('-',) * len(output)))

        if not self.flags['silent']:
            if self.flags['debug']:
                print(output)

        self.append(self.debug_filename, output)

    def devel(self, output):
        self.append(self.devel_filename, output)

    def info(self, output, underline=False):
        ''' When verbose flag set '''
        if underline:
            output = '%s\n%s' % (output, "".join(('-',) * len(output)))

        if not self.flags['silent']:
            if self.flags['verbose']:
                print(output)

        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def my_table(self, values, spacing=3, underline=False, order=None, headers=None, headers_upper=False, table=False, stream='default'):
        ''' Expects list of dict '''
        if values is None:
            values = []

        if len(values) == 0:
            if not table:
                return

        # Params fixup
        if table:
            spacing = 1
            underline = False

        if order is None:
            item = values[0]
            display = item.keys()
        else:
            display = order

        # keys holds the column length

        keys = {}
        if headers is None:
            for key in display:
                keys[key] = len(key)
        else:
            for index, value in enumerate(display):
                keys[value] = len(headers[index])

        for value in values:
            for key in keys:
                try:
                    value[key] = str(value[key])
                except BaseException:
                    value[key] = ''

                keys[key] = max(keys[key], len(value[key]))

        if headers is not None:
            index = 0
            for key in keys:
                keys[key] = max(keys[key], len(headers[index]))
                index = index + 1

        for key in keys:
            keys[key] = keys[key] + spacing

        # print header

        if headers is None:
            header = ''
            for key in keys:
                header = '%s%s' % (header, key.capitalize().ljust(keys[key]))
        else:
            header = ''
            if table:
                header = '| '
                table_top = '+-'

            index = 0
            for key in keys:

                column_title = headers[index]
                if headers_upper:
                    column_title = column_title.upper()

                if table:
                    table_top = '%s%s-+-' % (table_top, ''.ljust(keys[key], '-'))
                    header = '%s%s | ' % (header, column_title.ljust(keys[key]))
                else:
                    header = '%s%s' % (header, column_title.ljust(keys[key]))

                index = index + 1

            if table:
                header = header.rstrip(' ')
                table_top = table_top.rstrip('-')

        if table:
            header = '%s\n%s\n%s' % (
                table_top,
                header,
                table_top
            )

        self.print_stream('\n%s' % (header), stream)

        if underline:
            line = ''
            index = 0
            for key in keys:
                if table:
                    line = '%s%s%s | ' % (
                        line,
                        ''.ljust(keys[key] - spacing, '-'),
                        ''.ljust(spacing)
                    )

                else:
                    line = '%s%s%s' % (
                        line,
                        ''.ljust(keys[key] - spacing, '-'),
                        ''.ljust(spacing)
                    )
                index = index + 1

            self.print_stream(line, stream)

        for value in values:
            line = ''
            if table:
                line = '| '

            for key in keys:
                if table:
                    line = '%s%s | ' % (line, value[key].ljust(keys[key]))
                else:
                    line = '%s%s' % (line, value[key].ljust(keys[key]))

            self.print_stream(line, stream)

        if table:
            self.print_stream(table_top, stream)

    def get_dictionary_value(self, dictionary, key):
        my_dictionary = dictionary
        dictionary_value = None
        keys = key.split(':')
        for index, iter_key in enumerate(keys):
            if iter_key not in my_dictionary:
                break

            if index < len(keys) - 1:
                my_dictionary = my_dictionary[iter_key]
                continue

            dictionary_value = my_dictionary[iter_key]

        return dictionary_value

    def dictionary(self, items, exclude=[], title=None, underline=True, prefix=None, keys=None, values=None, title_keys=None, justify=False, newline=[], stream='default', start='\n'):
        header = ''
        if title is not None:
            header = '%s%s' % (start, title)
            if underline:
                header = '%s\n%s' % (header, "".join(('-',) * len(title)))

        body = ''

        # Get longest key
        # note that keys may have : syntax
        if justify:
            longest = 0
            if title_keys is None:
                if keys is None:
                    for i in items:
                        if i not in exclude:
                            longest = max(longest, len(i))
                if keys is not None:
                    for key in keys:
                        longest = max(longest, len(key.split(':')[-1]))

            if title_keys is not None:
                for title_key in title_keys:
                    longest = max(longest, len(title_key))

            longest = longest + 1

        # Print all items
        if keys is None:
            for item in items:
                if item not in exclude:
                    ikey = item
                    if justify:
                        ikey = ikey.ljust(longest)

                    if prefix is not None:
                        body = '%s%s%s: %s\n' % (body, prefix, ikey, items[item])
                    else:
                        body = '%s%s: %s\n' % (body, ikey, items[item])

        # Print selected keys with optional title
        if keys is not None:
            index = 0
            for key in keys:
                if key is not None:
                    ikey = key.split(':')[-1]
                    ivalue = self.get_dictionary_value(items, key)
                if key is None:
                    ikey = None
                    ivalue = values[index]

                if ivalue is not None:
                    if title_keys is not None:
                        ikey = title_keys[index]

                    if justify:
                        ikey = ikey.ljust(longest)

                    if prefix is not None:
                        body = '%s%s%s: %s\n' % (body, prefix, ikey, ivalue)
                    else:
                        body = '%s%s: %s\n' % (body, ikey, ivalue)

                if key in newline:
                    body = '%s\n' % (body)

                index = index + 1

        if stream is not None:
            if len(header) > 0:
                self.print_stream(header, stream)

            if len(body) > 0:
                self.print_stream(body, stream)

        output = '%s\n%s' % (header, body)
        return output

    def columns(self, data, spacing=2, stream='default', max_length=80):
        column_width = []
        column_height = []
        for col in data:
            column_height.append(len(col))
            col_width = 0
            for item in col:
                col_width = max(col_width, len(item))
            column_width.append(col_width)

        rows = []
        row_length = 0
        row = []
        for col_index in list(range(len(data))):
            if row_length > 0:
                if row_length + column_width[col_index] > max_length:
                    rows.append(row)
                    row = []
                    row_length = 0
                else:
                    row.append(
                        dict(
                            data=data[col_index],
                            width=column_width[col_index],
                            height=column_height[col_index]
                        )
                    )
                    row_length = row_length + column_width[col_index]
                    continue

            if row_length == 0:
                row.append(
                    dict(
                        data=data[col_index],
                        width=column_width[col_index],
                        height=column_height[col_index]
                    )
                )
                row_length = column_width[col_index]

        rows.append(row)

        # Fixup column width per row

        for row in rows:
            avg_column_width = int(max_length / len(row))
            for col in row:
                if col['width'] < avg_column_width:
                    col['width'] = avg_column_width - spacing - 1

        # Print out of rows

        for row in rows:
            row_lines = 0
            for col in row:
                row_lines = max(row_lines, col['height'])

            for line_index in list(range(row_lines)):
                line = ''
                for col in row:
                    try:
                        line = '%s%s%s' % (
                            line,
                            col['data'][line_index].ljust(col['width']),
                            ''.ljust(spacing)
                        )
                    except BaseException:
                        line = '%s%s%s' % (
                            line,
                            ''.ljust(col['width']),
                            ''.ljust(spacing)
                        )
                self.print_stream(line, stream)

            self.print_stream('', stream)

    def kubernetes_versions(self, versions, verbose, output):
        if output == 'json':
            self.print(json.dumps(versions, indent=4))
            return
        self.my_table(versions)

    def clusters_name(self, names, prefix=None):
        try:
            if names is None or len(names) == 0:
                self.print('[INFO] No cluster found')
                return

            for name in names:
                if prefix is None:
                    self.print(name)
                else:
                    self.print('%s%s' % (prefix, name))
        except BaseException:
            self.print('[ERROR] Exception')

    def my_logs(self, logs, stream='devel'):
        for log_entry in logs:
            if logs[log_entry] is not None:
                output = '\nLog: %s' % (log_entry)
                output = '%s\n%s\n' % (output, "".join(('-',) * len(output)))

                if stream == 'devel':
                    self.devel(output)
                    self.devel(logs[log_entry])

                if stream == 'default':
                    self.default(output)
                    self.default(logs[log_entry])
