from __future__ import print_function
from cloudmesh_client.db.CloudmeshDatabase import CloudmeshDatabase, CloudmeshMixin
from sqlalchemy import Column, Date, Integer, String


class DEFAULT(CloudmeshMixin, CloudmeshDatabase.Base):
    """table to store default values

    if the category is "global" it is meant to be a global variable

    todo: check if its global or general
    """
    __tablename__ = "default"
    __kind__ = 'default'
    __provider__ = 'general'

    value = Column(String)

    def __init__(self, **kwargs):
        super(DEFAULT, self).set_defaults(**kwargs)
        self.value = kwargs.get('value', None)
        print("KWARGS", kwargs)
        print("DDDDD", self.__dict__)


class VAR(CloudmeshMixin, CloudmeshDatabase.Base):
    """table to store peristant variable values
    """
    # name defined in mixin

    __tablename__ = "var"

    __kind__ = 'var'
    __provider__ = 'general'

    value = Column(String)

    def __init__(self,
                 name=None,
                 value=None,
                 type="str",
                 user=None):
        super(VAR, self).set_defaults(name=name, user=user)
        self.kind = 'var'

        self.type = str(type)
        self.value = str(value)


class LAUNCHER(CloudmeshMixin, CloudmeshDatabase.Base):
    """table to store default values

    if the category is "global" it is meant to be a global variable

    todo: check if its global or general
    """

    __tablename__ = "launcher"

    __kind__ = 'launcher'
    __provider__ = 'general'

    parameters = Column(String)  # This is the parameter represented as yaml object

    def __init__(self,
                 name=None,
                 user=None,
                 parameters=None):
        super(LAUNCHER, self).set_defaults(name=name, user=user)
        self.parameters = parameters


class KEY(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "key"

    __kind__ = 'key'
    __provider__ = 'general'

    value = Column(String)
    fingerprint = Column(String, unique=True)
    source = Column(String)
    comment = Column(String)
    uri = Column(String)
    is_default = Column(String)

    def __init__(self,
                 name,
                 value,
                 uri=None,
                 source=None,
                 fingerprint=None,
                 comment=None,
                 category=None,
                 user=None,
                 is_default="False"):
        super(KEY, self).set_defaults(name=name, user=user)

        self.value = value
        self.uri = uri
        self.comment = comment
        self.fingerprint = fingerprint
        self.source = source
        self.is_default = is_default


class GROUP(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "group"

    __kind__ = 'group'
    __provider__ = 'general'

    member = Column(String)
    species = Column(String)

    def __init__(self, **kwargs):
        super(GROUP, self).set_defaults(**kwargs)

        self.member = kwargs.get('member')
        self.species = kwargs.get('species') or 'vm'
        self.category = kwargs.get('category', 'general')
        self.type = 'str'

        print("INIT", kwargs, self.__dict__)


class RESERVATION(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "reservation"

    __kind__ = 'reservation'
    __provider__ = 'general'

    hosts = Column(String)  # should be list of strings
    description = Column(String)
    start_time = Column(String)  # date, time
    end_time = Column(String)  # date, time

    def __init__(self, user=None, name=None, hosts=None,
                 start=None, end=None, description=None,
                 project=None):
        super(RESERVATION, self).set_defaults(name=name, user=user)
        self.hosts = hosts
        self.start_time = start
        self.end_time = end
        self.description = description
        self.project = project


class SECGROUP(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "secgroup"

    __kind__ = 'secgroup'
    __provider__ = 'general'

    uuid = Column(String)

    def __init__(self,
                 name=None,
                 uuid=None,
                 user=None,
                 project=None):
        super(SECGROUP, self).set_defaults(name=name, user=user)

        self.uuid = uuid
        self.project = project


class SECGROUPRULE(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "secgrouprule"

    __kind__ = 'secgrouprule'
    __provider__ = 'general'

    groupid = Column(String)
    fromPort = Column(String)
    toPort = Column(String)
    protocol = Column(String)
    cidr = Column(String)
    uuid = Column(String)

    # noinspection PyPep8Naming
    def __init__(self,
                 uuid=None,
                 name=None,
                 groupid=None,
                 user=None,
                 project=None,
                 fromPort=None,
                 toPort=None,
                 protocol=None,
                 cidr=None):
        super(SECGROUPRULE, self).set_defaults(name=name, user=user)
        self.uuid = uuid
        self.groupid = groupid
        self.project = project
        self.fromPort = fromPort
        self.toPort = toPort
        self.protocol = protocol
        self.cidr = cidr


class BATCHJOB(CloudmeshMixin, CloudmeshDatabase.Base):
    __tablename__ = "batchjob"

    __kind__ = 'batchjob'
    __provider__ = 'general'

    dir = Column(String, default="string")
    nodes = Column(String, default="string")
    output_file = Column(String, default="string")
    queue = Column(String, default="string")
    time = Column(String, default="string")
    cluster = Column(String, default="string")
    sbatch_file_path = Column(String, default="string")
    cmd = Column(String, default="string")
    time = Column(String, default="string")
    group = Column(String, default="string")
    job_id = Column(String, default="string")

    def __init__(self,
                 name,
                 user=None,
                 category=None,
                 **kwargs
                 ):
        super(BATCHJOB, self).set_defaults(name=name, user=user)
        self.dir = kwargs.get('dir')
        self.nodes = kwargs.get('nodes')
        self.output_file = kwargs.pop('output_file')
        self.queue = kwargs.pop('queue')
        self.time = kwargs.pop('time')
        self.cluster = kwargs.pop('cluster')
        self.sbatch_file_path = kwargs.pop('sbatch_file_path')
        self.cmd = kwargs.pop('cmd')
        self.time = kwargs.pop('time')
        self.group = kwargs.pop('group')
        self.job_id = kwargs.pop('job_id')