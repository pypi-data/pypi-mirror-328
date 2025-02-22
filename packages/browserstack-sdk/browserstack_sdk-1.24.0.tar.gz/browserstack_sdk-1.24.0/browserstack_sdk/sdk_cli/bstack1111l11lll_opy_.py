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
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1lllll11l1l_opy_, bstack11111l1l11_opy_
class bstack111l111111_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l1l1l_opy_ (u"ࠦࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥዢ").format(self.name)
class bstack1111l1llll_opy_(Enum):
    NONE = 0
    bstack11111lll1l_opy_ = 1
    bstack111l11111l_opy_ = 2
    bstack1l1l1ll1l1l_opy_ = 3
    QUIT = 4
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack11l1l1l_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧዣ").format(self.name)
class bstack1111lllll1_opy_(bstack1lllll11l1l_opy_):
    framework_name: str
    framework_version: str
    state: bstack1111l1llll_opy_
    previous_state: bstack1111l1llll_opy_
    bstack1lllll1ll11_opy_: datetime
    bstack1l1ll111111_opy_: datetime
    def __init__(
        self,
        context: bstack11111l1l11_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1111l1llll_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1111l1llll_opy_.NONE
        self.bstack1lllll1ll11_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1ll111111_opy_ = datetime.now(tz=timezone.utc)
    def bstack1111l1l11l_opy_(self, bstack1l1ll111l11_opy_: bstack1111l1llll_opy_):
        bstack1l1ll1111ll_opy_ = bstack1111l1llll_opy_(bstack1l1ll111l11_opy_).name
        if not bstack1l1ll1111ll_opy_:
            return False
        if bstack1l1ll111l11_opy_ == self.state:
            return False
        if (
            bstack1l1ll111l11_opy_ == bstack1111l1llll_opy_.NONE
            or (self.state != bstack1111l1llll_opy_.NONE and bstack1l1ll111l11_opy_ == bstack1111l1llll_opy_.bstack11111lll1l_opy_)
            or (self.state < bstack1111l1llll_opy_.bstack11111lll1l_opy_ and bstack1l1ll111l11_opy_ == bstack1111l1llll_opy_.bstack111l11111l_opy_)
            or (self.state < bstack1111l1llll_opy_.bstack11111lll1l_opy_ and bstack1l1ll111l11_opy_ == bstack1111l1llll_opy_.QUIT)
        ):
            raise ValueError(bstack11l1l1l_opy_ (u"ࠨࡩ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡶࡤࡸࡪࠦࡴࡳࡣࡱࡷ࡮ࡺࡩࡰࡰ࠽ࠤࠧዤ") + str(self.state) + bstack11l1l1l_opy_ (u"ࠢࠡ࠿ࡁࠤࠧዥ") + str(bstack1l1ll111l11_opy_))
        self.previous_state = self.state
        self.state = bstack1l1ll111l11_opy_
        self.bstack1l1ll111111_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lllll1l1l1_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll11ll11l_opy_: Dict[str, bstack1111lllll1_opy_] = dict()
    framework_name: str
    framework_version: str
    classes: List[Type]
    def __init__(
        self,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
    ):
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.classes = classes
    @abc.abstractmethod
    def bstack1l1l1lllll1_opy_(self, instance: bstack1111lllll1_opy_, method_name: str, bstack1l1l1llll1l_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1l1llll11_opy_(
        self, method_name, previous_state: bstack1111l1llll_opy_, *args, **kwargs
    ) -> bstack1111l1llll_opy_:
        return
    @abc.abstractmethod
    def bstack1l1l1lll1ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1l1lll11l_opy_(self, bstack1l1l1ll1lll_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1l1l1ll1lll_opy_:
                bstack1l1l1ll1ll1_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1l1l1ll1ll1_opy_):
                    self.logger.warning(bstack11l1l1l_opy_ (u"ࠣࡷࡱࡴࡦࡺࡣࡩࡧࡧࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࠨዦ") + str(method_name) + bstack11l1l1l_opy_ (u"ࠤࠥዧ"))
                    continue
                bstack1l1l1llllll_opy_ = self.bstack1l1l1llll11_opy_(
                    method_name, previous_state=bstack1111l1llll_opy_.NONE
                )
                bstack1l1l1lll111_opy_ = self.bstack1l1l1ll1l11_opy_(
                    method_name,
                    (bstack1l1l1llllll_opy_ if bstack1l1l1llllll_opy_ else bstack1111l1llll_opy_.NONE),
                    bstack1l1l1ll1ll1_opy_,
                )
                if not callable(bstack1l1l1lll111_opy_):
                    self.logger.warning(bstack11l1l1l_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠣࡲࡴࡺࠠࡱࡣࡷࡧ࡭࡫ࡤ࠻ࠢࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࠫࡿࡸ࡫࡬ࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀ࠾ࠥࠨየ") + str(self.framework_version) + bstack11l1l1l_opy_ (u"ࠦ࠮ࠨዩ"))
                    continue
                setattr(clazz, method_name, bstack1l1l1lll111_opy_)
    def bstack1l1l1ll1l11_opy_(
        self,
        method_name: str,
        bstack1l1l1llllll_opy_: bstack1111l1llll_opy_,
        bstack1l1l1ll1ll1_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1l1lll1l1l_opy_ = datetime.now()
            (bstack1l1l1llllll_opy_,) = wrapped.__vars__
            bstack1l1l1llllll_opy_ = (
                bstack1l1l1llllll_opy_
                if bstack1l1l1llllll_opy_ and bstack1l1l1llllll_opy_ != bstack1111l1llll_opy_.NONE
                else self.bstack1l1l1llll11_opy_(method_name, previous_state=bstack1l1l1llllll_opy_, *args, **kwargs)
            )
            if bstack1l1l1llllll_opy_ == bstack1111l1llll_opy_.bstack11111lll1l_opy_:
                ctx = bstack1lllll11l1l_opy_.create_context(target)
                bstack1lllll1l1l1_opy_.bstack1lll11ll11l_opy_[ctx.id] = bstack1111lllll1_opy_(
                    ctx, self.framework_name, self.framework_version, bstack1l1l1llllll_opy_
                )
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡣࡳࡧࡤࡸࡪࡪ࠺ࠡࡽࡷࡥࡷ࡭ࡥࡵ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡧࡹࡾ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨዪ") + str(bstack1lllll1l1l1_opy_.bstack1lll11ll11l_opy_.keys()) + bstack11l1l1l_opy_ (u"ࠨࠢያ"))
            else:
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠢࡸࡴࡤࡴࡵ࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤࠡ࡫ࡱࡺࡴࡱࡥࡥ࠼ࠣࡿࡹࡧࡲࡨࡧࡷ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤዬ") + str(bstack1lllll1l1l1_opy_.bstack1lll11ll11l_opy_.keys()) + bstack11l1l1l_opy_ (u"ࠣࠤይ"))
            instance = bstack1lllll1l1l1_opy_.bstack1lll11l1ll1_opy_(target)
            if bstack1l1l1llllll_opy_ == bstack1111l1llll_opy_.NONE or not instance:
                ctx = bstack1lllll11l1l_opy_.create_context(target)
                self.logger.warning(bstack11l1l1l_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣࡹࡳࡺࡲࡢࡥ࡮ࡩࡩࡀࠠࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡣࡵࡺࡀࡿࡨࡺࡸࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨዮ") + str(bstack1lllll1l1l1_opy_.bstack1lll11ll11l_opy_.keys()) + bstack11l1l1l_opy_ (u"ࠥࠦዯ"))
                return bstack1l1l1ll1ll1_opy_(target, *args, **kwargs)
            bstack1ll1lllllll_opy_ = self.bstack1l1l1lll1ll_opy_(
                target,
                (instance, method_name),
                (bstack1l1l1llllll_opy_, bstack111l111111_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1111l1l11l_opy_(bstack1l1l1llllll_opy_):
                self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠥࡹࡴࡢࡶࡨ࠱ࡹࡸࡡ࡯ࡵ࡬ࡸ࡮ࡵ࡮࠻ࠢࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡶࡲࡦࡸ࡬ࡳࡺࡹ࡟ࡴࡶࡤࡸࡪࢃࠠ࠾ࡀࠣࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡳࡵࡣࡷࡩࢂࠦࠨࡼࡶࡼࡴࡪ࠮ࡴࡢࡴࡪࡩࡹ࠯ࡽ࠯ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡽࡤࡶ࡬ࡹࡽࠪࠢ࡞ࠦደ") + str(instance.ref()) + bstack11l1l1l_opy_ (u"ࠧࡣࠢዱ"))
            result = (
                bstack1ll1lllllll_opy_(target, bstack1l1l1ll1ll1_opy_, *args, **kwargs)
                if callable(bstack1ll1lllllll_opy_)
                else bstack1l1l1ll1ll1_opy_(target, *args, **kwargs)
            )
            bstack1l1l1lll1l1_opy_ = self.bstack1l1l1lll1ll_opy_(
                target,
                (instance, method_name),
                (bstack1l1l1llllll_opy_, bstack111l111111_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1l1lllll1_opy_(instance, method_name, datetime.now() - bstack1l1lll1l1l_opy_, *args, **kwargs)
            return bstack1l1l1lll1l1_opy_ if bstack1l1l1lll1l1_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1l1llllll_opy_,)
        return wrapped
    @staticmethod
    def bstack1lll11l1ll1_opy_(target: object, strict=True):
        ctx = bstack1lllll11l1l_opy_.create_context(target)
        instance = bstack1lllll1l1l1_opy_.bstack1lll11ll11l_opy_.get(ctx.id, None)
        if instance and instance.bstack1lllll11ll1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1ll1111l1ll_opy_(
        ctx: bstack11111l1l11_opy_, state: bstack1111l1llll_opy_, reverse=True
    ) -> List[bstack1111lllll1_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lllll1l1l1_opy_.bstack1lll11ll11l_opy_.values(),
            ),
            key=lambda t: t.bstack1lllll1ll11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1111ll111l_opy_(instance: bstack1111lllll1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack111l1111l1_opy_(instance: bstack1111lllll1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1111l1l11l_opy_(instance: bstack1111lllll1_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lllll1l1l1_opy_.logger.debug(bstack11l1l1l_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡ࡭ࡨࡽࡂࢁ࡫ࡦࡻࢀࠤࡻࡧ࡬ࡶࡧࡀࠦዲ") + str(value) + bstack11l1l1l_opy_ (u"ࠢࠣዳ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lllll1l1l1_opy_.bstack1lll11l1ll1_opy_(target, strict)
        return bstack1lllll1l1l1_opy_.bstack111l1111l1_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lllll1l1l1_opy_.bstack1lll11l1ll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True