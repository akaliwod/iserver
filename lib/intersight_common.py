import traceback
import time
from lib import isctl_helper
from lib import log_helper
from lib import output_helper


class IntersightCommon():
    def __init__(self, iaccount, iobject, get_filter=None, silent=False, verbose=False, debug=False):
        self.log = log_helper.Log()
        self.iaccount = iaccount
        self.isctl = isctl_helper.Isctl(iaccount)
        self.iobject = iobject
        self.my_output = output_helper.OutputHelper()
        self.cache = None
        if get_filter is None:
            self.get_filter = ''
        else:
            self.get_filter = '--filter %s' % (get_filter)

        self.flags = {}
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug

        self.my_output.set_flags(self.flags['silent'], self.flags['verbose'], self.flags['debug'])

    def prepare_cache(self):
        if self.cache is None:
            self.cache = self.get_all()

    def get_cache_moid(self, moid):
        self.prepare_cache()
        if self.cache is not None:
            for item in self.cache:
                if item['Moid'] == moid:
                    return item
        return None

    def set_get_filter(self, get_filter):
        self.get_filter = '--filter "%s"' % (get_filter)

    def get_all(self, max_errors=3, error_timeout=1):
        all_results = []
        top = 100
        skip = 0
        errors = 0
        while True:
            if skip == 0:
                command = 'isctl get %s %s -o json --top %s' % (self.iobject, self.get_filter, top)
            else:
                command = 'isctl get %s %s -o json --top %s --skip %s' % (self.iobject, self.get_filter, top, skip)

            response = self.isctl.get(command)

            if response is None:
                self.log.error('iwe_common.get_all', 'Command failed: %s' % (command))
                if errors >= max_errors:
                    self.log.error('iwe_common.get_all', 'Max command failures: %s' % (command))
                    break

                errors = errors + 1
                time.sleep(error_timeout)
                continue

            all_results = all_results + response
            if len(response) < top:
                break

            skip = skip + top

        return all_results

    def get(self, moid):
        command = 'isctl get %s moid %s -o json' % (self.iobject, moid)
        response = self.isctl.get(command)
        return response

    def get_moid(self, name):
        command = 'isctl get %s name "%s" -o json' % (self.iobject, name)
        response = self.isctl.get(command)
        if response is None:
            return None
        if isinstance(response, list):
            return None
        return response['Moid']

    def get_name(self, moid):
        return self.get_object_attribute(moid, 'Name')

    def is_moid(self, moid):
        return bool(self.get(moid) is not None)

    def is_name(self, name):
        return bool(self.get_moid(name) is not None)

    def get_by_name(self, name):
        command = 'isctl get %s name "%s" -o json' % (self.iobject, name)
        response = self.isctl.get(command)
        if response is None:
            return None
        if isinstance(response, list):
            return None
        return response

    def get_moids_list(self):
        return self.get_objects_attribute('Moid')

    def get_moids_dict(self):
        moids = {}
        attributes_list = self.get_objects_attributes(['Moid', 'Name'])
        if attributes_list is not None:
            for attributes in attributes_list:
                moids[attributes['Moid']] = attributes['Name']
        return moids

    def get_object_attribute(self, moid, attribute_name):
        attribute_value = None
        item = self.get(moid)
        if item is not None:
            if attribute_name in item:
                attribute_value = item[attribute_name]
        return attribute_value

    def get_object_attributes(self, moid, attribute_names):
        attribute_values = None
        item = self.get(moid)
        if item is not None:
            attribute_values = {}
            for attribute_name in attribute_names:
                if attribute_name in item:
                    attribute_values[attribute_name] = item[attribute_name]
        return attribute_values

    def get_objects_attribute(self, attribute_name, unique_only=False, sort=False):
        attributes = []
        items = self.get_all()
        if items is not None:
            for i in items:
                if attribute_name in i:
                    if not unique_only or i[attribute_name] not in attributes:
                        attributes.append(i[attribute_name])

        if sort:
            try:
                attributes = sorted(attributes)
            except BaseException:
                self.log.error('iwe_common.get_objects_attribute', 'Sort failed: %s' % (traceback.format_exc()))
                return None

        return attributes

    def get_objects_attributes(self, attribute_names, order_by=None):
        objects_attributes = None
        items = self.get_all()
        if items is not None:
            objects_attributes = []
            for item in items:
                attributes = {}
                for attribute_name in attribute_names:
                    if attribute_name in item:
                        attributes[attribute_name] = item[attribute_name]

                objects_attributes.append(attributes)

            if order_by is not None:
                try:
                    objects_attributes = sorted(objects_attributes, key=lambda i: i[order_by])
                except BaseException:
                    self.log.error('iwe_common.get_objects_attributes', 'Sort failed: %s' % (traceback.format_exc()))

        return objects_attributes

    def create(self, attributes, get_response=False, json_conversion=True):
        command = 'isctl create %s %s' % (self.iobject, attributes)
        response = self.isctl.create(command, get_response=get_response, json_conversion=json_conversion)
        return response

    def update(self, moid, attributes):
        command = 'isctl update %s moid %s %s' % (self.iobject, moid, attributes)
        response = self.isctl.update(command)
        return response

    def delete(self, moid):
        command = 'isctl delete %s moid %s' % (self.iobject, moid)
        response = self.isctl.delete(command)
        return response
