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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1llllll_opy_, bstack11lll11lll1_opy_, bstack1l11llll1l_opy_, bstack1ll111l1_opy_, bstack11lll1l1lll_opy_, bstack11ll1ll111l_opy_, bstack11lllll1ll1_opy_, bstack11llllll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l11l111l11_opy_ import bstack1l1111lll11_opy_
import bstack_utils.bstack1ll1llll1l_opy_ as bstack11l1111l1_opy_
from bstack_utils.bstack1l1l1ll1_opy_ import bstack1l1ll11l_opy_
import bstack_utils.accessibility as bstack111lllll_opy_
from bstack_utils.bstack1111111l1_opy_ import bstack1111111l1_opy_
from bstack_utils.bstack1ll111ll_opy_ import bstack1ll1l1ll_opy_
bstack11l11ll11l1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡤࡱ࡯ࡰࡪࡩࡴࡰࡴ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭᯸")
logger = logging.getLogger(__name__)
class bstack1l11l1ll_opy_:
    bstack1l11l111l11_opy_ = None
    bs_config = None
    bstack1ll1llll1_opy_ = None
    @classmethod
    @bstack1ll111l1_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack1l11ll1ll11_opy_, stage=STAGE.SINGLE)
    def launch(cls, bs_config, bstack1ll1llll1_opy_):
        cls.bs_config = bs_config
        cls.bstack1ll1llll1_opy_ = bstack1ll1llll1_opy_
        try:
            cls.bstack11l11ll11ll_opy_()
            bstack11l1l11111l_opy_ = bstack11ll1llllll_opy_(bs_config)
            bstack11l1l111l11_opy_ = bstack11lll11lll1_opy_(bs_config)
            data = bstack11l1111l1_opy_.bstack11l11l1llll_opy_(bs_config, bstack1ll1llll1_opy_)
            config = {
                bstack11l1l1l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ᯹"): (bstack11l1l11111l_opy_, bstack11l1l111l11_opy_),
                bstack11l1l1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ᯺"): cls.default_headers()
            }
            response = bstack1l11llll1l_opy_(bstack11l1l1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ᯻"), cls.request_url(bstack11l1l1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠴࠲ࡦࡺ࡯࡬ࡥࡵࠪ᯼")), data, config)
            if response.status_code != 200:
                bstack1ll1ll11lll_opy_ = response.json()
                if bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ᯽")] == False:
                    cls.bstack11l11l11l1l_opy_(bstack1ll1ll11lll_opy_)
                    return
                cls.bstack11l11ll111l_opy_(bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ᯾")])
                cls.bstack11l11l1l11l_opy_(bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᯿")])
                return None
            bstack11l11l11ll1_opy_ = cls.bstack11l11l1l1ll_opy_(response)
            return bstack11l11l11ll1_opy_
        except Exception as error:
            logger.error(bstack11l1l1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࡾࢁࠧᰀ").format(str(error)))
            return None
    @classmethod
    @bstack1ll111l1_opy_(class_method=True)
    def stop(cls, bstack11l11l11lll_opy_=None):
        if not bstack1l1ll11l_opy_.on() and not bstack111lllll_opy_.on():
            return
        if os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᰁ")) == bstack11l1l1l_opy_ (u"ࠤࡱࡹࡱࡲࠢᰂ") or os.environ.get(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᰃ")) == bstack11l1l1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᰄ"):
            logger.error(bstack11l1l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡱࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨᰅ"))
            return {
                bstack11l1l1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᰆ"): bstack11l1l1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᰇ"),
                bstack11l1l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᰈ"): bstack11l1l1l_opy_ (u"ࠩࡗࡳࡰ࡫࡮࠰ࡤࡸ࡭ࡱࡪࡉࡅࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤ࠭ࠢࡥࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡱ࡮࡭ࡨࡵࠢ࡫ࡥࡻ࡫ࠠࡧࡣ࡬ࡰࡪࡪࠧᰉ")
            }
        try:
            cls.bstack1l11l111l11_opy_.shutdown()
            data = {
                bstack11l1l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᰊ"): bstack11llllll_opy_()
            }
            if not bstack11l11l11lll_opy_ is None:
                data[bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠨᰋ")] = [{
                    bstack11l1l1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᰌ"): bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡣࡰ࡯࡬࡭ࡧࡧࠫᰍ"),
                    bstack11l1l1l_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࠧᰎ"): bstack11l11l11lll_opy_
                }]
            config = {
                bstack11l1l1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᰏ"): cls.default_headers()
            }
            bstack1l11111lll1_opy_ = bstack11l1l1l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡴࡰࡲࠪᰐ").format(os.environ[bstack11l1l1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᰑ")])
            bstack11l11l111ll_opy_ = cls.request_url(bstack1l11111lll1_opy_)
            response = bstack1l11llll1l_opy_(bstack11l1l1l_opy_ (u"ࠫࡕ࡛ࡔࠨᰒ"), bstack11l11l111ll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11l1l1l_opy_ (u"࡙ࠧࡴࡰࡲࠣࡶࡪࡷࡵࡦࡵࡷࠤࡳࡵࡴࠡࡱ࡮ࠦᰓ"))
        except Exception as error:
            logger.error(bstack11l1l1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡲࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡔࡦࡵࡷࡌࡺࡨ࠺࠻ࠢࠥᰔ") + str(error))
            return {
                bstack11l1l1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᰕ"): bstack11l1l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᰖ"),
                bstack11l1l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᰗ"): str(error)
            }
    @classmethod
    @bstack1ll111l1_opy_(class_method=True)
    def bstack11l11l1l1ll_opy_(cls, response):
        bstack1ll1ll11lll_opy_ = response.json() if not isinstance(response, dict) else response
        bstack11l11l11ll1_opy_ = {}
        if bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠪ࡮ࡼࡺࠧᰘ")) is None:
            os.environ[bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᰙ")] = bstack11l1l1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᰚ")
        else:
            os.environ[bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᰛ")] = bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠧ࡫ࡹࡷࠫᰜ"), bstack11l1l1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᰝ"))
        os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᰞ")] = bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᰟ"), bstack11l1l1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᰠ"))
        logger.info(bstack11l1l1l_opy_ (u"࡚ࠬࡥࡴࡶ࡫ࡹࡧࠦࡳࡵࡣࡵࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥ࡯ࡤ࠻ࠢࠪᰡ") + os.getenv(bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᰢ")));
        if bstack1l1ll11l_opy_.bstack1l11l111111_opy_(cls.bs_config, cls.bstack1ll1llll1_opy_.get(bstack11l1l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨᰣ"), bstack11l1l1l_opy_ (u"ࠨࠩᰤ"))) is True:
            bstack11l11l1lll1_opy_, build_hashed_id, bstack11l11l1111l_opy_ = cls.bstack11l111ll1ll_opy_(bstack1ll1ll11lll_opy_)
            if bstack11l11l1lll1_opy_ != None and build_hashed_id != None:
                bstack11l11l11ll1_opy_[bstack11l1l1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᰥ")] = {
                    bstack11l1l1l_opy_ (u"ࠪ࡮ࡼࡺ࡟ࡵࡱ࡮ࡩࡳ࠭ᰦ"): bstack11l11l1lll1_opy_,
                    bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᰧ"): build_hashed_id,
                    bstack11l1l1l_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩᰨ"): bstack11l11l1111l_opy_
                }
            else:
                bstack11l11l11ll1_opy_[bstack11l1l1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᰩ")] = {}
        else:
            bstack11l11l11ll1_opy_[bstack11l1l1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᰪ")] = {}
        if bstack111lllll_opy_.bstack11l11llll11_opy_(cls.bs_config) is True:
            bstack11l111lll11_opy_, build_hashed_id = cls.bstack11l11l1l111_opy_(bstack1ll1ll11lll_opy_)
            if bstack11l111lll11_opy_ != None and build_hashed_id != None:
                bstack11l11l11ll1_opy_[bstack11l1l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᰫ")] = {
                    bstack11l1l1l_opy_ (u"ࠩࡤࡹࡹ࡮࡟ࡵࡱ࡮ࡩࡳ࠭ᰬ"): bstack11l111lll11_opy_,
                    bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᰭ"): build_hashed_id,
                }
            else:
                bstack11l11l11ll1_opy_[bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᰮ")] = {}
        else:
            bstack11l11l11ll1_opy_[bstack11l1l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᰯ")] = {}
        if bstack11l11l11ll1_opy_[bstack11l1l1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᰰ")].get(bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩᰱ")) != None or bstack11l11l11ll1_opy_[bstack11l1l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᰲ")].get(bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᰳ")) != None:
            cls.bstack11l11l1ll11_opy_(bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠪ࡮ࡼࡺࠧᰴ")), bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᰵ")))
        return bstack11l11l11ll1_opy_
    @classmethod
    def bstack11l111ll1ll_opy_(cls, bstack1ll1ll11lll_opy_):
        if bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᰶ")) == None:
            cls.bstack11l11ll111l_opy_()
            return [None, None, None]
        if bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ᰷࠭")][bstack11l1l1l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ᰸")] != True:
            cls.bstack11l11ll111l_opy_(bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᰹")])
            return [None, None, None]
        logger.debug(bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࠠࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭᰺"))
        os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡃࡐࡏࡓࡐࡊ࡚ࡅࡅࠩ᰻")] = bstack11l1l1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ᰼")
        if bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡰࡷࡵࠩ᰽")):
            os.environ[bstack11l1l1l_opy_ (u"࠭ࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࡣࡋࡕࡒࡠࡅࡕࡅࡘࡎ࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪ᰾")] = json.dumps({
                bstack11l1l1l_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩ᰿"): bstack11ll1llllll_opy_(cls.bs_config),
                bstack11l1l1l_opy_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪ᱀"): bstack11lll11lll1_opy_(cls.bs_config)
            })
        if bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ᱁")):
            os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ᱂")] = bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭᱃")]
        if bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ᱄")].get(bstack11l1l1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ᱅"), {}).get(bstack11l1l1l_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫ᱆")):
            os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩ᱇")] = str(bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᱈")][bstack11l1l1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ᱉")][bstack11l1l1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ᱊")])
        else:
            os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭᱋")] = bstack11l1l1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ᱌")
        return [bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠧ࡫ࡹࡷࠫᱍ")], bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᱎ")], os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪᱏ")]]
    @classmethod
    def bstack11l11l1l111_opy_(cls, bstack1ll1ll11lll_opy_):
        if bstack1ll1ll11lll_opy_.get(bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᱐")) == None:
            cls.bstack11l11l1l11l_opy_()
            return [None, None]
        if bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ᱑")][bstack11l1l1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭᱒")] != True:
            cls.bstack11l11l1l11l_opy_(bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᱓")])
            return [None, None]
        if bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᱔")].get(bstack11l1l1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ᱕")):
            logger.debug(bstack11l1l1l_opy_ (u"ࠩࡗࡩࡸࡺࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭᱖"))
            parsed = json.loads(os.getenv(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ᱗"), bstack11l1l1l_opy_ (u"ࠫࢀࢃࠧ᱘")))
            capabilities = bstack11l1111l1_opy_.bstack11l11ll1l11_opy_(bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᱙")][bstack11l1l1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧᱚ")][bstack11l1l1l_opy_ (u"ࠧࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᱛ")], bstack11l1l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᱜ"), bstack11l1l1l_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨᱝ"))
            bstack11l111lll11_opy_ = capabilities[bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠨᱞ")]
            os.environ[bstack11l1l1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᱟ")] = bstack11l111lll11_opy_
            parsed[bstack11l1l1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᱠ")] = capabilities[bstack11l1l1l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᱡ")]
            os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨᱢ")] = json.dumps(parsed)
            scripts = bstack11l1111l1_opy_.bstack11l11ll1l11_opy_(bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᱣ")][bstack11l1l1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪᱤ")][bstack11l1l1l_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫᱥ")], bstack11l1l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᱦ"), bstack11l1l1l_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩ࠭ᱧ"))
            bstack1111111l1_opy_.bstack11l1l11l111_opy_(scripts)
            commands = bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᱨ")][bstack11l1l1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨᱩ")][bstack11l1l1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࡗࡳ࡜ࡸࡡࡱࠩᱪ")].get(bstack11l1l1l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫᱫ"))
            bstack1111111l1_opy_.bstack11l1l11ll1l_opy_(commands)
            bstack1111111l1_opy_.store()
        return [bstack11l111lll11_opy_, bstack1ll1ll11lll_opy_[bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬᱬ")]]
    @classmethod
    def bstack11l11ll111l_opy_(cls, response=None):
        os.environ[bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᱭ")] = bstack11l1l1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᱮ")
        os.environ[bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᱯ")] = bstack11l1l1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᱰ")
        os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧᱱ")] = bstack11l1l1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨᱲ")
        os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᱳ")] = bstack11l1l1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᱴ")
        os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ᱵ")] = bstack11l1l1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᱶ")
        cls.bstack11l11l11l1l_opy_(response, bstack11l1l1l_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢᱷ"))
        return [None, None, None]
    @classmethod
    def bstack11l11l1l11l_opy_(cls, response=None):
        os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᱸ")] = bstack11l1l1l_opy_ (u"ࠩࡱࡹࡱࡲࠧᱹ")
        os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᱺ")] = bstack11l1l1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩᱻ")
        os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᱼ")] = bstack11l1l1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᱽ")
        cls.bstack11l11l11l1l_opy_(response, bstack11l1l1l_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢ᱾"))
        return [None, None, None]
    @classmethod
    def bstack11l11l1ll11_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ᱿")] = jwt
        os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᲀ")] = build_hashed_id
    @classmethod
    def bstack11l11l11l1l_opy_(cls, response=None, product=bstack11l1l1l_opy_ (u"ࠥࠦᲁ")):
        if response == None:
            logger.error(product + bstack11l1l1l_opy_ (u"ࠦࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠨᲂ"))
        for error in response[bstack11l1l1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬᲃ")]:
            bstack11lll11l1ll_opy_ = error[bstack11l1l1l_opy_ (u"࠭࡫ࡦࡻࠪᲄ")]
            error_message = error[bstack11l1l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᲅ")]
            if error_message:
                if bstack11lll11l1ll_opy_ == bstack11l1l1l_opy_ (u"ࠣࡇࡕࡖࡔࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡅࡇࡑࡍࡊࡊࠢᲆ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11l1l1l_opy_ (u"ࠤࡇࡥࡹࡧࠠࡶࡲ࡯ࡳࡦࡪࠠࡵࡱࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࠥᲇ") + product + bstack11l1l1l_opy_ (u"ࠥࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣᲈ"))
    @classmethod
    def bstack11l11ll11ll_opy_(cls):
        if cls.bstack1l11l111l11_opy_ is not None:
            return
        cls.bstack1l11l111l11_opy_ = bstack1l1111lll11_opy_(cls.post_data)
        cls.bstack1l11l111l11_opy_.start()
    @classmethod
    def bstack11llll11_opy_(cls):
        if cls.bstack1l11l111l11_opy_ is None:
            return
        cls.bstack1l11l111l11_opy_.shutdown()
    @classmethod
    @bstack1ll111l1_opy_(class_method=True)
    def post_data(cls, bstack1l1l1l11_opy_, event_url=bstack11l1l1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᲉ")):
        config = {
            bstack11l1l1l_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᲊ"): cls.default_headers()
        }
        logger.debug(bstack11l1l1l_opy_ (u"ࠨࡰࡰࡵࡷࡣࡩࡧࡴࡢ࠼ࠣࡗࡪࡴࡤࡪࡰࡪࠤࡩࡧࡴࡢࠢࡷࡳࠥࡺࡥࡴࡶ࡫ࡹࡧࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࡵࠣࡿࢂࠨ᲋").format(bstack11l1l1l_opy_ (u"ࠧ࠭ࠢࠪ᲌").join([event[bstack11l1l1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ᲍")] for event in bstack1l1l1l11_opy_])))
        response = bstack1l11llll1l_opy_(bstack11l1l1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ᲎"), cls.request_url(event_url), bstack1l1l1l11_opy_, config)
        bstack11l11llllll_opy_ = response.json()
    @classmethod
    def bstack1lll11l1_opy_(cls, bstack1l1l1l11_opy_, event_url=bstack11l1l1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ᲏")):
        logger.debug(bstack11l1l1l_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡣࡧࡨࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦᲐ").format(bstack1l1l1l11_opy_[bstack11l1l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᲑ")]))
        if not bstack11l1111l1_opy_.bstack11l11l11111_opy_(bstack1l1l1l11_opy_[bstack11l1l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᲒ")]):
            logger.debug(bstack11l1l1l_opy_ (u"ࠢࡴࡧࡱࡨࡤࡪࡡࡵࡣ࠽ࠤࡓࡵࡴࠡࡣࡧࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧᲓ").format(bstack1l1l1l11_opy_[bstack11l1l1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᲔ")]))
            return
        bstack1lll11l11_opy_ = bstack11l1111l1_opy_.bstack11l11ll1111_opy_(bstack1l1l1l11_opy_[bstack11l1l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭Ვ")], bstack1l1l1l11_opy_.get(bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬᲖ")))
        if bstack1lll11l11_opy_ != None:
            if bstack1l1l1l11_opy_.get(bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭Თ")) != None:
                bstack1l1l1l11_opy_[bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧᲘ")][bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫᲙ")] = bstack1lll11l11_opy_
            else:
                bstack1l1l1l11_opy_[bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬᲚ")] = bstack1lll11l11_opy_
        if event_url == bstack11l1l1l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧᲛ"):
            cls.bstack11l11ll11ll_opy_()
            logger.debug(bstack11l1l1l_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡁࡥࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧᲜ").format(bstack1l1l1l11_opy_[bstack11l1l1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᲝ")]))
            cls.bstack1l11l111l11_opy_.add(bstack1l1l1l11_opy_)
        elif event_url == bstack11l1l1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩᲞ"):
            cls.post_data([bstack1l1l1l11_opy_], event_url)
    @classmethod
    @bstack1ll111l1_opy_(class_method=True)
    def bstack1ll1111l_opy_(cls, logs):
        bstack11l11l1l1l1_opy_ = []
        for log in logs:
            bstack11l11l11l11_opy_ = {
                bstack11l1l1l_opy_ (u"ࠬࡱࡩ࡯ࡦࠪᲟ"): bstack11l1l1l_opy_ (u"࠭ࡔࡆࡕࡗࡣࡑࡕࡇࠨᲠ"),
                bstack11l1l1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭Ს"): log[bstack11l1l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᲢ")],
                bstack11l1l1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᲣ"): log[bstack11l1l1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭Ფ")],
                bstack11l1l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡡࡵࡩࡸࡶ࡯࡯ࡵࡨࠫᲥ"): {},
                bstack11l1l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ღ"): log[bstack11l1l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᲧ")],
            }
            if bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᲨ") in log:
                bstack11l11l11l11_opy_[bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᲩ")] = log[bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᲪ")]
            elif bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᲫ") in log:
                bstack11l11l11l11_opy_[bstack11l1l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᲬ")] = log[bstack11l1l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᲭ")]
            bstack11l11l1l1l1_opy_.append(bstack11l11l11l11_opy_)
        cls.bstack1lll11l1_opy_({
            bstack11l1l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᲮ"): bstack11l1l1l_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᲯ"),
            bstack11l1l1l_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭Ჰ"): bstack11l11l1l1l1_opy_
        })
    @classmethod
    @bstack1ll111l1_opy_(class_method=True)
    def bstack11l11l111l1_opy_(cls, steps):
        bstack11l111lll1l_opy_ = []
        for step in steps:
            bstack11l111lllll_opy_ = {
                bstack11l1l1l_opy_ (u"ࠩ࡮࡭ࡳࡪࠧᲱ"): bstack11l1l1l_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡗࡉࡕ࠭Ჲ"),
                bstack11l1l1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᲳ"): step[bstack11l1l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᲴ")],
                bstack11l1l1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᲵ"): step[bstack11l1l1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᲶ")],
                bstack11l1l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᲷ"): step[bstack11l1l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᲸ")],
                bstack11l1l1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬᲹ"): step[bstack11l1l1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭Ჺ")]
            }
            if bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ᲻") in step:
                bstack11l111lllll_opy_[bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᲼")] = step[bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᲽ")]
            elif bstack11l1l1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᲾ") in step:
                bstack11l111lllll_opy_[bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᲿ")] = step[bstack11l1l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᳀")]
            bstack11l111lll1l_opy_.append(bstack11l111lllll_opy_)
        cls.bstack1lll11l1_opy_({
            bstack11l1l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ᳁"): bstack11l1l1l_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ᳂"),
            bstack11l1l1l_opy_ (u"࠭࡬ࡰࡩࡶࠫ᳃"): bstack11l111lll1l_opy_
        })
    @classmethod
    @bstack1ll111l1_opy_(class_method=True)
    def bstack11ll11l1l1_opy_(cls, screenshot):
        cls.bstack1lll11l1_opy_({
            bstack11l1l1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ᳄"): bstack11l1l1l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ᳅"),
            bstack11l1l1l_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ᳆"): [{
                bstack11l1l1l_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ᳇"): bstack11l1l1l_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࠭᳈"),
                bstack11l1l1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ᳉"): datetime.datetime.utcnow().isoformat() + bstack11l1l1l_opy_ (u"࡚࠭ࠨ᳊"),
                bstack11l1l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᳋"): screenshot[bstack11l1l1l_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ᳌")],
                bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᳍"): screenshot[bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ᳎")]
            }]
        }, event_url=bstack11l1l1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ᳏"))
    @classmethod
    @bstack1ll111l1_opy_(class_method=True)
    def bstack1ll11ll1l1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1lll11l1_opy_({
            bstack11l1l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ᳐"): bstack11l1l1l_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ᳑"),
            bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ᳒"): {
                bstack11l1l1l_opy_ (u"ࠣࡷࡸ࡭ࡩࠨ᳓"): cls.current_test_uuid(),
                bstack11l1l1l_opy_ (u"ࠤ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳ᳔ࠣ"): cls.bstack11lllll1_opy_(driver)
            }
        })
    @classmethod
    def bstack1ll11111_opy_(cls, event: str, bstack1l1l1l11_opy_: bstack1ll1l1ll_opy_):
        bstack1l1111l1_opy_ = {
            bstack11l1l1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫᳕ࠧ"): event,
            bstack1l1l1l11_opy_.bstack1l11111l_opy_(): bstack1l1l1l11_opy_.bstack1l111lll_opy_(event)
        }
        cls.bstack1lll11l1_opy_(bstack1l1111l1_opy_)
        result = getattr(bstack1l1l1l11_opy_, bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷ᳖ࠫ"), None)
        if event == bstack11l1l1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ᳗࠭"):
            threading.current_thread().bstackTestMeta = {bstack11l1l1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ᳘࠭"): bstack11l1l1l_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ᳙")}
        elif event == bstack11l1l1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ᳚"):
            threading.current_thread().bstackTestMeta = {bstack11l1l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ᳛"): getattr(result, bstack11l1l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶ᳜ࠪ"), bstack11l1l1l_opy_ (u"᳝ࠫࠬ"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕ᳞ࠩ"), None) is None or os.environ[bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖ᳟ࠪ")] == bstack11l1l1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ᳠")) and (os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭᳡"), None) is None or os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜᳢࡚ࠧ")] == bstack11l1l1l_opy_ (u"ࠥࡲࡺࡲ࡬᳣ࠣ")):
            return False
        return True
    @staticmethod
    def bstack11l11l1ll1l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11l1ll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11l1l1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧ᳤ࠪ"): bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ᳥"),
            bstack11l1l1l_opy_ (u"࠭ࡘ࠮ࡄࡖࡘࡆࡉࡋ࠮ࡖࡈࡗ࡙ࡕࡐࡔ᳦ࠩ"): bstack11l1l1l_opy_ (u"ࠧࡵࡴࡸࡩ᳧ࠬ")
        }
        if os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘ᳨ࠬ"), None):
            headers[bstack11l1l1l_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᳩ")] = bstack11l1l1l_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᳪ").format(os.environ[bstack11l1l1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠣᳫ")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11l1l1l_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫᳬ").format(bstack11l11ll11l1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦ᳭ࠪ"), None)
    @staticmethod
    def bstack11lllll1_opy_(driver):
        return {
            bstack11lll1l1lll_opy_(): bstack11ll1ll111l_opy_(driver)
        }
    @staticmethod
    def bstack11l111llll1_opy_(exception_info, report):
        return [{bstack11l1l1l_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᳮ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111l1ll111_opy_(typename):
        if bstack11l1l1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦᳯ") in typename:
            return bstack11l1l1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥᳰ")
        return bstack11l1l1l_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦᳱ")