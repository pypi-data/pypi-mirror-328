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
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1l111111l11_opy_, bstack1ll1l111l_opy_, get_host_info, bstack11lllll1111_opy_, \
 bstack11l1111ll1_opy_, bstack11llll1l_opy_, bstack1ll111l1_opy_, bstack11lllll1ll1_opy_, bstack11llllll_opy_
import bstack_utils.accessibility as bstack111lllll_opy_
from bstack_utils.bstack1l1l1ll1_opy_ import bstack1l1ll11l_opy_
from bstack_utils.percy import bstack11111l111_opy_
from bstack_utils.config import Config
bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
logger = logging.getLogger(__name__)
percy = bstack11111l111_opy_()
@bstack1ll111l1_opy_(class_method=False)
def bstack11l11l1llll_opy_(bs_config, bstack1ll1llll1_opy_):
  try:
    data = {
        bstack11l1l1l_opy_ (u"ࠫ࡫ࡵࡲ࡮ࡣࡷࠫᳲ"): bstack11l1l1l_opy_ (u"ࠬࡰࡳࡰࡰࠪᳳ"),
        bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺ࡟࡯ࡣࡰࡩࠬ᳴"): bs_config.get(bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᳵ"), bstack11l1l1l_opy_ (u"ࠨࠩᳶ")),
        bstack11l1l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ᳷"): bs_config.get(bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭᳸"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ᳹"): bs_config.get(bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᳺ")),
        bstack11l1l1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ᳻"): bs_config.get(bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ᳼"), bstack11l1l1l_opy_ (u"ࠨࠩ᳽")),
        bstack11l1l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭᳾"): bstack11llllll_opy_(),
        bstack11l1l1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ᳿"): bstack11lllll1111_opy_(bs_config),
        bstack11l1l1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠧᴀ"): get_host_info(),
        bstack11l1l1l_opy_ (u"ࠬࡩࡩࡠ࡫ࡱࡪࡴ࠭ᴁ"): bstack1ll1l111l_opy_(),
        bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡸࡵ࡯ࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᴂ"): os.environ.get(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ᴃ")),
        bstack11l1l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡳࡧࡵࡹࡳ࠭ᴄ"): os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧᴅ"), False),
        bstack11l1l1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡣࡨࡵ࡮ࡵࡴࡲࡰࠬᴆ"): bstack1l111111l11_opy_(),
        bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᴇ"): bstack11l111l1l1l_opy_(),
        bstack11l1l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡦࡨࡸࡦ࡯࡬ࡴࠩᴈ"): bstack11l111l11l1_opy_(bstack1ll1llll1_opy_),
        bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫᴉ"): bstack1l11l1111_opy_(bs_config, bstack1ll1llll1_opy_.get(bstack11l1l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨᴊ"), bstack11l1l1l_opy_ (u"ࠨࠩᴋ"))),
        bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᴌ"): bstack11l1111ll1_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack11l1l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡣࡼࡰࡴࡧࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࠡࡽࢀࠦᴍ").format(str(error)))
    return None
def bstack11l111l11l1_opy_(framework):
  return {
    bstack11l1l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫᴎ"): framework.get(bstack11l1l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭ᴏ"), bstack11l1l1l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭ᴐ")),
    bstack11l1l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪᴑ"): framework.get(bstack11l1l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᴒ")),
    bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᴓ"): framework.get(bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᴔ")),
    bstack11l1l1l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭ᴕ"): bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬᴖ"),
    bstack11l1l1l_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᴗ"): framework.get(bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᴘ"))
  }
def bstack1l11l1111_opy_(bs_config, framework):
  bstack111lll1l1_opy_ = False
  bstack1l1l11l1l1_opy_ = False
  bstack11l111l1ll1_opy_ = False
  if bstack11l1l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬᴙ") in bs_config:
    bstack11l111l1ll1_opy_ = True
  elif bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵ࠭ᴚ") in bs_config:
    bstack111lll1l1_opy_ = True
  else:
    bstack1l1l11l1l1_opy_ = True
  bstack1lll11l11_opy_ = {
    bstack11l1l1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᴛ"): bstack1l1ll11l_opy_.bstack1l11l11111l_opy_(bs_config, framework),
    bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᴜ"): bstack111lllll_opy_.bstack11l11llll11_opy_(bs_config),
    bstack11l1l1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᴝ"): bs_config.get(bstack11l1l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᴞ"), False),
    bstack11l1l1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᴟ"): bstack1l1l11l1l1_opy_,
    bstack11l1l1l_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᴠ"): bstack111lll1l1_opy_,
    bstack11l1l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᴡ"): bstack11l111l1ll1_opy_
  }
  return bstack1lll11l11_opy_
@bstack1ll111l1_opy_(class_method=False)
def bstack11l111l1l1l_opy_():
  try:
    bstack11l111l1l11_opy_ = json.loads(os.getenv(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫᴢ"), bstack11l1l1l_opy_ (u"ࠫࢀࢃࠧᴣ")))
    return {
        bstack11l1l1l_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠧᴤ"): bstack11l111l1l11_opy_
    }
  except Exception as error:
    logger.error(bstack11l1l1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣ࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡴࡧࡷࡸ࡮ࡴࡧࡴࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧᴥ").format(str(error)))
    return {}
def bstack11l11ll1l11_opy_(array, bstack11l111ll11l_opy_, bstack11l111l11ll_opy_):
  result = {}
  for o in array:
    key = o[bstack11l111ll11l_opy_]
    result[key] = o[bstack11l111l11ll_opy_]
  return result
def bstack11l11l11111_opy_(bstack11111l11l_opy_=bstack11l1l1l_opy_ (u"ࠧࠨᴦ")):
  bstack11l111l1lll_opy_ = bstack111lllll_opy_.on()
  bstack11l111ll1l1_opy_ = bstack1l1ll11l_opy_.on()
  bstack11l111ll111_opy_ = percy.bstack1ll11l111_opy_()
  if bstack11l111ll111_opy_ and not bstack11l111ll1l1_opy_ and not bstack11l111l1lll_opy_:
    return bstack11111l11l_opy_ not in [bstack11l1l1l_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬᴧ"), bstack11l1l1l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᴨ")]
  elif bstack11l111l1lll_opy_ and not bstack11l111ll1l1_opy_:
    return bstack11111l11l_opy_ not in [bstack11l1l1l_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᴩ"), bstack11l1l1l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᴪ"), bstack11l1l1l_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩᴫ")]
  return bstack11l111l1lll_opy_ or bstack11l111ll1l1_opy_ or bstack11l111ll111_opy_
@bstack1ll111l1_opy_(class_method=False)
def bstack11l11ll1111_opy_(bstack11111l11l_opy_, test=None):
  bstack11l111l111l_opy_ = bstack111lllll_opy_.on()
  if not bstack11l111l111l_opy_ or bstack11111l11l_opy_ not in [bstack11l1l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᴬ")] or test == None:
    return None
  return {
    bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᴭ"): bstack11l111l111l_opy_ and bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧᴮ"), None) == True and bstack111lllll_opy_.bstack11l1l111ll_opy_(test[bstack11l1l1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᴯ")])
  }