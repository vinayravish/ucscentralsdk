"""This module contains the general information for MgmtSvc ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class MgmtSvcConsts():
    RESTARTABLE_FALSE = "false"
    RESTARTABLE_NO = "no"
    RESTARTABLE_TRUE = "true"
    RESTARTABLE_YES = "yes"


class MgmtSvc(ManagedObject):
    """This is MgmtSvc class."""

    consts = MgmtSvcConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("MgmtSvc", "mgmtSvc", "mgmt-svc-[name]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], [u'mgmtEp'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "restartable": MoPropertyMeta("restartable", "restartable", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "restartable": "restartable", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.restartable = None
        self.status = None

        ManagedObject.__init__(self, "MgmtSvc", parent_mo_or_dn, **kwargs)
