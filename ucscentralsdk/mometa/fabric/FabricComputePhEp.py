"""This module contains the general information for FabricComputePhEp ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class FabricComputePhEpConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CHASSIS_ID_N_A = "N/A"
    EQ_TYPE_BLADE = "blade"
    EQ_TYPE_CARTRIDGE = "cartridge"
    EQ_TYPE_CHASSIS = "chassis"
    EQ_TYPE_FEX = "fex"
    EQ_TYPE_RACK_UNIT = "rack-unit"
    EQ_TYPE_SERVER_UNIT = "server-unit"
    EQ_TYPE_UNKNOWN = "unknown"
    LC_IN_SERVICE = "in-service"
    LC_MIGRATE = "migrate"
    LC_OUT_OF_SERVICE = "out-of-service"


class FabricComputePhEp(ManagedObject):
    """This is FabricComputePhEp class."""

    consts = FabricComputePhEpConsts()
    naming_props = set([u'vendor', u'model', u'serial'])

    mo_meta = MoMeta("FabricComputePhEp", "fabricComputePhEp", "compute-ep-ven-[vendor]-mod-[model]-ser-[serial]", VersionMeta.Version112a, "InputOutput", 0x3ff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'fabricDceSrv'], [u'fabricComputePhEpOperation'], ["Get", "Set"])

    prop_meta = {
        "address": MoPropertyMeta("address", "address", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["N/A"], ["1-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "eq_type": MoPropertyMeta("eq_type", "eqType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blade", "cartridge", "chassis", "fex", "rack-unit", "server-unit", "unknown"], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-service", "migrate", "out-of-service"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, 1, 32, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x200, 1, 510, None, [], []), 
    }

    prop_map = {
        "address": "address", 
        "adminState": "admin_state", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "eqType": "eq_type", 
        "lc": "lc", 
        "model": "model", 
        "name": "name", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "slotId": "slot_id", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, serial, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.serial = serial
        self.address = None
        self.admin_state = None
        self.chassis_id = None
        self.child_action = None
        self.eq_type = None
        self.lc = None
        self.name = None
        self.revision = None
        self.slot_id = None
        self.status = None

        ManagedObject.__init__(self, "FabricComputePhEp", parent_mo_or_dn, **kwargs)

