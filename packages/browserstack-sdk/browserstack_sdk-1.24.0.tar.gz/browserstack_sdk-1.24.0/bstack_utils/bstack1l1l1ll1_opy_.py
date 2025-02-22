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
import threading
from bstack_utils.helper import bstack1l1llllll1_opy_
from bstack_utils.constants import bstack1l11ll11l11_opy_, EVENTS, STAGE
from bstack_utils.bstack111111l1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l1ll11l_opy_:
    bstack1l11l111l11_opy_ = None
    @classmethod
    def bstack11l11l11ll_opy_(cls):
        if cls.on() and os.getenv(bstack11l1l1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ᝷")):
            logger.info(
                bstack11l1l1l_opy_ (u"࡙ࠩ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬ᝸").format(os.getenv(bstack11l1l1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣ᝹"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ᝺"), None) is None or os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ᝻")] == bstack11l1l1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ᝼"):
            return False
        return True
    @classmethod
    def bstack1l11l11111l_opy_(cls, bs_config, framework=bstack11l1l1l_opy_ (u"ࠢࠣ᝽")):
        bstack1l1l111llll_opy_ = False
        for fw in bstack1l11ll11l11_opy_:
            if fw in framework:
                bstack1l1l111llll_opy_ = True
        return bstack1l1llllll1_opy_(bs_config.get(bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ᝾"), bstack1l1l111llll_opy_))
    @classmethod
    def bstack1l111lllll1_opy_(cls, framework):
        return framework in bstack1l11ll11l11_opy_
    @classmethod
    def bstack1l11l111111_opy_(cls, bs_config, framework):
        return cls.bstack1l11l11111l_opy_(bs_config, framework) is True and cls.bstack1l111lllll1_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭᝿"), None)
    @staticmethod
    def bstack1l11ll1l_opy_():
        if getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧក"), None):
            return {
                bstack11l1l1l_opy_ (u"ࠫࡹࡿࡰࡦࠩខ"): bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࠪគ"),
                bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ឃ"): getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫង"), None)
            }
        if getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬច"), None):
            return {
                bstack11l1l1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧឆ"): bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨជ"),
                bstack11l1l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫឈ"): getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩញ"), None)
            }
        return None
    @staticmethod
    def bstack1l11l1111ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1ll11l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1l11ll_opy_(test, hook_name=None):
        bstack1l111llllll_opy_ = test.parent
        if hook_name in [bstack11l1l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫដ"), bstack11l1l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨឋ"), bstack11l1l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧឌ"), bstack11l1l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫឍ")]:
            bstack1l111llllll_opy_ = test
        scope = []
        while bstack1l111llllll_opy_ is not None:
            scope.append(bstack1l111llllll_opy_.name)
            bstack1l111llllll_opy_ = bstack1l111llllll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1l111llll1l_opy_(hook_type):
        if hook_type == bstack11l1l1l_opy_ (u"ࠥࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠣណ"):
            return bstack11l1l1l_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣ࡬ࡴࡵ࡫ࠣត")
        elif hook_type == bstack11l1l1l_opy_ (u"ࠧࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠤថ"):
            return bstack11l1l1l_opy_ (u"ࠨࡔࡦࡣࡵࡨࡴࡽ࡮ࠡࡪࡲࡳࡰࠨទ")
    @staticmethod
    def bstack1l11l1111l1_opy_(bstack11l11ll1_opy_):
        try:
            if not bstack1l1ll11l_opy_.on():
                return bstack11l11ll1_opy_
            if os.environ.get(bstack11l1l1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠧធ"), None) == bstack11l1l1l_opy_ (u"ࠣࡶࡵࡹࡪࠨន"):
                tests = os.environ.get(bstack11l1l1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘࠨប"), None)
                if tests is None or tests == bstack11l1l1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣផ"):
                    return bstack11l11ll1_opy_
                bstack11l11ll1_opy_ = tests.split(bstack11l1l1l_opy_ (u"ࠫ࠱࠭ព"))
                return bstack11l11ll1_opy_
        except Exception as exc:
            logger.debug(bstack11l1l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡷ࡫ࡲࡶࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡵ࠾ࠥࠨភ") + str(str(exc)) + bstack11l1l1l_opy_ (u"ࠨࠢម"))
        return bstack11l11ll1_opy_