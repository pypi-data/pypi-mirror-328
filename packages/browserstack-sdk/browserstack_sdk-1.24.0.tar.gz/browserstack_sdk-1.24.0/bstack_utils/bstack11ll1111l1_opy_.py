# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack1lllll1l_opy_ = 7
def bstack11l1l1l_opy_ (bstack1l111ll_opy_):
    global bstack111111l_opy_
    bstack111ll11_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1l111_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11lll11_opy_ = bstack111ll11_opy_ % len (bstack1l1l111_opy_)
    bstack111ll1l_opy_ = bstack1l1l111_opy_ [:bstack11lll11_opy_] + bstack1l1l111_opy_ [bstack11lll11_opy_:]
    if bstack111ll1_opy_:
        bstack11ll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack11ll111_opy_ + bstack111ll11_opy_) % bstack1lllll1l_opy_) for bstack11ll111_opy_, char in enumerate (bstack111ll1l_opy_)])
    else:
        bstack11ll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack11ll111_opy_ + bstack111ll11_opy_) % bstack1lllll1l_opy_) for bstack11ll111_opy_, char in enumerate (bstack111ll1l_opy_)])
    return eval (bstack11ll1ll_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack111111l1l_opy_ import get_logger
logger = get_logger(__name__)
bstack1l1l11l111l_opy_: Dict[str, float] = {}
bstack1l1l11l1l11_opy_: List = []
bstack1l1ll1l11l_opy_ = os.path.join(os.getcwd(), bstack11l1l1l_opy_ (u"ࠬࡲ࡯ࡨࠩᎵ"), bstack11l1l1l_opy_ (u"࠭࡫ࡦࡻ࠰ࡱࡪࡺࡲࡪࡥࡶ࠲࡯ࡹ࡯࡯ࠩᎶ"))
logging.getLogger(bstack11l1l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠩᎷ")).setLevel(logging.WARNING)
lock = FileLock(bstack1l1ll1l11l_opy_+bstack11l1l1l_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᎸ"))
class bstack1l1l11l11ll_opy_:
    duration: float
    name: str
    startTime: float
    worker: int
    status: bool
    failure: str
    details: Optional[str]
    entryType: str
    platform: Optional[int]
    command: Optional[str]
    hookType: Optional[str]
    cli: Optional[bool]
    def __init__(self, duration: float, name: str, start_time: float, bstack1l1l11l1ll1_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack1l1l11l1ll1_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11l1l1l_opy_ (u"ࠤࡰࡩࡦࡹࡵࡳࡧࠥᎹ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1111lll111_opy_:
    global bstack1l1l11l111l_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack1l1l11l111l_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11l1l1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᎺ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1111lll111_opy_.mark(end)
            bstack1111lll111_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11l1l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᎻ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack1l1l11l111l_opy_ or end not in bstack1l1l11l111l_opy_:
                logger.debug(bstack11l1l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦ࡫ࡦࡻࠣࡻ࡮ࡺࡨࠡࡸࡤࡰࡺ࡫ࠠࡼࡿࠣࡳࡷࠦࡥ࡯ࡦࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠢᎼ").format(start,end))
                return
            duration: float = bstack1l1l11l111l_opy_[end] - bstack1l1l11l111l_opy_[start]
            bstack1l1l11l1lll_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤᎽ"), bstack11l1l1l_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨᎾ")).lower() == bstack11l1l1l_opy_ (u"ࠣࡶࡵࡹࡪࠨᎿ")
            bstack1l1l11l1l1l_opy_: bstack1l1l11l11ll_opy_ = bstack1l1l11l11ll_opy_(duration, label, bstack1l1l11l111l_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11l1l1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤᏀ"), 0), command, test_name, hook_type, bstack1l1l11l1lll_opy_)
            del bstack1l1l11l111l_opy_[start]
            del bstack1l1l11l111l_opy_[end]
            bstack1111lll111_opy_.bstack1l1l11l11l1_opy_(bstack1l1l11l1l1l_opy_)
        except Exception as e:
            logger.debug(bstack11l1l1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᏁ").format(e))
    @staticmethod
    def bstack1l1l11l11l1_opy_(bstack1l1l11l1l1l_opy_):
        os.makedirs(os.path.dirname(bstack1l1ll1l11l_opy_)) if not os.path.exists(os.path.dirname(bstack1l1ll1l11l_opy_)) else None
        try:
            with lock:
                with open(bstack1l1ll1l11l_opy_, bstack11l1l1l_opy_ (u"ࠦࡷ࠱ࠢᏂ"), encoding=bstack11l1l1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᏃ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack1l1l11l1l1l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError:
            with lock:
                with open(bstack1l1ll1l11l_opy_, bstack11l1l1l_opy_ (u"ࠨࡷࠣᏄ"), encoding=bstack11l1l1l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᏅ")) as file:
                    data = [bstack1l1l11l1l1l_opy_.__dict__]
                    json.dump(data, file, indent=4)
    @staticmethod
    def bstack1l1l11ll11l_opy_(label: str) -> str:
        try:
            return bstack11l1l1l_opy_ (u"ࠣࡽࢀ࠾ࢀࢃࠢᏆ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11l1l1l_opy_ (u"ࠤࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᏇ").format(e))