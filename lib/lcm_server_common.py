import time

from progress.bar import IncrementalBar

from lib import isctl_helper
from lib import log_helper
from lib import output_helper
from lib import organization
from lib import compute_server_setting
from lib import workflow
from lib import workflow_task_info
from lib import workflow_info


class LcmServerCommon():
    def __init__(self, iaccount, silent=False, verbose=False, debug=False):
        self.iaccount = iaccount
        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper()
        self.isctl = isctl_helper.Isctl(iaccount)
        self.workflow_handler = workflow.Workflow(iaccount)
        self.workflow_task_info_handler = workflow_task_info.WorkflowTaskInfo(iaccount)
        self.organization = organization.Organization(iaccount)
        self.server_setting_handler = compute_server_setting.ComputeServerSetting(iaccount)
        self.workflow_info_handler = workflow_info.WorkflowInfo(
            iaccount,
            silent=silent,
            verbose=verbose,
            debug=debug
        )

        self.flags = {}
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug

        self.my_output.set_flags(self.flags['silent'], self.flags['verbose'], self.flags['debug'])

    def show_flags(self):
        self.my_output.dictionary(self.flags, title='Flags', stream='debug')

    def wait_workflows_start(self, servers, workflow_name, max_start_time=30):
        start_time = int(time.time())
        for server in servers:
            server['LcmWorkflowId'] = None

        if not self.flags['silent']:
            bar_handler = IncrementalBar('Workflows started', max=len(servers))
            bar_handler.goto(0)

        while True:
            workflows = self.workflow_handler.get_last()
            if workflows is None:
                time.sleep(5)
                continue

            started = 0
            for server in servers:
                if server['LcmWorkflowId'] is not None:
                    started = started + 1
                    continue

                for workflow_item in workflows:
                    if not self.workflow_handler.is_server_workflow(server['Moid'], workflow_item):
                        continue

                    if workflow_item['Name'] != workflow_name:
                        continue

                    if workflow_item['Moid'] in server['WorkflowsLastIds']:
                        continue

                    server['LcmWorkflowId'] = workflow_item['Moid']
                    started = started + 1
                    break

            if not self.flags['silent']:
                bar_handler.goto(started)

            if started == len(servers):
                break

            if int(time.time()) - start_time > max_start_time:
                self.my_output.error('Max start waiting time elapsed')
                return None

            time.sleep(5)

        if not self.flags['silent']:
            bar_handler.finish()
            self.my_output.files_only('Workflows started: [#######################] %s/%s' % (len(servers), len(servers)))

        return servers

    def wait_workflows_end(self, servers, max_complete_time=60):
        start_time = int(time.time())

        if not self.flags['silent']:
            bar_handler = IncrementalBar('Workflows finished', max=len(servers))
            bar_handler.goto(0)

        while True:
            workflows = self.workflow_handler.get_last()
            if workflows is None:
                time.sleep(5)
                continue

            finished = 0
            for server in servers:
                for workflow_item in workflows:
                    if workflow_item['Moid'] == server['LcmWorkflowId']:
                        server['LcmWorkflowStatus'] = workflow_item['Status']
                        server['LcmWorkflowInfo'] = self.workflow_handler.get_workflow_info(workflow_item)

                        if workflow_item['Status'] == 'COMPLETED':
                            finished = finished + 1

                        if workflow_item['Status'] == 'FAILED':
                            finished = finished + 1

                        break

            if not self.flags['silent']:
                bar_handler.goto(finished)

            if finished == len(servers):
                break

            if int(time.time()) - start_time > max_complete_time:
                self.my_output.error('Max complete waiting time elapsed')
                return None

            time.sleep(5)

        if not self.flags['silent']:
            bar_handler.finish()
            self.my_output.files_only('Workflows finished: [#######################] %s/%s' % (len(servers), len(servers)))

        return servers

    def wait_workflows(self, servers, workflow_name, max_start_time=30, max_complete_time=60, summary=False):
        servers = self.wait_workflows_start(servers, workflow_name, max_start_time=max_start_time)
        if servers is None:
            return False

        servers = self.wait_workflows_end(servers, max_complete_time=max_complete_time)
        if servers is None:
            return False

        if self.flags['silent']:
            return True

        if summary:
            headers = [
                'Server Moid',
                'Server Name',
                'Workflow ID',
                'Workflow Status'
            ]

            order = [
                'Moid',
                'Name',
                'LcmWorkflowId',
                'LcmWorkflowStatus'
            ]

            self.my_output.my_table(
                servers,
                order=order,
                headers=headers,
                table=True
            )

        for server in servers:
            server_workflow_info = {}
            server_workflow_info['server'] = server
            server_workflow_info['workflow'] = server['LcmWorkflowInfo']
            server_workflow_info['tasks'] = self.workflow_task_info_handler.get_workflow_tasks_info(
                server['LcmWorkflowId']
            )
            self.workflow_info_handler.print_workflow_info(server_workflow_info, stream='info')

        return True
