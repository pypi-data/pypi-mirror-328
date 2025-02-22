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
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1lllll11l1l_opy_, bstack11111l1l11_opy_
class bstack11111111ll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l1l1l_opy_ (u"ࠥࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨኰ").format(self.name)
class bstack111111lll1_opy_(Enum):
    NONE = 0
    BEFORE_ALL = 1
    LOG = 2
    SETUP_FIXTURE = 3
    INIT_TEST = 4
    BEFORE_EACH = 5
    AFTER_EACH = 6
    TEST = 7
    STEP = 8
    LOG_REPORT = 9
    AFTER_ALL = 10
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack11l1l1l_opy_ (u"࡙ࠦ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧ኱").format(self.name)
class bstack1lllllll1l1_opy_(bstack1lllll11l1l_opy_):
    bstack1lll1llllll_opy_: List[str]
    bstack1llll1l1lll_opy_: Dict[str, str]
    state: bstack111111lll1_opy_
    bstack1lllll1ll11_opy_: datetime
    bstack1l1ll111111_opy_: datetime
    def __init__(
        self,
        context: bstack11111l1l11_opy_,
        bstack1lll1llllll_opy_: List[str],
        bstack1llll1l1lll_opy_: Dict[str, str],
        state=bstack111111lll1_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1lll1llllll_opy_ = bstack1lll1llllll_opy_
        self.bstack1llll1l1lll_opy_ = bstack1llll1l1lll_opy_
        self.state = state
        self.bstack1lllll1ll11_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1ll111111_opy_ = datetime.now(tz=timezone.utc)
    def bstack1111l1l11l_opy_(self, bstack1l1ll111l11_opy_: bstack111111lll1_opy_):
        bstack1l1ll1111ll_opy_ = bstack111111lll1_opy_(bstack1l1ll111l11_opy_).name
        if not bstack1l1ll1111ll_opy_:
            return False
        if bstack1l1ll111l11_opy_ == self.state:
            return False
        self.state = bstack1l1ll111l11_opy_
        self.bstack1l1ll111111_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1lll1l11l1l_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1lll1l1l1l1_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1ll1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠣኲ")
    bstack1lll1l111l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡮ࡪࠢኳ")
    bstack1lll1ll1111_opy_ = bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠥኴ")
    bstack1lll1ll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡣࡵࡧࡴࡩࠤኵ")
    bstack1lll1lll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡵࡣࡪࡷࠧ኶")
    bstack1111111111_opy_ = bstack11l1l1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡷࡺࡲࡴࠣ኷")
    bstack1lll1l111ll_opy_ = bstack11l1l1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡸࡻ࡬ࡵࡡࡤࡸࠧኸ")
    bstack1lll11llll1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢኹ")
    bstack1llll11ll11_opy_ = bstack11l1l1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡪࡴࡤࡦࡦࡢࡥࡹࠨኺ")
    bstack1lll1l1lll1_opy_ = bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢኻ")
    bstack1lll1lll1ll_opy_ = bstack11l1l1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠢኼ")
    bstack1lll1ll1l11_opy_ = bstack11l1l1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠦኽ")
    bstack1llll1l111l_opy_ = bstack11l1l1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡥࡲࡨࡪࠨኾ")
    bstack1lll11lll11_opy_ = bstack11l1l1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪࠨ኿")
    bstack1111ll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࠨዀ")
    bstack111111l11l_opy_ = bstack11l1l1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡧࡩ࡭ࡷࡵࡩࠧ዁")
    bstack1lll111ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠦዂ")
    bstack1llll1ll111_opy_ = bstack11l1l1l_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡬ࡰࡩࡶࠦዃ")
    bstack1llll1111l1_opy_ = bstack11l1l1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡮ࡧࡷࡥࠧዄ")
    bstack1l1ll111l1l_opy_ = bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡵࡦࡳࡵ࡫ࡳࠨዅ")
    bstack11111l1lll_opy_ = bstack11l1l1l_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧ዆")
    bstack1lll111l111_opy_ = bstack11l1l1l_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣ዇")
    bstack1lll1111ll1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤ࡫࡮ࡥࡧࡧࡣࡦࡺࠢወ")
    bstack1llll11l1ll_opy_ = bstack11l1l1l_opy_ (u"ࠢࡩࡱࡲ࡯ࡤ࡯ࡤࠣዉ")
    bstack1llll111l1l_opy_ = bstack11l1l1l_opy_ (u"ࠣࡪࡲࡳࡰࡥࡲࡦࡵࡸࡰࡹࠨዊ")
    bstack1llll1l11ll_opy_ = bstack11l1l1l_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟࡭ࡱࡪࡷࠧዋ")
    bstack1llll1l1ll1_opy_ = bstack11l1l1l_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪࠨዌ")
    bstack1lll11ll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠦࡵ࡫࡮ࡥ࡫ࡱ࡫ࠧው")
    bstack1lll11lllll_opy_ = bstack11l1l1l_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨዎ")
    bstack1l1lll1ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠨࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠣዏ")
    bstack1llll111l11_opy_ = bstack11l1l1l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡒࡏࡈࠤዐ")
    bstack1lll11ll11l_opy_: Dict[str, bstack1lllllll1l1_opy_] = dict()
    bstack1l1ll1111l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1lll1llllll_opy_: List[str]
    bstack1llll1l1lll_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1lll1llllll_opy_: List[str],
        bstack1llll1l1lll_opy_: Dict[str, str],
    ):
        self.bstack1lll1llllll_opy_ = bstack1lll1llllll_opy_
        self.bstack1llll1l1lll_opy_ = bstack1llll1l1lll_opy_
    def track_event(
        self,
        context: bstack1lll1l11l1l_opy_,
        test_framework_state: bstack111111lll1_opy_,
        test_hook_state: bstack11111111ll_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢዑ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠤࠥዒ"))
    def bstack1lll1l11l11_opy_(
        self,
        instance: bstack1lllllll1l1_opy_,
        bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll111lll_opy_ = TestFramework.bstack1l1ll111ll1_opy_(bstack111l11llll_opy_)
        if not bstack1l1ll111lll_opy_ in TestFramework.bstack1l1ll1111l1_opy_:
            return
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠥ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࠨዓ") + str(len(TestFramework.bstack1l1ll1111l1_opy_[bstack1l1ll111lll_opy_])) + bstack11l1l1l_opy_ (u"ࠦࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠣዔ"))
        for callback in TestFramework.bstack1l1ll1111l1_opy_[bstack1l1ll111lll_opy_]:
            try:
                callback(self, instance, bstack111l11llll_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11l1l1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࠥዕ") + str(e) + bstack11l1l1l_opy_ (u"ࠨࠢዖ"))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1lll11l1111_opy_(self):
        return
    @abc.abstractmethod
    def bstack1llll1111ll_opy_(self, instance, bstack111l11llll_opy_):
        return
    @abc.abstractmethod
    def bstack1lll11l111l_opy_(self, instance, bstack111l11llll_opy_):
        return
    @staticmethod
    def bstack1lll11l1ll1_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1lllll11l1l_opy_.create_context(target)
        instance = TestFramework.bstack1lll11ll11l_opy_.get(ctx.id, None)
        if instance and instance.bstack1lllll11ll1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l1lllll1ll_opy_(reverse=True) -> List[bstack1lllllll1l1_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll11ll11l_opy_.values(),
            ),
            key=lambda t: t.bstack1lllll1ll11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1ll1111l1ll_opy_(ctx: bstack11111l1l11_opy_, reverse=True) -> List[bstack1lllllll1l1_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll11ll11l_opy_.values(),
            ),
            key=lambda t: t.bstack1lllll1ll11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1111ll111l_opy_(instance: bstack1lllllll1l1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack111l1111l1_opy_(instance: bstack1lllllll1l1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1111l1l11l_opy_(instance: bstack1lllllll1l1_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡴࡧࡷࡣࡸࡺࡡࡵࡧ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢ࡮ࡩࡾࡃࡻ࡬ࡧࡼࢁࠥࡼࡡ࡭ࡷࡨࡁࠧ዗") + str(value) + bstack11l1l1l_opy_ (u"ࠣࠤዘ"))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1lll1l1ll1l_opy_(instance: bstack1lllllll1l1_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11l1l1l_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩࡤ࡫࡮ࡵࡴ࡬ࡩࡸࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫࡮ࡵࡴ࡬ࡩࡸࡃࠢዙ") + str(entries) + bstack11l1l1l_opy_ (u"ࠥࠦዚ"))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l1ll11111l_opy_(instance: bstack111111lll1_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡣࡸࡺࡡࡵࡧ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢ࡮ࡩࡾࡃࡻ࡬ࡧࡼࢁࠥࡼࡡ࡭ࡷࡨࡁࠧዛ") + str(value) + bstack11l1l1l_opy_ (u"ࠧࠨዜ"))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1lll11l1ll1_opy_(target, strict)
        return TestFramework.bstack111l1111l1_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1lll11l1ll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l1ll111ll1_opy_(bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_]):
        return bstack11l1l1l_opy_ (u"ࠨ࠺ࠣዝ").join((bstack111111lll1_opy_(bstack111l11llll_opy_[0]).name, bstack11111111ll_opy_(bstack111l11llll_opy_[1]).name))
    @staticmethod
    def bstack1111ll1l1l_opy_(bstack111l11llll_opy_: Tuple[bstack111111lll1_opy_, bstack11111111ll_opy_], callback: Callable):
        bstack1l1ll111lll_opy_ = TestFramework.bstack1l1ll111ll1_opy_(bstack111l11llll_opy_)
        TestFramework.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡴࡧࡷࡣ࡭ࡵ࡯࡬ࡡࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥ࡮࡯ࡰ࡭ࡢࡶࡪ࡭ࡩࡴࡶࡵࡽࡤࡱࡥࡺ࠿ࠥዞ") + str(bstack1l1ll111lll_opy_) + bstack11l1l1l_opy_ (u"ࠣࠤዟ"))
        if not bstack1l1ll111lll_opy_ in TestFramework.bstack1l1ll1111l1_opy_:
            TestFramework.bstack1l1ll1111l1_opy_[bstack1l1ll111lll_opy_] = []
        TestFramework.bstack1l1ll1111l1_opy_[bstack1l1ll111lll_opy_].append(callback)
    @staticmethod
    def bstack1lll11l1l1l_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11l1l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡴࡪࡰࡶࠦዠ"):
            return klass.__qualname__
        return module + bstack11l1l1l_opy_ (u"ࠥ࠲ࠧዡ") + klass.__qualname__
    @staticmethod
    def bstack1lll1ll1lll_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}