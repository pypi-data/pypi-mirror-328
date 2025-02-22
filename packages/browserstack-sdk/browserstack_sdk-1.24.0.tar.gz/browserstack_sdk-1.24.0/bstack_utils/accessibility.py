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
import requests
import logging
import threading
from urllib.parse import urlparse
from bstack_utils.constants import bstack1l11l1lll11_opy_ as bstack11l11ll1lll_opy_, EVENTS
from bstack_utils.bstack1111111l1_opy_ import bstack1111111l1_opy_
from bstack_utils.helper import bstack11llllll_opy_, bstack1ll1l1l1_opy_, bstack11l1111ll1_opy_, bstack11ll1llllll_opy_, \
  bstack11lll11lll1_opy_, bstack1ll1l111l_opy_, get_host_info, bstack1l111111l11_opy_, bstack1l11llll1l_opy_, bstack1ll111l1_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack111111l1l_opy_ import get_logger
from bstack_utils.bstack11ll1111l1_opy_ import bstack1111lll111_opy_
logger = get_logger(__name__)
bstack11ll1111l1_opy_ = bstack1111lll111_opy_()
@bstack1ll111l1_opy_(class_method=False)
def _11l1l1111l1_opy_(driver, bstack1111l1ll_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11l1l1l_opy_ (u"࠭࡯ࡴࡡࡱࡥࡲ࡫ࠧᭂ"): caps.get(bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ᭃ"), None),
        bstack11l1l1l_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲ᭄ࠬ"): bstack1111l1ll_opy_.get(bstack11l1l1l_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᭅ"), None),
        bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩᭆ"): caps.get(bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᭇ"), None),
        bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᭈ"): caps.get(bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᭉ"), None)
    }
  except Exception as error:
    logger.debug(bstack11l1l1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫᭊ") + str(error))
  return response
def on():
    if os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᭋ"), None) is None or os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᭌ")] == bstack11l1l1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ᭍"):
        return False
    return True
def bstack11l11llll11_opy_(config):
  return config.get(bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ᭎"), False) or any([p.get(bstack11l1l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᭏"), False) == True for p in config.get(bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ᭐"), [])])
def bstack1lll11lll1_opy_(config, bstack1l11lll11_opy_):
  try:
    if not bstack11l1111ll1_opy_(config):
      return False
    bstack11l11ll1ll1_opy_ = config.get(bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᭑"), False)
    if int(bstack1l11lll11_opy_) < len(config.get(bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ᭒"), [])) and config[bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ᭓")][bstack1l11lll11_opy_]:
      bstack11l11llll1l_opy_ = config[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭᭔")][bstack1l11lll11_opy_].get(bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ᭕"), None)
    else:
      bstack11l11llll1l_opy_ = config.get(bstack11l1l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᭖"), None)
    if bstack11l11llll1l_opy_ != None:
      bstack11l11ll1ll1_opy_ = bstack11l11llll1l_opy_
    bstack11l1l111l1l_opy_ = os.getenv(bstack11l1l1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ᭗")) is not None and len(os.getenv(bstack11l1l1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ᭘"))) > 0 and os.getenv(bstack11l1l1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭᭙")) != bstack11l1l1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ᭚")
    return bstack11l11ll1ll1_opy_ and bstack11l1l111l1l_opy_
  except Exception as error:
    logger.debug(bstack11l1l1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡩࡷ࡯ࡦࡺ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪ᭛") + str(error))
  return False
def bstack11l1l111ll_opy_(test_tags):
  bstack1l1ll11l1l1_opy_ = os.getenv(bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ᭜"))
  if bstack1l1ll11l1l1_opy_ is None:
    return True
  bstack1l1ll11l1l1_opy_ = json.loads(bstack1l1ll11l1l1_opy_)
  try:
    include_tags = bstack1l1ll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ᭝")] if bstack11l1l1l_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ᭞") in bstack1l1ll11l1l1_opy_ and isinstance(bstack1l1ll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ᭟")], list) else []
    exclude_tags = bstack1l1ll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭᭠")] if bstack11l1l1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ᭡") in bstack1l1ll11l1l1_opy_ and isinstance(bstack1l1ll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ᭢")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11l1l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦ᭣") + str(error))
  return False
def bstack11l11lll1l1_opy_(config, frameworkName, bstack11l11ll1l1l_opy_, bstack11l11lllll1_opy_):
  bstack11l1l11111l_opy_ = bstack11ll1llllll_opy_(config)
  bstack11l1l111l11_opy_ = bstack11lll11lll1_opy_(config)
  if bstack11l1l11111l_opy_ is None or bstack11l1l111l11_opy_ is None:
    logger.error(bstack11l1l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭᭤"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ᭥"), bstack11l1l1l_opy_ (u"ࠧࡼࡿࠪ᭦")))
    data = {
        bstack11l1l1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭᭧"): config[bstack11l1l1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ᭨")],
        bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭᭩"): config.get(bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ᭪"), os.path.basename(os.getcwd())),
        bstack11l1l1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡘ࡮ࡳࡥࠨ᭫"): bstack11llllll_opy_(),
        bstack11l1l1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱ᭬ࠫ"): config.get(bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ᭭"), bstack11l1l1l_opy_ (u"ࠨࠩ᭮")),
        bstack11l1l1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ᭯"): {
            bstack11l1l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪ᭰"): frameworkName,
            bstack11l1l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ᭱"): bstack11l11ll1l1l_opy_,
            bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ᭲"): __version__,
            bstack11l1l1l_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ᭳"): bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ᭴"),
            bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ᭵"): bstack11l1l1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ᭶"),
            bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ᭷"): bstack11l11lllll1_opy_
        },
        bstack11l1l1l_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭᭸"): settings,
        bstack11l1l1l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡉ࡯࡯ࡶࡵࡳࡱ࠭᭹"): bstack1l111111l11_opy_(),
        bstack11l1l1l_opy_ (u"࠭ࡣࡪࡋࡱࡪࡴ࠭᭺"): bstack1ll1l111l_opy_(),
        bstack11l1l1l_opy_ (u"ࠧࡩࡱࡶࡸࡎࡴࡦࡰࠩ᭻"): get_host_info(),
        bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᭼"): bstack11l1111ll1_opy_(config)
    }
    headers = {
        bstack11l1l1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ᭽"): bstack11l1l1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭᭾"),
    }
    config = {
        bstack11l1l1l_opy_ (u"ࠫࡦࡻࡴࡩࠩ᭿"): (bstack11l1l11111l_opy_, bstack11l1l111l11_opy_),
        bstack11l1l1l_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᮀ"): headers
    }
    response = bstack1l11llll1l_opy_(bstack11l1l1l_opy_ (u"࠭ࡐࡐࡕࡗࠫᮁ"), bstack11l11ll1lll_opy_ + bstack11l1l1l_opy_ (u"ࠧ࠰ࡸ࠵࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹࠧᮂ"), data, config)
    bstack11l11llllll_opy_ = response.json()
    if bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩᮃ")]:
      parsed = json.loads(os.getenv(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᮄ"), bstack11l1l1l_opy_ (u"ࠪࡿࢂ࠭ᮅ")))
      parsed[bstack11l1l1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᮆ")] = bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠬࡪࡡࡵࡣࠪᮇ")][bstack11l1l1l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᮈ")]
      os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨᮉ")] = json.dumps(parsed)
      bstack1111111l1_opy_.bstack11l1l11l111_opy_(bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᮊ")][bstack11l1l1l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪᮋ")])
      bstack1111111l1_opy_.bstack11l1l11ll1l_opy_(bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠪࡨࡦࡺࡡࠨᮌ")][bstack11l1l1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ᮍ")])
      bstack1111111l1_opy_.store()
      return bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠬࡪࡡࡵࡣࠪᮎ")][bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫᮏ")], bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠧࡥࡣࡷࡥࠬᮐ")][bstack11l1l1l_opy_ (u"ࠨ࡫ࡧࠫᮑ")]
    else:
      logger.error(bstack11l1l1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠪᮒ") + bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᮓ")])
      if bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᮔ")] == bstack11l1l1l_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡰࡢࡵࡶࡩࡩ࠴ࠧᮕ"):
        for bstack11l11lll1ll_opy_ in bstack11l11llllll_opy_[bstack11l1l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭ᮖ")]:
          logger.error(bstack11l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᮗ")])
      return None, None
  except Exception as error:
    logger.error(bstack11l1l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠤᮘ") +  str(error))
    return None, None
def bstack11l1l1111ll_opy_():
  if os.getenv(bstack11l1l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᮙ")) is None:
    return {
        bstack11l1l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᮚ"): bstack11l1l1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᮛ"),
        bstack11l1l1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᮜ"): bstack11l1l1l_opy_ (u"࠭ࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡩࡣࡧࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠬᮝ")
    }
  data = {bstack11l1l1l_opy_ (u"ࠧࡦࡰࡧࡘ࡮ࡳࡥࠨᮞ"): bstack11llllll_opy_()}
  headers = {
      bstack11l1l1l_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᮟ"): bstack11l1l1l_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࠪᮠ") + os.getenv(bstack11l1l1l_opy_ (u"ࠥࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠣᮡ")),
      bstack11l1l1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᮢ"): bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᮣ")
  }
  response = bstack1l11llll1l_opy_(bstack11l1l1l_opy_ (u"࠭ࡐࡖࡖࠪᮤ"), bstack11l11ll1lll_opy_ + bstack11l1l1l_opy_ (u"ࠧ࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶ࠳ࡸࡺ࡯ࡱࠩᮥ"), data, { bstack11l1l1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᮦ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11l1l1l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡡࡵࠢࠥᮧ") + bstack1ll1l1l1_opy_().isoformat() + bstack11l1l1l_opy_ (u"ࠪ࡞ࠬᮨ"))
      return {bstack11l1l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᮩ"): bstack11l1l1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ᮪࠭"), bstack11l1l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫᮫ࠧ"): bstack11l1l1l_opy_ (u"ࠧࠨᮬ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11l1l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡨࡵ࡭ࡱ࡮ࡨࡸ࡮ࡵ࡮ࠡࡱࡩࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯࠼ࠣࠦᮭ") + str(error))
    return {
        bstack11l1l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᮮ"): bstack11l1l1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᮯ"),
        bstack11l1l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ᮰"): str(error)
    }
def bstack111ll1l11_opy_(caps, options, desired_capabilities={}):
  try:
    bstack1l1ll1ll1ll_opy_ = caps.get(bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᮱"), {}).get(bstack11l1l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ᮲"), caps.get(bstack11l1l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ᮳"), bstack11l1l1l_opy_ (u"ࠨࠩ᮴")))
    if bstack1l1ll1ll1ll_opy_:
      logger.warn(bstack11l1l1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ᮵"))
      return False
    if options:
      bstack11l11lll111_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack11l11lll111_opy_ = desired_capabilities
    else:
      bstack11l11lll111_opy_ = {}
    browser = caps.get(bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ᮶"), bstack11l1l1l_opy_ (u"ࠫࠬ᮷")).lower() or bstack11l11lll111_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ᮸"), bstack11l1l1l_opy_ (u"࠭ࠧ᮹")).lower()
    if browser != bstack11l1l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧᮺ"):
      logger.warning(bstack11l1l1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦᮻ"))
      return False
    browser_version = caps.get(bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᮼ")) or caps.get(bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᮽ")) or bstack11l11lll111_opy_.get(bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᮾ")) or bstack11l11lll111_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᮿ"), {}).get(bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᯀ")) or bstack11l11lll111_opy_.get(bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᯁ"), {}).get(bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᯂ"))
    if browser_version and browser_version != bstack11l1l1l_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩᯃ") and int(browser_version.split(bstack11l1l1l_opy_ (u"ࠪ࠲ࠬᯄ"))[0]) <= 98:
      logger.warning(bstack11l1l1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥ࠿࠸࠯ࠤᯅ"))
      return False
    if not options:
      bstack1l1ll11l11l_opy_ = caps.get(bstack11l1l1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᯆ")) or bstack11l11lll111_opy_.get(bstack11l1l1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᯇ"), {})
      if bstack11l1l1l_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫᯈ") in bstack1l1ll11l11l_opy_.get(bstack11l1l1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ᯉ"), []):
        logger.warn(bstack11l1l1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦᯊ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack11l1l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧᯋ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack1ll11l11lll_opy_ = config.get(bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᯌ"), {})
    bstack1ll11l11lll_opy_[bstack11l1l1l_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨᯍ")] = os.getenv(bstack11l1l1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᯎ"))
    bstack11l1l111ll1_opy_ = json.loads(os.getenv(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨᯏ"), bstack11l1l1l_opy_ (u"ࠨࡽࢀࠫᯐ"))).get(bstack11l1l1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᯑ"))
    caps[bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᯒ")] = True
    if bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᯓ") in caps:
      caps[bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᯔ")][bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᯕ")] = bstack1ll11l11lll_opy_
      caps[bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᯖ")][bstack11l1l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᯗ")][bstack11l1l1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᯘ")] = bstack11l1l111ll1_opy_
    else:
      caps[bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᯙ")] = bstack1ll11l11lll_opy_
      caps[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᯚ")][bstack11l1l1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᯛ")] = bstack11l1l111ll1_opy_
  except Exception as error:
    logger.debug(bstack11l1l1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢᯜ") +  str(error))
def bstack1l111l1l11_opy_(driver, bstack11l11lll11l_opy_):
  try:
    setattr(driver, bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧᯝ"), True)
    session = driver.session_id
    if session:
      bstack11l1l111111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11l1l111111_opy_ = False
      bstack11l1l111111_opy_ = url.scheme in [bstack11l1l1l_opy_ (u"ࠣࡪࡷࡸࡵࠨᯞ"), bstack11l1l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣᯟ")]
      if bstack11l1l111111_opy_:
        if bstack11l11lll11l_opy_:
          logger.info(bstack11l1l1l_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥᯠ"))
      return bstack11l11lll11l_opy_
  except Exception as e:
    logger.error(bstack11l1l1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢᯡ") + str(e))
    return False
def bstack1111l1l1_opy_(driver, name, path):
  try:
    bstack1l1ll1lllll_opy_ = {
        bstack11l1l1l_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬᯢ"): threading.current_thread().current_test_uuid,
        bstack11l1l1l_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᯣ"): os.environ.get(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᯤ"), bstack11l1l1l_opy_ (u"ࠨࠩᯥ")),
        bstack11l1l1l_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ᯦࠭"): os.environ.get(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᯧ"), bstack11l1l1l_opy_ (u"ࠫࠬᯨ"))
    }
    bstack1l1l11ll111_opy_ = bstack11ll1111l1_opy_.bstack1l1l11ll11l_opy_(EVENTS.bstack11lllll1l_opy_.value)
    bstack11ll1111l1_opy_.mark(bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᯩ"))
    logger.debug(bstack11l1l1l_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩᯪ"))
    try:
      logger.debug(driver.execute_async_script(bstack1111111l1_opy_.perform_scan, {bstack11l1l1l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᯫ"): name}))
      bstack11ll1111l1_opy_.end(bstack1l1l11ll111_opy_, bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᯬ"), bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᯭ"), True, None)
    except Exception as error:
      bstack11ll1111l1_opy_.end(bstack1l1l11ll111_opy_, bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᯮ"), bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᯯ"), False, str(error))
    bstack1l1l11ll111_opy_ = bstack11ll1111l1_opy_.bstack1l1l11ll11l_opy_(EVENTS.bstack1l11ll111ll_opy_.value)
    bstack11ll1111l1_opy_.mark(bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᯰ"))
    try:
      logger.debug(driver.execute_async_script(bstack1111111l1_opy_.bstack11l1l11l11l_opy_, bstack1l1ll1lllll_opy_))
      bstack11ll1111l1_opy_.end(bstack1l1l11ll111_opy_, bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᯱ"), bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠢ࠻ࡧࡱࡨ᯲ࠧ"),True, None)
    except Exception as error:
      bstack11ll1111l1_opy_.end(bstack1l1l11ll111_opy_, bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴ᯳ࠣ"), bstack1l1l11ll111_opy_ + bstack11l1l1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ᯴"),False, str(error))
    logger.info(bstack11l1l1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨ᯵"))
  except Exception as bstack1l1ll11ll11_opy_:
    logger.error(bstack11l1l1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ᯶") + str(path) + bstack11l1l1l_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢ᯷") + str(bstack1l1ll11ll11_opy_))