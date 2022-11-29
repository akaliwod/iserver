from lib import ip_helper


class ComputeFilter():
    """Class for server filtering
    """
    def __init__(self):
        pass

    def ip_filter_match(self, server, ip_filter):
        if len(ip_filter) == 0:
            return True

        for item in ip_filter:
            if item['type'] == 'address':
                if server['ManagementIp'] == item['value']:
                    return True

            if item['type'] == 'subnet':
                if ip_helper.is_ipv4_in_cidr(server['ManagementIp'], item['value']):
                    return True

        return False

    def name_filter_match(self, server, name_filter):
        if name_filter == '':
            return True

        for item in name_filter.split(','):
            if item.lower() in server['Name'].lower():
                return True

        return False

    def model_filter_match(self, server, model_filter):
        if model_filter == '':
            return True

        for item in model_filter.split(','):
            if item.lower() in server['Model'].lower():
                return True

        return False

    def locator_filter_match(self, server, locator_filter):
        if not locator_filter:
            return True

        if server['LocatorLedOn']:
            return True

        return False

    def power_off_filter_match(self, server, power_off):
        if not power_off:
            return True

        if server['OperPowerState'] != 'on':
            return True

        return False

    def alarms_filter_match(self, server, alarms):
        if not alarms:
            return True

        if server['AlarmSummary']['Warning'] == 0 and server['AlarmSummary']['Critical'] == 0:
            return False

        return True

    def ucsm_filter_match(self, server, ucsm):
        if not ucsm:
            return True

        if server['ManagementMode'] == 'UCSM':
            return True

        return False

    def disconnected_filter_match(self, server, disconnected):
        if not disconnected:
            return True

        if not server['Connected']:
            return True

        return False

    def standalone_filter_match(self, server, standalone):
        if not standalone:
            return True

        if server['ManagementMode'] != 'UCSM':
            return True

        return False

    def serial_filter_match(self, server, serials):
        if len(serials) == 0:
            return True

        if server['Serial'] in serials:
            return True

        return False

    def fan_filter_match(self, server, fan):
        if not fan:
            return True

        if not server['FanHealthy']:
            return True

        return False

    def psu_filter_match(self, server, psu):
        if not psu:
            return True

        if not server['PsuHealthy']:
            return True

        return False

    def pci_filter_match(self, server, pci_filter):
        if pci_filter == '':
            return True

        for item in pci_filter.split(','):
            for model in server['PciModels']:
                if item.lower() in model.lower():
                    return True

        return False

    def cpu_filter_match(self, server, cpu_filter):
        if cpu_filter == '':
            return True

        if cpu_filter.startswith('>='):
            if server['NumCpuCores'] >= int(cpu_filter.lstrip('>=')):
                return True
            return False

        if cpu_filter.startswith('ge'):
            if server['NumCpuCores'] >= int(cpu_filter.lstrip('ge')):
                return True
            return False

        if cpu_filter.startswith('<='):
            if server['NumCpuCores'] <= int(cpu_filter.lstrip('<=')):
                return True
            return False

        if cpu_filter.startswith('le'):
            if server['NumCpuCores'] <= int(cpu_filter.lstrip('le')):
                return True
            return False

        if cpu_filter.startswith('>'):
            if server['NumCpuCores'] > int(cpu_filter.lstrip('>')):
                return True
            return False

        if cpu_filter.startswith('gt'):
            if server['NumCpuCores'] > int(cpu_filter.lstrip('gt')):
                return True
            return False

        if cpu_filter.startswith('<'):
            if server['NumCpuCores'] < int(cpu_filter.lstrip('<')):
                return True
            return False

        if cpu_filter.startswith('lt'):
            if server['NumCpuCores'] < int(cpu_filter.lstrip('lt')):
                return True
            return False

        if cpu_filter.startswith('!='):
            if server['NumCpuCores'] != int(cpu_filter.lstrip('!=')):
                return True
            return False

        if cpu_filter.startswith('ne'):
            if server['NumCpuCores'] != int(cpu_filter.lstrip('ne')):
                return True
            return False

        if server['NumCpuCores'] == int(cpu_filter):
            return True

        return False

    def memory_filter_match(self, server, memory_filter):
        if memory_filter == '':
            return True

        if memory_filter.startswith('>='):
            if server['TotalMemoryGB'] >= int(memory_filter.lstrip('>=')):
                return True
            return False

        if memory_filter.startswith('ge'):
            if server['TotalMemoryGB'] >= int(memory_filter.lstrip('ge')):
                return True
            return False

        if memory_filter.startswith('<='):
            if server['TotalMemoryGB'] <= int(memory_filter.lstrip('<=')):
                return True
            return False

        if memory_filter.startswith('le'):
            if server['TotalMemoryGB'] <= int(memory_filter.lstrip('le')):
                return True
            return False

        if memory_filter.startswith('>'):
            if server['TotalMemoryGB'] > int(memory_filter.lstrip('>')):
                return True
            return False

        if memory_filter.startswith('gt'):
            if server['TotalMemoryGB'] > int(memory_filter.lstrip('gt')):
                return True
            return False

        if memory_filter.startswith('<'):
            if server['TotalMemoryGB'] < int(memory_filter.lstrip('<')):
                return True
            return False

        if memory_filter.startswith('lt'):
            if server['TotalMemoryGB'] < int(memory_filter.lstrip('lt')):
                return True
            return False

        if memory_filter.startswith('!='):
            if server['TotalMemoryGB'] != int(memory_filter.lstrip('!=')):
                return True
            return False

        if memory_filter.startswith('ne'):
            if server['TotalMemoryGB'] != int(memory_filter.lstrip('ne')):
                return True
            return False

        if server['TotalMemoryGB'] == int(memory_filter):
            return True

        return False

    def match_server(self, server, rules, base_match=False):
        if rules is None:
            return True

        if not self.ip_filter_match(server, rules['ip']):
            return False

        if not self.name_filter_match(server, rules['name']):
            return False

        if not self.model_filter_match(server, rules['model']):
            return False

        if not self.serial_filter_match(server, rules['serials']):
            return False

        # If match is based on the base server attributes, exit early
        if base_match:
            return True

        if not self.locator_filter_match(server, rules['locator']):
            return False

        if not self.power_off_filter_match(server, rules['power_off']):
            return False

        if not self.alarms_filter_match(server, rules['alarms']):
            return False

        if not self.ucsm_filter_match(server, rules['ucsm']):
            return False

        if not self.disconnected_filter_match(server, rules['disconnected']):
            return False

        if not self.standalone_filter_match(server, rules['standalone']):
            return False

        if not self.fan_filter_match(server, rules['fan']):
            return False

        if not self.psu_filter_match(server, rules['psu']):
            return False

        if not self.pci_filter_match(server, rules['pci']):
            return False

        if not self.cpu_filter_match(server, rules['cpu']):
            return False

        if not self.memory_filter_match(server, rules['memory']):
            return False

        return True
