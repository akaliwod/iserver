import traceback
import json
import yaml

from lib.intersight.intersight_common import IntersightCommon
from lib import ip_helper
from lib.intersight import software_repository_catalog
from lib.intersight import organization


class SoftwareConfigurationUtility(IntersightCommon):
    """Class for Intersight software configuration utility

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
        "BundleType": "",
        "Catalog": {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736567612d30276cb1",
            "ObjectType": "softwarerepository.Catalog",
            "link": "https://www.intersight.com/api/v1/softwarerepository/Catalogs/5dee1d736567612d30276cb1"
        },
        "ClassId": "firmware.ServerConfigurationUtilityDistributable",
        "ComponentMeta": [],
        "CreateTime": "2022-09-22T08:53:14.662Z",
        "Description": "",
        "DistributableMetas": [],
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "DownloadCount": 0,
        "Guid": "",
        "ImageType": "",
        "ImportAction": "None",
        "ImportState": "MetaOnly",
        "ImportedTime": "0001-01-01T00:00:00Z",
        "LastAccessTime": "0001-01-01T00:00:00Z",
        "Md5eTag": "",
        "Md5sum": "",
        "Mdfid": "",
        "ModTime": "2022-09-22T08:53:14.85Z",
        "Model": "",
        "Moid": "632c227a6567612d30187910",
        "Name": "SCU 6.2.2a",
        "ObjectType": "firmware.ServerConfigurationUtilityDistributable",
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
        "PlatformType": "",
        "RecommendedBuild": "",
        "Release": null,
        "ReleaseDate": "0001-01-01T00:00:00Z",
        "ReleaseNotesUrl": "",
        "Sha512sum": "",
        "SharedScope": "",
        "Size": 0,
        "SoftwareAdvisoryUrl": "",
        "SoftwareTypeId": "",
        "Source": {
            "ClassId": "softwarerepository.HttpServer",
            "IsPasswordSet": false,
            "LocationLink": "http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-scu-6.2.2a.iso",
            "ObjectType": "softwarerepository.HttpServer",
            "Username": ""
        },
        "SupportedModels": [
            "c220 m5"
        ],
        "Tags": [],
        "Vendor": "Cisco",
        "Version": "6.2.2a"
    }
    """
    def __init__(self, iaccount):
        self.iobject = 'firmware serverconfigurationutilitydistributable'
        IntersightCommon.__init__(self, iaccount, self.iobject)

    def get_all(self, max_errors=3, error_timeout=1):
        """Get all SCU objects

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
            list of dict: list of Intersight SCU objects
        """
        scus = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if scus is None:
            return scus

        organization_handler = organization.Organization(self.iaccount)
        organizations = organization_handler.get_moids_dict()

        verified = []
        for scu in scus:
            organization_id = None
            for permission in scu['PermissionResources']:
                if permission['ObjectType'] == 'organization.Organization':
                    organization_id = permission['Moid']

            if organization_id is None or organization_id not in organizations:
                # Organization ID must exist
                continue

            scu['Organization'] = organizations[organization_id]

            scu['Verified'] = False
            scu['Link'] = None
            scu['Type'] = None

            if scu['Source']['ClassId'] not in ['softwarerepository.HttpServer', 'softwarerepository.NfsServer']:
                continue

            if scu['Source']['ClassId'] == 'softwarerepository.HttpServer':
                scu['Type'] = 'url'
                scu['Link'] = scu['Source']['LocationLink']
                scu['Verified'] = ip_helper.is_url_accessible(scu['Link'])

            if scu['Source']['ClassId'] == 'softwarerepository.NfsServer':
                scu['Type'] = 'nfs'
                scu['Link'] = scu['Source']['FileLocation']
                scu['Verified'] = False

            verified.append(scu)

        return verified

    def validate_add(self, scu, name_unique=True):
        """Validate SCU create attributes

        Args:
            scus (dict): scu attributes
            name_unique (bool, optional): check if Name already exists. Defaults to True.

        Expected attributes: Name, Version, Link and Organization
        Organization (name) must exist
        If name_unique, then Name cannot already exist

        Returns:
            bool: validation success
            string: if validation fails, contains information on the reason
        """
        try:
            if not isinstance(scu, dict):
                return False, 'Dict scu attributes required'

            for key in ['Name', 'Version', 'Link', 'Organization']:
                if key not in scu:
                    return False, 'Attribute %s required' % (key)

            for key in ['Name', 'Version', 'Link']:
                if len(scu[key]) == 0:
                    return False, 'Attribute value %s required' % (key)

            if name_unique:
                if self.is_name(scu['Name']):
                    return False, 'Name %s already defined' % (scu['Name'])

            if not ip_helper.is_url_valid(scu['Link']):
                return False, 'Invalid link: %s' % (scu['Link'])

            organization_handler = organization.Organization(self.iaccount)
            if organization_handler.get_by_name(scu['Organization']) is None:
                return False, 'Organization not found: %s' % (scu['Organization'])

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def create(self, attributes):
        """Create SCU object in Intersight

        Args:
            attributes (dict): Expected keys Name, Version, Type, Link and Organization

        The bulk of code takes attributes and formats that with the Intersight specific parameters
        SupportedModels is hard-coded
        Catalog is found based on Organization value

        Returns:
            bool: success or failure
        """
        create_attributes = ''
        for key in ['Name', 'Version']:
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

        create_attributes = '%s --SupportedModels=ucs' % (create_attributes)

        organization_handler = organization.Organization(self.iaccount)
        organization_id = organization_handler.get_by_name(attributes['Organization'])['Moid']

        src_handler = software_repository_catalog.SoftwareRepositoryCatalog(self.iaccount)
        catalog_id = src_handler.get_user_catalog_id(organization_id)
        if catalog_id is None:
            return False

        create_attributes = '%s --Catalog=MoRef[Moid:%s]' % (create_attributes, catalog_id)

        return IntersightCommon.create(self, create_attributes)

    def get_set_output(self, scus):
        """Prepare YAML-based format from list of SCUs attributes

        Args:
            scus (list of dict): SCU objects likely returned by get_all method

        Select subset of scu object attributes that are supported by scu set operation
        - Moid, Name, Version, Type, Link

        Returns:
            string: YAML-formatted output
        """
        if scus is None:
            return None

        set_output = []
        for scu in scus:
            item = {}
            for key in ['Moid', 'Name', 'Version', 'Type', 'Link']:
                item[key] = scu[key]

            set_output.append(item)

        try:
            output = yaml.dump(
                set_output,
                default_flow_style=False
            )
        except BaseException:
            output = None

        return output

    def validate_set(self, scus):
        """Check SCU user input for set/update operation

        Args:
            scus (list of dict): User defined SCUs attributes

        Each entry in the list must have Moid key
        The rest of the fields is optional: Name, Version, Type, Link
        Organizaiton is not allowed to be updated
        Moid must exist
        Supported type: url and nfs

        Returns:
            boolean: validation successful
            string: failed validation description
        """
        try:
            ids = self.get_moids_list()
            if ids is None:
                return False, 'Exception in intersight scu check'

            if not isinstance(scus, list):
                return False, 'List of dict required'

            for scu in scus:
                if not isinstance(scu, dict):
                    return False, 'List of dict required'

                if scu['Moid'] not in ids:
                    return False, 'SCU Moid not found: %s' % (scu['Moid'])

                if 'Name' in scu and len(scu['Name']) > 0:
                    if self.is_name(scu['Name']):
                        return False, 'Name %s already defined' % (scu['Name'])

                is_link = False
                if 'Link' in scu and len(scu['Link']) > 0:
                    is_link = True

                is_type = False
                if 'Type' in scu and len(scu['Type']) > 0:
                    is_type = True

                if is_link and is_type:
                    if scu['Type'] not in ['url', 'nfs']:
                        return False, 'Unsupported type: %s' % (scu['Type'])

                    if scu['Link'].startswith('http'):
                        if not ip_helper.is_url_valid(scu['Link']):
                            return False, 'Invalid link: %s' % (scu['Link'])

        except BaseException:
            return False, traceback.format_exc()

        return True, None

    def update(self, moid, attributes):
        """Update SCU object in Intersight

        Args:
            moid (string): Moid of SCU object to be updated
            attributes (dict): Optional keys Name, Version, Type, Link

        Format SCU attributes with the Intersight specific parameters
        Supported Type: url and nfs

        Returns:
            bool: success or failure
        """
        update_attributes = ''
        for key in ['Name', 'Version']:
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

    def print(self, scus, verify=False):
        """Print software configuration utilities

        +-------------------------+---------------------------+-----------+----------+-------+-------------------------------------------------------------------------+
        | Organization            | SCU ID                    | SCU Name  | Version  | Type  | Link                                                                    |
        +-------------------------+---------------------------+-----------+----------+-------+-------------------------------------------------------------------------+
        | EMEAR-SPDC-Specialists  | 632afedf6567612d300aefe6  | 6.1.3c    | 6.1.3c   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-cxxx-scu-6.1.3c.iso  |
        | EMEAR-SPDC-Specialists  | 632c227a6567612d30187910  | 6.2.2a    | 6.2.2a   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-scu-6.2.2a.iso       |
        | EMEAR-SPDC-Specialists  | 63343b416567612d30776c72  | a         | b        | nfs   | 10.1.1.1/folder/file.iso                                                |
        +-------------------------+---------------------------+-----------+----------+-------+-------------------------------------------------------------------------+
        """

        order = [
            'Organization',
            'Moid',
            'Name',
            'Version',
            'Type',
            'Link'
        ]
        headers = [
            'Organization',
            'SCU ID',
            'SCU Name',
            'Version',
            'Type',
            'Link'
        ]

        if verify:
            order.append('Verified')
            headers.append('Verified')

        self.my_output.my_table(
            scus,
            order=order,
            headers=headers,
            table=True
        )
