"""This module contains the general information for ExtpolClientCont ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class ExtpolClientContConsts():
    pass


class ExtpolClientCont(ManagedObject):
    """This is ExtpolClientCont class."""

    consts = ExtpolClientContConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtpolClientCont", "extpolClientCont", "clients", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin"], [u'extpolRegistry'], [u'extpolClient', u'extpolDomain', u'extpolHBStatus'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "gen_num": MoPropertyMeta("gen_num", "genNum", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "genNum": "gen_num", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.gen_num = None
        self.status = None

        ManagedObject.__init__(self, "ExtpolClientCont", parent_mo_or_dn, **kwargs)

