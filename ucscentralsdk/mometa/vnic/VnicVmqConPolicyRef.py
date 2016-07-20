"""This module contains the general information for VnicVmqConPolicyRef ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class VnicVmqConPolicyRefConsts():
    pass


class VnicVmqConPolicyRef(ManagedObject):
    """This is VnicVmqConPolicyRef class."""

    consts = VnicVmqConPolicyRefConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicVmqConPolicyRef", "vnicVmqConPolicyRef", "vmq-con-ref", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["admin", "ls-config", "ls-network", "ls-server"], [u'vnicEther', u'vnicLanConnTempl'], [u'faultInst'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "oper_con_policy_name": MoPropertyMeta("oper_con_policy_name", "operConPolicyName", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "operConPolicyName": "oper_con_policy_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.con_policy_name = None
        self.oper_con_policy_name = None
        self.status = None

        ManagedObject.__init__(self, "VnicVmqConPolicyRef", parent_mo_or_dn, **kwargs)

