"""This module contains the general information for ControllerEpFsmStage ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class ControllerEpFsmStageConsts():
    LAST_UPDATE_TIME_ = ""
    NAME_QUIESCE_BEGIN = "QuiesceBegin"
    NAME_QUIESCE_FAIL = "QuiesceFail"
    NAME_QUIESCE_QUIESCE_IDMGR = "QuiesceQuiesceIDMgr"
    NAME_QUIESCE_QUIESCE_MGMT_CONTROLLER = "QuiesceQuiesceMgmtController"
    NAME_QUIESCE_QUIESCE_OPS_MGR = "QuiesceQuiesceOpsMgr"
    NAME_QUIESCE_QUIESCE_POLICY_MGR = "QuiesceQuiescePolicyMgr"
    NAME_QUIESCE_QUIESCE_RES_MGR = "QuiesceQuiesceResMgr"
    NAME_QUIESCE_QUIESCE_STATS_MGR = "QuiesceQuiesceStatsMgr"
    NAME_QUIESCE_SUCCESS = "QuiesceSuccess"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class ControllerEpFsmStage(ManagedObject):
    """This is ControllerEpFsmStage class."""

    consts = ControllerEpFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ControllerEpFsmStage", "controllerEpFsmStage", "stage-[name]", VersionMeta.Version141a, "OutputOnly", 0xf, [], [""], [u'controllerEpFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, None, None, None, None, ["QuiesceBegin", "QuiesceFail", "QuiesceQuiesceIDMgr", "QuiesceQuiesceMgmtController", "QuiesceQuiesceOpsMgr", "QuiesceQuiescePolicyMgr", "QuiesceQuiesceResMgr", "QuiesceQuiesceStatsMgr", "QuiesceSuccess", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "ControllerEpFsmStage", parent_mo_or_dn, **kwargs)

