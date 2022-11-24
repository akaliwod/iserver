#!usr/bin/env python

# Copyright (c) Cisco Systems Inc. 2022
# Author Arkadiusz Kaliwoda <akaliwod@cisco.com>

import datetime
import os
import json
import shutil
import traceback

from lib import output_helper
from lib import ssh

RUN_ID = None


class Log():
    def __init__(self):
        self.logs_directory = '/tmp/iserver'

        if RUN_ID is not None:
            self.logs_directory = os.path.join(self.logs_directory, RUN_ID)

        self.command_filename = os.path.join(self.logs_directory, 'command')
        self.error_filename = os.path.join(self.logs_directory, 'iserver.error')
        self.info_filename = os.path.join(self.logs_directory, 'iserver.info')
        self.debug_filename = os.path.join(self.logs_directory, 'iserver.debug')
        self.isctl_filename = os.path.join(self.logs_directory, 'isctl.debug')
        self.api_filename = os.path.join(self.logs_directory, 'api.debug')
        self.redfish_filename = os.path.join(self.logs_directory, 'redfish.debug')
        self.odata_filename = os.path.join(self.logs_directory, 'odata.debug')
        self.ssh_filename = os.path.join(self.logs_directory, 'ssh.debug')
        self.devel_filename = os.path.join(self.logs_directory, 'devel.debug')
        self.lcm_report_filename = os.path.join(self.logs_directory, 'lcm.report')

        self.mapping = {}
        self.mapping['command'] = self.command_filename
        self.mapping['error'] = self.error_filename
        self.mapping['info'] = self.info_filename
        self.mapping['debug'] = self.debug_filename
        self.mapping['isctl'] = self.isctl_filename
        self.mapping['api'] = self.api_filename
        self.mapping['odata'] = self.odata_filename
        self.mapping['redfish'] = self.redfish_filename
        self.mapping['ssh'] = self.ssh_filename

    def run_id(self, my_run_id):
        global RUN_ID
        RUN_ID = my_run_id

    def initialize(self, max_dirs=1000):
        try:
            if not os.path.isdir(self.logs_directory):
                os.makedirs(self.logs_directory, exist_ok=True)

            my_dirs = []
            for name in os.listdir(self.logs_directory):
                directory = os.path.join(self.logs_directory, name)
                if os.path.isdir(directory):
                    my_dirs.append(
                        dict(
                            directory=directory,
                            create_time=int(os.path.getmtime(directory))
                        )
                    )

            if len(my_dirs) > max_dirs:
                my_dirs = sorted(my_dirs, key=lambda i: i['create_time'])
                my_max = len(my_dirs) - max_dirs
                for index in range(0, my_max):
                    directory = my_dirs[index]['directory']
                    if directory.startswith(self.logs_directory):
                        shutil.rmtree(directory)

        except BaseException:
            print(traceback.format_exc())

    def clean(self):
        if RUN_ID is not None:
            shutil.rmtree(self.logs_directory)

    def analyze_isctl(self):
        result = {}
        result['read'] = False
        result['calls'] = 0
        result['success'] = 0
        result['failed'] = 0
        result['total_time'] = 0

        content = self.get_file(self.isctl_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                result['calls'] = result['calls'] + 1
                (when, success, duration, count, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

        return result

    def analyze_redfish(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['connect'] = 0
        result['disconnect'] = 0
        result['path'] = 0
        result['connect_time'] = 0
        result['disconnect_time'] = 0
        result['path_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.redfish_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                (when, success, duration, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                if command == 'connect':
                    result['connect'] = result['connect'] + 1
                    result['connect_time'] = result['connect_time'] + int(duration)

                if command == 'disconnect':
                    result['disconnect'] = result['disconnect'] + 1
                    result['disconnect_time'] = result['disconnect_time'] + int(duration)

                if command not in ['connect', 'disconnect']:
                    result['path'] = result['path'] + 1
                    result['path_time'] = result['path_time'] + int(duration)

                result['total_time'] = result['total_time'] + int(duration)

        return result

    def analyze_ssh(self):
        result = {}
        result['read'] = False
        result['calls'] = 0
        result['total_time'] = 0

        content = self.get_file(self.ssh_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                result['calls'] = result['calls'] + 1
                (when, success, duration, ip_address, command) = line.split('\t')
                result['total_time'] = result['total_time'] + int(duration)

        return result

    def analyze_log(self, filename):
        result = {}
        result['read'] = False
        result['lines'] = 0

        content = self.get_file(filename)
        if content is None:
            return result

        result['read'] = True
        result['lines'] = len(content.split('\n'))
        return result

    def analyze(self, duration):
        result = {}
        result['duration'] = duration
        result['isctl'] = self.analyze_isctl()
        result['redfish'] = self.analyze_redfish()
        result['ssh'] = self.analyze_ssh()
        result['error'] = self.analyze_log(self.error_filename)
        result['info'] = self.analyze_log(self.info_filename)
        result['debug'] = self.analyze_log(self.debug_filename)

        return result

    def get_file(self, filename):
        if os.path.isfile(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as file_handler:
                    return file_handler.read()
            except BaseException:
                pass
        return None

    def get_logs(self, files=None):
        if files is None:
            files = ['debug', 'info', 'error', 'isctl', 'ssh', 'redfish']

        content = {}
        for filename in files:
            if filename in self.mapping:
                content[filename] = self.get_file(self.mapping[filename])

        return content

    def ssh(self, ip_address, cmd, success, duration):
        try:
            current_time = datetime.datetime.now()
            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time, success, duration, ip_address, cmd)
            with open(self.ssh_filename, 'a', encoding='utf-8') as file_handler:
                file_handler.write(msg)

        except BaseException:
            print(traceback.format_exc())

    def redfish(self, command, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command
            )

            with open(self.redfish_filename, 'a', encoding='utf-8') as file_handler:
                file_handler.write(msg)

        except BaseException:
            print(traceback.format_exc())

    def get_api(self):
        content = self.get_file(self.api_filename)
        if content is None:
            return {}
        return json.loads(content)

    def api(self, command, content):
        try:
            apis = self.get_api()
            apis[command] = content
            with open(self.api_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(apis, indent=4))

        except BaseException:
            print(traceback.format_exc())

    def get_odata(self):
        content = self.get_file(self.odata_filename)
        if content is None:
            return {}
        return json.loads(content)

    def odata(self, path, content):
        try:
            odatas = self.get_odata()
            odatas[path] = content
            with open(self.odata_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(odatas, indent=4))

        except BaseException:
            print(traceback.format_exc())

    def cli(self, command, success, duration, item_count=None):
        try:
            current_time = datetime.datetime.now()

            count = '-'
            if item_count is not None:
                count = int(item_count)

            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                count,
                command
            )

            with open(self.isctl_filename, 'a', encoding='utf-8') as file_handler:
                file_handler.write(msg)

        except BaseException:
            print(traceback.format_exc())

    def error(self, location, message):
        try:
            current_time = datetime.datetime.now()
            msg = "[%s]\t[%s]\t%s\n" % (
                current_time, location, message)
            with open(self.error_filename, 'a', encoding='utf-8') as file_handler:
                file_handler.write(msg)

            self.info(location, message)

        except BaseException:
            print(traceback.format_exc())

    def info(self, location, message):
        try:
            current_time = datetime.datetime.now()
            msg = "[%s]\t[%s]\t%s\n" % (
                current_time, location, message)
            with open(self.info_filename, 'a', encoding='utf-8') as file_handler:
                file_handler.write(msg)

            self.debug(location, message)

        except BaseException:
            print(traceback.format_exc())

    def debug(self, location, message):
        try:
            current_time = datetime.datetime.now()
            msg = "[%s]\t[%s]\t%s\n" % (
                current_time, location, message)
            with open(self.debug_filename, 'a', encoding='utf-8') as file_handler:
                file_handler.write(msg)

        except BaseException:
            print(traceback.format_exc())

    def get_lcm_report(self):
        if os.path.isfile(self.lcm_report_filename):
            try:
                with open(self.lcm_report_filename, 'r', encoding='utf-8') as file_handler:
                    return json.loads(file_handler.read())

            except BaseException:
                print(traceback.format_exc())

        return None

    def set_lcm_report(self, report):
        try:
            with open(self.lcm_report_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(report, indent=4))

        except BaseException:
            print(traceback.format_exc())
            return False

        return True

    def set_command(self, command):
        try:
            with open(self.command_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(command)
        except BaseException:
            print(traceback.format_exc())

    def get_command(self):
        try:
            if os.path.isfile(self.command_filename):
                with open(self.command_filename, 'r', encoding='utf-8') as file_handler:
                    return file_handler.read()

        except BaseException:
            print(traceback.format_exc())

        return None

    def show_last_logs(self):
        my_dirs = []
        logs_directory = os.path.dirname(self.logs_directory)
        for name in os.listdir(logs_directory):
            directory = os.path.join(logs_directory, name)
            if os.path.isdir(directory):
                directory_info = {}
                directory_info['name'] = name
                directory_info['directory'] = directory
                directory_info['create_time'] = int(os.path.getmtime(directory))
                directory_info['time'] = datetime.datetime.fromtimestamp(directory_info['create_time']).strftime('%Y-%m-%d %H:%M:%S')

                command_filename = os.path.join(directory, 'command')
                command = self.get_file(command_filename)
                if command is not None:
                    directory_info['command'] = command
                    my_dirs.append(directory_info)

        my_dirs = sorted(my_dirs, key=lambda i: i['create_time'], reverse=True)

        my_output = output_helper.OutputHelper()
        my_output.my_table(
            my_dirs,
            order=['name', 'command', 'directory', 'time'],
            headers=['Name', 'Command', 'Directory', 'Time']
        )

    def get_command_directory(self, search_command):
        my_dirs = []
        logs_directory = os.path.dirname(self.logs_directory)
        for name in os.listdir(logs_directory):
            directory = os.path.join(logs_directory, name)
            if os.path.isdir(directory):
                directory_info = {}
                directory_info['name'] = name
                directory_info['directory'] = directory
                directory_info['create_time'] = int(os.path.getmtime(directory))
                directory_info['time'] = datetime.datetime.fromtimestamp(directory_info['create_time']).strftime('%Y-%m-%d %H:%M:%S')

                command_filename = os.path.join(directory, 'command')
                command = self.get_file(command_filename)
                if command is not None:
                    directory_info['command'] = command
                    my_dirs.append(directory_info)

        my_dirs = sorted(my_dirs, key=lambda i: i['create_time'], reverse=True)

        for my_dir in my_dirs:
            if my_dir['command'] == search_command:
                return my_dir['directory']

        if '"' in search_command:
            search_command = search_command.replace('"', '')
            for my_dir in my_dirs:
                if my_dir['command'] == search_command:
                    return my_dir['directory']

        return None

    def bug_report(self, name):
        logs_directory = os.path.dirname(self.logs_directory)
        directory = os.path.join(logs_directory, name)
        if not os.path.isdir(directory):
            print('Directory not found: %s' % (directory))
            return

        ssh_handler = ssh.Ssh('10.58.25.162', 'root', password='!Cisc0_123')
        for filename in os.listdir(directory):
            source = os.path.join(directory, filename)
            destination = os.path.join('/tmp/iserver-bug-reports', '%s.%s' % (name, filename))
            if not ssh_handler.scp_file(source, destination):
                print('Log upload failed: %s' % (source))
                return
            print('Log file uploaded: %s' % (source))
