from lib.intersight_common import IntersightCommon


class HclOperatingSystemVendor(IntersightCommon):
    """Class for intersight hcl operating system vendor objects

    {
        "AccountMoid": "",
        "Ancestors": [],
        "ClassId": "hcl.OperatingSystemVendor",
        "CreateTime": "2018-08-15T00:16:49.873Z",
        "DomainGroupMoid": "SystemDomainGroup",
        "ModTime": "2018-08-15T00:16:49.886Z",
        "Moid": "5b7370f16836726e35cc7028",
        "Name": "Microsoft",
        "ObjectType": "hcl.OperatingSystemVendor",
        "Owners": [
            "system"
        ],
        "SharedScope": "",
        "Tags": []
    }
    """
    def __init__(self, iaccount):
        self.iobject = 'hcl operatingsystemvendor'
        IntersightCommon.__init__(self, iaccount, self.iobject)

    def print(self, vendors):
        sorted_vendors = sorted(vendors, key=lambda i: i['Name'])

        order = [
            'Moid',
            'Name'
        ]
        headers = [
            'Moid',
            'Name'
        ]
        self.my_output.my_table(
            sorted_vendors,
            order=order,
            headers=headers,
            table=True
        )
