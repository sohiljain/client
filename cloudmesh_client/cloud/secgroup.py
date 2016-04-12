from __future__ import print_function

import requests

from cloudmesh_client.shell.console import Console
from cloudmesh_client.common.Printer import Printer
from cloudmesh_client.db import CloudmeshDatabase
from cloudmesh_client.cloud.iaas.CloudProvider import CloudProvider
from cloudmesh_client.cloud.ListResource import ListResource
from cloudmesh_client.common.LibcloudDict import LibcloudDict
from cloudmesh_client.common.dotdict import dotdict
from pprint import pprint
from cloudmesh_client.common.ConfigDict import ConfigDict
from cloudmesh_client.default import Default

requests.packages.urllib3.disable_warnings()


class SecGroup(ListResource):
    cm = CloudmeshDatabase()

    """
    NOT USED
    @classmethod
    def convert_list_to_dict(cls, os_result):
        d = {}
        for i, obj in enumerate(os_result):
            d[i] = {}
            d[i]["Id"] = obj.id
            d[i]["Name"] = obj.name
            d[i]["Description"] = obj.description
        return d
    """

    # noinspection PyPep8
    @classmethod
    def convert_rules_to_dict(cls, os_result):
        d = {}
        for i, obj in enumerate(os_result):

            if obj["ip_range"]["cidr"]:
                ip_range = obj["ip_range"]["cidr"]
            else:
                ip_range = "0.0.0.0/0"

            d[i] = {
                "IP Protocol": obj["ip_protocol"],
                "From Port": obj["from_port"],
                "To Port": obj["to_port"],
                "IP Range": ip_range
            }
        return d

    @classmethod
    def refresh(cls, cloud):
        """
        This method would refresh the secgroup list by first clearing
        the database, then inserting new data
        :param cloud: the cloud name
        """

        return cls.cm.refresh('secgroup', cloud)

    @classmethod
    def add_rule_to_db(cls, group=None, name=None, from_port=None, to_port=None, protocol=None, cidr=None):
        old_rule = {
            "category": "general",
            "kind": "secgrouprule",
            "name": name,
            "group": group
        }

        cls.cm.delete(**old_rule)
        try:
            rule = {
                "category": "general",
                "kind": "secgrouprule",
                "group": group,
                "name": name,
                'protocol': protocol,
                'fromPort': from_port,
                'toPort': to_port,
                'cidr': cidr
            }
            cls.cm.add(rule, replace=False)
        except Exception as ex:
            Console.error("Problem adding rule")

    @classmethod
    def upload(cls, cloud=None, group=None):

        if cloud is None:
            clouds = ConfigDict("cloudmesh.yaml")["cloudmesh"]["active"]
        else:
            clouds = [cloud]
        if group is None:
            rules = cls.list(output='dict')
            groups = set()
            for g in rules:
                r = rules[g]
                groups.add(r["group"])
            groups = list(groups)
        else:
            groups = [group]


        for c in clouds:
            for g in groups:
                SecGroup.delete(category=c, group=g)
                uuid = SecGroup.create(category=c, group=g)
                for key in rules:
                    r = rules[key]
                    if r["group"] == g:
                        SecGroup.add_rule(c,uuid,r["fromPort"],r["toPort"] , r['protocol'],r['cidr'])
                # create group



    @classmethod
    def create(cls, group=None, category=None):
        """
        Method creates a new security group in database
        & returns the uuid of the created group
        :param group:
        :param category:
        :return:
        """
        # Create the security group in given cloud
        try:
            cloud_provider = CloudProvider(category).provider
            secgroup = cloud_provider.create_secgroup(group)
            if secgroup:
                uuid = secgroup.id
                return uuid
            else:
                print("Failed to create security group, {}".format(secgroup))
        except Exception as e:
            print(
                "Exception creating security group in cloud, {}".format(e))

        return None

    @classmethod
    def list(cls,
             group=None,
             name=None,
             category='general',
             output='table',
             scope='all'):
        """
        This method queries the database to fetch list of secgroups
        filtered by cloud.
        :param cloud:
        :return:
        """

        query = dotdict({
            "kind": "secgrouprule",
            "scope": "all"
        })
        if category is "general":

            if group is not None:
                query.group = group
            if name is not None:
                query.name = name
            query.category = category

            elements = cls.cm.find(**query)

        else:
            elements = CloudProvider(category).provider.list_secgroup_rules(category)



        if elements is None:
            return None
        else:

            # pprint(elements)
            #
            # BUG this should not depend on cloud, but on "general"
            #
            # (order, header) = CloudProvider(cloud).get_attributes("secgroup")

            order = None
            header = None

            return Printer.write(elements,
                                 order=order,
                                 header=header,
                                 output=output)


    @classmethod
    def list_rules(cls, uuid=None, output='table'):
        """
        This method gets the security group rules
        from the cloudmesh database
        :param uuid:
        :return:
        """

        try:
            if uuid is None:
                rules = cls.cm.find(kind="secgrouprule")
            else:
                args = {
                    "group": uuid
                }

                rules = cls.cm.find(kind="secgrouprule", **args)

            # check if rules exist
            if rules is None:
                return "No rules for security group={} in the database. Try cm secgroup refresh.".format(uuid)

            # return table
            return (Printer.write(rules,
                                  order=["user",
                                         "group",
                                         "category",
                                         "name",
                                         "fromPort",
                                         "toPort",
                                         "protocol",
                                         "cidr"],
                                  output=output))

        except Exception as ex:
            Console.error("Listing Security group rules")

        return None

    @classmethod
    def enable_ssh(cls, secgroup_name='default', cloud="general"):
        ret = False
        if cloud in LibcloudDict.Libcloud_category_list:
            Console.info("Creating and adding security group for libcloud")
            cloud_provider = CloudProvider(cloud).provider
            cloud_provider.create_sec_group(cloud, secgroup_name)
            cloud_provider.enable_ssh(cloud, secgroup_name)
        else:
            cloud_provider = CloudProvider(cloud).provider.provider
            secgroups = cloud_provider.security_groups.list()
            for asecgroup in secgroups:
                if asecgroup.name == secgroup_name:
                    rules = asecgroup.rules
                    rule_exists = False
                    # structure of a secgroup rule:
                    # {u'from_port': 22, u'group': {}, u'ip_protocol': u'tcp', u'to_port': 22, u'parent_group_id': u'UUIDHERE', u'ip_range': {u'cidr': u'0.0.0.0/0'}, u'id': u'UUIDHERE'}
                    for arule in rules:
                        if arule["from_port"] == 22 and \
                                        arule["to_port"] == 22 and \
                                        arule["ip_protocol"] == 'tcp' and \
                                        arule["ip_range"] == {'cidr': '0.0.0.0/0'}:
                            # print (arule["id"])
                            rule_exists = True
                            break
                    if not rule_exists:
                        cloud_provider.security_group_rules.create(
                            asecgroup.id,
                            ip_protocol='tcp',
                            from_port=22,
                            to_port=22,
                            cidr='0.0.0.0/0')
                    # else:
                    #    print ("The rule allowing ssh login did exist!")
                    ret = True
                    break

        # print ("*" * 80)
        # d = SecGroup.convert_list_to_dict(secgroups)
        # print (d)
        return ret

    @classmethod
    def get(cls, name=None, cloud="general"):
        """
        This method queries the database to fetch secgroup
        with given name filtered by cloud.
        :param name:
        :param cloud:
        :return:
        """

        try:
            args = {
                "name": name,
                'scope': 'fisrt',
                'kind': "secgroup",
                "output": "object",
            }
            if cloud is not None and cloud is not 'general':
                args["category"] = cloud

            secgroup = cls.cm.find(**args)

            if secgroup is None:
                return None
            else:
                return secgroup[0]

        except Exception as ex:
            Console.error("get secgroup")
            return None

    @classmethod
    def add_rule(cls, cloud, secgroup_uuid, from_port, to_port, protocol, cidr):
        try:

            # Get the nova client object
            cloud_provider = CloudProvider(cloud).provider

            # Create add secgroup rules to the cloud
            args = {
                'uuid': secgroup_uuid,
                'protocol': protocol,
                'from_port': from_port,
                'to_port': to_port,
                'cidr': cidr
            }
            rule_id = cloud_provider.add_secgroup_rule(**args)


            # create local db record
            rule = {"kind": "secgrouprule",
                    "uuid": str(rule_id),
                    "category": cloud,
                    "fromPort": from_port,
                    "toPort": to_port,
                    "protocol": protocol,
                    "cidr": cidr}
            """
            cls.cm.add(**rule)
            cls.cm.save()
            """
            Console.ok("Added rule {category} {uuid} {fromPort} {toPort} {protocol} {cidr}"
                       .format(**rule))
        except Exception as ex:
            if "This rule already exists" in ex.message:
                Console.ok("Rule already exists. Added rule.")
                return
            else:
                Console.error(ex.message, ex)
        return

    @classmethod
    def delete(cls,
               category='general',
               group=None,
               name=None):
        # name is anme of the rule

        if category=='general':
            if name is None and group is not None:

                # delete the entire group
                cls.cm.delete(kind="secgrouprule", group=group)

            elif name is not None and group is not None:
                # delete specific rule
                cls.cm.delete(name=name, kind="secgrouprule", group=group)
            elif name is None and group is None:
                # delete all groups
                cls.cm.delete(kind="secgrouprule")


            if Default.secgroup == group:
                Default.set_secgroup(None)

        else:
            provider = CloudProvider(category).provider

            # delete on cloud
            if  group is not None:
                provider.delete_secgroup(name)
                # delete the entire group
            elif group is None:
                # delete all groups
                pass




    @classmethod
    def delete_secgroup(cls, name=None, cloud=None):
        try:
            # Find the secgroup from the cloud
            cloud_provider = CloudProvider(cloud).provider
            result = cloud_provider.delete_secgroup(name)
            return result
        except Exception as ex:
            Console.error("delete group")

    @classmethod
    def delete_rule(cls, cloud, secgroup, from_port, to_port, protocol, cidr):
        try:
            args = {
                "group": secgroup["uuid"],
                "fromPort": from_port,
                "toPort": to_port,
                "protocol": protocol,
                "cidr": cidr
            }

            rule = cls.cm.find(kind="secgrouprule",
                               output="object",
                               scope="first",
                               **args)

            if rule is not None:
                # get the nova client for cloud
                cloud_provider = CloudProvider(cloud).provider
                # delete the rule from the cloud
                cloud_provider.delete_secgroup_rule(rule.uuid)
                # delete the local db record
                cls.cm.delete(rule)
                return "Rule [{fromPort} | {toPort} | {protocol} | {cidr}] deleted" \
                    .format(**args)
            else:
                return None

        except Exception as ex:
            Console.error("delete rule")

        return

    @classmethod
    def delete_all_rules(cls, secgroup):
        try:

            args = {
                "group": secgroup["uuid"]
            }
            rules = cls.cm.find(kind="secgrouprule", output="object", **args)

            if rules is not None:
                for rule in rules:
                    cls.cm.delete(rule)
                    Console.ok("Rule [{fromPort} | {toPort} | {protocol} | {cidr}] deleted"
                               .format(**rule))
            else:
                pass
        except Exception as ex:
            Console.error("delete all rules")

        return


if __name__ == '__main__':
    nova = CloudProvider.set("kilo")

    # groups = nova.security_groups.list()
    # print(groups)
    # print("\n\n")
    # d = SecGroup.convert_list_to_dict(groups)
    # print(d)

    # security_group = nova.security_groups.create(name="oct17_secgroup", description="Created by Gourav")
    print("Created sec group\n")

    # rule = nova.security_group_rules.create(security_group.id, ip_protocol="icmp",
    #                                        from_port=-1, to_port=-1, cidr="0.0.0.0/0")
    print("Created sec group rules\n")
    # print(rule)

    security_group = nova.security_groups.find(name="oct17_secgroup")
    rules = security_group.rules
    print(rules)

    d = SecGroup.convert_rules_to_dict(rules)
    print(d)

    nova.security_group_rules.delete('6220f8a4-e4fb-4340-bfe7-ffa028a7c6af')
    print("Deleted Sec Group Rule")
