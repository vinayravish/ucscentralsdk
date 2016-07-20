"""This module contains the general information for BiosVfOnboardSATAController ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class BiosVfOnboardSATAControllerConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_ONBOARD_SATACONTROLLER_DISABLED = "disabled"
    VP_ONBOARD_SATACONTROLLER_ENABLED = "enabled"
    VP_ONBOARD_SATACONTROLLER_PLATFORM_DEFAULT = "platform-default"
    VP_ONBOARD_SATACONTROLLER_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SATAMODE_AHCI = "ahci"
    VP_SATAMODE_COMPATIBILITY = "compatibility"
    VP_SATAMODE_ENHANCED = "enhanced"
    VP_SATAMODE_PLATFORM_DEFAULT = "platform-default"
    VP_SATAMODE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_SATAMODE_SW_RAID = "sw-raid"


class BiosVfOnboardSATAController(ManagedObject):
    """This is BiosVfOnboardSATAController class."""

    consts = BiosVfOnboardSATAControllerConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfOnboardSATAController", "biosVfOnboardSATAController", "Onboard-SATA-controller", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["read-only"], [u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_onboard_sata_controller": MoPropertyMeta("vp_onboard_sata_controller", "vpOnboardSATAController", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
        "vp_sata_mode": MoPropertyMeta("vp_sata_mode", "vpSATAMode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["ahci", "compatibility", "enhanced", "platform-default", "platform-recommended", "sw-raid"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpOnboardSATAController": "vp_onboard_sata_controller", 
        "vpSATAMode": "vp_sata_mode", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_onboard_sata_controller = None
        self.vp_sata_mode = None

        ManagedObject.__init__(self, "BiosVfOnboardSATAController", parent_mo_or_dn, **kwargs)

