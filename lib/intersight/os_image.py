import json
import traceback
import yaml

from lib.intersight.intersight_common import IntersightCommon
from lib import ip_helper
from lib.intersight import organization
from lib.intersight import hcl_operating_system_vendor
from lib.intersight import hcl_operating_system
from lib.intersight import software_repository_catalog


class OsImage(IntersightCommon):
    """Class for Intersight operating system image

    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5dee1d736567612d30276cb1",
                "ObjectType": "softwarerepository.Catalog",
                "link": "https://www.intersight.com/api/v1/softwarerepository/Catalogs/5dee1d736567612d30276cb1"
            }
        ],
        "Catalog": {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736567612d30276cb1",
            "ObjectType": "softwarerepository.Catalog",
            "link": "https://www.intersight.com/api/v1/softwarerepository/Catalogs/5dee1d736567612d30276cb1"
        },
        "ClassId": "softwarerepository.OperatingSystemFile",
        "CreateTime": "2022-09-25T14:42:02.675Z",
        "Description": "",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "DownloadCount": 0,
        "ImportAction": "None",
        "ImportState": "MetaOnly",
        "ImportedTime": "0001-01-01T00:00:00Z",
        "LastAccessTime": "0001-01-01T00:00:00Z",
        "Md5eTag": "",
        "Md5sum": "",
        "ModTime": "2022-09-25T14:42:03.013Z",
        "Moid": "633068b96567612d304a7844",
        "Name": "Ubuntu 22.04LTS",
        "ObjectType": "softwarerepository.OperatingSystemFile",
        "Owners": [
            "5be4b2ce67626c6d661ca38d"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736567612d30276cb1",
            "ObjectType": "softwarerepository.Catalog",
            "link": "https://www.intersight.com/api/v1/softwarerepository/Catalogs/5dee1d736567612d30276cb1"
        },
        "PermissionResources": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5dee1d736972652d321d26b5",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
            }
        ],
        "ReleaseDate": "0001-01-01T00:00:00Z",
        "Sha512sum": "",
        "SharedScope": "",
        "Size": 0,
        "SoftwareAdvisoryUrl": "",
        "Source": {
            "ClassId": "softwarerepository.HttpServer",
            "IsPasswordSet": false,
            "LocationLink": "http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso",
            "ObjectType": "softwarerepository.HttpServer",
            "Username": ""
        },
        "Tags": [],
        "Vendor": "Ubuntu",
        "Version": "Ubuntu Server 22.04 LTS",
        "Verified": true,
        "Link": "http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso"
    }
    """
    def __init__(self, iaccount):
        self.iobject = 'softwarerepository operatingsystemfile'
        self.hcl_os_vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount)
        self.hcl_os_version_handler = hcl_operating_system.HclOperatingSystem(iaccount)

        IntersightCommon.__init__(self, iaccount, self.iobject)

    def get_all(self, max_errors=3, error_timeout=1):
        """Get all OS image objects

        Args:
            max_errors (int, optional): if API call fails retry until max_errors. Defaults to 3.
            error_timeout (int, optional): if API response takes longer than error_timeout, then consider API as failed. Defaults to 1.

        Extend the raw get API call with custom attributes
        - Organization: organization name
        - Type: url, nfs
        - Link: normalized location
        - Verified: check if url is reachable. not supported for nfs type

        Note: cfs type not supported

        Returns:
            list of dict: list of Intersight OS image objects
        """
        images = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if images is None:
            return images

        organization_handler = organization.Organization(self.iaccount)
        organizations = organization_handler.get_moids_dict()

        verified = []
        for image in images:
            organization_id = None
            for permission in image['PermissionResources']:
                if permission['ObjectType'] == 'organization.Organization':
                    organization_id = permission['Moid']

            if organization_id is None or organization_id not in organizations:
                # Organization ID must exist
                continue

            image['Organization'] = organizations[organization_id]

            image['Verified'] = False
            image['Type'] = None
            image['Link'] = None

            if image['Source']['ClassId'] not in ['softwarerepository.HttpServer', 'softwarerepository.NfsServer']:
                continue

            if image['Source']['ClassId'] == 'softwarerepository.HttpServer':
                image['Type'] = 'url'
                image['Link'] = image['Source']['LocationLink']
                image['Verified'] = ip_helper.is_url_accessible(image['Link'])

            if image['Source']['ClassId'] == 'softwarerepository.NfsServer':
                image['Type'] = 'nfs'
                image['Link'] = image['Source']['FileLocation']
                image['Verified'] = False

            verified.append(image)

        return verified

    def validate_add(self, image, name_unique=True):
        """Validate os image create attributes

        Args:
            image (dict): image attributes
            name_unique (bool, optional): check if Name already exists. Defaults to True.

        Expected attributes: Name, Vendor, Version, Link and Organization
        Vendor and Version must be defined in HCL catalog
        Organization (name) must exist
        If name_unique, then Name cannot already exist

        Returns:
            bool: validation success
            string: if validation fails, contains information on the reason
        """
        try:
            if not isinstance(image, dict):
                return False, 'Dict image attributes required'

            for key in ['Name', 'Vendor', 'Version', 'Link', 'Organization']:
                if key not in image:
                    return False, 'Attribute %s required' % (key)

            if image['Vendor'] == '':
                return False, 'Define vendor'

            vendor_attributes = self.hcl_os_vendor_handler.get_by_name(image['Vendor'])
            if vendor_attributes is None:
                return False, 'Vendor not found: %s' % (image['Vendor'])
            vendor_id = vendor_attributes['Moid']

            if image['Version'] == '':
                return False, 'Define version'

            if not self.hcl_os_version_handler.is_vendor_version(vendor_id, image['Version']):
                return False, 'Invalid version for vendor: %s' % (image['Version'])

            organization_handler = organization.Organization(self.iaccount)
            if organization_handler.get_by_name(image['Organization']) is None:
                return False, 'Organization not found: %s' % (image['Organization'])

            if name_unique:
                if self.is_name(image['Name']):
                    return False, 'Name %s already defined' % (image['Name'])

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def create(self, attributes):
        """Create os image object in Intersight

        Args:
            attributes (dict): Expected keys Name, Vendor, Version, Type, Link and Organization

        The bulk of code takes attributes and formats that with the Intersight specific parameters
        Catalog is found based on Organization value

        Returns:
            bool: success or failure
        """
        create_attributes = ''
        for key in ['Name', 'Vendor', 'Version']:
            value = str(attributes[key])
            if len(value.split(' ')) > 1:
                create_attributes = '%s --%s=\'%s\'' % (create_attributes, key, value)
            else:
                create_attributes = '%s --%s=%s' % (create_attributes, key, value)

        if attributes['Type'] not in ['url', 'nfs']:
            return False

        if attributes['Type'] == 'url':
            source = {}
            source['ClassId'] = 'softwarerepository.HttpServer'
            source['LocationLink'] = attributes['Link']
            source['ObjectType'] = 'softwarerepository.HttpServer'
            create_attributes = '%s --%s=\'%s\'' % (create_attributes, 'Source', json.dumps(source))

        if attributes['Type'] == 'nfs':
            source = {}
            source['ClassId'] = 'softwarerepository.NfsServer'
            source['FileLocation'] = attributes['Link']
            source['ObjectType'] = 'softwarerepository.NfsServer'
            create_attributes = '%s --%s=\'%s\'' % (create_attributes, 'Source', json.dumps(source))

        organization_handler = organization.Organization(self.iaccount)
        organization_id = organization_handler.get_by_name(attributes['Organization'])['Moid']

        src_handler = software_repository_catalog.SoftwareRepositoryCatalog(self.iaccount)
        catalog_id = src_handler.get_user_catalog_id(organization_id)
        if catalog_id is None:
            return False

        create_attributes = '%s --Catalog=MoRef[Moid:%s]' % (create_attributes, catalog_id)

        return IntersightCommon.create(self, create_attributes)

    def get_set_output(self, images):
        """Prepare YAML-based format from list of os image attributes

        Args:
            images (list of dict): Os image objects likely returned by get_all method

        Select subset of image object attributes that are supported by set operation
        - Moid, Name, Vendor, Version, Type, Link

        Returns:
            string: YAML-formatted output
        """
        if images is None:
            return None

        set_output = []
        for image in images:
            item = {}
            for key in ['Moid', 'Name', 'Vendor', 'Version', 'Type', 'Link']:
                item[key] = image[key]

            set_output.append(item)

        try:
            output = yaml.dump(
                set_output,
                default_flow_style=False
            )
        except BaseException:
            output = None

        return output

    def validate_set(self, images):
        """Check os image user input for set/update operation

        Args:
            images (list of dict): User defined os image attributes

        Each entry in the list must have keys: ...

        Returns:
            boolean: validation successful
            string: failed validation description
        """
        try:
            ids = self.get_moids_list()
            if ids is None:
                return False, 'Exception in intersight os image check'

            if not isinstance(images, list):
                return False, 'List required'

            for image in images:
                if not isinstance(image, dict):
                    return False, 'List of dict required'

                if image['Moid'] not in ids:
                    return False, 'SCU Moid not found: %s' % (image['Moid'])

                if 'Name' in image and len(image['Name']) > 0:
                    if self.is_name(image['Name']):
                        return False, 'Name %s already defined' % (image['Name'])

                is_link = False
                if 'Link' in image and len(image['Link']) > 0:
                    is_link = True

                is_type = False
                if 'Type' in image and len(image['Type']) > 0:
                    is_type = True

                if is_link and is_type:
                    if image['Type'] not in ['url', 'nfs']:
                        return False, 'Unsupported type: %s' % (image['Type'])

                    if image['Link'].startswith('http'):
                        if not ip_helper.is_url_valid(image['Link']):
                            return False, 'Invalid link: %s' % (image['Link'])

                is_vendor = False
                if 'Vendor' in image and len(image['Vendor']) > 0:
                    is_vendor = True

                is_version = False
                if 'Version' in image and len(image['Version']) > 0:
                    is_version = True

                if is_vendor and is_version:
                    vendor_attributes = self.hcl_os_vendor_handler.get_by_name(image['Vendor'])
                    if vendor_attributes is None:
                        return False, 'Vendor not found: %s' % (image['Vendor'])
                    vendor_id = vendor_attributes['Moid']

                    if image['Version'] == '':
                        return False, 'Define version'

                    if not self.hcl_os_version_handler.is_vendor_version(vendor_id, image['Version']):
                        return False, 'Invalid version for vendor: %s' % (image['Version'])
                else:
                    if not is_vendor and not is_version:
                        pass
                    else:
                        return False, 'Define both vendor and version'

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def update(self, moid, attributes):
        """Update OS image object in Intersight

        Args:
            moid (string): Moid of os image object to be updated
            attributes (dict): Expected keys Name, Vendor, Version, Type, Link

        Format image attributes with the Intersight specific parameters
        Supported Type: url and nfs

        Returns:
            bool: success or failure
        """
        update_attributes = ''
        for key in ['Name', 'Vendor', 'Version']:
            if key in attributes and len(attributes[key]) > 0:
                value = str(attributes[key])
                if len(value.split(' ')) > 1:
                    update_attributes = '%s --%s=\'%s\'' % (update_attributes, key, value)
                else:
                    update_attributes = '%s --%s=%s' % (update_attributes, key, value)

        is_link = False
        if 'Link' in attributes and len(attributes['Link']) > 0:
            is_link = True

        is_type = False
        if 'Type' in attributes and len(attributes['Type']) > 0:
            is_type = True

        if is_link and is_type:
            if attributes['Type'] == 'url':
                source = {}
                source['ClassId'] = 'softwarerepository.HttpServer'
                source['LocationLink'] = attributes['Link']
                source['ObjectType'] = 'softwarerepository.HttpServer'
                update_attributes = '%s --%s=\'%s\'' % (update_attributes, 'Source', json.dumps(source))

            if attributes['Type'] == 'nfs':
                source = {}
                source['ClassId'] = 'softwarerepository.NfsServer'
                source['FileLocation'] = attributes['Link']
                source['ObjectType'] = 'softwarerepository.NfsServer'
                update_attributes = '%s --%s=\'%s\'' % (update_attributes, 'Source', json.dumps(source))

        return IntersightCommon.update(self, moid, update_attributes)

    def print(self, images, verify=False):
        """Print operating system images
        +-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
        | Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link                                                              |
        +-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
        | EMEAR-SPDC-Specialists  | 61b9c6ff6567612d30140473  | Centos 7.6 Minimal         | CentOS  | CentOS 7.6                 | url   | http://10.60.0.252/Centos/CentOS-7-x86_64-DVD-1810.iso            |
        | EMEAR-SPDC-Specialists  | 61c0ba846567612d305ffc9f  | Ubuntu Server 20.04.3 LTS  | Ubuntu  | Ubuntu Server 20.04.3 LTS  | nfs   | 10.49.234.1/home/filer/ubuntu-20.04.3-live-server-amd64.iso       |
        | EMEAR-SPDC-Specialists  | 632c42d86567612d3019ee47  | Ubuntu 20.04.3 LTS         | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.60.0.252/2-IMAGES/ubuntu-20.04.3-live-server-amd64.iso  |
        | EMEAR-SPDC-Specialists  | 633068b96567612d304a7844  | Ubuntu 22.04LTS            | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso  |
        +-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
        """

        order = [
            'Organization',
            'Moid',
            'Name',
            'Vendor',
            'Version',
            'Type',
            'Link'
        ]
        headers = [
            'Organization',
            'Image ID',
            'Image Name',
            'Vendor',
            'Version',
            'Type',
            'Link'
        ]

        if verify:
            order.append('Verified')
            headers.append('Verified')

        self.my_output.my_table(
            images,
            order=order,
            headers=headers,
            table=True
        )
