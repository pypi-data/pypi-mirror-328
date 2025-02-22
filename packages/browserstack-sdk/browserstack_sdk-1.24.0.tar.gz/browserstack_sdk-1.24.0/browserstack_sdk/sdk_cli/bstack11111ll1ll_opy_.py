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
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1111l11lll_opy_ import (
    bstack1lllll1l1l1_opy_,
    bstack1111lllll1_opy_,
    bstack1111l1llll_opy_,
    bstack111l111111_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1111l1ll1l_opy_(bstack1lllll1l1l1_opy_):
    bstack1l1l1l1l111_opy_ = bstack11l1l1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨጇ")
    NAME = bstack11l1l1l_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤገ")
    bstack1ll1111llll_opy_ = bstack11l1l1l_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭ࠤጉ")
    bstack1ll1111l111_opy_ = bstack11l1l1l_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤጊ")
    bstack1l1l11llll1_opy_ = bstack11l1l1l_opy_ (u"ࠥ࡭ࡳࡶࡵࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣጋ")
    bstack1l1lll1111l_opy_ = bstack11l1l1l_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥጌ")
    bstack1l1lllllll1_opy_ = bstack11l1l1l_opy_ (u"ࠧ࡯ࡳࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡩࡷࡥࠦግ")
    bstack1l1l1l111l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥጎ")
    bstack1l1l1l11111_opy_ = bstack11l1l1l_opy_ (u"ࠢࡦࡰࡧࡩࡩࡥࡡࡵࠤጏ")
    bstack1111ll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࠤጐ")
    bstack1111ll1lll_opy_ = bstack11l1l1l_opy_ (u"ࠤࡱࡩࡼࡹࡥࡴࡵ࡬ࡳࡳࠨ጑")
    bstack1l1l1l11l1l_opy_ = bstack11l1l1l_opy_ (u"ࠥ࡫ࡪࡺࠢጒ")
    bstack1ll11111ll1_opy_ = bstack11l1l1l_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣጓ")
    bstack1l1l1l1l1l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࠣጔ")
    bstack1l1l1l11lll_opy_ = bstack11l1l1l_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࡣࡶࡽࡳࡩࠢጕ")
    bstack1l1l11lll1l_opy_ = bstack11l1l1l_opy_ (u"ࠢࡲࡷ࡬ࡸࠧ጖")
    bstack1l1ll1111l1_opy_: Dict[str, List[Callable]] = dict()
    bstack111l1l1l11_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1111ll1111_opy_: Any
    bstack1l1l11lllll_opy_: Dict
    def __init__(
        self,
        bstack111l1l1l11_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1111ll1111_opy_: Dict[str, Any],
        methods=[bstack11l1l1l_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥ጗"), bstack11l1l1l_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤጘ"), bstack11l1l1l_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦጙ"), bstack11l1l1l_opy_ (u"ࠦࡶࡻࡩࡵࠤጚ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack111l1l1l11_opy_ = bstack111l1l1l11_opy_
        self.platform_index = platform_index
        self.bstack1l1l1lll11l_opy_(methods)
        self.bstack1111ll1111_opy_ = bstack1111ll1111_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lllll1l1l1_opy_.get_data(bstack1111l1ll1l_opy_.bstack1ll1111l111_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lllll1l1l1_opy_.get_data(bstack1111l1ll1l_opy_.bstack1ll1111llll_opy_, target, strict)
    @staticmethod
    def bstack1l1l11lll11_opy_(target: object, strict=True):
        return bstack1lllll1l1l1_opy_.get_data(bstack1111l1ll1l_opy_.bstack1l1l11llll1_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lllll1l1l1_opy_.get_data(bstack1111l1ll1l_opy_.bstack1l1lll1111l_opy_, target, strict)
    @staticmethod
    def bstack11111l1ll1_opy_(instance: bstack1111lllll1_opy_) -> bool:
        return bstack1lllll1l1l1_opy_.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1l1lllllll1_opy_, False)
    @staticmethod
    def bstack1l1ll1l111l_opy_(instance: bstack1111lllll1_opy_, default_value=None):
        return bstack1lllll1l1l1_opy_.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1ll1111llll_opy_, default_value)
    @staticmethod
    def bstack1l1lll11111_opy_(instance: bstack1111lllll1_opy_, default_value=None):
        return bstack1lllll1l1l1_opy_.bstack111l1111l1_opy_(instance, bstack1111l1ll1l_opy_.bstack1l1lll1111l_opy_, default_value)
    @staticmethod
    def bstack1lllll1lll1_opy_(hub_url: str, bstack1l1l11ll1ll_opy_=bstack11l1l1l_opy_ (u"ࠧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠤጛ")):
        try:
            bstack1l1l1l1111l_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack1l1l1l1111l_opy_.endswith(bstack1l1l11ll1ll_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll11l11_opy_(method_name: str):
        return method_name == bstack11l1l1l_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢጜ")
    @staticmethod
    def bstack111l11l1ll_opy_(method_name: str, *args):
        return (
            bstack1111l1ll1l_opy_.bstack1l1lll11l11_opy_(method_name)
            and bstack1111l1ll1l_opy_.bstack1111lll11l_opy_(*args) == bstack1111l1ll1l_opy_.bstack1111ll1lll_opy_
        )
    @staticmethod
    def bstack1l1ll1l1l1l_opy_(method_name: str, *args):
        if not bstack1111l1ll1l_opy_.bstack1l1lll11l11_opy_(method_name):
            return False
        if not bstack1111l1ll1l_opy_.bstack1l1l1l1l1l1_opy_ in bstack1111l1ll1l_opy_.bstack1111lll11l_opy_(*args):
            return False
        bstack1ll1lllll11_opy_ = bstack1111l1ll1l_opy_.bstack1ll1llll11l_opy_(*args)
        return bstack1ll1lllll11_opy_ and bstack11l1l1l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢጝ") in bstack1ll1lllll11_opy_ and bstack11l1l1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤጞ") in bstack1ll1lllll11_opy_[bstack11l1l1l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤጟ")]
    @staticmethod
    def bstack1l1ll1l1lll_opy_(method_name: str, *args):
        if not bstack1111l1ll1l_opy_.bstack1l1lll11l11_opy_(method_name):
            return False
        if not bstack1111l1ll1l_opy_.bstack1l1l1l1l1l1_opy_ in bstack1111l1ll1l_opy_.bstack1111lll11l_opy_(*args):
            return False
        bstack1ll1lllll11_opy_ = bstack1111l1ll1l_opy_.bstack1ll1llll11l_opy_(*args)
        return (
            bstack1ll1lllll11_opy_
            and bstack11l1l1l_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥጠ") in bstack1ll1lllll11_opy_
            and bstack11l1l1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡥࡵ࡭ࡵࡺࠢጡ") in bstack1ll1lllll11_opy_[bstack11l1l1l_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧጢ")]
        )
    @staticmethod
    def bstack1111lll11l_opy_(*args):
        return str(bstack1111l1ll1l_opy_.bstack1ll1lll11ll_opy_(*args)).lower()
    @staticmethod
    def bstack1ll1lll11ll_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1ll1llll11l_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack1llll111l1_opy_(driver):
        command_executor = getattr(driver, bstack11l1l1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤጣ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack11l1l1l_opy_ (u"ࠢࡠࡷࡵࡰࠧጤ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack11l1l1l_opy_ (u"ࠣࡡࡦࡰ࡮࡫࡮ࡵࡡࡦࡳࡳ࡬ࡩࡨࠤጥ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack11l1l1l_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦࡡࡶࡩࡷࡼࡥࡳࡡࡤࡨࡩࡸࠢጦ"), None)
        return hub_url
    def bstack111l11lll1_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack11l1l1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨጧ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack11l1l1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢጨ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack11l1l1l_opy_ (u"ࠧࡥࡵࡳ࡮ࠥጩ")):
                setattr(command_executor, bstack11l1l1l_opy_ (u"ࠨ࡟ࡶࡴ࡯ࠦጪ"), hub_url)
                result = True
        if result:
            self.bstack111l1l1l11_opy_ = hub_url
            bstack1111l1ll1l_opy_.bstack1111l1l11l_opy_(instance, bstack1111l1ll1l_opy_.bstack1ll1111llll_opy_, hub_url)
            bstack1111l1ll1l_opy_.bstack1111l1l11l_opy_(
                instance, bstack1111l1ll1l_opy_.bstack1l1lllllll1_opy_, bstack1111l1ll1l_opy_.bstack1lllll1lll1_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1ll111ll1_opy_(bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_]):
        return bstack11l1l1l_opy_ (u"ࠢ࠻ࠤጫ").join((bstack1111l1llll_opy_(bstack111l11llll_opy_[0]).name, bstack111l111111_opy_(bstack111l11llll_opy_[1]).name))
    @staticmethod
    def bstack1111ll1l1l_opy_(bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_], callback: Callable):
        bstack1l1ll111lll_opy_ = bstack1111l1ll1l_opy_.bstack1l1ll111ll1_opy_(bstack111l11llll_opy_)
        if not bstack1l1ll111lll_opy_ in bstack1111l1ll1l_opy_.bstack1l1ll1111l1_opy_:
            bstack1111l1ll1l_opy_.bstack1l1ll1111l1_opy_[bstack1l1ll111lll_opy_] = []
        bstack1111l1ll1l_opy_.bstack1l1ll1111l1_opy_[bstack1l1ll111lll_opy_].append(callback)
    def bstack1l1l1lllll1_opy_(self, instance: bstack1111lllll1_opy_, method_name: str, bstack1l1l1llll1l_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack11l1l1l_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣጬ")):
            return
        cmd = args[0] if method_name == bstack11l1l1l_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࠥጭ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack1l1l1l11ll1_opy_ = bstack11l1l1l_opy_ (u"ࠥ࠾ࠧጮ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠧጯ") + bstack1l1l1l11ll1_opy_, bstack1l1l1llll1l_opy_)
    def bstack1l1l1lll1ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111lllll1_opy_, str],
        bstack111l11llll_opy_: Tuple[bstack1111l1llll_opy_, bstack111l111111_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1l1llllll_opy_, bstack1l1l1l11l11_opy_ = bstack111l11llll_opy_
        bstack1l1ll111lll_opy_ = bstack1111l1ll1l_opy_.bstack1l1ll111ll1_opy_(bstack111l11llll_opy_)
        self.logger.debug(bstack11l1l1l_opy_ (u"ࠧࡵ࡮ࡠࡪࡲࡳࡰࡀࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧጰ") + str(kwargs) + bstack11l1l1l_opy_ (u"ࠨࠢጱ"))
        if bstack1l1l1llllll_opy_ == bstack1111l1llll_opy_.bstack11111lll1l_opy_:
            if bstack1l1l1l11l11_opy_ == bstack111l111111_opy_.POST and not bstack1111l1ll1l_opy_.bstack1ll1111l111_opy_ in instance.data:
                session_id = getattr(target, bstack11l1l1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦጲ"), None)
                if session_id:
                    instance.data[bstack1111l1ll1l_opy_.bstack1ll1111l111_opy_] = session_id
        elif (
            bstack1l1l1llllll_opy_ == bstack1111l1llll_opy_.bstack111l11111l_opy_
            and bstack1111l1ll1l_opy_.bstack1111lll11l_opy_(*args) == bstack1111l1ll1l_opy_.bstack1111ll1lll_opy_
        ):
            if bstack1l1l1l11l11_opy_ == bstack111l111111_opy_.PRE:
                hub_url = bstack1111l1ll1l_opy_.bstack1llll111l1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1111l1ll1l_opy_.bstack1ll1111llll_opy_: hub_url,
                            bstack1111l1ll1l_opy_.bstack1l1lllllll1_opy_: bstack1111l1ll1l_opy_.bstack1lllll1lll1_opy_(hub_url),
                            bstack1111l1ll1l_opy_.bstack1111ll11l1_opy_: int(
                                os.environ.get(bstack11l1l1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣጳ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1ll1lllll11_opy_ = bstack1111l1ll1l_opy_.bstack1ll1llll11l_opy_(*args)
                bstack1l1l11lll11_opy_ = bstack1ll1lllll11_opy_.get(bstack11l1l1l_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣጴ"), None) if bstack1ll1lllll11_opy_ else None
                if isinstance(bstack1l1l11lll11_opy_, dict):
                    instance.data[bstack1111l1ll1l_opy_.bstack1l1l11llll1_opy_] = copy.deepcopy(bstack1l1l11lll11_opy_)
                    instance.data[bstack1111l1ll1l_opy_.bstack1l1lll1111l_opy_] = bstack1l1l11lll11_opy_
            elif bstack1l1l1l11l11_opy_ == bstack111l111111_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack11l1l1l_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤጵ"), dict()).get(bstack11l1l1l_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡎࡪࠢጶ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1111l1ll1l_opy_.bstack1ll1111l111_opy_: framework_session_id,
                                bstack1111l1ll1l_opy_.bstack1l1l1l111l1_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1l1llllll_opy_ == bstack1111l1llll_opy_.bstack111l11111l_opy_
            and bstack1111l1ll1l_opy_.bstack1111lll11l_opy_(*args) == bstack1111l1ll1l_opy_.bstack1l1l11lll1l_opy_
            and bstack1l1l1l11l11_opy_ == bstack111l111111_opy_.POST
        ):
            instance.data[bstack1111l1ll1l_opy_.bstack1l1l1l11111_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1ll111lll_opy_ in bstack1111l1ll1l_opy_.bstack1l1ll1111l1_opy_:
            bstack1l1l1l111ll_opy_ = None
            for callback in bstack1111l1ll1l_opy_.bstack1l1ll1111l1_opy_[bstack1l1ll111lll_opy_]:
                try:
                    bstack1l1l1l1l11l_opy_ = callback(self, target, exec, bstack111l11llll_opy_, result, *args, **kwargs)
                    if bstack1l1l1l111ll_opy_ == None:
                        bstack1l1l1l111ll_opy_ = bstack1l1l1l1l11l_opy_
                except Exception as e:
                    self.logger.error(bstack11l1l1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࠥጷ") + str(e) + bstack11l1l1l_opy_ (u"ࠨࠢጸ"))
                    traceback.print_exc()
            if bstack1l1l1l11l11_opy_ == bstack111l111111_opy_.PRE and callable(bstack1l1l1l111ll_opy_):
                return bstack1l1l1l111ll_opy_
            elif bstack1l1l1l11l11_opy_ == bstack111l111111_opy_.POST and bstack1l1l1l111ll_opy_:
                return bstack1l1l1l111ll_opy_
    def bstack1l1l1llll11_opy_(
        self, method_name, previous_state: bstack1111l1llll_opy_, *args, **kwargs
    ) -> bstack1111l1llll_opy_:
        if method_name == bstack11l1l1l_opy_ (u"ࠢࡠࡡ࡬ࡲ࡮ࡺ࡟ࡠࠤጹ") or method_name == bstack11l1l1l_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣጺ"):
            return bstack1111l1llll_opy_.bstack11111lll1l_opy_
        if method_name == bstack11l1l1l_opy_ (u"ࠤࡴࡹ࡮ࡺࠢጻ"):
            return bstack1111l1llll_opy_.QUIT
        if method_name == bstack11l1l1l_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦጼ"):
            if previous_state != bstack1111l1llll_opy_.NONE:
                bstack1lll1111111_opy_ = bstack1111l1ll1l_opy_.bstack1111lll11l_opy_(*args)
                if bstack1lll1111111_opy_ == bstack1111l1ll1l_opy_.bstack1111ll1lll_opy_:
                    return bstack1111l1llll_opy_.bstack11111lll1l_opy_
            return bstack1111l1llll_opy_.bstack111l11111l_opy_
        return bstack1111l1llll_opy_.NONE