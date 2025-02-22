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
import atexit
import signal
import yaml
import socket
import datetime
import string
import random
import collections.abc
import traceback
import copy
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.measure import bstack11ll1111l1_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from browserstack_sdk.bstack1111111l_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11l1lll111_opy_ import bstack1l11l11111_opy_
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack11l11ll111_opy_():
  global CONFIG
  headers = {
        bstack11l1l1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ৖"): bstack11l1l1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩৗ"),
      }
  proxies = bstack1l1lll1ll_opy_(CONFIG, bstack11l111l111_opy_)
  try:
    response = requests.get(bstack11l111l111_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack11ll11111l_opy_ = response.json()[bstack11l1l1l_opy_ (u"ࠧࡩࡷࡥࡷࠬ৘")]
      logger.debug(bstack11ll11ll1_opy_.format(response.json()))
      return bstack11ll11111l_opy_
    else:
      logger.debug(bstack1l11l1l11l_opy_.format(bstack11l1l1l_opy_ (u"ࠣࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡎࡘࡕࡎࠡࡲࡤࡶࡸ࡫ࠠࡦࡴࡵࡳࡷࠦࠢ৙")))
  except Exception as e:
    logger.debug(bstack1l11l1l11l_opy_.format(e))
def bstack1ll111l1l1_opy_(hub_url):
  global CONFIG
  url = bstack11l1l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦ৚")+  hub_url + bstack11l1l1l_opy_ (u"ࠥ࠳ࡨ࡮ࡥࡤ࡭ࠥ৛")
  headers = {
        bstack11l1l1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪড়"): bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨঢ়"),
      }
  proxies = bstack1l1lll1ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11ll111ll1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack11llll111_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack11lll11l1_opy_, stage=STAGE.SINGLE)
def bstack11l1l1ll11_opy_():
  try:
    global bstack11l11111l_opy_
    bstack11ll11111l_opy_ = bstack11l11ll111_opy_()
    bstack1llllll11_opy_ = []
    results = []
    for bstack1l11l111l1_opy_ in bstack11ll11111l_opy_:
      bstack1llllll11_opy_.append(bstack1ll111l11_opy_(target=bstack1ll111l1l1_opy_,args=(bstack1l11l111l1_opy_,)))
    for t in bstack1llllll11_opy_:
      t.start()
    for t in bstack1llllll11_opy_:
      results.append(t.join())
    bstack1111l111l_opy_ = {}
    for item in results:
      hub_url = item[bstack11l1l1l_opy_ (u"࠭ࡨࡶࡤࡢࡹࡷࡲࠧ৞")]
      latency = item[bstack11l1l1l_opy_ (u"ࠧ࡭ࡣࡷࡩࡳࡩࡹࠨয়")]
      bstack1111l111l_opy_[hub_url] = latency
    bstack11l11l11l1_opy_ = min(bstack1111l111l_opy_, key= lambda x: bstack1111l111l_opy_[x])
    bstack11l11111l_opy_ = bstack11l11l11l1_opy_
    logger.debug(bstack1l11l11l1_opy_.format(bstack11l11l11l1_opy_))
  except Exception as e:
    logger.debug(bstack1ll1l1l1l1_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack111111l1l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l11l1l11_opy_, bstack1l11llll1l_opy_, bstack1lll111l1l_opy_, bstack11llll1l_opy_, \
  bstack11l1111ll1_opy_, \
  Notset, bstack1l11ll1lll_opy_, \
  bstack1l1lllll11_opy_, bstack1l111l11ll_opy_, bstack11l11l11l_opy_, bstack1ll1l111l_opy_, bstack11l1ll111l_opy_, bstack1l11l111ll_opy_, \
  bstack1l1ll11111_opy_, \
  bstack1l1lllllll_opy_, bstack11l111l1ll_opy_, bstack1l11ll11ll_opy_, bstack11l111l1l1_opy_, \
  bstack11ll11ll1l_opy_, bstack1lll1ll1l1_opy_, bstack1l1llllll1_opy_, bstack1ll1l1ll1_opy_
from bstack_utils.bstack1llll1lll1_opy_ import bstack11llll1lll_opy_, bstack1ll11ll1l_opy_
from bstack_utils.bstack1l11111l1l_opy_ import bstack1lll1lll1l_opy_
from bstack_utils.bstack1ll1111l1l_opy_ import bstack11ll11l1ll_opy_, bstack11lll1ll1_opy_
from bstack_utils.bstack1111111l1_opy_ import bstack1111111l1_opy_
from bstack_utils.proxy import bstack1lll11l11l_opy_, bstack1l1lll1ll_opy_, bstack1lll1111l1_opy_, bstack1ll11l1111_opy_
from browserstack_sdk.bstack111l11l1_opy_ import *
from browserstack_sdk.bstack11l1111l_opy_ import *
from bstack_utils.bstack11ll11l111_opy_ import bstack1l1l1ll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1l1llll11l_opy_ import bstack1l1llll11l_opy_, Events, bstack11ll1l1lll_opy_, bstack11l11lll1_opy_
from browserstack_sdk.bstack11l11lll_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack111111l1l_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11llll1ll1_opy_, stage=STAGE.SINGLE)
def bstack1ll1ll11l_opy_():
    global bstack11l11111l_opy_
    try:
        bstack1llll111l_opy_ = bstack1ll1ll1l1l_opy_()
        bstack1l1llll11_opy_(bstack1llll111l_opy_)
        hub_url = bstack1llll111l_opy_.get(bstack11l1l1l_opy_ (u"ࠣࡷࡵࡰࠧৠ"), bstack11l1l1l_opy_ (u"ࠤࠥৡ"))
        if hub_url.endswith(bstack11l1l1l_opy_ (u"ࠪ࠳ࡼࡪ࠯ࡩࡷࡥࠫৢ")):
            hub_url = hub_url.rsplit(bstack11l1l1l_opy_ (u"ࠫ࠴ࡽࡤ࠰ࡪࡸࡦࠬৣ"), 1)[0]
        if hub_url.startswith(bstack11l1l1l_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࠭৤")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11l1l1l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࠨ৥")):
            hub_url = hub_url[8:]
        bstack11l11111l_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1ll1ll1l1l_opy_():
    global CONFIG
    bstack111l1ll11_opy_ = CONFIG.get(bstack11l1l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ০"), {}).get(bstack11l1l1l_opy_ (u"ࠨࡩࡵ࡭ࡩࡔࡡ࡮ࡧࠪ১"), bstack11l1l1l_opy_ (u"ࠩࡑࡓࡤࡍࡒࡊࡆࡢࡒࡆࡓࡅࡠࡒࡄࡗࡘࡋࡄࠨ২"))
    if not isinstance(bstack111l1ll11_opy_, str):
        raise ValueError(bstack11l1l1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡊࡶ࡮ࡪࠠ࡯ࡣࡰࡩࠥࡳࡵࡴࡶࠣࡦࡪࠦࡡࠡࡸࡤࡰ࡮ࡪࠠࡴࡶࡵ࡭ࡳ࡭ࠢ৩"))
    try:
        bstack1llll111l_opy_ = bstack1l111ll11_opy_(bstack111l1ll11_opy_)
        return bstack1llll111l_opy_
    except Exception as e:
        logger.error(bstack11l1l1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡀࠠࡼࡿࠥ৪").format(str(e)))
        return {}
def bstack1l111ll11_opy_(bstack111l1ll11_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11l1l1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ৫")] or not CONFIG[bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ৬")]:
            raise ValueError(bstack11l1l1l_opy_ (u"ࠢࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠢࡲࡶࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠤ৭"))
        url = bstack1l1l111l1l_opy_ + bstack111l1ll11_opy_
        auth = (CONFIG[bstack11l1l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ৮")], CONFIG[bstack11l1l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ৯")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1l111ll1l_opy_ = json.loads(response.text)
            return bstack1l111ll1l_opy_
    except ValueError as ve:
        logger.error(bstack11l1l1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡀࠠࡼࡿࠥৰ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11l1l1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸࠦ࠺ࠡࡽࢀࠦৱ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l1llll11_opy_(bstack1lll11l1ll_opy_):
    global CONFIG
    if bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ৲") not in CONFIG or str(CONFIG[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ৳")]).lower() == bstack11l1l1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭৴"):
        CONFIG[bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧ৵")] = False
    elif bstack11l1l1l_opy_ (u"ࠩ࡬ࡷ࡙ࡸࡩࡢ࡮ࡊࡶ࡮ࡪࠧ৶") in bstack1lll11l1ll_opy_:
        bstack1l11ll1l1l_opy_ = CONFIG.get(bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ৷"), {})
        logger.debug(bstack11l1l1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡲ࡯ࡤࡣ࡯ࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠥࡴࠤ৸"), bstack1l11ll1l1l_opy_)
        bstack1lllll11l1_opy_ = bstack1lll11l1ll_opy_.get(bstack11l1l1l_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡗ࡫ࡰࡦࡣࡷࡩࡷࡹࠢ৹"), [])
        bstack1l1111l11l_opy_ = bstack11l1l1l_opy_ (u"ࠨࠬࠣ৺").join(bstack1lllll11l1_opy_)
        logger.debug(bstack11l1l1l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡃࡶࡵࡷࡳࡲࠦࡲࡦࡲࡨࡥࡹ࡫ࡲࠡࡵࡷࡶ࡮ࡴࡧ࠻ࠢࠨࡷࠧ৻"), bstack1l1111l11l_opy_)
        bstack1ll1111ll_opy_ = {
            bstack11l1l1l_opy_ (u"ࠣ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥৼ"): bstack11l1l1l_opy_ (u"ࠤࡤࡸࡸ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠣ৽"),
            bstack11l1l1l_opy_ (u"ࠥࡪࡴࡸࡣࡦࡎࡲࡧࡦࡲࠢ৾"): bstack11l1l1l_opy_ (u"ࠦࡹࡸࡵࡦࠤ৿"),
            bstack11l1l1l_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࠲ࡸࡥࡱࡧࡤࡸࡪࡸࠢ਀"): bstack1l1111l11l_opy_
        }
        bstack1l11ll1l1l_opy_.update(bstack1ll1111ll_opy_)
        logger.debug(bstack11l1l1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾࡛ࠥࡰࡥࡣࡷࡩࡩࠦ࡬ࡰࡥࡤࡰࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠦࡵࠥਁ"), bstack1l11ll1l1l_opy_)
        CONFIG[bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫਂ")] = bstack1l11ll1l1l_opy_
        logger.debug(bstack11l1l1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡇ࡫ࡱࡥࡱࠦࡃࡐࡐࡉࡍࡌࡀࠠࠦࡵࠥਃ"), CONFIG)
def bstack1lllll111l_opy_():
    bstack1llll111l_opy_ = bstack1ll1ll1l1l_opy_()
    if not bstack1llll111l_opy_[bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩ਄")]:
      raise ValueError(bstack11l1l1l_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࡕࡳ࡮ࠣ࡭ࡸࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡧࡴࡲࡱࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠧਅ"))
    return bstack1llll111l_opy_[bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡖࡴ࡯ࠫਆ")] + bstack11l1l1l_opy_ (u"ࠬࡅࡣࡢࡲࡶࡁࠬਇ")
@measure(event_name=EVENTS.bstack111l1l11l_opy_, stage=STAGE.SINGLE)
def bstack1l11lll1l_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨਈ")], CONFIG[bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪਉ")])
        url = bstack111ll1l11l_opy_
        logger.debug(bstack11l1l1l_opy_ (u"ࠣࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹࠠࡧࡴࡲࡱࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤ࡙ࡻࡲࡣࡱࡖࡧࡦࡲࡥࠡࡃࡓࡍࠧਊ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11l1l1l_opy_ (u"ࠤࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠣ਋"): bstack11l1l1l_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳࠨ਌")})
            if response.status_code == 200:
                bstack1l1ll11ll1_opy_ = json.loads(response.text)
                bstack1llll111ll_opy_ = bstack1l1ll11ll1_opy_.get(bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡶࠫ਍"), [])
                if bstack1llll111ll_opy_:
                    bstack11lllll11l_opy_ = bstack1llll111ll_opy_[0]
                    build_hashed_id = bstack11lllll11l_opy_.get(bstack11l1l1l_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ਎"))
                    bstack1lllll1l1l_opy_ = bstack11l111llll_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1lllll1l1l_opy_])
                    logger.info(bstack11l1lll11l_opy_.format(bstack1lllll1l1l_opy_))
                    bstack1l1lll11l_opy_ = CONFIG[bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩਏ")]
                    if bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩਐ") in CONFIG:
                      bstack1l1lll11l_opy_ += bstack11l1l1l_opy_ (u"ࠨࠢࠪ਑") + CONFIG[bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ਒")]
                    if bstack1l1lll11l_opy_ != bstack11lllll11l_opy_.get(bstack11l1l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨਓ")):
                      logger.debug(bstack1ll1111l11_opy_.format(bstack11lllll11l_opy_.get(bstack11l1l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩਔ")), bstack1l1lll11l_opy_))
                    return result
                else:
                    logger.debug(bstack11l1l1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡓࡵࠠࡣࡷ࡬ࡰࡩࡹࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠯ࠤਕ"))
            else:
                logger.debug(bstack11l1l1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹ࠮ࠣਖ"))
        except Exception as e:
            logger.error(bstack11l1l1l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࡴࠢ࠽ࠤࢀࢃࠢਗ").format(str(e)))
    else:
        logger.debug(bstack11l1l1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡄࡑࡑࡊࡎࡍࠠࡪࡵࠣࡲࡴࡺࠠࡴࡧࡷ࠲࡛ࠥ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹ࠮ࠣਘ"))
    return [None, None]
import bstack_utils.bstack1ll1llll1l_opy_ as bstack11l1111l1_opy_
import bstack_utils.bstack1ll11111ll_opy_ as bstack1lll11ll11_opy_
from browserstack_sdk.sdk_cli.cli import cli
if os.getenv(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡎࡏࡐࡍࡖࠫਙ")):
  cli.bstack1ll1llll11_opy_()
else:
  os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡈࡐࡑࡎࡗࠬਚ")] = bstack11l1l1l_opy_ (u"ࠫࡹࡸࡵࡦࠩਛ")
bstack11lll11111_opy_ = bstack11l1l1l_opy_ (u"ࠬࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠥࠦࡩࡧࠪࡳࡥ࡬࡫ࠠ࠾࠿ࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠥࢁ࡜࡯ࠢࠣࠤࡹࡸࡹࡼ࡞ࡱࠤࡨࡵ࡮ࡴࡶࠣࡪࡸࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪ࡟ࠫ࡫ࡹ࡜ࠨࠫ࠾ࡠࡳࠦࠠࠡࠢࠣࡪࡸ࠴ࡡࡱࡲࡨࡲࡩࡌࡩ࡭ࡧࡖࡽࡳࡩࠨࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬࠱ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡱࡡ࡬ࡲࡩ࡫ࡸࠪࠢ࠮ࠤࠧࡀࠢࠡ࠭ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࠪࡤࡻࡦ࡯ࡴࠡࡰࡨࡻࡕࡧࡧࡦ࠴࠱ࡩࡻࡧ࡬ࡶࡣࡷࡩ࠭ࠨࠨࠪࠢࡀࡂࠥࢁࡽࠣ࠮ࠣࡠࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧ࡭ࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡆࡨࡸࡦ࡯࡬ࡴࠤࢀࡠࠬ࠯ࠩࠪ࡝ࠥ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩࠨ࡝ࠪࠢ࠮ࠤࠧ࠲࡜࡝ࡰࠥ࠭ࡡࡴࠠࠡࠢࠣࢁࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࢂࡢ࡮ࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠬਜ")
bstack11ll11lll1_opy_ = bstack11l1l1l_opy_ (u"࠭࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࡞ࡱࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࡞ࡱࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࡠࡳ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࡢ࡮࡭ࡧࡷࠤࡨࡧࡰࡴ࠽࡟ࡲࡹࡸࡹࠡࡽ࡟ࡲࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࡜࡯ࠢࠣࢁࠥࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࠡࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻ࡝ࡰࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࡥࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠤࡼࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࡽࡡ࠮࡟ࡲࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࡠࡳࠦࠠࡾࠫ࡟ࡲࢂࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠬਝ")
from ._version import __version__
bstack1ll11l1ll1_opy_ = None
CONFIG = {}
bstack1l111ll1l1_opy_ = {}
bstack1l1l11l11l_opy_ = {}
bstack1l1lll1111_opy_ = None
bstack1ll11ll1ll_opy_ = None
bstack11l1ll111_opy_ = None
bstack1ll1l1l11l_opy_ = -1
bstack1ll1ll111l_opy_ = 0
bstack1l11l1111l_opy_ = bstack11lll1l1ll_opy_
bstack1l1l11ll11_opy_ = 1
bstack11ll11lll_opy_ = False
bstack1ll111111l_opy_ = False
bstack11l1ll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࠨਞ")
bstack1ll1lll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࠩਟ")
bstack1ll1111ll1_opy_ = False
bstack1l111111l_opy_ = True
bstack1lll1l1ll_opy_ = bstack11l1l1l_opy_ (u"ࠩࠪਠ")
bstack11ll1ll1l_opy_ = []
bstack11l11111l_opy_ = bstack11l1l1l_opy_ (u"ࠪࠫਡ")
bstack11l111lll1_opy_ = False
bstack1llll1l1ll_opy_ = None
bstack1l1l1l1lll_opy_ = None
bstack1ll1l1111_opy_ = None
bstack1ll11ll111_opy_ = -1
bstack111l1lllll_opy_ = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠫࢃ࠭ਢ")), bstack11l1l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬਣ"), bstack11l1l1l_opy_ (u"࠭࠮ࡳࡱࡥࡳࡹ࠳ࡲࡦࡲࡲࡶࡹ࠳ࡨࡦ࡮ࡳࡩࡷ࠴ࡪࡴࡱࡱࠫਤ"))
bstack1lllll111_opy_ = 0
bstack1ll11ll11l_opy_ = 0
bstack11l1ll11ll_opy_ = []
bstack1ll111l11l_opy_ = []
bstack1l1l111111_opy_ = []
bstack11l11lll1l_opy_ = []
bstack1l1111111_opy_ = bstack11l1l1l_opy_ (u"ࠧࠨਥ")
bstack1lll1lll11_opy_ = bstack11l1l1l_opy_ (u"ࠨࠩਦ")
bstack11lll11lll_opy_ = False
bstack1ll11lll11_opy_ = False
bstack1llll1l111_opy_ = {}
bstack11l11l1ll1_opy_ = None
bstack1lll1lllll_opy_ = None
bstack1ll1lll11l_opy_ = None
bstack1lll1ll111_opy_ = None
bstack111ll1111l_opy_ = None
bstack11l11ll11l_opy_ = None
bstack1l1llll1l1_opy_ = None
bstack111lll1ll_opy_ = None
bstack111lllll1l_opy_ = None
bstack1l1111l1ll_opy_ = None
bstack11llll111l_opy_ = None
bstack11l1l1l1l1_opy_ = None
bstack1lll1l111l_opy_ = None
bstack1l1ll1l1l1_opy_ = None
bstack1l1lll111_opy_ = None
bstack1l1l1l111l_opy_ = None
bstack1ll111ll11_opy_ = None
bstack11lll1l1l1_opy_ = None
bstack1l11llll11_opy_ = None
bstack11l1lll1ll_opy_ = None
bstack1llll1l11l_opy_ = None
bstack111ll11ll1_opy_ = None
bstack1l1lll11l1_opy_ = False
bstack1llllll1l1_opy_ = bstack11l1l1l_opy_ (u"ࠤࠥਧ")
logger = bstack111111l1l_opy_.get_logger(__name__, bstack1l11l1111l_opy_)
bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
percy = bstack11111l111_opy_()
bstack11ll1l1l1_opy_ = bstack1l11l11111_opy_()
bstack111111lll_opy_ = bstack11l11lll_opy_()
def bstack111l1llll1_opy_():
  global CONFIG
  global bstack11lll11lll_opy_
  global bstack11111l11_opy_
  bstack1lll111ll1_opy_ = bstack1lllllllll_opy_(CONFIG)
  if bstack11l1111ll1_opy_(CONFIG):
    if (bstack11l1l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬਨ") in bstack1lll111ll1_opy_ and str(bstack1lll111ll1_opy_[bstack11l1l1l_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭਩")]).lower() == bstack11l1l1l_opy_ (u"ࠬࡺࡲࡶࡧࠪਪ")):
      bstack11lll11lll_opy_ = True
    bstack11111l11_opy_.bstack1lllll1ll_opy_(bstack1lll111ll1_opy_.get(bstack11l1l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪਫ"), False))
  else:
    bstack11lll11lll_opy_ = True
    bstack11111l11_opy_.bstack1lllll1ll_opy_(True)
def bstack11ll1ll11l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1ll1l1111l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11llll11ll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11l1l1l_opy_ (u"ࠢ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡤࡱࡱࡪ࡮࡭ࡦࡪ࡮ࡨࠦਬ") == args[i].lower() or bstack11l1l1l_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡳ࡬ࡩࡨࠤਭ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1lll1l1ll_opy_
      bstack1lll1l1ll_opy_ += bstack11l1l1l_opy_ (u"ࠩ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨࡈ࡬ࡰࡪࠦࠧਮ") + path
      return path
  return None
bstack1l111l11l_opy_ = re.compile(bstack11l1l1l_opy_ (u"ࡵࠦ࠳࠰࠿࡝ࠦࡾࠬ࠳࠰࠿ࠪࡿ࠱࠮ࡄࠨਯ"))
def bstack1lllllll1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l111l11l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11l1l1l_opy_ (u"ࠦࠩࢁࠢਰ") + group + bstack11l1l1l_opy_ (u"ࠧࢃࠢ਱"), os.environ.get(group))
  return value
def bstack1l1ll11l1l_opy_():
  bstack111l11l1l_opy_ = bstack11llll11ll_opy_()
  if bstack111l11l1l_opy_ and os.path.exists(os.path.abspath(bstack111l11l1l_opy_)):
    fileName = bstack111l11l1l_opy_
  if bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪਲ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫਲ਼")])) and not bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪ਴") in locals():
    fileName = os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭ਵ")]
  if bstack11l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡏࡣࡰࡩࠬਸ਼") in locals():
    bstack1l1l1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack1l1l1ll_opy_ = bstack11l1l1l_opy_ (u"ࠫࠬ਷")
  bstack1llll11l1l_opy_ = os.getcwd()
  bstack11111l1ll_opy_ = bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨਸ")
  bstack1111lll1l_opy_ = bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿࡡ࡮࡮ࠪਹ")
  while (not os.path.exists(bstack1l1l1ll_opy_)) and bstack1llll11l1l_opy_ != bstack11l1l1l_opy_ (u"ࠢࠣ਺"):
    bstack1l1l1ll_opy_ = os.path.join(bstack1llll11l1l_opy_, bstack11111l1ll_opy_)
    if not os.path.exists(bstack1l1l1ll_opy_):
      bstack1l1l1ll_opy_ = os.path.join(bstack1llll11l1l_opy_, bstack1111lll1l_opy_)
    if bstack1llll11l1l_opy_ != os.path.dirname(bstack1llll11l1l_opy_):
      bstack1llll11l1l_opy_ = os.path.dirname(bstack1llll11l1l_opy_)
    else:
      bstack1llll11l1l_opy_ = bstack11l1l1l_opy_ (u"ࠣࠤ਻")
  return bstack1l1l1ll_opy_ if os.path.exists(bstack1l1l1ll_opy_) else None
def bstack11l11l1l11_opy_():
  bstack1l1l1ll_opy_ = bstack1l1ll11l1l_opy_()
  if not os.path.exists(bstack1l1l1ll_opy_):
    bstack1l11ll111l_opy_(
      bstack1llllllll1_opy_.format(os.getcwd()))
  try:
    with open(bstack1l1l1ll_opy_, bstack11l1l1l_opy_ (u"ࠩࡵ਼ࠫ")) as stream:
      yaml.add_implicit_resolver(bstack11l1l1l_opy_ (u"ࠥࠥࡵࡧࡴࡩࡧࡻࠦ਽"), bstack1l111l11l_opy_)
      yaml.add_constructor(bstack11l1l1l_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧਾ"), bstack1lllllll1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack1l1l1ll_opy_, bstack11l1l1l_opy_ (u"ࠬࡸࠧਿ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1l11ll111l_opy_(bstack11l11l1ll_opy_.format(str(exc)))
def bstack1l11ll1l11_opy_(config):
  bstack111l111l1_opy_ = bstack111lll1lll_opy_(config)
  for option in list(bstack111l111l1_opy_):
    if option.lower() in bstack1lll11111_opy_ and option != bstack1lll11111_opy_[option.lower()]:
      bstack111l111l1_opy_[bstack1lll11111_opy_[option.lower()]] = bstack111l111l1_opy_[option]
      del bstack111l111l1_opy_[option]
  return config
def bstack11lll1l11_opy_():
  global bstack1l1l11l11l_opy_
  for key, bstack1lll111ll_opy_ in bstack1l1l11lll_opy_.items():
    if isinstance(bstack1lll111ll_opy_, list):
      for var in bstack1lll111ll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l1l11l11l_opy_[key] = os.environ[var]
          break
    elif bstack1lll111ll_opy_ in os.environ and os.environ[bstack1lll111ll_opy_] and str(os.environ[bstack1lll111ll_opy_]).strip():
      bstack1l1l11l11l_opy_[key] = os.environ[bstack1lll111ll_opy_]
  if bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨੀ") in os.environ:
    bstack1l1l11l11l_opy_[bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫੁ")] = {}
    bstack1l1l11l11l_opy_[bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬੂ")][bstack11l1l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੃")] = os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ੄")]
def bstack1l1l11llll_opy_():
  global bstack1l111ll1l1_opy_
  global bstack1lll1l1ll_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack11l1l1l_opy_ (u"ࠫ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੅").lower() == val.lower():
      bstack1l111ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੆")] = {}
      bstack1l111ll1l1_opy_[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪੇ")][bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩੈ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1lll11lll_opy_ in bstack1111ll111_opy_.items():
    if isinstance(bstack1lll11lll_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1lll11lll_opy_:
          if idx < len(sys.argv) and bstack11l1l1l_opy_ (u"ࠨ࠯࠰ࠫ੉") + var.lower() == val.lower() and not key in bstack1l111ll1l1_opy_:
            bstack1l111ll1l1_opy_[key] = sys.argv[idx + 1]
            bstack1lll1l1ll_opy_ += bstack11l1l1l_opy_ (u"ࠩࠣ࠱࠲࠭੊") + var + bstack11l1l1l_opy_ (u"ࠪࠤࠬੋ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack11l1l1l_opy_ (u"ࠫ࠲࠳ࠧੌ") + bstack1lll11lll_opy_.lower() == val.lower() and not key in bstack1l111ll1l1_opy_:
          bstack1l111ll1l1_opy_[key] = sys.argv[idx + 1]
          bstack1lll1l1ll_opy_ += bstack11l1l1l_opy_ (u"ࠬࠦ࠭࠮੍ࠩ") + bstack1lll11lll_opy_ + bstack11l1l1l_opy_ (u"࠭ࠠࠨ੎") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack11lll1l11l_opy_(config):
  bstack1l1lll1lll_opy_ = config.keys()
  for bstack111lllllll_opy_, bstack1llll1llll_opy_ in bstack11l111ll1_opy_.items():
    if bstack1llll1llll_opy_ in bstack1l1lll1lll_opy_:
      config[bstack111lllllll_opy_] = config[bstack1llll1llll_opy_]
      del config[bstack1llll1llll_opy_]
  for bstack111lllllll_opy_, bstack1llll1llll_opy_ in bstack11111ll11_opy_.items():
    if isinstance(bstack1llll1llll_opy_, list):
      for bstack11lll1l111_opy_ in bstack1llll1llll_opy_:
        if bstack11lll1l111_opy_ in bstack1l1lll1lll_opy_:
          config[bstack111lllllll_opy_] = config[bstack11lll1l111_opy_]
          del config[bstack11lll1l111_opy_]
          break
    elif bstack1llll1llll_opy_ in bstack1l1lll1lll_opy_:
      config[bstack111lllllll_opy_] = config[bstack1llll1llll_opy_]
      del config[bstack1llll1llll_opy_]
  for bstack11lll1l111_opy_ in list(config):
    for bstack1l1ll1ll11_opy_ in bstack11lll11ll_opy_:
      if bstack11lll1l111_opy_.lower() == bstack1l1ll1ll11_opy_.lower() and bstack11lll1l111_opy_ != bstack1l1ll1ll11_opy_:
        config[bstack1l1ll1ll11_opy_] = config[bstack11lll1l111_opy_]
        del config[bstack11lll1l111_opy_]
  bstack111ll1lll1_opy_ = [{}]
  if not config.get(bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ੏")):
    config[bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ੐")] = [{}]
  bstack111ll1lll1_opy_ = config[bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬੑ")]
  for platform in bstack111ll1lll1_opy_:
    for bstack11lll1l111_opy_ in list(platform):
      for bstack1l1ll1ll11_opy_ in bstack11lll11ll_opy_:
        if bstack11lll1l111_opy_.lower() == bstack1l1ll1ll11_opy_.lower() and bstack11lll1l111_opy_ != bstack1l1ll1ll11_opy_:
          platform[bstack1l1ll1ll11_opy_] = platform[bstack11lll1l111_opy_]
          del platform[bstack11lll1l111_opy_]
  for bstack111lllllll_opy_, bstack1llll1llll_opy_ in bstack11111ll11_opy_.items():
    for platform in bstack111ll1lll1_opy_:
      if isinstance(bstack1llll1llll_opy_, list):
        for bstack11lll1l111_opy_ in bstack1llll1llll_opy_:
          if bstack11lll1l111_opy_ in platform:
            platform[bstack111lllllll_opy_] = platform[bstack11lll1l111_opy_]
            del platform[bstack11lll1l111_opy_]
            break
      elif bstack1llll1llll_opy_ in platform:
        platform[bstack111lllllll_opy_] = platform[bstack1llll1llll_opy_]
        del platform[bstack1llll1llll_opy_]
  for bstack1lll111l11_opy_ in bstack111ll1ll11_opy_:
    if bstack1lll111l11_opy_ in config:
      if not bstack111ll1ll11_opy_[bstack1lll111l11_opy_] in config:
        config[bstack111ll1ll11_opy_[bstack1lll111l11_opy_]] = {}
      config[bstack111ll1ll11_opy_[bstack1lll111l11_opy_]].update(config[bstack1lll111l11_opy_])
      del config[bstack1lll111l11_opy_]
  for platform in bstack111ll1lll1_opy_:
    for bstack1lll111l11_opy_ in bstack111ll1ll11_opy_:
      if bstack1lll111l11_opy_ in list(platform):
        if not bstack111ll1ll11_opy_[bstack1lll111l11_opy_] in platform:
          platform[bstack111ll1ll11_opy_[bstack1lll111l11_opy_]] = {}
        platform[bstack111ll1ll11_opy_[bstack1lll111l11_opy_]].update(platform[bstack1lll111l11_opy_])
        del platform[bstack1lll111l11_opy_]
  config = bstack1l11ll1l11_opy_(config)
  return config
def bstack1l1l1l1ll_opy_(config):
  global bstack1ll1lll1l1_opy_
  bstack1l11ll11l1_opy_ = False
  if bstack11l1l1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ੒") in config and str(config[bstack11l1l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ੓")]).lower() != bstack11l1l1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ੔"):
    if bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ੕") not in config or str(config[bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ੖")]).lower() == bstack11l1l1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ੗"):
      config[bstack11l1l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨ੘")] = False
    else:
      bstack1llll111l_opy_ = bstack1ll1ll1l1l_opy_()
      if bstack11l1l1l_opy_ (u"ࠪ࡭ࡸ࡚ࡲࡪࡣ࡯ࡋࡷ࡯ࡤࠨਖ਼") in bstack1llll111l_opy_:
        if not bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨਗ਼") in config:
          config[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩਜ਼")] = {}
        config[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪੜ")][bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ੝")] = bstack11l1l1l_opy_ (u"ࠨࡣࡷࡷ࠲ࡸࡥࡱࡧࡤࡸࡪࡸࠧਫ਼")
        bstack1l11ll11l1_opy_ = True
        bstack1ll1lll1l1_opy_ = config[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੟")].get(bstack11l1l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੠"))
  if bstack11l1111ll1_opy_(config) and bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ੡") in config and str(config[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ੢")]).lower() != bstack11l1l1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ੣") and not bstack1l11ll11l1_opy_:
    if not bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ੤") in config:
      config[bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੥")] = {}
    if not config[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੦")].get(bstack11l1l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠧ੧")) and not bstack11l1l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੨") in config[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੩")]:
      bstack11llllll_opy_ = datetime.datetime.now()
      bstack1ll1l1l1ll_opy_ = bstack11llllll_opy_.strftime(bstack11l1l1l_opy_ (u"࠭ࠥࡥࡡࠨࡦࡤࠫࡈࠦࡏࠪ੪"))
      hostname = socket.gethostname()
      bstack1l1ll1l1l_opy_ = bstack11l1l1l_opy_ (u"ࠧࠨ੫").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11l1l1l_opy_ (u"ࠨࡽࢀࡣࢀࢃ࡟ࡼࡿࠪ੬").format(bstack1ll1l1l1ll_opy_, hostname, bstack1l1ll1l1l_opy_)
      config[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੭")][bstack11l1l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੮")] = identifier
    bstack1ll1lll1l1_opy_ = config[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੯")].get(bstack11l1l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧੰ"))
  return config
def bstack111llll1ll_opy_():
  bstack1lll1l1l1l_opy_ =  bstack1ll1l111l_opy_()[bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠬੱ")]
  return bstack1lll1l1l1l_opy_ if bstack1lll1l1l1l_opy_ else -1
def bstack1l1l11ll1l_opy_(bstack1lll1l1l1l_opy_):
  global CONFIG
  if not bstack11l1l1l_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩੲ") in CONFIG[bstack11l1l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪੳ")]:
    return
  CONFIG[bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫੴ")] = CONFIG[bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬੵ")].replace(
    bstack11l1l1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭੶"),
    str(bstack1lll1l1l1l_opy_)
  )
def bstack111ll11l1l_opy_():
  global CONFIG
  if not bstack11l1l1l_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫ੷") in CONFIG[bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੸")]:
    return
  bstack11llllll_opy_ = datetime.datetime.now()
  bstack1ll1l1l1ll_opy_ = bstack11llllll_opy_.strftime(bstack11l1l1l_opy_ (u"ࠧࠦࡦ࠰ࠩࡧ࠳ࠥࡉ࠼ࠨࡑࠬ੹"))
  CONFIG[bstack11l1l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ੺")] = CONFIG[bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੻")].replace(
    bstack11l1l1l_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩ੼"),
    bstack1ll1l1l1ll_opy_
  )
def bstack1lll1111l_opy_():
  global CONFIG
  if bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੽") in CONFIG and not bool(CONFIG[bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੾")]):
    del CONFIG[bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੿")]
    return
  if not bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઀") in CONFIG:
    CONFIG[bstack11l1l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઁ")] = bstack11l1l1l_opy_ (u"ࠩࠦࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬં")
  if bstack11l1l1l_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩઃ") in CONFIG[bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭઄")]:
    bstack111ll11l1l_opy_()
    os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩઅ")] = CONFIG[bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઆ")]
  if not bstack11l1l1l_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩઇ") in CONFIG[bstack11l1l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઈ")]:
    return
  bstack1lll1l1l1l_opy_ = bstack11l1l1l_opy_ (u"ࠩࠪઉ")
  bstack1l111l1ll_opy_ = bstack111llll1ll_opy_()
  if bstack1l111l1ll_opy_ != -1:
    bstack1lll1l1l1l_opy_ = bstack11l1l1l_opy_ (u"ࠪࡇࡎࠦࠧઊ") + str(bstack1l111l1ll_opy_)
  if bstack1lll1l1l1l_opy_ == bstack11l1l1l_opy_ (u"ࠫࠬઋ"):
    bstack1ll1ll1ll1_opy_ = bstack1l1l11111l_opy_(CONFIG[bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨઌ")])
    if bstack1ll1ll1ll1_opy_ != -1:
      bstack1lll1l1l1l_opy_ = str(bstack1ll1ll1ll1_opy_)
  if bstack1lll1l1l1l_opy_:
    bstack1l1l11ll1l_opy_(bstack1lll1l1l1l_opy_)
    os.environ[bstack11l1l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪઍ")] = CONFIG[bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઎")]
def bstack11l1l11ll_opy_(bstack1ll1l1ll1l_opy_, bstack1l1l11l1l_opy_, path):
  json_data = {
    bstack11l1l1l_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬએ"): bstack1l1l11l1l_opy_
  }
  if os.path.exists(path):
    bstack111l1l1l1_opy_ = json.load(open(path, bstack11l1l1l_opy_ (u"ࠩࡵࡦࠬઐ")))
  else:
    bstack111l1l1l1_opy_ = {}
  bstack111l1l1l1_opy_[bstack1ll1l1ll1l_opy_] = json_data
  with open(path, bstack11l1l1l_opy_ (u"ࠥࡻ࠰ࠨઑ")) as outfile:
    json.dump(bstack111l1l1l1_opy_, outfile)
def bstack1l1l11111l_opy_(bstack1ll1l1ll1l_opy_):
  bstack1ll1l1ll1l_opy_ = str(bstack1ll1l1ll1l_opy_)
  bstack1lll1l1111_opy_ = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠫࢃ࠭઒")), bstack11l1l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬઓ"))
  try:
    if not os.path.exists(bstack1lll1l1111_opy_):
      os.makedirs(bstack1lll1l1111_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"࠭ࡾࠨઔ")), bstack11l1l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧક"), bstack11l1l1l_opy_ (u"ࠨ࠰ࡥࡹ࡮ࡲࡤ࠮ࡰࡤࡱࡪ࠳ࡣࡢࡥ࡫ࡩ࠳ࡰࡳࡰࡰࠪખ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11l1l1l_opy_ (u"ࠩࡺࠫગ")):
        pass
      with open(file_path, bstack11l1l1l_opy_ (u"ࠥࡻ࠰ࠨઘ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11l1l1l_opy_ (u"ࠫࡷ࠭ઙ")) as bstack11l1lll1l_opy_:
      bstack1ll1l1l111_opy_ = json.load(bstack11l1lll1l_opy_)
    if bstack1ll1l1ll1l_opy_ in bstack1ll1l1l111_opy_:
      bstack111l1llll_opy_ = bstack1ll1l1l111_opy_[bstack1ll1l1ll1l_opy_][bstack11l1l1l_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩચ")]
      bstack1lll1l1l1_opy_ = int(bstack111l1llll_opy_) + 1
      bstack11l1l11ll_opy_(bstack1ll1l1ll1l_opy_, bstack1lll1l1l1_opy_, file_path)
      return bstack1lll1l1l1_opy_
    else:
      bstack11l1l11ll_opy_(bstack1ll1l1ll1l_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack111llll1l_opy_.format(str(e)))
    return -1
def bstack11l111l11l_opy_(config):
  if not config[bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨછ")] or not config[bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪજ")]:
    return True
  else:
    return False
def bstack111l1lll1l_opy_(config, index=0):
  global bstack1ll1111ll1_opy_
  bstack11l1ll1l1_opy_ = {}
  caps = bstack11l1l1l1ll_opy_ + bstack1lllll1111_opy_
  if config.get(bstack11l1l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬઝ"), False):
    bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ઞ")] = True
    bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧટ")] = config.get(bstack11l1l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨઠ"), {})
  if bstack1ll1111ll1_opy_:
    caps += bstack111l1ll1l_opy_
  for key in config:
    if key in caps + [bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨડ")]:
      continue
    bstack11l1ll1l1_opy_[key] = config[key]
  if bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩઢ") in config:
    for bstack111lll1ll1_opy_ in config[bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪણ")][index]:
      if bstack111lll1ll1_opy_ in caps:
        continue
      bstack11l1ll1l1_opy_[bstack111lll1ll1_opy_] = config[bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫત")][index][bstack111lll1ll1_opy_]
  bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡸࡺࡎࡢ࡯ࡨࠫથ")] = socket.gethostname()
  if bstack11l1l1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫદ") in bstack11l1ll1l1_opy_:
    del (bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬધ")])
  return bstack11l1ll1l1_opy_
def bstack1111l1l11_opy_(config):
  global bstack1ll1111ll1_opy_
  bstack1l1l1l11l1_opy_ = {}
  caps = bstack1lllll1111_opy_
  if bstack1ll1111ll1_opy_:
    caps += bstack111l1ll1l_opy_
  for key in caps:
    if key in config:
      bstack1l1l1l11l1_opy_[key] = config[key]
  return bstack1l1l1l11l1_opy_
def bstack1111l1lll_opy_(bstack11l1ll1l1_opy_, bstack1l1l1l11l1_opy_):
  bstack1l11lllll_opy_ = {}
  for key in bstack11l1ll1l1_opy_.keys():
    if key in bstack11l111ll1_opy_:
      bstack1l11lllll_opy_[bstack11l111ll1_opy_[key]] = bstack11l1ll1l1_opy_[key]
    else:
      bstack1l11lllll_opy_[key] = bstack11l1ll1l1_opy_[key]
  for key in bstack1l1l1l11l1_opy_:
    if key in bstack11l111ll1_opy_:
      bstack1l11lllll_opy_[bstack11l111ll1_opy_[key]] = bstack1l1l1l11l1_opy_[key]
    else:
      bstack1l11lllll_opy_[key] = bstack1l1l1l11l1_opy_[key]
  return bstack1l11lllll_opy_
def bstack1llllll1ll_opy_(config, index=0):
  global bstack1ll1111ll1_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11ll11llll_opy_ = bstack1l11l1l11_opy_(bstack11llll1ll_opy_, config, logger)
  bstack1l1l1l11l1_opy_ = bstack1111l1l11_opy_(config)
  bstack11l1lll11_opy_ = bstack1lllll1111_opy_
  bstack11l1lll11_opy_ += bstack11ll11111_opy_
  bstack1l1l1l11l1_opy_ = update(bstack1l1l1l11l1_opy_, bstack11ll11llll_opy_)
  if bstack1ll1111ll1_opy_:
    bstack11l1lll11_opy_ += bstack111l1ll1l_opy_
  if bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨન") in config:
    if bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ઩") in config[bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪપ")][index]:
      caps[bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ફ")] = config[bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬબ")][index][bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨભ")]
    if bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬમ") in config[bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨય")][index]:
      caps[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧર")] = str(config[bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ઱")][index][bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩલ")])
    bstack11l1l1l1l_opy_ = bstack1l11l1l11_opy_(bstack11llll1ll_opy_, config[bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬળ")][index], logger)
    bstack11l1lll11_opy_ += list(bstack11l1l1l1l_opy_.keys())
    for bstack11ll1ll1l1_opy_ in bstack11l1lll11_opy_:
      if bstack11ll1ll1l1_opy_ in config[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭઴")][index]:
        if bstack11ll1ll1l1_opy_ == bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭વ"):
          try:
            bstack11l1l1l1l_opy_[bstack11ll1ll1l1_opy_] = str(config[bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨશ")][index][bstack11ll1ll1l1_opy_] * 1.0)
          except:
            bstack11l1l1l1l_opy_[bstack11ll1ll1l1_opy_] = str(config[bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩષ")][index][bstack11ll1ll1l1_opy_])
        else:
          bstack11l1l1l1l_opy_[bstack11ll1ll1l1_opy_] = config[bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪસ")][index][bstack11ll1ll1l1_opy_]
        del (config[bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫહ")][index][bstack11ll1ll1l1_opy_])
    bstack1l1l1l11l1_opy_ = update(bstack1l1l1l11l1_opy_, bstack11l1l1l1l_opy_)
  bstack11l1ll1l1_opy_ = bstack111l1lll1l_opy_(config, index)
  for bstack11lll1l111_opy_ in bstack1lllll1111_opy_ + list(bstack11ll11llll_opy_.keys()):
    if bstack11lll1l111_opy_ in bstack11l1ll1l1_opy_:
      bstack1l1l1l11l1_opy_[bstack11lll1l111_opy_] = bstack11l1ll1l1_opy_[bstack11lll1l111_opy_]
      del (bstack11l1ll1l1_opy_[bstack11lll1l111_opy_])
  if bstack1l11ll1lll_opy_(config):
    bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ઺")] = True
    caps.update(bstack1l1l1l11l1_opy_)
    caps[bstack11l1l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ઻")] = bstack11l1ll1l1_opy_
  else:
    bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆ઼ࠫ")] = False
    caps.update(bstack1111l1lll_opy_(bstack11l1ll1l1_opy_, bstack1l1l1l11l1_opy_))
    if bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪઽ") in caps:
      caps[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧા")] = caps[bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬિ")]
      del (caps[bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ી")])
    if bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪુ") in caps:
      caps[bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬૂ")] = caps[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬૃ")]
      del (caps[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ૄ")])
  return caps
def bstack1llll111l1_opy_():
  global bstack11l11111l_opy_
  global CONFIG
  if bstack1ll1l1111l_opy_() <= version.parse(bstack11l1l1l_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ૅ")):
    if bstack11l11111l_opy_ != bstack11l1l1l_opy_ (u"ࠧࠨ૆"):
      return bstack11l1l1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤે") + bstack11l11111l_opy_ + bstack11l1l1l_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨૈ")
    return bstack111lll11l_opy_
  if bstack11l11111l_opy_ != bstack11l1l1l_opy_ (u"ࠪࠫૉ"):
    return bstack11l1l1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨ૊") + bstack11l11111l_opy_ + bstack11l1l1l_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨો")
  return bstack1ll11lll1_opy_
def bstack11111111l_opy_(options):
  return hasattr(options, bstack11l1l1l_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧૌ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l1111l11_opy_(options, bstack1l111lll11_opy_):
  for bstack1l1l111lll_opy_ in bstack1l111lll11_opy_:
    if bstack1l1l111lll_opy_ in [bstack11l1l1l_opy_ (u"ࠧࡢࡴࡪࡷ્ࠬ"), bstack11l1l1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ૎")]:
      continue
    if bstack1l1l111lll_opy_ in options._experimental_options:
      options._experimental_options[bstack1l1l111lll_opy_] = update(options._experimental_options[bstack1l1l111lll_opy_],
                                                         bstack1l111lll11_opy_[bstack1l1l111lll_opy_])
    else:
      options.add_experimental_option(bstack1l1l111lll_opy_, bstack1l111lll11_opy_[bstack1l1l111lll_opy_])
  if bstack11l1l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ૏") in bstack1l111lll11_opy_:
    for arg in bstack1l111lll11_opy_[bstack11l1l1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨૐ")]:
      options.add_argument(arg)
    del (bstack1l111lll11_opy_[bstack11l1l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩ૑")])
  if bstack11l1l1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ૒") in bstack1l111lll11_opy_:
    for ext in bstack1l111lll11_opy_[bstack11l1l1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ૓")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l111lll11_opy_[bstack11l1l1l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ૔")])
def bstack1l111l11l1_opy_(options, bstack1l11lll11l_opy_):
  if bstack11l1l1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ૕") in bstack1l11lll11l_opy_:
    for bstack1l1lll1l1_opy_ in bstack1l11lll11l_opy_[bstack11l1l1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ૖")]:
      if bstack1l1lll1l1_opy_ in options._preferences:
        options._preferences[bstack1l1lll1l1_opy_] = update(options._preferences[bstack1l1lll1l1_opy_], bstack1l11lll11l_opy_[bstack11l1l1l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ૗")][bstack1l1lll1l1_opy_])
      else:
        options.set_preference(bstack1l1lll1l1_opy_, bstack1l11lll11l_opy_[bstack11l1l1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ૘")][bstack1l1lll1l1_opy_])
  if bstack11l1l1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ૙") in bstack1l11lll11l_opy_:
    for arg in bstack1l11lll11l_opy_[bstack11l1l1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ૚")]:
      options.add_argument(arg)
def bstack1ll1111l1_opy_(options, bstack11l1llll1l_opy_):
  if bstack11l1l1l_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࠨ૛") in bstack11l1llll1l_opy_:
    options.use_webview(bool(bstack11l1llll1l_opy_[bstack11l1l1l_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࠩ૜")]))
  bstack11l1111l11_opy_(options, bstack11l1llll1l_opy_)
def bstack1ll1l1ll11_opy_(options, bstack1ll111111_opy_):
  for bstack1l1l111ll_opy_ in bstack1ll111111_opy_:
    if bstack1l1l111ll_opy_ in [bstack11l1l1l_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭૝"), bstack11l1l1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ૞")]:
      continue
    options.set_capability(bstack1l1l111ll_opy_, bstack1ll111111_opy_[bstack1l1l111ll_opy_])
  if bstack11l1l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩ૟") in bstack1ll111111_opy_:
    for arg in bstack1ll111111_opy_[bstack11l1l1l_opy_ (u"ࠬࡧࡲࡨࡵࠪૠ")]:
      options.add_argument(arg)
  if bstack11l1l1l_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪૡ") in bstack1ll111111_opy_:
    options.bstack1l11lll111_opy_(bool(bstack1ll111111_opy_[bstack11l1l1l_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫૢ")]))
def bstack1lll1ll11l_opy_(options, bstack1l1111111l_opy_):
  for bstack11l11ll1l1_opy_ in bstack1l1111111l_opy_:
    if bstack11l11ll1l1_opy_ in [bstack11l1l1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬૣ"), bstack11l1l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ૤")]:
      continue
    options._options[bstack11l11ll1l1_opy_] = bstack1l1111111l_opy_[bstack11l11ll1l1_opy_]
  if bstack11l1l1l_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ૥") in bstack1l1111111l_opy_:
    for bstack1ll1llllll_opy_ in bstack1l1111111l_opy_[bstack11l1l1l_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ૦")]:
      options.bstack1lllllll11_opy_(
        bstack1ll1llllll_opy_, bstack1l1111111l_opy_[bstack11l1l1l_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૧")][bstack1ll1llllll_opy_])
  if bstack11l1l1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ૨") in bstack1l1111111l_opy_:
    for arg in bstack1l1111111l_opy_[bstack11l1l1l_opy_ (u"ࠧࡢࡴࡪࡷࠬ૩")]:
      options.add_argument(arg)
def bstack1l1ll111l_opy_(options, caps):
  if not hasattr(options, bstack11l1l1l_opy_ (u"ࠨࡍࡈ࡝ࠬ૪")):
    return
  if options.KEY == bstack11l1l1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ૫") and options.KEY in caps:
    bstack11l1111l11_opy_(options, caps[bstack11l1l1l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ૬")])
  elif options.KEY == bstack11l1l1l_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૭") and options.KEY in caps:
    bstack1l111l11l1_opy_(options, caps[bstack11l1l1l_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪ૮")])
  elif options.KEY == bstack11l1l1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ૯") and options.KEY in caps:
    bstack1ll1l1ll11_opy_(options, caps[bstack11l1l1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ૰")])
  elif options.KEY == bstack11l1l1l_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૱") and options.KEY in caps:
    bstack1ll1111l1_opy_(options, caps[bstack11l1l1l_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૲")])
  elif options.KEY == bstack11l1l1l_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૳") and options.KEY in caps:
    bstack1lll1ll11l_opy_(options, caps[bstack11l1l1l_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૴")])
def bstack11lllll1l1_opy_(caps):
  global bstack1ll1111ll1_opy_
  if isinstance(os.environ.get(bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭૵")), str):
    bstack1ll1111ll1_opy_ = eval(os.getenv(bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ૶")))
  if bstack1ll1111ll1_opy_:
    if bstack11ll1ll11l_opy_() < version.parse(bstack11l1l1l_opy_ (u"ࠧ࠳࠰࠶࠲࠵࠭૷")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11l1l1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ૸")
    if bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧૹ") in caps:
      browser = caps[bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨૺ")]
    elif bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬૻ") in caps:
      browser = caps[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ૼ")]
    browser = str(browser).lower()
    if browser == bstack11l1l1l_opy_ (u"࠭ࡩࡱࡪࡲࡲࡪ࠭૽") or browser == bstack11l1l1l_opy_ (u"ࠧࡪࡲࡤࡨࠬ૾"):
      browser = bstack11l1l1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨ૿")
    if browser == bstack11l1l1l_opy_ (u"ࠩࡶࡥࡲࡹࡵ࡯ࡩࠪ଀"):
      browser = bstack11l1l1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪଁ")
    if browser not in [bstack11l1l1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫଂ"), bstack11l1l1l_opy_ (u"ࠬ࡫ࡤࡨࡧࠪଃ"), bstack11l1l1l_opy_ (u"࠭ࡩࡦࠩ଄"), bstack11l1l1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧଅ"), bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩଆ")]:
      return None
    try:
      package = bstack11l1l1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࠮ࡼࡿ࠱ࡳࡵࡺࡩࡰࡰࡶࠫଇ").format(browser)
      name = bstack11l1l1l_opy_ (u"ࠪࡓࡵࡺࡩࡰࡰࡶࠫଈ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11111111l_opy_(options):
        return None
      for bstack11lll1l111_opy_ in caps.keys():
        options.set_capability(bstack11lll1l111_opy_, caps[bstack11lll1l111_opy_])
      bstack1l1ll111l_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1ll1l111l1_opy_(options, bstack11ll1l1ll1_opy_):
  if not bstack11111111l_opy_(options):
    return
  for bstack11lll1l111_opy_ in bstack11ll1l1ll1_opy_.keys():
    if bstack11lll1l111_opy_ in bstack11ll11111_opy_:
      continue
    if bstack11lll1l111_opy_ in options._caps and type(options._caps[bstack11lll1l111_opy_]) in [dict, list]:
      options._caps[bstack11lll1l111_opy_] = update(options._caps[bstack11lll1l111_opy_], bstack11ll1l1ll1_opy_[bstack11lll1l111_opy_])
    else:
      options.set_capability(bstack11lll1l111_opy_, bstack11ll1l1ll1_opy_[bstack11lll1l111_opy_])
  bstack1l1ll111l_opy_(options, bstack11ll1l1ll1_opy_)
  if bstack11l1l1l_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪଉ") in options._caps:
    if options._caps[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪଊ")] and options._caps[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫଋ")].lower() != bstack11l1l1l_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨଌ"):
      del options._caps[bstack11l1l1l_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧ଍")]
def bstack111ll111ll_opy_(proxy_config):
  if bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭଎") in proxy_config:
    proxy_config[bstack11l1l1l_opy_ (u"ࠪࡷࡸࡲࡐࡳࡱࡻࡽࠬଏ")] = proxy_config[bstack11l1l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨଐ")]
    del (proxy_config[bstack11l1l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ଑")])
  if bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ଒") in proxy_config and proxy_config[bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪଓ")].lower() != bstack11l1l1l_opy_ (u"ࠨࡦ࡬ࡶࡪࡩࡴࠨଔ"):
    proxy_config[bstack11l1l1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬକ")] = bstack11l1l1l_opy_ (u"ࠪࡱࡦࡴࡵࡢ࡮ࠪଖ")
  if bstack11l1l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡄࡹࡹࡵࡣࡰࡰࡩ࡭࡬࡛ࡲ࡭ࠩଗ") in proxy_config:
    proxy_config[bstack11l1l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨଘ")] = bstack11l1l1l_opy_ (u"࠭ࡰࡢࡥࠪଙ")
  return proxy_config
def bstack111111l11_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ଚ") in config:
    return proxy
  config[bstack11l1l1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧଛ")] = bstack111ll111ll_opy_(config[bstack11l1l1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨଜ")])
  if proxy == None:
    proxy = Proxy(config[bstack11l1l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩଝ")])
  return proxy
def bstack1l11ll111_opy_(self):
  global CONFIG
  global bstack11l1l1l1l1_opy_
  try:
    proxy = bstack1lll1111l1_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11l1l1l_opy_ (u"ࠫ࠳ࡶࡡࡤࠩଞ")):
        proxies = bstack1lll11l11l_opy_(proxy, bstack1llll111l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1ll111_opy_ = proxies.popitem()
          if bstack11l1l1l_opy_ (u"ࠧࡀ࠯࠰ࠤଟ") in bstack1ll1ll111_opy_:
            return bstack1ll1ll111_opy_
          else:
            return bstack11l1l1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢଠ") + bstack1ll1ll111_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11l1l1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦଡ").format(str(e)))
  return bstack11l1l1l1l1_opy_(self)
def bstack1l111l1l1l_opy_():
  global CONFIG
  return bstack1ll11l1111_opy_(CONFIG) and bstack1l11l111ll_opy_() and bstack1ll1l1111l_opy_() >= version.parse(bstack1111111ll_opy_)
def bstack11lllll1ll_opy_():
  global CONFIG
  return (bstack11l1l1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫଢ") in CONFIG or bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ଣ") in CONFIG) and bstack1l1ll11111_opy_()
def bstack111lll1lll_opy_(config):
  bstack111l111l1_opy_ = {}
  if bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧତ") in config:
    bstack111l111l1_opy_ = config[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨଥ")]
  if bstack11l1l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଦ") in config:
    bstack111l111l1_opy_ = config[bstack11l1l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଧ")]
  proxy = bstack1lll1111l1_opy_(config)
  if proxy:
    if proxy.endswith(bstack11l1l1l_opy_ (u"ࠧ࠯ࡲࡤࡧࠬନ")) and os.path.isfile(proxy):
      bstack111l111l1_opy_[bstack11l1l1l_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫ଩")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11l1l1l_opy_ (u"ࠩ࠱ࡴࡦࡩࠧପ")):
        proxies = bstack1l1lll1ll_opy_(config, bstack1llll111l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1ll111_opy_ = proxies.popitem()
          if bstack11l1l1l_opy_ (u"ࠥ࠾࠴࠵ࠢଫ") in bstack1ll1ll111_opy_:
            parsed_url = urlparse(bstack1ll1ll111_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11l1l1l_opy_ (u"ࠦ࠿࠵࠯ࠣବ") + bstack1ll1ll111_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack111l111l1_opy_[bstack11l1l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨଭ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack111l111l1_opy_[bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩମ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack111l111l1_opy_[bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪଯ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack111l111l1_opy_[bstack11l1l1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫର")] = str(parsed_url.password)
  return bstack111l111l1_opy_
def bstack1lllllllll_opy_(config):
  if bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧ଱") in config:
    return config[bstack11l1l1l_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨଲ")]
  return {}
def bstack1l111111l1_opy_(caps):
  global bstack1ll1lll1l1_opy_
  if bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬଳ") in caps:
    caps[bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭଴")][bstack11l1l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬଵ")] = True
    if bstack1ll1lll1l1_opy_:
      caps[bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨଶ")][bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪଷ")] = bstack1ll1lll1l1_opy_
  else:
    caps[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧସ")] = True
    if bstack1ll1lll1l1_opy_:
      caps[bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫହ")] = bstack1ll1lll1l1_opy_
@measure(event_name=EVENTS.bstack1lllll1ll1_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1l1ll1ll1l_opy_():
  global CONFIG
  if not bstack11l1111ll1_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ଺") in CONFIG and bstack1l1llllll1_opy_(CONFIG[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ଻")]):
    if (
      bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵ଼ࠪ") in CONFIG
      and bstack1l1llllll1_opy_(CONFIG[bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଽ")].get(bstack11l1l1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡈࡩ࡯ࡣࡵࡽࡎࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡡࡵ࡫ࡲࡲࠬା")))
    ):
      logger.debug(bstack11l1l1l_opy_ (u"ࠤࡏࡳࡨࡧ࡬ࠡࡤ࡬ࡲࡦࡸࡹࠡࡰࡲࡸࠥࡹࡴࡢࡴࡷࡩࡩࠦࡡࡴࠢࡶ࡯࡮ࡶࡂࡪࡰࡤࡶࡾࡏ࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡨࡲࡦࡨ࡬ࡦࡦࠥି"))
      return
    bstack111l111l1_opy_ = bstack111lll1lll_opy_(CONFIG)
    bstack1ll111l111_opy_(CONFIG[bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ୀ")], bstack111l111l1_opy_)
def bstack1ll111l111_opy_(key, bstack111l111l1_opy_):
  global bstack1ll11l1ll1_opy_
  logger.info(bstack1lll11ll1_opy_)
  try:
    bstack1ll11l1ll1_opy_ = Local()
    bstack1l11111111_opy_ = {bstack11l1l1l_opy_ (u"ࠫࡰ࡫ࡹࠨୁ"): key}
    bstack1l11111111_opy_.update(bstack111l111l1_opy_)
    logger.debug(bstack1l1ll1111l_opy_.format(str(bstack1l11111111_opy_)))
    bstack1ll11l1ll1_opy_.start(**bstack1l11111111_opy_)
    if bstack1ll11l1ll1_opy_.isRunning():
      logger.info(bstack1l1ll11ll_opy_)
  except Exception as e:
    bstack1l11ll111l_opy_(bstack1l1l1lll11_opy_.format(str(e)))
def bstack1ll111llll_opy_():
  global bstack1ll11l1ll1_opy_
  if bstack1ll11l1ll1_opy_.isRunning():
    logger.info(bstack11l1l11l1l_opy_)
    bstack1ll11l1ll1_opy_.stop()
  bstack1ll11l1ll1_opy_ = None
def bstack11l1l1ll1_opy_(bstack11ll1l111_opy_=[]):
  global CONFIG
  bstack11l111ll11_opy_ = []
  bstack1ll111l1ll_opy_ = [bstack11l1l1l_opy_ (u"ࠬࡵࡳࠨୂ"), bstack11l1l1l_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩୃ"), bstack11l1l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫୄ"), bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ୅"), bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ୆"), bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫେ")]
  try:
    for err in bstack11ll1l111_opy_:
      bstack11l1l11111_opy_ = {}
      for k in bstack1ll111l1ll_opy_:
        val = CONFIG[bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧୈ")][int(err[bstack11l1l1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ୉")])].get(k)
        if val:
          bstack11l1l11111_opy_[k] = val
      if(err[bstack11l1l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ୊")] != bstack11l1l1l_opy_ (u"ࠧࠨୋ")):
        bstack11l1l11111_opy_[bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹࡹࠧୌ")] = {
          err[bstack11l1l1l_opy_ (u"ࠩࡱࡥࡲ࡫୍ࠧ")]: err[bstack11l1l1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ୎")]
        }
        bstack11l111ll11_opy_.append(bstack11l1l11111_opy_)
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡰࡴࡰࡥࡹࡺࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷ࠾ࠥ࠭୏") + str(e))
  finally:
    return bstack11l111ll11_opy_
def bstack11ll1lll1_opy_(file_name):
  bstack1lll1llll1_opy_ = []
  try:
    bstack1l1ll111ll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l1ll111ll_opy_):
      with open(bstack1l1ll111ll_opy_) as f:
        bstack111lll1l11_opy_ = json.load(f)
        bstack1lll1llll1_opy_ = bstack111lll1l11_opy_
      os.remove(bstack1l1ll111ll_opy_)
    return bstack1lll1llll1_opy_
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧ࡫ࡱࡨ࡮ࡴࡧࠡࡧࡵࡶࡴࡸࠠ࡭࡫ࡶࡸ࠿ࠦࠧ୐") + str(e))
    return bstack1lll1llll1_opy_
def bstack11lll1111_opy_():
  try:
      from bstack_utils.constants import bstack1ll1l11l1l_opy_, EVENTS
      from bstack_utils.helper import bstack1l11llll1l_opy_, get_host_info, bstack11111l11_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1l1ll1l11l_opy_ = os.path.join(os.getcwd(), bstack11l1l1l_opy_ (u"࠭࡬ࡰࡩࠪ୑"), bstack11l1l1l_opy_ (u"ࠧ࡬ࡧࡼ࠱ࡲ࡫ࡴࡳ࡫ࡦࡷ࠳ࡰࡳࡰࡰࠪ୒"))
      lock = FileLock(bstack1l1ll1l11l_opy_+bstack11l1l1l_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢ୓"))
      def bstack1lll11l1_opy_():
          try:
              with lock:
                  with open(bstack1l1ll1l11l_opy_, bstack11l1l1l_opy_ (u"ࠤࡵࠦ୔"), encoding=bstack11l1l1l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤ୕")) as file:
                      data = json.load(file)
                      config = {
                          bstack11l1l1l_opy_ (u"ࠦ࡭࡫ࡡࡥࡧࡵࡷࠧୖ"): {
                              bstack11l1l1l_opy_ (u"ࠧࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠦୗ"): bstack11l1l1l_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠤ୘"),
                          }
                      }
                      bstack1l11l1l111_opy_ = datetime.utcnow()
                      bstack11llllll_opy_ = bstack1l11l1l111_opy_.strftime(bstack11l1l1l_opy_ (u"࡛ࠢࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࠲ࠪ࡬ࠠࡖࡖࡆࠦ୙"))
                      test_id = os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭୚")) if os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ୛")) else bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧଡ଼"))
                      payload = {
                          bstack11l1l1l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠣଢ଼"): bstack11l1l1l_opy_ (u"ࠧࡹࡤ࡬ࡡࡨࡺࡪࡴࡴࡴࠤ୞"),
                          bstack11l1l1l_opy_ (u"ࠨࡤࡢࡶࡤࠦୟ"): {
                              bstack11l1l1l_opy_ (u"ࠢࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩࠨୠ"): test_id,
                              bstack11l1l1l_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࡡࡧࡥࡾࠨୡ"): bstack11llllll_opy_,
                              bstack11l1l1l_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࠨୢ"): bstack11l1l1l_opy_ (u"ࠥࡗࡉࡑࡆࡦࡣࡷࡹࡷ࡫ࡐࡦࡴࡩࡳࡷࡳࡡ࡯ࡥࡨࠦୣ"),
                              bstack11l1l1l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢ࡮ࡸࡵ࡮ࠣ୤"): {
                                  bstack11l1l1l_opy_ (u"ࠧࡳࡥࡢࡵࡸࡶࡪࡹࠢ୥"): data,
                                  bstack11l1l1l_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣ୦"): bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤ୧"))
                              },
                              bstack11l1l1l_opy_ (u"ࠣࡷࡶࡩࡷࡥࡤࡢࡶࡤࠦ୨"): bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠤࡸࡷࡪࡸࡎࡢ࡯ࡨࠦ୩")),
                              bstack11l1l1l_opy_ (u"ࠥ࡬ࡴࡹࡴࡠ࡫ࡱࡪࡴࠨ୪"): get_host_info()
                          }
                      }
                      response = bstack1l11llll1l_opy_(bstack11l1l1l_opy_ (u"ࠦࡕࡕࡓࡕࠤ୫"), bstack1ll1l11l1l_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11l1l1l_opy_ (u"ࠧࡊࡡࡵࡣࠣࡷࡪࡴࡴࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡵࡱࠣࡿࢂࠦࡷࡪࡶ࡫ࠤࡩࡧࡴࡢࠢࡾࢁࠧ୬").format(bstack1ll1l11l1l_opy_, payload))
                      else:
                          logger.debug(bstack11l1l1l_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡧࡱࡵࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨ୭").format(bstack1ll1l11l1l_opy_, payload))
          except Exception as e:
              logger.debug(bstack11l1l1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡࡽࢀࠦ୮").format(e))
      bstack1lll11l1_opy_()
      bstack1l111l11ll_opy_(bstack1l1ll1l11l_opy_, logger)
  except:
    pass
def bstack1l1l1ll111_opy_():
  global bstack1llllll1l1_opy_
  global bstack11ll1ll1l_opy_
  global bstack11l1ll11ll_opy_
  global bstack1ll111l11l_opy_
  global bstack1l1l111111_opy_
  global bstack1lll1lll11_opy_
  global CONFIG
  bstack1llll11l1_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ୯"))
  if bstack1llll11l1_opy_ in [bstack11l1l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ୰"), bstack11l1l1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩୱ")]:
    bstack1ll111ll1_opy_()
  percy.shutdown()
  if bstack1llllll1l1_opy_:
    logger.warning(bstack11l1l111l1_opy_.format(str(bstack1llllll1l1_opy_)))
  else:
    try:
      bstack111l1l1l1_opy_ = bstack1l1lllll11_opy_(bstack11l1l1l_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪ୲"), logger)
      if bstack111l1l1l1_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪ୳")) and bstack111l1l1l1_opy_.get(bstack11l1l1l_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ୴")).get(bstack11l1l1l_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ୵")):
        logger.warning(bstack11l1l111l1_opy_.format(str(bstack111l1l1l1_opy_[bstack11l1l1l_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭୶")][bstack11l1l1l_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ୷")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l1llll11l_opy_.invoke(Events.bstack11l1ll1ll1_opy_)
  logger.info(bstack11l1llllll_opy_)
  global bstack1ll11l1ll1_opy_
  if bstack1ll11l1ll1_opy_:
    bstack1ll111llll_opy_()
  try:
    for driver in bstack11ll1ll1l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1ll11l1ll_opy_)
  if bstack1lll1lll11_opy_ == bstack11l1l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ୸"):
    bstack1l1l111111_opy_ = bstack11ll1lll1_opy_(bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ୹"))
  if bstack1lll1lll11_opy_ == bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ୺") and len(bstack1ll111l11l_opy_) == 0:
    bstack1ll111l11l_opy_ = bstack11ll1lll1_opy_(bstack11l1l1l_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ୻"))
    if len(bstack1ll111l11l_opy_) == 0:
      bstack1ll111l11l_opy_ = bstack11ll1lll1_opy_(bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭୼"))
  bstack1111l11l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࠩ୽")
  if len(bstack11l1ll11ll_opy_) > 0:
    bstack1111l11l1_opy_ = bstack11l1l1ll1_opy_(bstack11l1ll11ll_opy_)
  elif len(bstack1ll111l11l_opy_) > 0:
    bstack1111l11l1_opy_ = bstack11l1l1ll1_opy_(bstack1ll111l11l_opy_)
  elif len(bstack1l1l111111_opy_) > 0:
    bstack1111l11l1_opy_ = bstack11l1l1ll1_opy_(bstack1l1l111111_opy_)
  elif len(bstack11l11lll1l_opy_) > 0:
    bstack1111l11l1_opy_ = bstack11l1l1ll1_opy_(bstack11l11lll1l_opy_)
  if bool(bstack1111l11l1_opy_):
    bstack1l1l1l1l1l_opy_(bstack1111l11l1_opy_)
  else:
    bstack1l1l1l1l1l_opy_()
  bstack1l111l11ll_opy_(bstack11l1111ll_opy_, logger)
  if bstack1llll11l1_opy_ not in [bstack11l1l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ୾")]:
    bstack11lll1111_opy_()
  bstack111111l1l_opy_.bstack1ll1111l_opy_(CONFIG)
  if len(bstack1l1l111111_opy_) > 0:
    sys.exit(len(bstack1l1l111111_opy_))
def bstack11ll1l1l11_opy_(bstack11l1l1llll_opy_, frame):
  global bstack11111l11_opy_
  logger.error(bstack1l111l1lll_opy_)
  bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭୿"), bstack11l1l1llll_opy_)
  if hasattr(signal, bstack11l1l1l_opy_ (u"ࠫࡘ࡯ࡧ࡯ࡣ࡯ࡷࠬ஀")):
    bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ஁"), signal.Signals(bstack11l1l1llll_opy_).name)
  else:
    bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭ஂ"), bstack11l1l1l_opy_ (u"ࠧࡔࡋࡊ࡙ࡓࡑࡎࡐ࡙ࡑࠫஃ"))
  if cli.is_running():
    bstack1l1llll11l_opy_.invoke(Events.bstack11l1ll1ll1_opy_)
  bstack1llll11l1_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ஄"))
  if bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩஅ") and not cli.is_enabled(CONFIG):
    bstack1l11l1ll_opy_.stop(bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪஆ")))
  bstack1l1l1ll111_opy_()
  sys.exit(1)
def bstack1l11ll111l_opy_(err):
  logger.critical(bstack11l1lllll_opy_.format(str(err)))
  bstack1l1l1l1l1l_opy_(bstack11l1lllll_opy_.format(str(err)), True)
  atexit.unregister(bstack1l1l1ll111_opy_)
  bstack1ll111ll1_opy_()
  sys.exit(1)
def bstack1ll11l1l11_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l1l1l1l1l_opy_(message, True)
  atexit.unregister(bstack1l1l1ll111_opy_)
  bstack1ll111ll1_opy_()
  sys.exit(1)
def bstack1l1l1l1111_opy_():
  global CONFIG
  global bstack1l111ll1l1_opy_
  global bstack1l1l11l11l_opy_
  global bstack1l111111l_opy_
  CONFIG = bstack11l11l1l11_opy_()
  load_dotenv(CONFIG.get(bstack11l1l1l_opy_ (u"ࠫࡪࡴࡶࡇ࡫࡯ࡩࠬஇ")))
  bstack11lll1l11_opy_()
  bstack1l1l11llll_opy_()
  CONFIG = bstack11lll1l11l_opy_(CONFIG)
  update(CONFIG, bstack1l1l11l11l_opy_)
  update(CONFIG, bstack1l111ll1l1_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1l1l1l1ll_opy_(CONFIG)
  bstack1l111111l_opy_ = bstack11l1111ll1_opy_(CONFIG)
  os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨஈ")] = bstack1l111111l_opy_.__str__()
  bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧஉ"), bstack1l111111l_opy_)
  if (bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪஊ") in CONFIG and bstack11l1l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ஋") in bstack1l111ll1l1_opy_) or (
          bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ஌") in CONFIG and bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭஍") not in bstack1l1l11l11l_opy_):
    if os.getenv(bstack11l1l1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨஎ")):
      CONFIG[bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧஏ")] = os.getenv(bstack11l1l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪஐ"))
    else:
      if not CONFIG.get(bstack11l1l1l_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠥ஑"), bstack11l1l1l_opy_ (u"ࠣࠤஒ")) in bstack1ll1ll1ll_opy_:
        bstack1lll1111l_opy_()
  elif (bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬஓ") not in CONFIG and bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬஔ") in CONFIG) or (
          bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧக") in bstack1l1l11l11l_opy_ and bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ஖") not in bstack1l111ll1l1_opy_):
    del (CONFIG[bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ஗")])
  if bstack11l111l11l_opy_(CONFIG):
    bstack1l11ll111l_opy_(bstack1l1lll1l11_opy_)
  Config.bstack111ll1ll_opy_().set_property(bstack11l1l1l_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤ஘"), CONFIG[bstack11l1l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪங")])
  bstack1ll11111l_opy_()
  bstack1lll1111ll_opy_()
  if bstack1ll1111ll1_opy_ and not CONFIG.get(bstack11l1l1l_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧச"), bstack11l1l1l_opy_ (u"ࠥࠦ஛")) in bstack1ll1ll1ll_opy_:
    CONFIG[bstack11l1l1l_opy_ (u"ࠫࡦࡶࡰࠨஜ")] = bstack11l11l1l1l_opy_(CONFIG)
    logger.info(bstack11l1l11l1_opy_.format(CONFIG[bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱࠩ஝")]))
  if not bstack1l111111l_opy_:
    CONFIG[bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩஞ")] = [{}]
def bstack11llllll1l_opy_(config, bstack1l11ll1l1_opy_):
  global CONFIG
  global bstack1ll1111ll1_opy_
  CONFIG = config
  bstack1ll1111ll1_opy_ = bstack1l11ll1l1_opy_
def bstack1lll1111ll_opy_():
  global CONFIG
  global bstack1ll1111ll1_opy_
  if bstack11l1l1l_opy_ (u"ࠧࡢࡲࡳࠫட") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1ll11l1l11_opy_(e, bstack111l11l11_opy_)
    bstack1ll1111ll1_opy_ = True
    bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ஠"), True)
def bstack11l11l1l1l_opy_(config):
  bstack1l1111l11_opy_ = bstack11l1l1l_opy_ (u"ࠩࠪ஡")
  app = config[bstack11l1l1l_opy_ (u"ࠪࡥࡵࡶࠧ஢")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack11l1ll1111_opy_:
      if os.path.exists(app):
        bstack1l1111l11_opy_ = bstack11lll1l1l_opy_(config, app)
      elif bstack111l111ll_opy_(app):
        bstack1l1111l11_opy_ = app
      else:
        bstack1l11ll111l_opy_(bstack1111l11ll_opy_.format(app))
    else:
      if bstack111l111ll_opy_(app):
        bstack1l1111l11_opy_ = app
      elif os.path.exists(app):
        bstack1l1111l11_opy_ = bstack11lll1l1l_opy_(app)
      else:
        bstack1l11ll111l_opy_(bstack1l111lllll_opy_)
  else:
    if len(app) > 2:
      bstack1l11ll111l_opy_(bstack111lll11l1_opy_)
    elif len(app) == 2:
      if bstack11l1l1l_opy_ (u"ࠫࡵࡧࡴࡩࠩண") in app and bstack11l1l1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨத") in app:
        if os.path.exists(app[bstack11l1l1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ஥")]):
          bstack1l1111l11_opy_ = bstack11lll1l1l_opy_(config, app[bstack11l1l1l_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ஦")], app[bstack11l1l1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ஧")])
        else:
          bstack1l11ll111l_opy_(bstack1111l11ll_opy_.format(app))
      else:
        bstack1l11ll111l_opy_(bstack111lll11l1_opy_)
    else:
      for key in app:
        if key in bstack1l111l1l1_opy_:
          if key == bstack11l1l1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧந"):
            if os.path.exists(app[key]):
              bstack1l1111l11_opy_ = bstack11lll1l1l_opy_(config, app[key])
            else:
              bstack1l11ll111l_opy_(bstack1111l11ll_opy_.format(app))
          else:
            bstack1l1111l11_opy_ = app[key]
        else:
          bstack1l11ll111l_opy_(bstack11l1l11l11_opy_)
  return bstack1l1111l11_opy_
def bstack111l111ll_opy_(bstack1l1111l11_opy_):
  import re
  bstack1ll1l11ll_opy_ = re.compile(bstack11l1l1l_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥன"))
  bstack1l111llll_opy_ = re.compile(bstack11l1l1l_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬ࠲࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣப"))
  if bstack11l1l1l_opy_ (u"ࠬࡨࡳ࠻࠱࠲ࠫ஫") in bstack1l1111l11_opy_ or re.fullmatch(bstack1ll1l11ll_opy_, bstack1l1111l11_opy_) or re.fullmatch(bstack1l111llll_opy_, bstack1l1111l11_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack111llll1l1_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11lll1l1l_opy_(config, path, bstack1l111ll11l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11l1l1l_opy_ (u"࠭ࡲࡣࠩ஬")).read()).hexdigest()
  bstack11lll1111l_opy_ = bstack11ll111l1l_opy_(md5_hash)
  bstack1l1111l11_opy_ = None
  if bstack11lll1111l_opy_:
    logger.info(bstack1lll1llll_opy_.format(bstack11lll1111l_opy_, md5_hash))
    return bstack11lll1111l_opy_
  bstack1l1lll1l1l_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11l1l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࠬ஭"): (os.path.basename(path), open(os.path.abspath(path), bstack11l1l1l_opy_ (u"ࠨࡴࡥࠫம")), bstack11l1l1l_opy_ (u"ࠩࡷࡩࡽࡺ࠯ࡱ࡮ࡤ࡭ࡳ࠭ய")),
      bstack11l1l1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ர"): bstack1l111ll11l_opy_
    }
  )
  response = requests.post(bstack11l1ll11l_opy_, data=multipart_data,
                           headers={bstack11l1l1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪற"): multipart_data.content_type},
                           auth=(config[bstack11l1l1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧல")], config[bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩள")]))
  try:
    res = json.loads(response.text)
    bstack1l1111l11_opy_ = res[bstack11l1l1l_opy_ (u"ࠧࡢࡲࡳࡣࡺࡸ࡬ࠨழ")]
    logger.info(bstack1111ll1l1_opy_.format(bstack1l1111l11_opy_))
    bstack1l1l1l1l11_opy_(md5_hash, bstack1l1111l11_opy_)
    cli.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠣࡪࡷࡸࡵࡀࡵࡱ࡮ࡲࡥࡩࡥࡡࡱࡲࠥவ"), datetime.datetime.now() - bstack1l1lll1l1l_opy_)
  except ValueError as err:
    bstack1l11ll111l_opy_(bstack1lll1ll11_opy_.format(str(err)))
  return bstack1l1111l11_opy_
def bstack1ll11111l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l1l11ll11_opy_
  bstack1llllllll_opy_ = 1
  bstack1l1l1lll1l_opy_ = 1
  if bstack11l1l1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩஶ") in CONFIG:
    bstack1l1l1lll1l_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪஷ")]
  else:
    bstack1l1l1lll1l_opy_ = bstack1l1l1l1l1_opy_(framework_name, args) or 1
  if bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧஸ") in CONFIG:
    bstack1llllllll_opy_ = len(CONFIG[bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨஹ")])
  bstack1l1l11ll11_opy_ = int(bstack1l1l1lll1l_opy_) * int(bstack1llllllll_opy_)
def bstack1l1l1l1l1_opy_(framework_name, args):
  if framework_name == bstack1l111lll1l_opy_ and args and bstack11l1l1l_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ஺") in args:
      bstack11l11lllll_opy_ = args.index(bstack11l1l1l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ஻"))
      return int(args[bstack11l11lllll_opy_ + 1]) or 1
  return 1
def bstack11ll111l1l_opy_(md5_hash):
  bstack1l1l1ll11l_opy_ = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠨࢀࠪ஼")), bstack11l1l1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ஽"), bstack11l1l1l_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫா"))
  if os.path.exists(bstack1l1l1ll11l_opy_):
    bstack1l111l111_opy_ = json.load(open(bstack1l1l1ll11l_opy_, bstack11l1l1l_opy_ (u"ࠫࡷࡨࠧி")))
    if md5_hash in bstack1l111l111_opy_:
      bstack111lll111l_opy_ = bstack1l111l111_opy_[md5_hash]
      bstack1l11ll1ll_opy_ = datetime.datetime.now()
      bstack11ll1l1111_opy_ = datetime.datetime.strptime(bstack111lll111l_opy_[bstack11l1l1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨீ")], bstack11l1l1l_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪு"))
      if (bstack1l11ll1ll_opy_ - bstack11ll1l1111_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack111lll111l_opy_[bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬூ")]):
        return None
      return bstack111lll111l_opy_[bstack11l1l1l_opy_ (u"ࠨ࡫ࡧࠫ௃")]
  else:
    return None
def bstack1l1l1l1l11_opy_(md5_hash, bstack1l1111l11_opy_):
  bstack1lll1l1111_opy_ = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠩࢁࠫ௄")), bstack11l1l1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ௅"))
  if not os.path.exists(bstack1lll1l1111_opy_):
    os.makedirs(bstack1lll1l1111_opy_)
  bstack1l1l1ll11l_opy_ = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠫࢃ࠭ெ")), bstack11l1l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬே"), bstack11l1l1l_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧை"))
  bstack111ll11l11_opy_ = {
    bstack11l1l1l_opy_ (u"ࠧࡪࡦࠪ௉"): bstack1l1111l11_opy_,
    bstack11l1l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫொ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l1l1l_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ோ")),
    bstack11l1l1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨௌ"): str(__version__)
  }
  if os.path.exists(bstack1l1l1ll11l_opy_):
    bstack1l111l111_opy_ = json.load(open(bstack1l1l1ll11l_opy_, bstack11l1l1l_opy_ (u"ࠫࡷࡨ்ࠧ")))
  else:
    bstack1l111l111_opy_ = {}
  bstack1l111l111_opy_[md5_hash] = bstack111ll11l11_opy_
  with open(bstack1l1l1ll11l_opy_, bstack11l1l1l_opy_ (u"ࠧࡽࠫࠣ௎")) as outfile:
    json.dump(bstack1l111l111_opy_, outfile)
def bstack1llll1l1l1_opy_(self):
  return
def bstack1l1lll1ll1_opy_(self):
  return
def bstack11l11l1lll_opy_(self):
  global bstack1lll1l111l_opy_
  bstack1lll1l111l_opy_(self)
def bstack1l11lll1l1_opy_():
  global bstack1ll1l1111_opy_
  bstack1ll1l1111_opy_ = True
@measure(event_name=EVENTS.bstack11lll1lll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1l1l1l11ll_opy_(self):
  global bstack11l1ll11l1_opy_
  global bstack1l1lll1111_opy_
  global bstack1lll1lllll_opy_
  try:
    if bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭௏") in bstack11l1ll11l1_opy_ and self.session_id != None and bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫௐ"), bstack11l1l1l_opy_ (u"ࠨࠩ௑")) != bstack11l1l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ௒"):
      bstack1ll111ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ௓") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ௔")
      if bstack1ll111ll1l_opy_ == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ௕"):
        bstack11ll11ll1l_opy_(logger)
      if self != None:
        bstack11ll11l1ll_opy_(self, bstack1ll111ll1l_opy_, bstack11l1l1l_opy_ (u"࠭ࠬࠡࠩ௖").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11l1l1l_opy_ (u"ࠧࠨௗ")
    if bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ௘") in bstack11l1ll11l1_opy_ and getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ௙"), None):
      bstack111lll1l_opy_.bstack111lll11_opy_(self, bstack1llll1l111_opy_, logger, wait=True)
    if bstack11l1l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ௚") in bstack11l1ll11l1_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11ll11l1ll_opy_(self, bstack11l1l1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ௛"))
      bstack1lll11ll11_opy_.bstack1l111l1111_opy_(self)
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨ௜") + str(e))
  bstack1lll1lllll_opy_(self)
  self.session_id = None
def bstack1l11lllll1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack11ll1111ll_opy_
    global bstack11l1ll11l1_opy_
    command_executor = kwargs.get(bstack11l1l1l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠩ௝"), bstack11l1l1l_opy_ (u"ࠧࠨ௞"))
    bstack11l11llll_opy_ = False
    if type(command_executor) == str and bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ௟") in command_executor:
      bstack11l11llll_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ௠") in str(getattr(command_executor, bstack11l1l1l_opy_ (u"ࠪࡣࡺࡸ࡬ࠨ௡"), bstack11l1l1l_opy_ (u"ࠫࠬ௢"))):
      bstack11l11llll_opy_ = True
    else:
      return bstack11l11l1ll1_opy_(self, *args, **kwargs)
    if bstack11l11llll_opy_:
      bstack1lll11l11_opy_ = bstack11l1111l1_opy_.bstack1l11l1111_opy_(CONFIG, bstack11l1ll11l1_opy_)
      if kwargs.get(bstack11l1l1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭௣")):
        kwargs[bstack11l1l1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ௤")] = bstack11ll1111ll_opy_(kwargs[bstack11l1l1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ௥")], bstack11l1ll11l1_opy_, bstack1lll11l11_opy_)
      elif kwargs.get(bstack11l1l1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ௦")):
        kwargs[bstack11l1l1l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ௧")] = bstack11ll1111ll_opy_(kwargs[bstack11l1l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ௨")], bstack11l1ll11l1_opy_, bstack1lll11l11_opy_)
  except Exception as e:
    logger.error(bstack11l1l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦ௩").format(str(e)))
  return bstack11l11l1ll1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1lll1ll1ll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11l11llll1_opy_(self, command_executor=bstack11l1l1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨ௪"), *args, **kwargs):
  bstack11l1ll1ll_opy_ = bstack1l11lllll1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l1ll11l_opy_.on():
    return bstack11l1ll1ll_opy_
  try:
    logger.debug(bstack11l1l1l_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪ௫").format(str(command_executor)))
    logger.debug(bstack11l1l1l_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾࠩ௬").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ௭") in command_executor._url:
      bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ௮"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭௯") in command_executor):
    bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ௰"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1lll11l1l1_opy_ = getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭௱"), None)
  if bstack11l1l1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭௲") in bstack11l1ll11l1_opy_ or bstack11l1l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭௳") in bstack11l1ll11l1_opy_:
    bstack1l11l1ll_opy_.bstack1ll11ll1l1_opy_(self)
  if bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ௴") in bstack11l1ll11l1_opy_ and bstack1lll11l1l1_opy_ and bstack1lll11l1l1_opy_.get(bstack11l1l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ௵"), bstack11l1l1l_opy_ (u"ࠪࠫ௶")) == bstack11l1l1l_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ௷"):
    bstack1l11l1ll_opy_.bstack1ll11ll1l1_opy_(self)
  return bstack11l1ll1ll_opy_
def bstack1l1l111l1_opy_(args):
  return bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭௸") in str(args)
def bstack11l111l1l_opy_(self, driver_command, *args, **kwargs):
  global bstack11l1lll1ll_opy_
  global bstack1l1lll11l1_opy_
  bstack1l1ll1l111_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ௹"), None) and bstack11llll1l_opy_(
          threading.current_thread(), bstack11l1l1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭௺"), None)
  bstack1l1l1ll1ll_opy_ = getattr(self, bstack11l1l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ௻"), None) != None and getattr(self, bstack11l1l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ௼"), None) == True
  if not bstack1l1lll11l1_opy_ and bstack1l111111l_opy_ and bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ௽") in CONFIG and CONFIG[bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ௾")] == True and bstack1111111l1_opy_.bstack1llll1ll1_opy_(driver_command) and (bstack1l1l1ll1ll_opy_ or bstack1l1ll1l111_opy_) and not bstack1l1l111l1_opy_(args):
    try:
      bstack1l1lll11l1_opy_ = True
      logger.debug(bstack11l1l1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧ௿").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11l1l1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫఀ").format(str(err)))
    bstack1l1lll11l1_opy_ = False
  response = bstack11l1lll1ll_opy_(self, driver_command, *args, **kwargs)
  if (bstack11l1l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ఁ") in str(bstack11l1ll11l1_opy_).lower() or bstack11l1l1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨం") in str(bstack11l1ll11l1_opy_).lower()) and bstack1l1ll11l_opy_.on():
    try:
      if driver_command == bstack11l1l1l_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭ః"):
        bstack1l11l1ll_opy_.bstack11ll11l1l1_opy_({
            bstack11l1l1l_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩఄ"): response[bstack11l1l1l_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪఅ")],
            bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬఆ"): bstack1l11l1ll_opy_.current_test_uuid() if bstack1l11l1ll_opy_.current_test_uuid() else bstack1l1ll11l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1l1l1ll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1l1lll1111_opy_
  global bstack1ll1l1l11l_opy_
  global bstack11l1ll111_opy_
  global bstack11ll11lll_opy_
  global bstack1ll111111l_opy_
  global bstack11l1ll11l1_opy_
  global bstack11l11l1ll1_opy_
  global bstack11ll1ll1l_opy_
  global bstack1ll11ll111_opy_
  global bstack1llll1l111_opy_
  CONFIG[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨఇ")] = str(bstack11l1ll11l1_opy_) + str(__version__)
  bstack1ll1l1l11_opy_ = os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬఈ")]
  bstack1lll11l11_opy_ = bstack11l1111l1_opy_.bstack1l11l1111_opy_(CONFIG, bstack11l1ll11l1_opy_)
  CONFIG[bstack11l1l1l_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫఉ")] = bstack1ll1l1l11_opy_
  CONFIG[bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫఊ")] = bstack1lll11l11_opy_
  command_executor = bstack1llll111l1_opy_()
  logger.debug(bstack11l11lll11_opy_.format(command_executor))
  proxy = bstack111111l11_opy_(CONFIG, proxy)
  bstack1l11lll11_opy_ = 0 if bstack1ll1l1l11l_opy_ < 0 else bstack1ll1l1l11l_opy_
  try:
    if bstack11ll11lll_opy_ is True:
      bstack1l11lll11_opy_ = int(multiprocessing.current_process().name)
    elif bstack1ll111111l_opy_ is True:
      bstack1l11lll11_opy_ = int(threading.current_thread().name)
  except:
    bstack1l11lll11_opy_ = 0
  bstack11ll1l1ll1_opy_ = bstack1llllll1ll_opy_(CONFIG, bstack1l11lll11_opy_)
  logger.debug(bstack1l1111ll1l_opy_.format(str(bstack11ll1l1ll1_opy_)))
  if bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧఋ") in CONFIG and bstack1l1llllll1_opy_(CONFIG[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨఌ")]):
    bstack1l111111l1_opy_(bstack11ll1l1ll1_opy_)
  if bstack111lllll_opy_.bstack1lll11lll1_opy_(CONFIG, bstack1l11lll11_opy_) and bstack111lllll_opy_.bstack111ll1l11_opy_(bstack11ll1l1ll1_opy_, options, desired_capabilities):
    threading.current_thread().a11yPlatform = True
    if not cli.accessibility.is_enabled():
      bstack111lllll_opy_.set_capabilities(bstack11ll1l1ll1_opy_, CONFIG)
  if desired_capabilities:
    bstack11ll1ll11_opy_ = bstack11lll1l11l_opy_(desired_capabilities)
    bstack11ll1ll11_opy_[bstack11l1l1l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ఍")] = bstack1l11ll1lll_opy_(CONFIG)
    bstack1111lll11_opy_ = bstack1llllll1ll_opy_(bstack11ll1ll11_opy_)
    if bstack1111lll11_opy_:
      bstack11ll1l1ll1_opy_ = update(bstack1111lll11_opy_, bstack11ll1l1ll1_opy_)
    desired_capabilities = None
  if options:
    bstack1ll1l111l1_opy_(options, bstack11ll1l1ll1_opy_)
  if not options:
    options = bstack11lllll1l1_opy_(bstack11ll1l1ll1_opy_)
  bstack1llll1l111_opy_ = CONFIG.get(bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఎ"))[bstack1l11lll11_opy_]
  if proxy and bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧఏ")):
    options.proxy(proxy)
  if options and bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧఐ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1ll1l1111l_opy_() < version.parse(bstack11l1l1l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ఑")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11ll1l1ll1_opy_)
  logger.info(bstack1l1ll11l1_opy_)
  bstack11ll1111l1_opy_.end(EVENTS.bstack1lll11l111_opy_.value, EVENTS.bstack1lll11l111_opy_.value + bstack11l1l1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥఒ"), EVENTS.bstack1lll11l111_opy_.value + bstack11l1l1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤఓ"), status=True, failure=None, test_name=bstack11l1ll111_opy_)
  if bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬఔ")):
    bstack11l11l1ll1_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
  elif bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬక")):
    bstack11l11l1ll1_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧఖ")):
    bstack11l11l1ll1_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack11l11l1ll1_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1llll1111l_opy_ = bstack11l1l1l_opy_ (u"ࠨࠩగ")
    if bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪఘ")):
      bstack1llll1111l_opy_ = self.caps.get(bstack11l1l1l_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥఙ"))
    else:
      bstack1llll1111l_opy_ = self.capabilities.get(bstack11l1l1l_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦచ"))
    if bstack1llll1111l_opy_:
      bstack1l11ll11ll_opy_(bstack1llll1111l_opy_)
      if bstack1ll1l1111l_opy_() <= version.parse(bstack11l1l1l_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬఛ")):
        self.command_executor._url = bstack11l1l1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢజ") + bstack11l11111l_opy_ + bstack11l1l1l_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦఝ")
      else:
        self.command_executor._url = bstack11l1l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥఞ") + bstack1llll1111l_opy_ + bstack11l1l1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥట")
      logger.debug(bstack1ll1lllll1_opy_.format(bstack1llll1111l_opy_))
    else:
      logger.debug(bstack11ll11l11l_opy_.format(bstack11l1l1l_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦఠ")))
  except Exception as e:
    logger.debug(bstack11ll11l11l_opy_.format(e))
  if bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪడ") in bstack11l1ll11l1_opy_:
    bstack1ll1lll111_opy_(bstack1ll1l1l11l_opy_, bstack1ll11ll111_opy_)
  bstack1l1lll1111_opy_ = self.session_id
  if bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬఢ") in bstack11l1ll11l1_opy_ or bstack11l1l1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ణ") in bstack11l1ll11l1_opy_ or bstack11l1l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭త") in bstack11l1ll11l1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1lll11l1l1_opy_ = getattr(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩథ"), None)
  if bstack11l1l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩద") in bstack11l1ll11l1_opy_ or bstack11l1l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩధ") in bstack11l1ll11l1_opy_:
    bstack1l11l1ll_opy_.bstack1ll11ll1l1_opy_(self)
  if bstack11l1l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫన") in bstack11l1ll11l1_opy_ and bstack1lll11l1l1_opy_ and bstack1lll11l1l1_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ఩"), bstack11l1l1l_opy_ (u"࠭ࠧప")) == bstack11l1l1l_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨఫ"):
    bstack1l11l1ll_opy_.bstack1ll11ll1l1_opy_(self)
  bstack11ll1ll1l_opy_.append(self)
  if bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫబ") in CONFIG and bstack11l1l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧభ") in CONFIG[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭మ")][bstack1l11lll11_opy_]:
    bstack11l1ll111_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧయ")][bstack1l11lll11_opy_][bstack11l1l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪర")]
  logger.debug(bstack11ll1llll_opy_.format(bstack1l1lll1111_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1lllll111l_opy_
    def bstack11lll11ll1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack11l111lll1_opy_
      if(bstack11l1l1l_opy_ (u"ࠨࡩ࡯ࡦࡨࡼ࠳ࡰࡳࠣఱ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠧࡿࠩల")), bstack11l1l1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨళ"), bstack11l1l1l_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫఴ")), bstack11l1l1l_opy_ (u"ࠪࡻࠬవ")) as fp:
          fp.write(bstack11l1l1l_opy_ (u"ࠦࠧశ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11l1l1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢష")))):
          with open(args[1], bstack11l1l1l_opy_ (u"࠭ࡲࠨస")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11l1l1l_opy_ (u"ࠧࡢࡵࡼࡲࡨࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡡࡱࡩࡼࡖࡡࡨࡧࠫࡧࡴࡴࡴࡦࡺࡷ࠰ࠥࡶࡡࡨࡧࠣࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮࠭హ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11lll11111_opy_)
            if bstack11l1l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ఺") in CONFIG and str(CONFIG[bstack11l1l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭఻")]).lower() != bstack11l1l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦ఼ࠩ"):
                bstack1l11l1lll1_opy_ = bstack1lllll111l_opy_()
                bstack11ll11lll1_opy_ = bstack11l1l1l_opy_ (u"ࠫࠬ࠭ࠊ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠍࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶ࡡࡀࠐࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠷࡝࠼ࠌࡦࡳࡳࡹࡴࠡࡲࡢ࡭ࡳࡪࡥࡹࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠷ࡣ࠻ࠋࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯ࡵ࡯࡭ࡨ࡫ࠨ࠱࠮ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸࠯࠻ࠋࡥࡲࡲࡸࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯ࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨࠩ࠼ࠌ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽࡾࠎࠥࠦ࡬ࡦࡶࠣࡧࡦࡶࡳ࠼ࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࡷࡶࡾࠦࡻࡼࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࠼ࠌࠣࠤࢂࢃࠠࡤࡣࡷࡧ࡭ࠦࠨࡦࡺࠬࠤࢀࢁࠊࠡࠢࠣࠤࡨࡵ࡮ࡴࡱ࡯ࡩ࠳࡫ࡲࡳࡱࡵࠬࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࡀࠢ࠭ࠢࡨࡼ࠮ࡁࠊࠡࠢࢀࢁࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻࡼࠌࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࠬࢁࡣࡥࡲࡘࡶࡱࢃࠧࠡ࠭ࠣࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪ࠮ࠍࠤࠥࠦࠠ࠯࠰࠱ࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠍࠤࠥࢃࡽࠪ࠽ࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࡾࡿ࠾ࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠍࠫࠬ࠭ఽ").format(bstack1l11l1lll1_opy_=bstack1l11l1lll1_opy_)
            lines.insert(1, bstack11ll11lll1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11l1l1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢా")), bstack11l1l1l_opy_ (u"࠭ࡷࠨి")) as bstack1l1l1111l_opy_:
              bstack1l1l1111l_opy_.writelines(lines)
        CONFIG[bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩీ")] = str(bstack11l1ll11l1_opy_) + str(__version__)
        bstack1ll1l1l11_opy_ = os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ు")]
        bstack1lll11l11_opy_ = bstack11l1111l1_opy_.bstack1l11l1111_opy_(CONFIG, bstack11l1ll11l1_opy_)
        CONFIG[bstack11l1l1l_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬూ")] = bstack1ll1l1l11_opy_
        CONFIG[bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬృ")] = bstack1lll11l11_opy_
        bstack1l11lll11_opy_ = 0 if bstack1ll1l1l11l_opy_ < 0 else bstack1ll1l1l11l_opy_
        try:
          if bstack11ll11lll_opy_ is True:
            bstack1l11lll11_opy_ = int(multiprocessing.current_process().name)
          elif bstack1ll111111l_opy_ is True:
            bstack1l11lll11_opy_ = int(threading.current_thread().name)
        except:
          bstack1l11lll11_opy_ = 0
        CONFIG[bstack11l1l1l_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦౄ")] = False
        CONFIG[bstack11l1l1l_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ౅")] = True
        bstack11ll1l1ll1_opy_ = bstack1llllll1ll_opy_(CONFIG, bstack1l11lll11_opy_)
        logger.debug(bstack1l1111ll1l_opy_.format(str(bstack11ll1l1ll1_opy_)))
        if CONFIG.get(bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪె")):
          bstack1l111111l1_opy_(bstack11ll1l1ll1_opy_)
        if bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪే") in CONFIG and bstack11l1l1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ై") in CONFIG[bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ౉")][bstack1l11lll11_opy_]:
          bstack11l1ll111_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ొ")][bstack1l11lll11_opy_][bstack11l1l1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩో")]
        args.append(os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠬࢄࠧౌ")), bstack11l1l1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ్࠭"), bstack11l1l1l_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩ౎")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11ll1l1ll1_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11l1l1l_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥ౏"))
      bstack11l111lll1_opy_ = True
      return bstack1l1lll111_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11l111111_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1ll1l1l11l_opy_
    global bstack11l1ll111_opy_
    global bstack11ll11lll_opy_
    global bstack1ll111111l_opy_
    global bstack11l1ll11l1_opy_
    CONFIG[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ౐")] = str(bstack11l1ll11l1_opy_) + str(__version__)
    bstack1ll1l1l11_opy_ = os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ౑")]
    bstack1lll11l11_opy_ = bstack11l1111l1_opy_.bstack1l11l1111_opy_(CONFIG, bstack11l1ll11l1_opy_)
    CONFIG[bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧ౒")] = bstack1ll1l1l11_opy_
    CONFIG[bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ౓")] = bstack1lll11l11_opy_
    bstack1l11lll11_opy_ = 0 if bstack1ll1l1l11l_opy_ < 0 else bstack1ll1l1l11l_opy_
    try:
      if bstack11ll11lll_opy_ is True:
        bstack1l11lll11_opy_ = int(multiprocessing.current_process().name)
      elif bstack1ll111111l_opy_ is True:
        bstack1l11lll11_opy_ = int(threading.current_thread().name)
    except:
      bstack1l11lll11_opy_ = 0
    CONFIG[bstack11l1l1l_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ౔")] = True
    bstack11ll1l1ll1_opy_ = bstack1llllll1ll_opy_(CONFIG, bstack1l11lll11_opy_)
    logger.debug(bstack1l1111ll1l_opy_.format(str(bstack11ll1l1ll1_opy_)))
    if CONFIG.get(bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ౕࠫ")):
      bstack1l111111l1_opy_(bstack11ll1l1ll1_opy_)
    if bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶౖࠫ") in CONFIG and bstack11l1l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ౗") in CONFIG[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ౘ")][bstack1l11lll11_opy_]:
      bstack11l1ll111_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧౙ")][bstack1l11lll11_opy_][bstack11l1l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪౚ")]
    import urllib
    import json
    if bstack11l1l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ౛") in CONFIG and str(CONFIG[bstack11l1l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ౜")]).lower() != bstack11l1l1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧౝ"):
        bstack11l1l1111l_opy_ = bstack1lllll111l_opy_()
        bstack1l11l1lll1_opy_ = bstack11l1l1111l_opy_ + urllib.parse.quote(json.dumps(bstack11ll1l1ll1_opy_))
    else:
        bstack1l11l1lll1_opy_ = bstack11l1l1l_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫ౞") + urllib.parse.quote(json.dumps(bstack11ll1l1ll1_opy_))
    browser = self.connect(bstack1l11l1lll1_opy_)
    return browser
except Exception as e:
    pass
def bstack1l1111l111_opy_():
    global bstack11l111lll1_opy_
    global bstack11l1ll11l1_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1lll11ll1l_opy_
        global bstack11111l11_opy_
        if not bstack1l111111l_opy_:
          global bstack111ll11ll1_opy_
          if not bstack111ll11ll1_opy_:
            from bstack_utils.helper import bstack111l11lll_opy_, bstack11lll1lll1_opy_, bstack1ll11l1l1_opy_
            bstack111ll11ll1_opy_ = bstack111l11lll_opy_()
            bstack11lll1lll1_opy_(bstack11l1ll11l1_opy_)
            bstack1lll11l11_opy_ = bstack11l1111l1_opy_.bstack1l11l1111_opy_(CONFIG, bstack11l1ll11l1_opy_)
            bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧ౟"), bstack1lll11l11_opy_)
          BrowserType.connect = bstack1lll11ll1l_opy_
          return
        BrowserType.launch = bstack11l111111_opy_
        bstack11l111lll1_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11lll11ll1_opy_
      bstack11l111lll1_opy_ = True
    except Exception as e:
      pass
def bstack1l1ll1ll1_opy_(context, bstack1l1ll1lll_opy_):
  try:
    context.page.evaluate(bstack11l1l1l_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧౠ"), bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩౡ")+ json.dumps(bstack1l1ll1lll_opy_) + bstack11l1l1l_opy_ (u"ࠨࡽࡾࠤౢ"))
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧౣ"), e)
def bstack11ll1lllll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11l1l1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ౤"), bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ౥") + json.dumps(message) + bstack11l1l1l_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭౦") + json.dumps(level) + bstack11l1l1l_opy_ (u"ࠫࢂࢃࠧ౧"))
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽࠣ౨"), e)
@measure(event_name=EVENTS.bstack1l1ll1l1ll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1111ll11l_opy_(self, url):
  global bstack1l1ll1l1l1_opy_
  try:
    bstack111llllll_opy_(url)
  except Exception as err:
    logger.debug(bstack1l111l111l_opy_.format(str(err)))
  try:
    bstack1l1ll1l1l1_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1llll11l11_opy_):
        bstack111llllll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l111l111l_opy_.format(str(err)))
    raise e
def bstack1l11l1l1ll_opy_(self):
  global bstack1l1l1l1lll_opy_
  bstack1l1l1l1lll_opy_ = self
  return
def bstack1l1ll1lll1_opy_(self):
  global bstack1llll1l1ll_opy_
  bstack1llll1l1ll_opy_ = self
  return
def bstack1l1111ll11_opy_(test_name, bstack1l1111lll_opy_):
  global CONFIG
  if percy.bstack1ll11l111_opy_() == bstack11l1l1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ౩"):
    bstack1ll1ll11l1_opy_ = os.path.relpath(bstack1l1111lll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1ll1ll11l1_opy_)
    bstack11ll11ll11_opy_ = suite_name + bstack11l1l1l_opy_ (u"ࠢ࠮ࠤ౪") + test_name
    threading.current_thread().percySessionName = bstack11ll11ll11_opy_
def bstack11lll11l1l_opy_(self, test, *args, **kwargs):
  global bstack1ll1lll11l_opy_
  test_name = None
  bstack1l1111lll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l1111lll_opy_ = str(test.source)
  bstack1l1111ll11_opy_(test_name, bstack1l1111lll_opy_)
  bstack1ll1lll11l_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1llll1ll11_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack111lll11ll_opy_(driver, bstack11ll11ll11_opy_):
  if not bstack11lll11lll_opy_ and bstack11ll11ll11_opy_:
      bstack1l11lll1ll_opy_ = {
          bstack11l1l1l_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ౫"): bstack11l1l1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ౬"),
          bstack11l1l1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭౭"): {
              bstack11l1l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ౮"): bstack11ll11ll11_opy_
          }
      }
      bstack11lll111ll_opy_ = bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ౯").format(json.dumps(bstack1l11lll1ll_opy_))
      driver.execute_script(bstack11lll111ll_opy_)
  if bstack1ll11ll1ll_opy_:
      bstack1l1ll1llll_opy_ = {
          bstack11l1l1l_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭౰"): bstack11l1l1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ౱"),
          bstack11l1l1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ౲"): {
              bstack11l1l1l_opy_ (u"ࠩࡧࡥࡹࡧࠧ౳"): bstack11ll11ll11_opy_ + bstack11l1l1l_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ౴"),
              bstack11l1l1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ౵"): bstack11l1l1l_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ౶")
          }
      }
      if bstack1ll11ll1ll_opy_.status == bstack11l1l1l_opy_ (u"࠭ࡐࡂࡕࡖࠫ౷"):
          bstack11ll1ll111_opy_ = bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ౸").format(json.dumps(bstack1l1ll1llll_opy_))
          driver.execute_script(bstack11ll1ll111_opy_)
          bstack11ll11l1ll_opy_(driver, bstack11l1l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ౹"))
      elif bstack1ll11ll1ll_opy_.status == bstack11l1l1l_opy_ (u"ࠩࡉࡅࡎࡒࠧ౺"):
          reason = bstack11l1l1l_opy_ (u"ࠥࠦ౻")
          bstack1l1ll1111_opy_ = bstack11ll11ll11_opy_ + bstack11l1l1l_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠬ౼")
          if bstack1ll11ll1ll_opy_.message:
              reason = str(bstack1ll11ll1ll_opy_.message)
              bstack1l1ll1111_opy_ = bstack1l1ll1111_opy_ + bstack11l1l1l_opy_ (u"ࠬࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࠬ౽") + reason
          bstack1l1ll1llll_opy_[bstack11l1l1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ౾")] = {
              bstack11l1l1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭౿"): bstack11l1l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧಀ"),
              bstack11l1l1l_opy_ (u"ࠩࡧࡥࡹࡧࠧಁ"): bstack1l1ll1111_opy_
          }
          bstack11ll1ll111_opy_ = bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨಂ").format(json.dumps(bstack1l1ll1llll_opy_))
          driver.execute_script(bstack11ll1ll111_opy_)
          bstack11ll11l1ll_opy_(driver, bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫಃ"), reason)
          bstack1lll1ll1l1_opy_(reason, str(bstack1ll11ll1ll_opy_), str(bstack1ll1l1l11l_opy_), logger)
@measure(event_name=EVENTS.bstack111ll1llll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11llll1l1l_opy_(driver, test):
  if percy.bstack1ll11l111_opy_() == bstack11l1l1l_opy_ (u"ࠧࡺࡲࡶࡧࠥ಄") and percy.bstack1l11l1l1l1_opy_() == bstack11l1l1l_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣಅ"):
      bstack11l11l111_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪಆ"), None)
      bstack11l11111l1_opy_(driver, bstack11l11l111_opy_, test)
  if bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬಇ"), None) and bstack11llll1l_opy_(
          threading.current_thread(), bstack11l1l1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨಈ"), None):
      logger.info(bstack11l1l1l_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠢࠥಉ"))
      bstack111lllll_opy_.bstack1111l1l1_opy_(driver, name=test.name, path=test.source)
def bstack11l1l1l11l_opy_(test, bstack11ll11ll11_opy_):
    try:
      bstack1l1lll1l1l_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11l1l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩಊ")] = bstack11ll11ll11_opy_
      if bstack1ll11ll1ll_opy_:
        if bstack1ll11ll1ll_opy_.status == bstack11l1l1l_opy_ (u"ࠬࡖࡁࡔࡕࠪಋ"):
          data[bstack11l1l1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ಌ")] = bstack11l1l1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ಍")
        elif bstack1ll11ll1ll_opy_.status == bstack11l1l1l_opy_ (u"ࠨࡈࡄࡍࡑ࠭ಎ"):
          data[bstack11l1l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩಏ")] = bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪಐ")
          if bstack1ll11ll1ll_opy_.message:
            data[bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ಑")] = str(bstack1ll11ll1ll_opy_.message)
      user = CONFIG[bstack11l1l1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧಒ")]
      key = CONFIG[bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩಓ")]
      url = bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠳ࢀࢃ࠮࡫ࡵࡲࡲࠬಔ").format(user, key, bstack1l1lll1111_opy_)
      headers = {
        bstack11l1l1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧಕ"): bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬಖ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
        cli.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡨࡦࡺࡥࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠢಗ"), datetime.datetime.now() - bstack1l1lll1l1l_opy_)
    except Exception as e:
      logger.error(bstack11l1111111_opy_.format(str(e)))
def bstack11l11l1l1_opy_(test, bstack11ll11ll11_opy_):
  global CONFIG
  global bstack1llll1l1ll_opy_
  global bstack1l1l1l1lll_opy_
  global bstack1l1lll1111_opy_
  global bstack1ll11ll1ll_opy_
  global bstack11l1ll111_opy_
  global bstack1lll1ll111_opy_
  global bstack111ll1111l_opy_
  global bstack11l11ll11l_opy_
  global bstack1llll1l11l_opy_
  global bstack11ll1ll1l_opy_
  global bstack1llll1l111_opy_
  try:
    if not bstack1l1lll1111_opy_:
      with open(os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠫࢃ࠭ಘ")), bstack11l1l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬಙ"), bstack11l1l1l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨಚ"))) as f:
        bstack1l11l1ll1_opy_ = json.loads(bstack11l1l1l_opy_ (u"ࠢࡼࠤಛ") + f.read().strip() + bstack11l1l1l_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪಜ") + bstack11l1l1l_opy_ (u"ࠤࢀࠦಝ"))
        bstack1l1lll1111_opy_ = bstack1l11l1ll1_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack11ll1ll1l_opy_:
    for driver in bstack11ll1ll1l_opy_:
      if bstack1l1lll1111_opy_ == driver.session_id:
        if test:
          bstack11llll1l1l_opy_(driver, test)
        bstack111lll11ll_opy_(driver, bstack11ll11ll11_opy_)
  elif bstack1l1lll1111_opy_:
    bstack11l1l1l11l_opy_(test, bstack11ll11ll11_opy_)
  if bstack1llll1l1ll_opy_:
    bstack111ll1111l_opy_(bstack1llll1l1ll_opy_)
  if bstack1l1l1l1lll_opy_:
    bstack11l11ll11l_opy_(bstack1l1l1l1lll_opy_)
  if bstack1ll1l1111_opy_:
    bstack1llll1l11l_opy_()
def bstack11l1llll1_opy_(self, test, *args, **kwargs):
  bstack11ll11ll11_opy_ = None
  if test:
    bstack11ll11ll11_opy_ = str(test.name)
  bstack11l11l1l1_opy_(test, bstack11ll11ll11_opy_)
  bstack1lll1ll111_opy_(self, test, *args, **kwargs)
def bstack11ll1l11l1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l1llll1l1_opy_
  global CONFIG
  global bstack11ll1ll1l_opy_
  global bstack1l1lll1111_opy_
  bstack1l11l1llll_opy_ = None
  try:
    if bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩಞ"), None):
      try:
        if not bstack1l1lll1111_opy_:
          with open(os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠫࢃ࠭ಟ")), bstack11l1l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬಠ"), bstack11l1l1l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨಡ"))) as f:
            bstack1l11l1ll1_opy_ = json.loads(bstack11l1l1l_opy_ (u"ࠢࡼࠤಢ") + f.read().strip() + bstack11l1l1l_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪಣ") + bstack11l1l1l_opy_ (u"ࠤࢀࠦತ"))
            bstack1l1lll1111_opy_ = bstack1l11l1ll1_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack11ll1ll1l_opy_:
        for driver in bstack11ll1ll1l_opy_:
          if bstack1l1lll1111_opy_ == driver.session_id:
            bstack1l11l1llll_opy_ = driver
    bstack111ll111l1_opy_ = bstack111lllll_opy_.bstack11l1l111ll_opy_(test.tags)
    if bstack1l11l1llll_opy_:
      threading.current_thread().isA11yTest = bstack111lllll_opy_.bstack1l111l1l11_opy_(bstack1l11l1llll_opy_, bstack111ll111l1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack111ll111l1_opy_
  except:
    pass
  bstack1l1llll1l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1ll11ll1ll_opy_
  try:
    bstack1ll11ll1ll_opy_ = self._test
  except:
    bstack1ll11ll1ll_opy_ = self.test
def bstack1l111lll1_opy_():
  global bstack111l1lllll_opy_
  try:
    if os.path.exists(bstack111l1lllll_opy_):
      os.remove(bstack111l1lllll_opy_)
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ಥ") + str(e))
def bstack1ll1l11l11_opy_():
  global bstack111l1lllll_opy_
  bstack111l1l1l1_opy_ = {}
  try:
    if not os.path.isfile(bstack111l1lllll_opy_):
      with open(bstack111l1lllll_opy_, bstack11l1l1l_opy_ (u"ࠫࡼ࠭ದ")):
        pass
      with open(bstack111l1lllll_opy_, bstack11l1l1l_opy_ (u"ࠧࡽࠫࠣಧ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack111l1lllll_opy_):
      bstack111l1l1l1_opy_ = json.load(open(bstack111l1lllll_opy_, bstack11l1l1l_opy_ (u"࠭ࡲࡣࠩನ")))
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩ಩") + str(e))
  finally:
    return bstack111l1l1l1_opy_
def bstack1ll1lll111_opy_(platform_index, item_index):
  global bstack111l1lllll_opy_
  try:
    bstack111l1l1l1_opy_ = bstack1ll1l11l11_opy_()
    bstack111l1l1l1_opy_[item_index] = platform_index
    with open(bstack111l1lllll_opy_, bstack11l1l1l_opy_ (u"ࠣࡹ࠮ࠦಪ")) as outfile:
      json.dump(bstack111l1l1l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧಫ") + str(e))
def bstack1llll1l1l_opy_(bstack1ll111lll_opy_):
  global CONFIG
  bstack11l1lllll1_opy_ = bstack11l1l1l_opy_ (u"ࠪࠫಬ")
  if not bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧಭ") in CONFIG:
    logger.info(bstack11l1l1l_opy_ (u"ࠬࡔ࡯ࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠤࡵࡧࡳࡴࡧࡧࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡵࡩࡵࡵࡲࡵࠢࡩࡳࡷࠦࡒࡰࡤࡲࡸࠥࡸࡵ࡯ࠩಮ"))
  try:
    platform = CONFIG[bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಯ")][bstack1ll111lll_opy_]
    if bstack11l1l1l_opy_ (u"ࠧࡰࡵࠪರ") in platform:
      bstack11l1lllll1_opy_ += str(platform[bstack11l1l1l_opy_ (u"ࠨࡱࡶࠫಱ")]) + bstack11l1l1l_opy_ (u"ࠩ࠯ࠤࠬಲ")
    if bstack11l1l1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ಳ") in platform:
      bstack11l1lllll1_opy_ += str(platform[bstack11l1l1l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧ಴")]) + bstack11l1l1l_opy_ (u"ࠬ࠲ࠠࠨವ")
    if bstack11l1l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪಶ") in platform:
      bstack11l1lllll1_opy_ += str(platform[bstack11l1l1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫಷ")]) + bstack11l1l1l_opy_ (u"ࠨ࠮ࠣࠫಸ")
    if bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫಹ") in platform:
      bstack11l1lllll1_opy_ += str(platform[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ಺")]) + bstack11l1l1l_opy_ (u"ࠫ࠱ࠦࠧ಻")
    if bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧ಼ࠪ") in platform:
      bstack11l1lllll1_opy_ += str(platform[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫಽ")]) + bstack11l1l1l_opy_ (u"ࠧ࠭ࠢࠪಾ")
    if bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩಿ") in platform:
      bstack11l1lllll1_opy_ += str(platform[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪೀ")]) + bstack11l1l1l_opy_ (u"ࠪ࠰ࠥ࠭ು")
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠫࡘࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡹࡸࡩ࡯ࡩࠣࡪࡴࡸࠠࡳࡧࡳࡳࡷࡺࠠࡨࡧࡱࡩࡷࡧࡴࡪࡱࡱࠫೂ") + str(e))
  finally:
    if bstack11l1lllll1_opy_[len(bstack11l1lllll1_opy_) - 2:] == bstack11l1l1l_opy_ (u"ࠬ࠲ࠠࠨೃ"):
      bstack11l1lllll1_opy_ = bstack11l1lllll1_opy_[:-2]
    return bstack11l1lllll1_opy_
def bstack1l111ll111_opy_(path, bstack11l1lllll1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11l1llll11_opy_ = ET.parse(path)
    bstack11l111111l_opy_ = bstack11l1llll11_opy_.getroot()
    bstack1111lllll_opy_ = None
    for suite in bstack11l111111l_opy_.iter(bstack11l1l1l_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬೄ")):
      if bstack11l1l1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ೅") in suite.attrib:
        suite.attrib[bstack11l1l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ೆ")] += bstack11l1l1l_opy_ (u"ࠩࠣࠫೇ") + bstack11l1lllll1_opy_
        bstack1111lllll_opy_ = suite
    bstack1llll1ll1l_opy_ = None
    for robot in bstack11l111111l_opy_.iter(bstack11l1l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩೈ")):
      bstack1llll1ll1l_opy_ = robot
    bstack11lll111l1_opy_ = len(bstack1llll1ll1l_opy_.findall(bstack11l1l1l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ೉")))
    if bstack11lll111l1_opy_ == 1:
      bstack1llll1ll1l_opy_.remove(bstack1llll1ll1l_opy_.findall(bstack11l1l1l_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫೊ"))[0])
      bstack111ll1l1l_opy_ = ET.Element(bstack11l1l1l_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬೋ"), attrib={bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬೌ"): bstack11l1l1l_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࡳࠨ್"), bstack11l1l1l_opy_ (u"ࠩ࡬ࡨࠬ೎"): bstack11l1l1l_opy_ (u"ࠪࡷ࠵࠭೏")})
      bstack1llll1ll1l_opy_.insert(1, bstack111ll1l1l_opy_)
      bstack1111l1ll1_opy_ = None
      for suite in bstack1llll1ll1l_opy_.iter(bstack11l1l1l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ೐")):
        bstack1111l1ll1_opy_ = suite
      bstack1111l1ll1_opy_.append(bstack1111lllll_opy_)
      bstack1ll11111l1_opy_ = None
      for status in bstack1111lllll_opy_.iter(bstack11l1l1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ೑")):
        bstack1ll11111l1_opy_ = status
      bstack1111l1ll1_opy_.append(bstack1ll11111l1_opy_)
    bstack11l1llll11_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠫ೒") + str(e))
def bstack11llll11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11lll1l1l1_opy_
  global CONFIG
  if bstack11l1l1l_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦ೓") in options:
    del options[bstack11l1l1l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧ೔")]
  json_data = bstack1ll1l11l11_opy_()
  for bstack1l1ll11lll_opy_ in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11l1l1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࡠࡴࡨࡷࡺࡲࡴࡴࠩೕ"), str(bstack1l1ll11lll_opy_), bstack11l1l1l_opy_ (u"ࠪࡳࡺࡺࡰࡶࡶ࠱ࡼࡲࡲࠧೖ"))
    bstack1l111ll111_opy_(path, bstack1llll1l1l_opy_(json_data[bstack1l1ll11lll_opy_]))
  bstack1l111lll1_opy_()
  return bstack11lll1l1l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1ll1l1lll1_opy_(self, ff_profile_dir):
  global bstack111lll1ll_opy_
  if not ff_profile_dir:
    return None
  return bstack111lll1ll_opy_(self, ff_profile_dir)
def bstack11111ll1l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1ll1lll1l1_opy_
  bstack1lllll11l_opy_ = []
  if bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೗") in CONFIG:
    bstack1lllll11l_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೘")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11l1l1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࠢ೙")],
      pabot_args[bstack11l1l1l_opy_ (u"ࠢࡷࡧࡵࡦࡴࡹࡥࠣ೚")],
      argfile,
      pabot_args.get(bstack11l1l1l_opy_ (u"ࠣࡪ࡬ࡺࡪࠨ೛")),
      pabot_args[bstack11l1l1l_opy_ (u"ࠤࡳࡶࡴࡩࡥࡴࡵࡨࡷࠧ೜")],
      platform[0],
      bstack1ll1lll1l1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11l1l1l_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࡫࡯࡬ࡦࡵࠥೝ")] or [(bstack11l1l1l_opy_ (u"ࠦࠧೞ"), None)]
    for platform in enumerate(bstack1lllll11l_opy_)
  ]
def bstack11ll1l111l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack111ll1ll1_opy_=bstack11l1l1l_opy_ (u"ࠬ࠭೟")):
  global bstack1l1111l1ll_opy_
  self.platform_index = platform_index
  self.bstack11l1l11ll1_opy_ = bstack111ll1ll1_opy_
  bstack1l1111l1ll_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l1ll1l11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack11llll111l_opy_
  global bstack1lll1l1ll_opy_
  bstack1l1lll11ll_opy_ = copy.deepcopy(item)
  if not bstack11l1l1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨೠ") in item.options:
    bstack1l1lll11ll_opy_.options[bstack11l1l1l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩೡ")] = []
  bstack1l111llll1_opy_ = bstack1l1lll11ll_opy_.options[bstack11l1l1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪೢ")].copy()
  for v in bstack1l1lll11ll_opy_.options[bstack11l1l1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫೣ")]:
    if bstack11l1l1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩ೤") in v:
      bstack1l111llll1_opy_.remove(v)
    if bstack11l1l1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫ೥") in v:
      bstack1l111llll1_opy_.remove(v)
    if bstack11l1l1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ೦") in v:
      bstack1l111llll1_opy_.remove(v)
  bstack1l111llll1_opy_.insert(0, bstack11l1l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜࠿ࢁࡽࠨ೧").format(bstack1l1lll11ll_opy_.platform_index))
  bstack1l111llll1_opy_.insert(0, bstack11l1l1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࠾ࢀࢃࠧ೨").format(bstack1l1lll11ll_opy_.bstack11l1l11ll1_opy_))
  bstack1l1lll11ll_opy_.options[bstack11l1l1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ೩")] = bstack1l111llll1_opy_
  if bstack1lll1l1ll_opy_:
    bstack1l1lll11ll_opy_.options[bstack11l1l1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ೪")].insert(0, bstack11l1l1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕ࠽ࡿࢂ࠭೫").format(bstack1lll1l1ll_opy_))
  return bstack11llll111l_opy_(caller_id, datasources, is_last, bstack1l1lll11ll_opy_, outs_dir)
def bstack111l11ll1_opy_(command, item_index):
  if bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ೬")):
    os.environ[bstack11l1l1l_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭೭")] = json.dumps(CONFIG[bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೮")][item_index % bstack1ll1ll111l_opy_])
  global bstack1lll1l1ll_opy_
  if bstack1lll1l1ll_opy_:
    command[0] = command[0].replace(bstack11l1l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭೯"), bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤࠬ೰") + str(
      item_index) + bstack11l1l1l_opy_ (u"ࠩࠣࠫೱ") + bstack1lll1l1ll_opy_, 1)
  else:
    command[0] = command[0].replace(bstack11l1l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩೲ"),
                                    bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨೳ") + str(item_index), 1)
def bstack11llll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111lllll1l_opy_
  bstack111l11ll1_opy_(command, item_index)
  return bstack111lllll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11l1lll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111lllll1l_opy_
  bstack111l11ll1_opy_(command, item_index)
  return bstack111lllll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1l11111l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111lllll1l_opy_
  bstack111l11ll1_opy_(command, item_index)
  return bstack111lllll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack111ll1l1l1_opy_(self, runner, quiet=False, capture=True):
  global bstack1ll1111lll_opy_
  bstack11ll1l11ll_opy_ = bstack1ll1111lll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11l1l1l_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬ೴")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11l1l1l_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪ೵")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11ll1l11ll_opy_
def bstack1lll1l111_opy_(runner, hook_name, context, element, bstack11l11ll1ll_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack111111lll_opy_.bstack11l1l11l_opy_(hook_name, element)
    bstack11l11ll1ll_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack111111lll_opy_.bstack11l1l111_opy_(element)
      if hook_name not in [bstack11l1l1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫ೶"), bstack11l1l1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫ೷")] and args and hasattr(args[0], bstack11l1l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩ೸")):
        args[0].error_message = bstack11l1l1l_opy_ (u"ࠪࠫ೹")
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡩࡣࡱࡨࡱ࡫ࠠࡩࡱࡲ࡯ࡸࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭೺").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1lll1ll_opy_, stage=STAGE.SINGLE, hook_type=bstack11l1l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡆࡲ࡬ࠣ೻"), bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11ll1l11l_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
    if runner.hooks.get(bstack11l1l1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥ೼")).__name__ != bstack11l1l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣࡩ࡫ࡦࡢࡷ࡯ࡸࡤ࡮࡯ࡰ࡭ࠥ೽"):
      bstack1lll1l111_opy_(runner, name, context, runner, bstack11l11ll1ll_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack111lll111_opy_(bstack11l1l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ೾")) else context.browser
      runner.driver_initialised = bstack11l1l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ೿")
    except Exception as e:
      logger.debug(bstack11l1l1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧ࠽ࠤࢀࢃࠧഀ").format(str(e)))
def bstack1l11ll1111_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
    bstack1lll1l111_opy_(runner, name, context, context.feature, bstack11l11ll1ll_opy_, *args)
    try:
      if not bstack11lll11lll_opy_:
        bstack1l11l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack111lll111_opy_(bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪഁ")) else context.browser
        if is_driver_active(bstack1l11l1llll_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11l1l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨം")
          bstack1l1ll1lll_opy_ = str(runner.feature.name)
          bstack1l1ll1ll1_opy_(context, bstack1l1ll1lll_opy_)
          bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫഃ") + json.dumps(bstack1l1ll1lll_opy_) + bstack11l1l1l_opy_ (u"ࠧࡾࡿࠪഄ"))
    except Exception as e:
      logger.debug(bstack11l1l1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨഅ").format(str(e)))
def bstack11ll1l1l1l_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
    if hasattr(context, bstack11l1l1l_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫആ")):
        bstack111111lll_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11l1l1l_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬഇ")) else context.feature
    bstack1lll1l111_opy_(runner, name, context, target, bstack11l11ll1ll_opy_, *args)
@measure(event_name=EVENTS.bstack1l11111l11_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11lllll111_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
    if len(context.scenario.tags) == 0: bstack111111lll_opy_.start_test(context)
    bstack1lll1l111_opy_(runner, name, context, context.scenario, bstack11l11ll1ll_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1lll11ll11_opy_.bstack1llllll1l_opy_(context, *args)
    try:
      bstack1l11l1llll_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪഈ"), context.browser)
      if is_driver_active(bstack1l11l1llll_opy_):
        bstack1l11l1ll_opy_.bstack1ll11ll1l1_opy_(bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫഉ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l1l1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣഊ")
        if (not bstack11lll11lll_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l1ll1lll_opy_ = str(runner.feature.name)
          bstack1l1ll1lll_opy_ = feature_name + bstack11l1l1l_opy_ (u"ࠧࠡ࠯ࠣࠫഋ") + scenario_name
          if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥഌ"):
            bstack1l1ll1ll1_opy_(context, bstack1l1ll1lll_opy_)
            bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ഍") + json.dumps(bstack1l1ll1lll_opy_) + bstack11l1l1l_opy_ (u"ࠪࢁࢂ࠭എ"))
    except Exception as e:
      logger.debug(bstack11l1l1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬഏ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1lll1ll_opy_, stage=STAGE.SINGLE, hook_type=bstack11l1l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡘࡺࡥࡱࠤഐ"), bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11l1l1111_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
    bstack1lll1l111_opy_(runner, name, context, args[0], bstack11l11ll1ll_opy_, *args)
    try:
      bstack1l11l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack111lll111_opy_(bstack11l1l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ഑")) else context.browser
      if is_driver_active(bstack1l11l1llll_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l1l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧഒ")
        bstack111111lll_opy_.bstack11ll11ll_opy_(args[0])
        if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨഓ"):
          feature_name = bstack1l1ll1lll_opy_ = str(runner.feature.name)
          bstack1l1ll1lll_opy_ = feature_name + bstack11l1l1l_opy_ (u"ࠩࠣ࠱ࠥ࠭ഔ") + context.scenario.name
          bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨക") + json.dumps(bstack1l1ll1lll_opy_) + bstack11l1l1l_opy_ (u"ࠫࢂࢃࠧഖ"))
    except Exception as e:
      logger.debug(bstack11l1l1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩഗ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1lll1ll_opy_, stage=STAGE.SINGLE, hook_type=bstack11l1l1l_opy_ (u"ࠨࡡࡧࡶࡨࡶࡘࡺࡥࡱࠤഘ"), bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack11l11l1111_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
  bstack111111lll_opy_.bstack11ll1l11_opy_(args[0])
  try:
    bstack1l1111l1l_opy_ = args[0].status.name
    bstack1l11l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ങ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1l11l1llll_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11l1l1l_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨച")
        feature_name = bstack1l1ll1lll_opy_ = str(runner.feature.name)
        bstack1l1ll1lll_opy_ = feature_name + bstack11l1l1l_opy_ (u"ࠩࠣ࠱ࠥ࠭ഛ") + context.scenario.name
        bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨജ") + json.dumps(bstack1l1ll1lll_opy_) + bstack11l1l1l_opy_ (u"ࠫࢂࢃࠧഝ"))
    if str(bstack1l1111l1l_opy_).lower() == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬഞ"):
      bstack11l11ll1l_opy_ = bstack11l1l1l_opy_ (u"࠭ࠧട")
      bstack1lll1l11ll_opy_ = bstack11l1l1l_opy_ (u"ࠧࠨഠ")
      bstack11ll1lll1l_opy_ = bstack11l1l1l_opy_ (u"ࠨࠩഡ")
      try:
        import traceback
        bstack11l11ll1l_opy_ = runner.exception.__class__.__name__
        bstack11l1llll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1lll1l11ll_opy_ = bstack11l1l1l_opy_ (u"ࠩࠣࠫഢ").join(bstack11l1llll_opy_)
        bstack11ll1lll1l_opy_ = bstack11l1llll_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lll1l1l11_opy_.format(str(e)))
      bstack11l11ll1l_opy_ += bstack11ll1lll1l_opy_
      bstack11ll1lllll_opy_(context, json.dumps(str(args[0].name) + bstack11l1l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤണ") + str(bstack1lll1l11ll_opy_)),
                          bstack11l1l1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥത"))
      if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥഥ"):
        bstack11lll1ll1_opy_(getattr(context, bstack11l1l1l_opy_ (u"࠭ࡰࡢࡩࡨࠫദ"), None), bstack11l1l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢധ"), bstack11l11ll1l_opy_)
        bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ന") + json.dumps(str(args[0].name) + bstack11l1l1l_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣഩ") + str(bstack1lll1l11ll_opy_)) + bstack11l1l1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪപ"))
      if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤഫ"):
        bstack11ll11l1ll_opy_(bstack1l11l1llll_opy_, bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬബ"), bstack11l1l1l_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥഭ") + str(bstack11l11ll1l_opy_))
    else:
      bstack11ll1lllll_opy_(context, bstack11l1l1l_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣമ"), bstack11l1l1l_opy_ (u"ࠣ࡫ࡱࡪࡴࠨയ"))
      if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢര"):
        bstack11lll1ll1_opy_(getattr(context, bstack11l1l1l_opy_ (u"ࠪࡴࡦ࡭ࡥࠨറ"), None), bstack11l1l1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦല"))
      bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪള") + json.dumps(str(args[0].name) + bstack11l1l1l_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥഴ")) + bstack11l1l1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭വ"))
      if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨശ"):
        bstack11ll11l1ll_opy_(bstack1l11l1llll_opy_, bstack11l1l1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤഷ"))
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩസ").format(str(e)))
  bstack1lll1l111_opy_(runner, name, context, args[0], bstack11l11ll1ll_opy_, *args)
@measure(event_name=EVENTS.bstack11ll111111_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1l11ll11l_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
  bstack111111lll_opy_.end_test(args[0])
  try:
    bstack1ll11l1l1l_opy_ = args[0].status.name
    bstack1l11l1llll_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪഹ"), context.browser)
    bstack1lll11ll11_opy_.bstack1l111l1111_opy_(bstack1l11l1llll_opy_)
    if str(bstack1ll11l1l1l_opy_).lower() == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬഺ"):
      bstack11l11ll1l_opy_ = bstack11l1l1l_opy_ (u"഻࠭ࠧ")
      bstack1lll1l11ll_opy_ = bstack11l1l1l_opy_ (u"ࠧࠨ഼")
      bstack11ll1lll1l_opy_ = bstack11l1l1l_opy_ (u"ࠨࠩഽ")
      try:
        import traceback
        bstack11l11ll1l_opy_ = runner.exception.__class__.__name__
        bstack11l1llll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1lll1l11ll_opy_ = bstack11l1l1l_opy_ (u"ࠩࠣࠫാ").join(bstack11l1llll_opy_)
        bstack11ll1lll1l_opy_ = bstack11l1llll_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lll1l1l11_opy_.format(str(e)))
      bstack11l11ll1l_opy_ += bstack11ll1lll1l_opy_
      bstack11ll1lllll_opy_(context, json.dumps(str(args[0].name) + bstack11l1l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤി") + str(bstack1lll1l11ll_opy_)),
                          bstack11l1l1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥീ"))
      if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢു") or runner.driver_initialised == bstack11l1l1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ൂ"):
        bstack11lll1ll1_opy_(getattr(context, bstack11l1l1l_opy_ (u"ࠧࡱࡣࡪࡩࠬൃ"), None), bstack11l1l1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣൄ"), bstack11l11ll1l_opy_)
        bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ൅") + json.dumps(str(args[0].name) + bstack11l1l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤെ") + str(bstack1lll1l11ll_opy_)) + bstack11l1l1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫേ"))
      if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢൈ") or runner.driver_initialised == bstack11l1l1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭൉"):
        bstack11ll11l1ll_opy_(bstack1l11l1llll_opy_, bstack11l1l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧൊ"), bstack11l1l1l_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧോ") + str(bstack11l11ll1l_opy_))
    else:
      bstack11ll1lllll_opy_(context, bstack11l1l1l_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥൌ"), bstack11l1l1l_opy_ (u"ࠥ࡭ࡳ࡬࡯്ࠣ"))
      if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨൎ") or runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ൏"):
        bstack11lll1ll1_opy_(getattr(context, bstack11l1l1l_opy_ (u"࠭ࡰࡢࡩࡨࠫ൐"), None), bstack11l1l1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ൑"))
      bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭൒") + json.dumps(str(args[0].name) + bstack11l1l1l_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨ൓")) + bstack11l1l1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩൔ"))
      if runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨൕ") or runner.driver_initialised == bstack11l1l1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬൖ"):
        bstack11ll11l1ll_opy_(bstack1l11l1llll_opy_, bstack11l1l1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨൗ"))
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩ൘").format(str(e)))
  bstack1lll1l111_opy_(runner, name, context, context.scenario, bstack11l11ll1ll_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1ll1lllll_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
    target = context.scenario if hasattr(context, bstack11l1l1l_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪ൙")) else context.feature
    bstack1lll1l111_opy_(runner, name, context, target, bstack11l11ll1ll_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack111ll11l1_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
    try:
      bstack1l11l1llll_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ൚"), context.browser)
      bstack11l1l1ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠪࠫ൛")
      if context.failed is True:
        bstack11l111l11_opy_ = []
        bstack1ll1lll1l_opy_ = []
        bstack1l11111ll1_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack11l111l11_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1llll_opy_ = traceback.format_tb(exc_tb)
            bstack1lll1ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠫࠥ࠭൜").join(bstack11l1llll_opy_)
            bstack1ll1lll1l_opy_.append(bstack1lll1ll1l_opy_)
            bstack1l11111ll1_opy_.append(bstack11l1llll_opy_[-1])
        except Exception as e:
          logger.debug(bstack1lll1l1l11_opy_.format(str(e)))
        bstack11l11ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠬ࠭൝")
        for i in range(len(bstack11l111l11_opy_)):
          bstack11l11ll1l_opy_ += bstack11l111l11_opy_[i] + bstack1l11111ll1_opy_[i] + bstack11l1l1l_opy_ (u"࠭࡜࡯ࠩ൞")
        bstack11l1l1ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠧࠡࠩൟ").join(bstack1ll1lll1l_opy_)
        if runner.driver_initialised in [bstack11l1l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤൠ"), bstack11l1l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨൡ")]:
          bstack11ll1lllll_opy_(context, bstack11l1l1ll1l_opy_, bstack11l1l1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤൢ"))
          bstack11lll1ll1_opy_(getattr(context, bstack11l1l1l_opy_ (u"ࠫࡵࡧࡧࡦࠩൣ"), None), bstack11l1l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ൤"), bstack11l11ll1l_opy_)
          bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ൥") + json.dumps(bstack11l1l1ll1l_opy_) + bstack11l1l1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧ൦"))
          bstack11ll11l1ll_opy_(bstack1l11l1llll_opy_, bstack11l1l1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ൧"), bstack11l1l1l_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢ൨") + str(bstack11l11ll1l_opy_))
          bstack1llll1111_opy_ = bstack11l111l1l1_opy_(bstack11l1l1ll1l_opy_, runner.feature.name, logger)
          if (bstack1llll1111_opy_ != None):
            bstack11l11lll1l_opy_.append(bstack1llll1111_opy_)
      else:
        if runner.driver_initialised in [bstack11l1l1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦ൩"), bstack11l1l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣ൪")]:
          bstack11ll1lllll_opy_(context, bstack11l1l1l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣ൫") + str(runner.feature.name) + bstack11l1l1l_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ൬"), bstack11l1l1l_opy_ (u"ࠢࡪࡰࡩࡳࠧ൭"))
          bstack11lll1ll1_opy_(getattr(context, bstack11l1l1l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭൮"), None), bstack11l1l1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ൯"))
          bstack1l11l1llll_opy_.execute_script(bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ൰") + json.dumps(bstack11l1l1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢ൱") + str(runner.feature.name) + bstack11l1l1l_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢ൲")) + bstack11l1l1l_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ൳"))
          bstack11ll11l1ll_opy_(bstack1l11l1llll_opy_, bstack11l1l1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ൴"))
          bstack1llll1111_opy_ = bstack11l111l1l1_opy_(bstack11l1l1ll1l_opy_, runner.feature.name, logger)
          if (bstack1llll1111_opy_ != None):
            bstack11l11lll1l_opy_.append(bstack1llll1111_opy_)
    except Exception as e:
      logger.debug(bstack11l1l1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪ൵").format(str(e)))
    bstack1lll1l111_opy_(runner, name, context, context.feature, bstack11l11ll1ll_opy_, *args)
@measure(event_name=EVENTS.bstack1ll1lll1ll_opy_, stage=STAGE.SINGLE, hook_type=bstack11l1l1l_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡂ࡮࡯ࠦ൶"), bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1llll1l11_opy_(runner, name, context, bstack11l11ll1ll_opy_, *args):
    bstack1lll1l111_opy_(runner, name, context, runner, bstack11l11ll1ll_opy_, *args)
def bstack1ll11llll1_opy_(self, name, context, *args):
  if bstack1l111111l_opy_:
    platform_index = int(threading.current_thread()._name) % bstack1ll1ll111l_opy_
    bstack11lllllll1_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭൷")][platform_index]
    os.environ[bstack11l1l1l_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬ൸")] = json.dumps(bstack11lllllll1_opy_)
  global bstack11l11ll1ll_opy_
  if not hasattr(self, bstack11l1l1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࡦࠪ൹")):
    self.driver_initialised = None
  bstack11llll1l11_opy_ = {
      bstack11l1l1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪൺ"): bstack11ll1l11l_opy_,
      bstack11l1l1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨൻ"): bstack1l11ll1111_opy_,
      bstack11l1l1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡶࡤ࡫ࠬർ"): bstack11ll1l1l1l_opy_,
      bstack11l1l1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫൽ"): bstack11lllll111_opy_,
      bstack11l1l1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠨൾ"): bstack11l1l1111_opy_,
      bstack11l1l1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨൿ"): bstack11l11l1111_opy_,
      bstack11l1l1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭඀"): bstack1l11ll11l_opy_,
      bstack11l1l1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡺࡡࡨࠩඁ"): bstack1ll1lllll_opy_,
      bstack11l1l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧං"): bstack111ll11l1_opy_,
      bstack11l1l1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫඃ"): bstack1llll1l11_opy_
  }
  handler = bstack11llll1l11_opy_.get(name, bstack11l11ll1ll_opy_)
  handler(self, name, context, bstack11l11ll1ll_opy_, *args)
  if name in [bstack11l1l1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩ඄"), bstack11l1l1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫඅ"), bstack11l1l1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧආ")]:
    try:
      bstack1l11l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack111lll111_opy_(bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඇ")) else context.browser
      bstack1l1111llll_opy_ = (
        (name == bstack11l1l1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩඈ") and self.driver_initialised == bstack11l1l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦඉ")) or
        (name == bstack11l1l1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨඊ") and self.driver_initialised == bstack11l1l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥඋ")) or
        (name == bstack11l1l1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫඌ") and self.driver_initialised in [bstack11l1l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨඍ"), bstack11l1l1l_opy_ (u"ࠧ࡯࡮ࡴࡶࡨࡴࠧඎ")]) or
        (name == bstack11l1l1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪඏ") and self.driver_initialised == bstack11l1l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧඐ"))
      )
      if bstack1l1111llll_opy_:
        self.driver_initialised = None
        bstack1l11l1llll_opy_.quit()
    except Exception:
      pass
def bstack11lll1llll_opy_(config, startdir):
  return bstack11l1l1l_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨඑ").format(bstack11l1l1l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣඒ"))
notset = Notset()
def bstack1llllll11l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l1l1l111l_opy_
  if str(name).lower() == bstack11l1l1l_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪඓ"):
    return bstack11l1l1l_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥඔ")
  else:
    return bstack1l1l1l111l_opy_(self, name, default, skip)
def bstack1l11l111l_opy_(item, when):
  global bstack1ll111ll11_opy_
  try:
    bstack1ll111ll11_opy_(item, when)
  except Exception as e:
    pass
def bstack1l1111lll1_opy_():
  return
def bstack1l1lllll1l_opy_(type, name, status, reason, bstack1l1llll1ll_opy_, bstack11lll111l_opy_):
  bstack1l11lll1ll_opy_ = {
    bstack11l1l1l_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬඕ"): type,
    bstack11l1l1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩඖ"): {}
  }
  if type == bstack11l1l1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ඗"):
    bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ඘")][bstack11l1l1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ඙")] = bstack1l1llll1ll_opy_
    bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ක")][bstack11l1l1l_opy_ (u"ࠫࡩࡧࡴࡢࠩඛ")] = json.dumps(str(bstack11lll111l_opy_))
  if type == bstack11l1l1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ග"):
    bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩඝ")][bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬඞ")] = name
  if type == bstack11l1l1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫඟ"):
    bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬච")][bstack11l1l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪඡ")] = status
    if status == bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫජ"):
      bstack1l11lll1ll_opy_[bstack11l1l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨඣ")][bstack11l1l1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ඤ")] = json.dumps(str(reason))
  bstack11lll111ll_opy_ = bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬඥ").format(json.dumps(bstack1l11lll1ll_opy_))
  return bstack11lll111ll_opy_
def bstack1ll11l11l_opy_(driver_command, response):
    if driver_command == bstack11l1l1l_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬඦ"):
        bstack1l11l1ll_opy_.bstack11ll11l1l1_opy_({
            bstack11l1l1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨට"): response[bstack11l1l1l_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩඨ")],
            bstack11l1l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫඩ"): bstack1l11l1ll_opy_.current_test_uuid()
        })
def bstack11l1l1l11_opy_(item, call, rep):
  global bstack1l11llll11_opy_
  global bstack11ll1ll1l_opy_
  global bstack11lll11lll_opy_
  name = bstack11l1l1l_opy_ (u"ࠬ࠭ඪ")
  try:
    if rep.when == bstack11l1l1l_opy_ (u"࠭ࡣࡢ࡮࡯ࠫණ"):
      bstack1l1lll1111_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack11lll11lll_opy_:
          name = str(rep.nodeid)
          bstack1l11l1ll1l_opy_ = bstack1l1lllll1l_opy_(bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨඬ"), name, bstack11l1l1l_opy_ (u"ࠨࠩත"), bstack11l1l1l_opy_ (u"ࠩࠪථ"), bstack11l1l1l_opy_ (u"ࠪࠫද"), bstack11l1l1l_opy_ (u"ࠫࠬධ"))
          threading.current_thread().bstack111llll11_opy_ = name
          for driver in bstack11ll1ll1l_opy_:
            if bstack1l1lll1111_opy_ == driver.session_id:
              driver.execute_script(bstack1l11l1ll1l_opy_)
      except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬන").format(str(e)))
      try:
        bstack1l1l1ll1l1_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11l1l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ඲"):
          status = bstack11l1l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧඳ") if rep.outcome.lower() == bstack11l1l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨප") else bstack11l1l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩඵ")
          reason = bstack11l1l1l_opy_ (u"ࠪࠫබ")
          if status == bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫභ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11l1l1l_opy_ (u"ࠬ࡯࡮ࡧࡱࠪම") if status == bstack11l1l1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ඹ") else bstack11l1l1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ය")
          data = name + bstack11l1l1l_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪර") if status == bstack11l1l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ඼") else name + bstack11l1l1l_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭ල") + reason
          bstack11l11l111l_opy_ = bstack1l1lllll1l_opy_(bstack11l1l1l_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭඾"), bstack11l1l1l_opy_ (u"ࠬ࠭඿"), bstack11l1l1l_opy_ (u"࠭ࠧව"), bstack11l1l1l_opy_ (u"ࠧࠨශ"), level, data)
          for driver in bstack11ll1ll1l_opy_:
            if bstack1l1lll1111_opy_ == driver.session_id:
              driver.execute_script(bstack11l11l111l_opy_)
      except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬෂ").format(str(e)))
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭ස").format(str(e)))
  bstack1l11llll11_opy_(item, call, rep)
def bstack11l11111l1_opy_(driver, bstack1l1l1ll1l_opy_, test=None):
  global bstack1ll1l1l11l_opy_
  if test != None:
    bstack11lll11l11_opy_ = getattr(test, bstack11l1l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨහ"), None)
    bstack111lllll11_opy_ = getattr(test, bstack11l1l1l_opy_ (u"ࠫࡺࡻࡩࡥࠩළ"), None)
    PercySDK.screenshot(driver, bstack1l1l1ll1l_opy_, bstack11lll11l11_opy_=bstack11lll11l11_opy_, bstack111lllll11_opy_=bstack111lllll11_opy_, bstack1ll11l11l1_opy_=bstack1ll1l1l11l_opy_)
  else:
    PercySDK.screenshot(driver, bstack1l1l1ll1l_opy_)
@measure(event_name=EVENTS.bstack1l1lllll1_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1ll1l11111_opy_(driver):
  if bstack11ll1l1l1_opy_.bstack1ll11l111l_opy_() is True or bstack11ll1l1l1_opy_.capturing() is True:
    return
  bstack11ll1l1l1_opy_.bstack1lll111l1_opy_()
  while not bstack11ll1l1l1_opy_.bstack1ll11l111l_opy_():
    bstack1llll11lll_opy_ = bstack11ll1l1l1_opy_.bstack11llllll11_opy_()
    bstack11l11111l1_opy_(driver, bstack1llll11lll_opy_)
  bstack11ll1l1l1_opy_.bstack11l1ll1l11_opy_()
def bstack1lll111111_opy_(sequence, driver_command, response = None, bstack11l1ll1l1l_opy_ = None, args = None):
    try:
      if sequence != bstack11l1l1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬෆ"):
        return
      if percy.bstack1ll11l111_opy_() == bstack11l1l1l_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧ෇"):
        return
      bstack1llll11lll_opy_ = bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ෈"), None)
      for command in bstack1l11l1lll_opy_:
        if command == driver_command:
          for driver in bstack11ll1ll1l_opy_:
            bstack1ll1l11111_opy_(driver)
      bstack1ll1ll1111_opy_ = percy.bstack1l11l1l1l1_opy_()
      if driver_command in bstack1l1llllll_opy_[bstack1ll1ll1111_opy_]:
        bstack11ll1l1l1_opy_.bstack1l11ll1ll1_opy_(bstack1llll11lll_opy_, driver_command)
    except Exception as e:
      pass
@measure(event_name=EVENTS.bstack1lll11l111_opy_, stage=STAGE.bstack1l1llll111_opy_)
def bstack11ll111ll_opy_(framework_name):
  if bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ෉")):
      return
  bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ්࠭"), True)
  global bstack11l1ll11l1_opy_
  global bstack11l111lll1_opy_
  global bstack1ll11lll11_opy_
  bstack11l1ll11l1_opy_ = framework_name
  logger.info(bstack1l11l11lll_opy_.format(bstack11l1ll11l1_opy_.split(bstack11l1l1l_opy_ (u"ࠪ࠱ࠬ෋"))[0]))
  bstack111l1llll1_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l111111l_opy_:
      Service.start = bstack1llll1l1l1_opy_
      Service.stop = bstack1l1lll1ll1_opy_
      webdriver.Remote.get = bstack1111ll11l_opy_
      WebDriver.close = bstack11l11l1lll_opy_
      WebDriver.quit = bstack1l1l1l11ll_opy_
      webdriver.Remote.__init__ = bstack1l1l1ll11_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack1l111111l_opy_:
        webdriver.Remote.__init__ = bstack11l11llll1_opy_
    WebDriver.execute = bstack11l111l1l_opy_
    bstack11l111lll1_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l111111l_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l11lll1l1_opy_
  except Exception as e:
    pass
  bstack1l1111l111_opy_()
  if not bstack11l111lll1_opy_:
    bstack1ll11l1l11_opy_(bstack11l1l1l_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨ෌"), bstack1l1l1111l1_opy_)
  if bstack1l111l1l1l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._1llllll111_opy_ = bstack1l11ll111_opy_
    except Exception as e:
      logger.error(bstack1l11l11l1l_opy_.format(str(e)))
  if bstack11lllll1ll_opy_():
    bstack1l1lllllll_opy_(CONFIG, logger)
  if (bstack11l1l1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ෍") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1ll11l111_opy_() == bstack11l1l1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ෎"):
          bstack1lll1lll1l_opy_(bstack1lll111111_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1ll1l1lll1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l1ll1lll1_opy_
      except Exception as e:
        logger.warn(bstack111l1lll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1l11l1l1ll_opy_
      except Exception as e:
        logger.debug(bstack1l11l11ll_opy_ + str(e))
    except Exception as e:
      bstack1ll11l1l11_opy_(e, bstack111l1lll1_opy_)
    Output.start_test = bstack11lll11l1l_opy_
    Output.end_test = bstack11l1llll1_opy_
    TestStatus.__init__ = bstack11ll1l11l1_opy_
    QueueItem.__init__ = bstack11ll1l111l_opy_
    pabot._create_items = bstack11111ll1l_opy_
    try:
      from pabot import __version__ as bstack1llll11ll1_opy_
      if version.parse(bstack1llll11ll1_opy_) >= version.parse(bstack11l1l1l_opy_ (u"ࠧ࠳࠰࠴࠹࠳࠶ࠧා")):
        pabot._run = bstack1l11111l1_opy_
      elif version.parse(bstack1llll11ll1_opy_) >= version.parse(bstack11l1l1l_opy_ (u"ࠨ࠴࠱࠵࠸࠴࠰ࠨැ")):
        pabot._run = bstack11l1lll1l1_opy_
      else:
        pabot._run = bstack11llll1l1_opy_
    except Exception as e:
      pabot._run = bstack11llll1l1_opy_
    pabot._create_command_for_execution = bstack1l1ll1l11_opy_
    pabot._report_results = bstack11llll11l_opy_
  if bstack11l1l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩෑ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll11l1l11_opy_(e, bstack1l1l1llll1_opy_)
    Runner.run_hook = bstack1ll11llll1_opy_
    Step.run = bstack111ll1l1l1_opy_
  if bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪි") in str(framework_name).lower():
    if not bstack1l111111l_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11lll1llll_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l1111lll1_opy_
      Config.getoption = bstack1llllll11l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11l1l1l11_opy_
    except Exception as e:
      pass
def bstack1lllll11ll_opy_():
  global CONFIG
  if bstack11l1l1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫී") in CONFIG and int(CONFIG[bstack11l1l1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬු")]) > 1:
    logger.warn(bstack1lllll1lll_opy_)
def bstack11l111lll_opy_(arg, bstack11111ll1_opy_, bstack1lll1llll1_opy_=None):
  global CONFIG
  global bstack11l11111l_opy_
  global bstack1ll1111ll1_opy_
  global bstack1l111111l_opy_
  global bstack11111l11_opy_
  bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭෕")
  if bstack11111ll1_opy_ and isinstance(bstack11111ll1_opy_, str):
    bstack11111ll1_opy_ = eval(bstack11111ll1_opy_)
  CONFIG = bstack11111ll1_opy_[bstack11l1l1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧූ")]
  bstack11l11111l_opy_ = bstack11111ll1_opy_[bstack11l1l1l_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩ෗")]
  bstack1ll1111ll1_opy_ = bstack11111ll1_opy_[bstack11l1l1l_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫෘ")]
  bstack1l111111l_opy_ = bstack11111ll1_opy_[bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ෙ")]
  bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬේ"), bstack1l111111l_opy_)
  os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧෛ")] = bstack1llll11l1_opy_
  os.environ[bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬො")] = json.dumps(CONFIG)
  os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧෝ")] = bstack11l11111l_opy_
  os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩෞ")] = str(bstack1ll1111ll1_opy_)
  os.environ[bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨෟ")] = str(True)
  if bstack11l11l11l_opy_(arg, [bstack11l1l1l_opy_ (u"ࠪ࠱ࡳ࠭෠"), bstack11l1l1l_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ෡")]) != -1:
    os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭෢")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1ll1l11lll_opy_)
    return
  bstack1l1l11l1ll_opy_()
  global bstack1l1l11ll11_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1ll1lll1l1_opy_
  global bstack1lll1l1ll_opy_
  global bstack1ll111l11l_opy_
  global bstack1ll11lll11_opy_
  global bstack11ll11lll_opy_
  arg.append(bstack11l1l1l_opy_ (u"ࠨ࠭ࡘࠤ෣"))
  arg.append(bstack11l1l1l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡎࡱࡧࡹࡱ࡫ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡰࡴࡴࡸࡴࡦࡦ࠽ࡴࡾࡺࡥࡴࡶ࠱ࡔࡾࡺࡥࡴࡶ࡚ࡥࡷࡴࡩ࡯ࡩࠥ෤"))
  arg.append(bstack11l1l1l_opy_ (u"ࠣ࠯࡚ࠦ෥"))
  arg.append(bstack11l1l1l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡗ࡬ࡪࠦࡨࡰࡱ࡮࡭ࡲࡶ࡬ࠣ෦"))
  global bstack11l11l1ll1_opy_
  global bstack1lll1lllll_opy_
  global bstack11l1lll1ll_opy_
  global bstack1l1llll1l1_opy_
  global bstack111lll1ll_opy_
  global bstack1l1111l1ll_opy_
  global bstack11llll111l_opy_
  global bstack1lll1l111l_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack11l1l1l1l1_opy_
  global bstack1l1l1l111l_opy_
  global bstack1ll111ll11_opy_
  global bstack1l11llll11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11l11l1ll1_opy_ = webdriver.Remote.__init__
    bstack1lll1lllll_opy_ = WebDriver.quit
    bstack1lll1l111l_opy_ = WebDriver.close
    bstack1l1ll1l1l1_opy_ = WebDriver.get
    bstack11l1lll1ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1ll11l1111_opy_(CONFIG) and bstack1l11l111ll_opy_():
    if bstack1ll1l1111l_opy_() < version.parse(bstack1111111ll_opy_):
      logger.error(bstack1ll11ll11_opy_.format(bstack1ll1l1111l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack11l1l1l1l1_opy_ = RemoteConnection._1llllll111_opy_
      except Exception as e:
        logger.error(bstack1l11l11l1l_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l1l1l111l_opy_ = Config.getoption
    from _pytest import runner
    bstack1ll111ll11_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1111ll1l_opy_)
  try:
    from pytest_bdd import reporting
    bstack1l11llll11_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11l1l1l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫ෧"))
  bstack1ll1lll1l1_opy_ = CONFIG.get(bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ෨"), {}).get(bstack11l1l1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ෩"))
  bstack11ll11lll_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11ll1111l_opy_():
      bstack1l1llll11l_opy_.invoke(Events.CONNECT, bstack11l11lll1_opy_())
    platform_index = int(os.environ.get(bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭෪"), bstack11l1l1l_opy_ (u"ࠧ࠱ࠩ෫")))
  else:
    bstack11ll111ll_opy_(bstack1ll1l11ll1_opy_)
  os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩ෬")] = CONFIG[bstack11l1l1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ෭")]
  os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭෮")] = CONFIG[bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ෯")]
  os.environ[bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ෰")] = bstack1l111111l_opy_.__str__()
  from _pytest.config import main as bstack11l1l1l111_opy_
  bstack111111ll1_opy_ = []
  try:
    bstack111l1l111_opy_ = bstack11l1l1l111_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1l1l11111_opy_()
    if bstack11l1l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪ෱") in multiprocessing.current_process().__dict__.keys():
      for bstack1llll11ll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack111111ll1_opy_.append(bstack1llll11ll_opy_)
    try:
      bstack1l1ll11l11_opy_ = (bstack111111ll1_opy_, int(bstack111l1l111_opy_))
      bstack1lll1llll1_opy_.append(bstack1l1ll11l11_opy_)
    except:
      bstack1lll1llll1_opy_.append((bstack111111ll1_opy_, bstack111l1l111_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack111111ll1_opy_.append({bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬෲ"): bstack11l1l1l_opy_ (u"ࠨࡒࡵࡳࡨ࡫ࡳࡴࠢࠪෳ") + os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ෴")), bstack11l1l1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ෵"): traceback.format_exc(), bstack11l1l1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ෶"): int(os.environ.get(bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ෷")))})
    bstack1lll1llll1_opy_.append((bstack111111ll1_opy_, 1))
def bstack1l1l11ll1_opy_(arg):
  global bstack1ll11ll11l_opy_
  bstack11ll111ll_opy_(bstack1llll1lll_opy_)
  os.environ[bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ෸")] = str(bstack1ll1111ll1_opy_)
  from behave.__main__ import main as bstack11ll1lll11_opy_
  status_code = bstack11ll1lll11_opy_(arg)
  if status_code != 0:
    bstack1ll11ll11l_opy_ = status_code
def bstack1ll11l11ll_opy_():
  logger.info(bstack111ll11lll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭෹"), help=bstack11l1l1l_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡳࡳ࡬ࡩࡨࠩ෺"))
  parser.add_argument(bstack11l1l1l_opy_ (u"ࠩ࠰ࡹࠬ෻"), bstack11l1l1l_opy_ (u"ࠪ࠱࠲ࡻࡳࡦࡴࡱࡥࡲ࡫ࠧ෼"), help=bstack11l1l1l_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧࠪ෽"))
  parser.add_argument(bstack11l1l1l_opy_ (u"ࠬ࠳࡫ࠨ෾"), bstack11l1l1l_opy_ (u"࠭࠭࠮࡭ࡨࡽࠬ෿"), help=bstack11l1l1l_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠨ฀"))
  parser.add_argument(bstack11l1l1l_opy_ (u"ࠨ࠯ࡩࠫก"), bstack11l1l1l_opy_ (u"ࠩ࠰࠱࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧข"), help=bstack11l1l1l_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩฃ"))
  bstack111lll1111_opy_ = parser.parse_args()
  try:
    bstack1l1l111l11_opy_ = bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡴࡥࡳ࡫ࡦ࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨค")
    if bstack111lll1111_opy_.framework and bstack111lll1111_opy_.framework not in (bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬฅ"), bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧฆ")):
      bstack1l1l111l11_opy_ = bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ง")
    bstack11lllllll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1l111l11_opy_)
    bstack1ll1ll11ll_opy_ = open(bstack11lllllll_opy_, bstack11l1l1l_opy_ (u"ࠨࡴࠪจ"))
    bstack11llllll1_opy_ = bstack1ll1ll11ll_opy_.read()
    bstack1ll1ll11ll_opy_.close()
    if bstack111lll1111_opy_.username:
      bstack11llllll1_opy_ = bstack11llllll1_opy_.replace(bstack11l1l1l_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩฉ"), bstack111lll1111_opy_.username)
    if bstack111lll1111_opy_.key:
      bstack11llllll1_opy_ = bstack11llllll1_opy_.replace(bstack11l1l1l_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬช"), bstack111lll1111_opy_.key)
    if bstack111lll1111_opy_.framework:
      bstack11llllll1_opy_ = bstack11llllll1_opy_.replace(bstack11l1l1l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬซ"), bstack111lll1111_opy_.framework)
    file_name = bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨฌ")
    file_path = os.path.abspath(file_name)
    bstack11lllll11_opy_ = open(file_path, bstack11l1l1l_opy_ (u"࠭ࡷࠨญ"))
    bstack11lllll11_opy_.write(bstack11llllll1_opy_)
    bstack11lllll11_opy_.close()
    logger.info(bstack11lll1ll1l_opy_)
    try:
      os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩฎ")] = bstack111lll1111_opy_.framework if bstack111lll1111_opy_.framework != None else bstack11l1l1l_opy_ (u"ࠣࠤฏ")
      config = yaml.safe_load(bstack11llllll1_opy_)
      config[bstack11l1l1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩฐ")] = bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡷࡪࡺࡵࡱࠩฑ")
      bstack11111llll_opy_(bstack11l111ll1l_opy_, config)
    except Exception as e:
      logger.debug(bstack11ll1llll1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll11llll_opy_.format(str(e)))
def bstack11111llll_opy_(bstack11111l11l_opy_, config, bstack1l1111ll1_opy_={}):
  global bstack1l111111l_opy_
  global bstack1lll1lll11_opy_
  global bstack11111l11_opy_
  if not config:
    return
  bstack11llll11l1_opy_ = bstack11ll111l1_opy_ if not bstack1l111111l_opy_ else (
    bstack111ll1lll_opy_ if bstack11l1l1l_opy_ (u"ࠫࡦࡶࡰࠨฒ") in config else (
        bstack1l1l1111ll_opy_ if config.get(bstack11l1l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩณ")) else bstack1l1l1lll1_opy_
    )
)
  bstack111lll1l1_opy_ = False
  bstack1l1l11l1l1_opy_ = False
  if bstack1l111111l_opy_ is True:
      if bstack11l1l1l_opy_ (u"࠭ࡡࡱࡲࠪด") in config:
          bstack111lll1l1_opy_ = True
      else:
          bstack1l1l11l1l1_opy_ = True
  bstack1lll11l11_opy_ = bstack11l1111l1_opy_.bstack1l11l1111_opy_(config, bstack1lll1lll11_opy_)
  bstack1l1l11l111_opy_ = bstack1ll11ll1l_opy_()
  data = {
    bstack11l1l1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩต"): config[bstack11l1l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪถ")],
    bstack11l1l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬท"): config[bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ธ")],
    bstack11l1l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨน"): bstack11111l11l_opy_,
    bstack11l1l1l_opy_ (u"ࠬࡪࡥࡵࡧࡦࡸࡪࡪࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩบ"): os.environ.get(bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨป"), bstack1lll1lll11_opy_),
    bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩผ"): bstack1l1111111_opy_,
    bstack11l1l1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮ࠪฝ"): bstack11l111l1ll_opy_(),
    bstack11l1l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬพ"): {
      bstack11l1l1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨฟ"): str(config[bstack11l1l1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫภ")]) if bstack11l1l1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬม") in config else bstack11l1l1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢย"),
      bstack11l1l1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡘࡨࡶࡸ࡯࡯࡯ࠩร"): sys.version,
      bstack11l1l1l_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪฤ"): bstack111ll11111_opy_(os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫล"), bstack1lll1lll11_opy_)),
      bstack11l1l1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬฦ"): bstack11l1l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫว"),
      bstack11l1l1l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ศ"): bstack11llll11l1_opy_,
      bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫษ"): bstack1lll11l11_opy_,
      bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩ࠭ส"): os.environ[bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ห")],
      bstack11l1l1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬฬ"): os.environ.get(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬอ"), bstack1lll1lll11_opy_),
      bstack11l1l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧฮ"): bstack11llll1lll_opy_(os.environ.get(bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧฯ"), bstack1lll1lll11_opy_)),
      bstack11l1l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬะ"): bstack1l1l11l111_opy_.get(bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬั")),
      bstack11l1l1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧา"): bstack1l1l11l111_opy_.get(bstack11l1l1l_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪำ")),
      bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ิ"): config[bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧี")] if config[bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨึ")] else bstack11l1l1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢื"),
      bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳุࠩ"): str(config[bstack11l1l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴูࠪ")]) if bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵฺࠫ") in config else bstack11l1l1l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ฻"),
      bstack11l1l1l_opy_ (u"ࠫࡴࡹࠧ฼"): sys.platform,
      bstack11l1l1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ฽"): socket.gethostname(),
      bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ฾"): bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ฿"))
    }
  }
  if not bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨเ")) is None:
    data[bstack11l1l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬแ")][bstack11l1l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡒ࡫ࡴࡢࡦࡤࡸࡦ࠭โ")] = {
      bstack11l1l1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫใ"): bstack11l1l1l_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪไ"),
      bstack11l1l1l_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭ๅ"): bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧๆ")),
      bstack11l1l1l_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࡏࡷࡰࡦࡪࡸࠧ็"): bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳ่ࠬ"))
    }
  if bstack11111l11l_opy_ == bstack11lll1ll11_opy_:
    data[bstack11l1l1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ้࠭")][bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨ๊ࠩ")] = bstack1ll1l1ll1_opy_(config)
    data[bstack11l1l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ๋")][bstack11l1l1l_opy_ (u"࠭ࡩࡴࡒࡨࡶࡨࡿࡁࡶࡶࡲࡉࡳࡧࡢ࡭ࡧࡧࠫ์")] = percy.bstack1l1llll1l_opy_
    data[bstack11l1l1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪํ")][bstack11l1l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࡂࡶ࡫࡯ࡨࡎࡪࠧ๎")] = percy.percy_build_id
  update(data[bstack11l1l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ๏")], bstack1l1111ll1_opy_)
  try:
    response = bstack1l11llll1l_opy_(bstack11l1l1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ๐"), bstack1lll111l1l_opy_(bstack11l1111l1l_opy_), data, {
      bstack11l1l1l_opy_ (u"ࠫࡦࡻࡴࡩࠩ๑"): (config[bstack11l1l1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ๒")], config[bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ๓")])
    })
    if response:
      logger.debug(bstack111ll1111_opy_.format(bstack11111l11l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11llllllll_opy_.format(str(e)))
def bstack111ll11111_opy_(framework):
  return bstack11l1l1l_opy_ (u"ࠢࡼࡿ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦ๔").format(str(framework), __version__) if framework else bstack11l1l1l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࡻࡾࠤ๕").format(
    __version__)
def bstack1l1l11l1ll_opy_():
  global CONFIG
  global bstack1l11l1111l_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l1l1l1111_opy_()
    logger.debug(bstack111ll1ll1l_opy_.format(str(CONFIG)))
    bstack1l11l1111l_opy_ = bstack111111l1l_opy_.bstack11ll111lll_opy_(CONFIG, bstack1l11l1111l_opy_)
    bstack111l1llll1_opy_()
  except Exception as e:
    logger.error(bstack11l1l1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨ๖") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11ll111l11_opy_
  atexit.register(bstack1l1l1ll111_opy_)
  signal.signal(signal.SIGINT, bstack11ll1l1l11_opy_)
  signal.signal(signal.SIGTERM, bstack11ll1l1l11_opy_)
def bstack11ll111l11_opy_(exctype, value, traceback):
  global bstack11ll1ll1l_opy_
  try:
    for driver in bstack11ll1ll1l_opy_:
      bstack11ll11l1ll_opy_(driver, bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๗"), bstack11l1l1l_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢ๘") + str(value))
  except Exception:
    pass
  logger.info(bstack1lll111lll_opy_)
  bstack1l1l1l1l1l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l1l1l1l1l_opy_(message=bstack11l1l1l_opy_ (u"ࠬ࠭๙"), bstack111lll1l1l_opy_ = False):
  global CONFIG
  bstack1ll1111111_opy_ = bstack11l1l1l_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠨ๚") if bstack111lll1l1l_opy_ else bstack11l1l1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭๛")
  try:
    if message:
      bstack1l1111ll1_opy_ = {
        bstack1ll1111111_opy_ : str(message)
      }
      bstack11111llll_opy_(bstack11lll1ll11_opy_, CONFIG, bstack1l1111ll1_opy_)
    else:
      bstack11111llll_opy_(bstack11lll1ll11_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l111l1ll1_opy_.format(str(e)))
def bstack1l11111ll_opy_(bstack1111ll1ll_opy_, size):
  bstack11l11ll11_opy_ = []
  while len(bstack1111ll1ll_opy_) > size:
    bstack111ll111l_opy_ = bstack1111ll1ll_opy_[:size]
    bstack11l11ll11_opy_.append(bstack111ll111l_opy_)
    bstack1111ll1ll_opy_ = bstack1111ll1ll_opy_[size:]
  bstack11l11ll11_opy_.append(bstack1111ll1ll_opy_)
  return bstack11l11ll11_opy_
def bstack11ll11l11_opy_(args):
  if bstack11l1l1l_opy_ (u"ࠨ࠯ࡰࠫ๜") in args and bstack11l1l1l_opy_ (u"ࠩࡳࡨࡧ࠭๝") in args:
    return True
  return False
def run_on_browserstack(bstack1111llll1_opy_=None, bstack1lll1llll1_opy_=None, bstack1l11l1ll11_opy_=False):
  global CONFIG
  global bstack11l11111l_opy_
  global bstack1ll1111ll1_opy_
  global bstack1lll1lll11_opy_
  global bstack11111l11_opy_
  bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠪࠫ๞")
  bstack1l111l11ll_opy_(bstack11l1111ll_opy_, logger)
  if bstack1111llll1_opy_ and isinstance(bstack1111llll1_opy_, str):
    bstack1111llll1_opy_ = eval(bstack1111llll1_opy_)
  if bstack1111llll1_opy_:
    CONFIG = bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫ๟")]
    bstack11l11111l_opy_ = bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭๠")]
    bstack1ll1111ll1_opy_ = bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ๡")]
    bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ๢"), bstack1ll1111ll1_opy_)
    bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ๣")
  bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ๤"), uuid4().__str__())
  logger.info(bstack11l1l1l_opy_ (u"ࠪࡗࡉࡑࠠࡳࡷࡱࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࠨ๥") + bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭๦")));
  logger.debug(bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪ࠽ࠨ๧") + bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ๨")))
  if not bstack1l11l1ll11_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1ll1l11lll_opy_)
      return
    if sys.argv[1] == bstack11l1l1l_opy_ (u"ࠧ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪ๩") or sys.argv[1] == bstack11l1l1l_opy_ (u"ࠨ࠯ࡹࠫ๪"):
      logger.info(bstack11l1l1l_opy_ (u"ࠩࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡒࡼࡸ࡭ࡵ࡮ࠡࡕࡇࡏࠥࡼࡻࡾࠩ๫").format(__version__))
      return
    if sys.argv[1] == bstack11l1l1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ๬"):
      bstack1ll11l11ll_opy_()
      return
  args = sys.argv
  bstack1l1l11l1ll_opy_()
  global bstack1l1l11ll11_opy_
  global bstack1ll1ll111l_opy_
  global bstack11ll11lll_opy_
  global bstack1ll111111l_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1ll1lll1l1_opy_
  global bstack1lll1l1ll_opy_
  global bstack11l1ll11ll_opy_
  global bstack1ll111l11l_opy_
  global bstack1ll11lll11_opy_
  global bstack1lllll111_opy_
  bstack1ll1ll111l_opy_ = len(CONFIG.get(bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ๭"), []))
  if not bstack1llll11l1_opy_:
    if args[1] == bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ๮") or args[1] == bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ๯"):
      bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ๰")
      args = args[2:]
    elif args[1] == bstack11l1l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ๱"):
      bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ๲")
      args = args[2:]
    elif args[1] == bstack11l1l1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ๳"):
      bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ๴")
      args = args[2:]
    elif args[1] == bstack11l1l1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭๵"):
      bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ๶")
      args = args[2:]
    elif args[1] == bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ๷"):
      bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ๸")
      args = args[2:]
    elif args[1] == bstack11l1l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ๹"):
      bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ๺")
      args = args[2:]
    else:
      if not bstack11l1l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ๻") in CONFIG or str(CONFIG[bstack11l1l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ๼")]).lower() in [bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭๽"), bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨ๾")]:
        bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ๿")
        args = args[1:]
      elif str(CONFIG[bstack11l1l1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ຀")]).lower() == bstack11l1l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩກ"):
        bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪຂ")
        args = args[1:]
      elif str(CONFIG[bstack11l1l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ຃")]).lower() == bstack11l1l1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬຄ"):
        bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭຅")
        args = args[1:]
      elif str(CONFIG[bstack11l1l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫຆ")]).lower() == bstack11l1l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩງ"):
        bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪຈ")
        args = args[1:]
      elif str(CONFIG[bstack11l1l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧຉ")]).lower() == bstack11l1l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬຊ"):
        bstack1llll11l1_opy_ = bstack11l1l1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭຋")
        args = args[1:]
      else:
        os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩຌ")] = bstack1llll11l1_opy_
        bstack1l11ll111l_opy_(bstack11ll1l1ll_opy_)
  os.environ[bstack11l1l1l_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩຍ")] = bstack1llll11l1_opy_
  bstack1lll1lll11_opy_ = bstack1llll11l1_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack11l11111ll_opy_ = bstack1lll11111l_opy_[bstack11l1l1l_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕ࠯ࡅࡈࡉ࠭ຎ")] if bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪຏ") and bstack11l1ll111l_opy_() else bstack1llll11l1_opy_
      bstack1l1llll11l_opy_.invoke(Events.bstack1lll1l11l_opy_, bstack11ll1l1lll_opy_(
        sdk_version=__version__,
        path_config=bstack1l1ll11l1l_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack11l11111ll_opy_,
        frameworks=[bstack11l11111ll_opy_],
        framework_versions={
          bstack11l11111ll_opy_: bstack11llll1lll_opy_(bstack11l1l1l_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪຐ") if bstack1llll11l1_opy_ in [bstack11l1l1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫຑ"), bstack11l1l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬຒ"), bstack11l1l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨຓ")] else bstack1llll11l1_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥດ"), None):
        CONFIG[bstack11l1l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦຕ")] = cli.config.get(bstack11l1l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧຖ"), None)
    except Exception as e:
      bstack1l1llll11l_opy_.invoke(Events.bstack1ll1lll11_opy_, e.__traceback__, 1)
    if bstack1ll1111ll1_opy_:
      CONFIG[bstack11l1l1l_opy_ (u"ࠦࡦࡶࡰࠣທ")] = cli.config[bstack11l1l1l_opy_ (u"ࠧࡧࡰࡱࠤຘ")]
      logger.info(bstack11l1l11l1_opy_.format(CONFIG[bstack11l1l1l_opy_ (u"࠭ࡡࡱࡲࠪນ")]))
  else:
    bstack1l1llll11l_opy_.clear()
  global bstack1l1lll111_opy_
  global bstack111ll11ll1_opy_
  if bstack1111llll1_opy_:
    try:
      bstack1l1lll1l1l_opy_ = datetime.datetime.now()
      os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩບ")] = bstack1llll11l1_opy_
      bstack11111llll_opy_(bstack1lll1lll1_opy_, CONFIG)
      cli.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠣࡪࡷࡸࡵࡀࡳࡥ࡭ࡢࡸࡪࡹࡴࡠࡣࡷࡸࡪࡳࡰࡵࡧࡧࠦປ"), datetime.datetime.now() - bstack1l1lll1l1l_opy_)
    except Exception as e:
      logger.debug(bstack11l1l1lll1_opy_.format(str(e)))
  global bstack11l11l1ll1_opy_
  global bstack1lll1lllll_opy_
  global bstack1ll1lll11l_opy_
  global bstack1lll1ll111_opy_
  global bstack11l11ll11l_opy_
  global bstack111ll1111l_opy_
  global bstack1l1llll1l1_opy_
  global bstack111lll1ll_opy_
  global bstack111lllll1l_opy_
  global bstack1l1111l1ll_opy_
  global bstack11llll111l_opy_
  global bstack1lll1l111l_opy_
  global bstack11l11ll1ll_opy_
  global bstack1ll1111lll_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack11l1l1l1l1_opy_
  global bstack1l1l1l111l_opy_
  global bstack1ll111ll11_opy_
  global bstack11lll1l1l1_opy_
  global bstack1l11llll11_opy_
  global bstack11l1lll1ll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11l11l1ll1_opy_ = webdriver.Remote.__init__
    bstack1lll1lllll_opy_ = WebDriver.quit
    bstack1lll1l111l_opy_ = WebDriver.close
    bstack1l1ll1l1l1_opy_ = WebDriver.get
    bstack11l1lll1ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l1lll111_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack111l11lll_opy_
    bstack111ll11ll1_opy_ = bstack111l11lll_opy_()
  except Exception as e:
    pass
  try:
    global bstack1llll1l11l_opy_
    from QWeb.keywords import browser
    bstack1llll1l11l_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1ll11l1111_opy_(CONFIG) and bstack1l11l111ll_opy_():
    if bstack1ll1l1111l_opy_() < version.parse(bstack1111111ll_opy_):
      logger.error(bstack1ll11ll11_opy_.format(bstack1ll1l1111l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack11l1l1l1l1_opy_ = RemoteConnection._1llllll111_opy_
      except Exception as e:
        logger.error(bstack1l11l11l1l_opy_.format(str(e)))
  if not CONFIG.get(bstack11l1l1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫຜ"), False) and not bstack1111llll1_opy_:
    logger.info(bstack111111111_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11l1l1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧຝ") in CONFIG and str(CONFIG[bstack11l1l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨພ")]).lower() != bstack11l1l1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫຟ"):
      bstack1ll1ll11l_opy_()
    elif bstack1llll11l1_opy_ != bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ຠ") or (bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧມ") and not bstack1111llll1_opy_):
      bstack11l1l1ll11_opy_()
  if (bstack1llll11l1_opy_ in [bstack11l1l1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧຢ"), bstack11l1l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨຣ"), bstack11l1l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ຤")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1ll1l1lll1_opy_
        bstack111ll1111l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack111l1lll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11l11ll11l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1l11l11ll_opy_ + str(e))
    except Exception as e:
      bstack1ll11l1l11_opy_(e, bstack111l1lll1_opy_)
    if bstack1llll11l1_opy_ != bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬລ"):
      bstack1l111lll1_opy_()
    bstack1ll1lll11l_opy_ = Output.start_test
    bstack1lll1ll111_opy_ = Output.end_test
    bstack1l1llll1l1_opy_ = TestStatus.__init__
    bstack111lllll1l_opy_ = pabot._run
    bstack1l1111l1ll_opy_ = QueueItem.__init__
    bstack11llll111l_opy_ = pabot._create_command_for_execution
    bstack11lll1l1l1_opy_ = pabot._report_results
  if bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ຦"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll11l1l11_opy_(e, bstack1l1l1llll1_opy_)
    bstack11l11ll1ll_opy_ = Runner.run_hook
    bstack1ll1111lll_opy_ = Step.run
  if bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ວ"):
    try:
      from _pytest.config import Config
      bstack1l1l1l111l_opy_ = Config.getoption
      from _pytest import runner
      bstack1ll111ll11_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1111ll1l_opy_)
    try:
      from pytest_bdd import reporting
      bstack1l11llll11_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11l1l1l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨຨ"))
  try:
    framework_name = bstack11l1l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧຩ") if bstack1llll11l1_opy_ in [bstack11l1l1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨສ"), bstack11l1l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩຫ"), bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬຬ")] else bstack1lllll1l1_opy_(bstack1llll11l1_opy_)
    bstack1ll1llll1_opy_ = {
      bstack11l1l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭ອ"): bstack11l1l1l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨຮ") if bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧຯ") and bstack11l1ll111l_opy_() else framework_name,
      bstack11l1l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬະ"): bstack11llll1lll_opy_(framework_name),
      bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧັ"): __version__,
      bstack11l1l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫາ"): bstack1llll11l1_opy_
    }
    if bstack1llll11l1_opy_ in bstack11l1l11lll_opy_:
      if bstack1l111111l_opy_ and bstack11l1l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫຳ") in CONFIG and CONFIG[bstack11l1l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬິ")] == True:
        if bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ີ") in CONFIG:
          os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨຶ")] = os.getenv(bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩື"), json.dumps(CONFIG[bstack11l1l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴຸࠩ")]))
          CONFIG[bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵູࠪ")].pop(bstack11l1l1l_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦ຺ࠩ"), None)
          CONFIG[bstack11l1l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬົ")].pop(bstack11l1l1l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫຼ"), None)
        bstack1ll1llll1_opy_[bstack11l1l1l_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧຽ")] = {
          bstack11l1l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭຾"): bstack11l1l1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ຿"),
          bstack11l1l1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫເ"): str(bstack1ll1l1111l_opy_())
        }
    if bstack1llll11l1_opy_ not in [bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬແ")] and not cli.is_running():
      bstack1l1lll111l_opy_ = bstack1l11l1ll_opy_.launch(CONFIG, bstack1ll1llll1_opy_)
  except Exception as e:
    logger.debug(bstack1l1l1l11l_opy_.format(bstack11l1l1l_opy_ (u"࡚ࠬࡥࡴࡶࡋࡹࡧ࠭ໂ"), str(e)))
  if bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ໃ"):
    bstack11ll11lll_opy_ = True
    if bstack1111llll1_opy_ and bstack1l11l1ll11_opy_:
      bstack1ll1lll1l1_opy_ = CONFIG.get(bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫໄ"), {}).get(bstack11l1l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໅"))
      bstack11ll111ll_opy_(bstack1ll11lll1l_opy_)
    elif bstack1111llll1_opy_:
      bstack1ll1lll1l1_opy_ = CONFIG.get(bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ໆ"), {}).get(bstack11l1l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ໇"))
      global bstack11ll1ll1l_opy_
      try:
        if bstack11ll11l11_opy_(bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫່ࠧ")]) and multiprocessing.current_process().name == bstack11l1l1l_opy_ (u"ࠬ࠶້ࠧ"):
          bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦ໊ࠩ")].remove(bstack11l1l1l_opy_ (u"ࠧ࠮࡯໋ࠪ"))
          bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ໌")].remove(bstack11l1l1l_opy_ (u"ࠩࡳࡨࡧ࠭ໍ"))
          bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭໎")] = bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ໏")][0]
          with open(bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ໐")], bstack11l1l1l_opy_ (u"࠭ࡲࠨ໑")) as f:
            file_content = f.read()
          bstack1ll1l111ll_opy_ = bstack11l1l1l_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡸࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡧࡠࡦࡥࠬࡸ࡫࡬ࡧ࠮ࡤࡶ࡬࠲ࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥ໒").format(str(bstack1111llll1_opy_))
          bstack111ll1l1ll_opy_ = bstack1ll1l111ll_opy_ + file_content
          bstack1ll1l1l1l_opy_ = bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ໓")] + bstack11l1l1l_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫ໔")
          with open(bstack1ll1l1l1l_opy_, bstack11l1l1l_opy_ (u"ࠪࡻࠬ໕")):
            pass
          with open(bstack1ll1l1l1l_opy_, bstack11l1l1l_opy_ (u"ࠦࡼ࠱ࠢ໖")) as f:
            f.write(bstack111ll1l1ll_opy_)
          import subprocess
          process_data = subprocess.run([bstack11l1l1l_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧ໗"), bstack1ll1l1l1l_opy_])
          if os.path.exists(bstack1ll1l1l1l_opy_):
            os.unlink(bstack1ll1l1l1l_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11ll11l11_opy_(bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ໘")]):
            bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ໙")].remove(bstack11l1l1l_opy_ (u"ࠨ࠯ࡰࠫ໚"))
            bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ໛")].remove(bstack11l1l1l_opy_ (u"ࠪࡴࡩࡨࠧໜ"))
            bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧໝ")] = bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨໞ")][0]
          bstack11ll111ll_opy_(bstack1ll11lll1l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩໟ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11l1l1l_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩ໠")] = bstack11l1l1l_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ໡")
          mod_globals[bstack11l1l1l_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ໢")] = os.path.abspath(bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭໣")])
          exec(open(bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ໤")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11l1l1l_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬ໥").format(str(e)))
          for driver in bstack11ll1ll1l_opy_:
            bstack1lll1llll1_opy_.append({
              bstack11l1l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ໦"): bstack1111llll1_opy_[bstack11l1l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ໧")],
              bstack11l1l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ໨"): str(e),
              bstack11l1l1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ໩"): multiprocessing.current_process().name
            })
            bstack11ll11l1ll_opy_(driver, bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ໪"), bstack11l1l1l_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢ໫") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11ll1ll1l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1ll1111ll1_opy_, CONFIG, logger)
      bstack1l1ll1ll1l_opy_()
      bstack1lllll11ll_opy_()
      bstack11111ll1_opy_ = {
        bstack11l1l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ໬"): args[0],
        bstack11l1l1l_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭໭"): CONFIG,
        bstack11l1l1l_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ໮"): bstack11l11111l_opy_,
        bstack11l1l1l_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ໯"): bstack1ll1111ll1_opy_
      }
      percy.bstack11l1111lll_opy_()
      if bstack11l1l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ໰") in CONFIG:
        bstack111l1ll1_opy_ = []
        manager = multiprocessing.Manager()
        bstack111l111l_opy_ = manager.list()
        if bstack11ll11l11_opy_(args):
          for index, platform in enumerate(CONFIG[bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭໱")]):
            if index == 0:
              bstack11111ll1_opy_[bstack11l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ໲")] = args
            bstack111l1ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack11111ll1_opy_, bstack111l111l_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ໳")]):
            bstack111l1ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack11111ll1_opy_, bstack111l111l_opy_)))
        for t in bstack111l1ll1_opy_:
          t.start()
        for t in bstack111l1ll1_opy_:
          t.join()
        bstack11l1ll11ll_opy_ = list(bstack111l111l_opy_)
      else:
        if bstack11ll11l11_opy_(args):
          bstack11111ll1_opy_[bstack11l1l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ໴")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack11111ll1_opy_,))
          test.start()
          test.join()
        else:
          bstack11ll111ll_opy_(bstack1ll11lll1l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11l1l1l_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩ໵")] = bstack11l1l1l_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ໶")
          mod_globals[bstack11l1l1l_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ໷")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ໸") or bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ໹"):
    percy.init(bstack1ll1111ll1_opy_, CONFIG, logger)
    percy.bstack11l1111lll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1ll11l1l11_opy_(e, bstack111l1lll1_opy_)
    bstack1l1ll1ll1l_opy_()
    bstack11ll111ll_opy_(bstack1l111lll1l_opy_)
    if bstack1l111111l_opy_:
      bstack1ll11111l_opy_(bstack1l111lll1l_opy_, args)
      if bstack11l1l1l_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ໺") in args:
        i = args.index(bstack11l1l1l_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ໻"))
        args.pop(i)
        args.pop(i)
      if bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ໼") not in CONFIG:
        CONFIG[bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ໽")] = [{}]
        bstack1ll1ll111l_opy_ = 1
      if bstack1l1l11ll11_opy_ == 0:
        bstack1l1l11ll11_opy_ = 1
      args.insert(0, str(bstack1l1l11ll11_opy_))
      args.insert(0, str(bstack11l1l1l_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ໾")))
    if bstack1l11l1ll_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1l1l1lllll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack111llll11l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11l1l1l_opy_ (u"ࠥࡖࡔࡈࡏࡕࡡࡒࡔ࡙ࡏࡏࡏࡕࠥ໿"),
        ).parse_args(bstack1l1l1lllll_opy_)
        bstack11l1l111l_opy_ = args.index(bstack1l1l1lllll_opy_[0]) if len(bstack1l1l1lllll_opy_) > 0 else len(args)
        args.insert(bstack11l1l111l_opy_, str(bstack11l1l1l_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨༀ")))
        args.insert(bstack11l1l111l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡸ࡯ࡣࡱࡷࡣࡱ࡯ࡳࡵࡧࡱࡩࡷ࠴ࡰࡺࠩ༁"))))
        if bstack1l1llllll1_opy_(os.environ.get(bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫ༂"))) and str(os.environ.get(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫ༃"), bstack11l1l1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭༄"))) != bstack11l1l1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ༅"):
          for bstack1l11l1l1l_opy_ in bstack111llll11l_opy_:
            args.remove(bstack1l11l1l1l_opy_)
          bstack1l1l1l111_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧ༆")).split(bstack11l1l1l_opy_ (u"ࠫ࠱࠭༇"))
          for bstack111lllll1_opy_ in bstack1l1l1l111_opy_:
            args.append(bstack111lllll1_opy_)
      except Exception as e:
        logger.error(bstack11l1l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࠣ༈").format(e))
    pabot.main(args)
  elif bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ༉"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1ll11l1l11_opy_(e, bstack111l1lll1_opy_)
    for a in args:
      if bstack11l1l1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭༊") in a:
        bstack1ll1l1l11l_opy_ = int(a.split(bstack11l1l1l_opy_ (u"ࠨ࠼ࠪ་"))[1])
      if bstack11l1l1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭༌") in a:
        bstack1ll1lll1l1_opy_ = str(a.split(bstack11l1l1l_opy_ (u"ࠪ࠾ࠬ།"))[1])
      if bstack11l1l1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫ༎") in a:
        bstack1lll1l1ll_opy_ = str(a.split(bstack11l1l1l_opy_ (u"ࠬࡀࠧ༏"))[1])
    bstack1ll11l1lll_opy_ = None
    if bstack11l1l1l_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬ༐") in args:
      i = args.index(bstack11l1l1l_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭༑"))
      args.pop(i)
      bstack1ll11l1lll_opy_ = args.pop(i)
    if bstack1ll11l1lll_opy_ is not None:
      global bstack1ll11ll111_opy_
      bstack1ll11ll111_opy_ = bstack1ll11l1lll_opy_
    bstack11ll111ll_opy_(bstack1l111lll1l_opy_)
    run_cli(args)
    if bstack11l1l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬ༒") in multiprocessing.current_process().__dict__.keys():
      for bstack1llll11ll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1lll1llll1_opy_.append(bstack1llll11ll_opy_)
  elif bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༓"):
    bstack1l1ll111l1_opy_ = bstack111lll1l_opy_(args, logger, CONFIG, bstack1l111111l_opy_)
    bstack1l1ll111l1_opy_.bstack111l1l11_opy_()
    bstack1l1ll1ll1l_opy_()
    bstack1ll111111l_opy_ = True
    bstack1ll11lll11_opy_ = bstack1l1ll111l1_opy_.bstack111ll11l_opy_()
    bstack1l1ll111l1_opy_.bstack11111ll1_opy_(bstack11lll11lll_opy_)
    bstack1l1l11l11_opy_ = bstack1l1ll111l1_opy_.bstack11111lll_opy_(bstack11l111lll_opy_, {
      bstack11l1l1l_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ༔"): bstack11l11111l_opy_,
      bstack11l1l1l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭༕"): bstack1ll1111ll1_opy_,
      bstack11l1l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ༖"): bstack1l111111l_opy_
    })
    try:
      bstack111111ll1_opy_, bstack1111l1l1l_opy_ = map(list, zip(*bstack1l1l11l11_opy_))
      bstack1ll111l11l_opy_ = bstack111111ll1_opy_[0]
      for status_code in bstack1111l1l1l_opy_:
        if status_code != 0:
          bstack1lllll111_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11l1l1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡢࡰࡧࠤࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠰ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠺ࠡࡽࢀࠦ༗").format(str(e)))
  elif bstack1llll11l1_opy_ == bstack11l1l1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫༘ࠧ"):
    try:
      from behave.__main__ import main as bstack11ll1lll11_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1ll11l1l11_opy_(e, bstack1l1l1llll1_opy_)
    bstack1l1ll1ll1l_opy_()
    bstack1ll111111l_opy_ = True
    bstack1111l111_opy_ = 1
    if bstack11l1l1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ༙") in CONFIG:
      bstack1111l111_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ༚")]
    if bstack11l1l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭༛") in CONFIG:
      bstack11ll11l1l_opy_ = int(bstack1111l111_opy_) * int(len(CONFIG[bstack11l1l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ༜")]))
    else:
      bstack11ll11l1l_opy_ = int(bstack1111l111_opy_)
    config = Configuration(args)
    bstack1l11111lll_opy_ = config.paths
    if len(bstack1l11111lll_opy_) == 0:
      import glob
      pattern = bstack11l1l1l_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫ༝")
      bstack111l1l1ll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack111l1l1ll_opy_)
      config = Configuration(args)
      bstack1l11111lll_opy_ = config.paths
    bstack11l11ll1_opy_ = [os.path.normpath(item) for item in bstack1l11111lll_opy_]
    bstack111l1111l_opy_ = [os.path.normpath(item) for item in args]
    bstack1l11llll1_opy_ = [item for item in bstack111l1111l_opy_ if item not in bstack11l11ll1_opy_]
    import platform as pf
    if pf.system().lower() == bstack11l1l1l_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧ༞"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11l11ll1_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1ll1ll1lll_opy_)))
                    for bstack1ll1ll1lll_opy_ in bstack11l11ll1_opy_]
    bstack11111l1l_opy_ = []
    for spec in bstack11l11ll1_opy_:
      bstack111ll111_opy_ = []
      bstack111ll111_opy_ += bstack1l11llll1_opy_
      bstack111ll111_opy_.append(spec)
      bstack11111l1l_opy_.append(bstack111ll111_opy_)
    execution_items = []
    for bstack111ll111_opy_ in bstack11111l1l_opy_:
      if bstack11l1l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ༟") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11l1l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ༠")]):
          item = {}
          item[bstack11l1l1l_opy_ (u"ࠩࡤࡶ࡬࠭༡")] = bstack11l1l1l_opy_ (u"ࠪࠤࠬ༢").join(bstack111ll111_opy_)
          item[bstack11l1l1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ༣")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11l1l1l_opy_ (u"ࠬࡧࡲࡨࠩ༤")] = bstack11l1l1l_opy_ (u"࠭ࠠࠨ༥").join(bstack111ll111_opy_)
        item[bstack11l1l1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭༦")] = 0
        execution_items.append(item)
    bstack111l1lll11_opy_ = bstack1l11111ll_opy_(execution_items, bstack11ll11l1l_opy_)
    for execution_item in bstack111l1lll11_opy_:
      bstack111l1ll1_opy_ = []
      for item in execution_item:
        bstack111l1ll1_opy_.append(bstack1ll111l11_opy_(name=str(item[bstack11l1l1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ༧")]),
                                             target=bstack1l1l11ll1_opy_,
                                             args=(item[bstack11l1l1l_opy_ (u"ࠩࡤࡶ࡬࠭༨")],)))
      for t in bstack111l1ll1_opy_:
        t.start()
      for t in bstack111l1ll1_opy_:
        t.join()
  else:
    bstack1l11ll111l_opy_(bstack11ll1l1ll_opy_)
  if not bstack1111llll1_opy_:
    bstack1ll111ll1_opy_()
    if(bstack1llll11l1_opy_ in [bstack11l1l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ༩"), bstack11l1l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༪")]):
      bstack11lll1111_opy_()
  bstack111111l1l_opy_.bstack1l111ll1ll_opy_()
def browserstack_initialize(bstack111ll1l111_opy_=None):
  logger.info(bstack11l1l1l_opy_ (u"ࠬࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡻ࡮ࡺࡨࠡࡣࡵ࡫ࡸࡀࠠࠨ༫") + str(bstack111ll1l111_opy_))
  run_on_browserstack(bstack111ll1l111_opy_, None, True)
@measure(event_name=EVENTS.bstack1lll1l1ll1_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1ll111ll1_opy_():
  global CONFIG
  global bstack1lll1lll11_opy_
  global bstack1lllll111_opy_
  global bstack1ll11ll11l_opy_
  global bstack11111l11_opy_
  if cli.is_running():
    bstack1l1llll11l_opy_.invoke(Events.bstack11l1ll1ll1_opy_)
  if bstack1lll1lll11_opy_ == bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༬"):
    if not cli.is_enabled(CONFIG):
      bstack1l11l1ll_opy_.stop()
  else:
    bstack1l11l1ll_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l1ll11l_opy_.bstack11l11l11ll_opy_()
  if bstack11l1l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ༭") in CONFIG and str(CONFIG[bstack11l1l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ༮")]).lower() != bstack11l1l1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ༯"):
    bstack1ll1l1llll_opy_, bstack1lllll1l1l_opy_ = bstack1l11lll1l_opy_()
  else:
    bstack1ll1l1llll_opy_, bstack1lllll1l1l_opy_ = get_build_link()
  bstack1ll111l1l_opy_(bstack1ll1l1llll_opy_)
  logger.info(bstack11l1l1l_opy_ (u"ࠪࡗࡉࡑࠠࡳࡷࡱࠤࡪࡴࡤࡦࡦࠣࡪࡴࡸࠠࡪࡦ࠽ࠫ༰") + bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭༱"), bstack11l1l1l_opy_ (u"ࠬ࠭༲")) + bstack11l1l1l_opy_ (u"࠭ࠬࠡࡶࡨࡷࡹ࡮ࡵࡣࠢ࡬ࡨ࠿ࠦࠧ༳") + os.getenv(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ༴"), bstack11l1l1l_opy_ (u"ࠨ༵ࠩ")))
  if bstack1ll1l1llll_opy_ is not None and bstack111llll1ll_opy_() != -1:
    sessions = bstack1llll11111_opy_(bstack1ll1l1llll_opy_)
    bstack1l11l11l11_opy_(sessions, bstack1lllll1l1l_opy_)
  if bstack1lll1lll11_opy_ == bstack11l1l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༶") and bstack1lllll111_opy_ != 0:
    sys.exit(bstack1lllll111_opy_)
  if bstack1lll1lll11_opy_ == bstack11l1l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧ༷ࠪ") and bstack1ll11ll11l_opy_ != 0:
    sys.exit(bstack1ll11ll11l_opy_)
def bstack1ll111l1l_opy_(new_id):
    global bstack1l1111111_opy_
    bstack1l1111111_opy_ = new_id
def bstack1lllll1l1_opy_(bstack1l1l11lll1_opy_):
  if bstack1l1l11lll1_opy_:
    return bstack1l1l11lll1_opy_.capitalize()
  else:
    return bstack11l1l1l_opy_ (u"ࠫࠬ༸")
@measure(event_name=EVENTS.bstack111l1ll1l1_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1l11l11ll1_opy_(bstack1l11llllll_opy_):
  if bstack11l1l1l_opy_ (u"ࠬࡴࡡ࡮ࡧ༹ࠪ") in bstack1l11llllll_opy_ and bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ༺")] != bstack11l1l1l_opy_ (u"ࠧࠨ༻"):
    return bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭༼")]
  else:
    bstack11ll11ll11_opy_ = bstack11l1l1l_opy_ (u"ࠤࠥ༽")
    if bstack11l1l1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ༾") in bstack1l11llllll_opy_ and bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ༿")] != None:
      bstack11ll11ll11_opy_ += bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬཀ")] + bstack11l1l1l_opy_ (u"ࠨࠬࠡࠤཁ")
      if bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠧࡰࡵࠪག")] == bstack11l1l1l_opy_ (u"ࠣ࡫ࡲࡷࠧགྷ"):
        bstack11ll11ll11_opy_ += bstack11l1l1l_opy_ (u"ࠤ࡬ࡓࡘࠦࠢང")
      bstack11ll11ll11_opy_ += (bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧཅ")] or bstack11l1l1l_opy_ (u"ࠫࠬཆ"))
      return bstack11ll11ll11_opy_
    else:
      bstack11ll11ll11_opy_ += bstack1lllll1l1_opy_(bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ཇ")]) + bstack11l1l1l_opy_ (u"ࠨࠠࠣ཈") + (
              bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩཉ")] or bstack11l1l1l_opy_ (u"ࠨࠩཊ")) + bstack11l1l1l_opy_ (u"ࠤ࠯ࠤࠧཋ")
      if bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"ࠪࡳࡸ࠭ཌ")] == bstack11l1l1l_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧཌྷ"):
        bstack11ll11ll11_opy_ += bstack11l1l1l_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥཎ")
      bstack11ll11ll11_opy_ += bstack1l11llllll_opy_[bstack11l1l1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪཏ")] or bstack11l1l1l_opy_ (u"ࠧࠨཐ")
      return bstack11ll11ll11_opy_
@measure(event_name=EVENTS.bstack1ll11lllll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1ll1ll1l1_opy_(bstack1lll11l1l_opy_):
  if bstack1lll11l1l_opy_ == bstack11l1l1l_opy_ (u"ࠣࡦࡲࡲࡪࠨད"):
    return bstack11l1l1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬདྷ")
  elif bstack1lll11l1l_opy_ == bstack11l1l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥན"):
    return bstack11l1l1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧཔ")
  elif bstack1lll11l1l_opy_ == bstack11l1l1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧཕ"):
    return bstack11l1l1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭བ")
  elif bstack1lll11l1l_opy_ == bstack11l1l1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨབྷ"):
    return bstack11l1l1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪམ")
  elif bstack1lll11l1l_opy_ == bstack11l1l1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥཙ"):
    return bstack11l1l1l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨཚ")
  elif bstack1lll11l1l_opy_ == bstack11l1l1l_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧཛ"):
    return bstack11l1l1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ཛྷ")
  else:
    return bstack11l1l1l_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࠪཝ") + bstack1lllll1l1_opy_(
      bstack1lll11l1l_opy_) + bstack11l1l1l_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ཞ")
def bstack1lll1l11l1_opy_(session):
  return bstack11l1l1l_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨཟ").format(
    session[bstack11l1l1l_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭འ")], bstack1l11l11ll1_opy_(session), bstack1ll1ll1l1_opy_(session[bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩཡ")]),
    bstack1ll1ll1l1_opy_(session[bstack11l1l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫར")]),
    bstack1lllll1l1_opy_(session[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ལ")] or session[bstack11l1l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ཤ")] or bstack11l1l1l_opy_ (u"ࠧࠨཥ")) + bstack11l1l1l_opy_ (u"ࠣࠢࠥས") + (session[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫཧ")] or bstack11l1l1l_opy_ (u"ࠪࠫཨ")),
    session[bstack11l1l1l_opy_ (u"ࠫࡴࡹࠧཀྵ")] + bstack11l1l1l_opy_ (u"ࠧࠦࠢཪ") + session[bstack11l1l1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪཫ")], session[bstack11l1l1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩཬ")] or bstack11l1l1l_opy_ (u"ࠨࠩ཭"),
    session[bstack11l1l1l_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭཮")] if session[bstack11l1l1l_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧ཯")] else bstack11l1l1l_opy_ (u"ࠫࠬ཰"))
@measure(event_name=EVENTS.bstack1lllll1l11_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def bstack1l11l11l11_opy_(sessions, bstack1lllll1l1l_opy_):
  try:
    bstack1l1111l1l1_opy_ = bstack11l1l1l_opy_ (u"ࠧࠨཱ")
    if not os.path.exists(bstack111l1ll1ll_opy_):
      os.mkdir(bstack111l1ll1ll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1l1l_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ིࠫ")), bstack11l1l1l_opy_ (u"ࠧࡳཱིࠩ")) as f:
      bstack1l1111l1l1_opy_ = f.read()
    bstack1l1111l1l1_opy_ = bstack1l1111l1l1_opy_.replace(bstack11l1l1l_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁུࠬ"), str(len(sessions)))
    bstack1l1111l1l1_opy_ = bstack1l1111l1l1_opy_.replace(bstack11l1l1l_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾཱུࠩ"), bstack1lllll1l1l_opy_)
    bstack1l1111l1l1_opy_ = bstack1l1111l1l1_opy_.replace(bstack11l1l1l_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀࠫྲྀ"),
                                              sessions[0].get(bstack11l1l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨཷ")) if sessions[0] else bstack11l1l1l_opy_ (u"ࠬ࠭ླྀ"))
    with open(os.path.join(bstack111l1ll1ll_opy_, bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪཹ")), bstack11l1l1l_opy_ (u"ࠧࡸེࠩ")) as stream:
      stream.write(bstack1l1111l1l1_opy_.split(bstack11l1l1l_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁཻࠬ"))[0])
      for session in sessions:
        stream.write(bstack1lll1l11l1_opy_(session))
      stream.write(bstack1l1111l1l1_opy_.split(bstack11l1l1l_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂོ࠭"))[1])
    logger.info(bstack11l1l1l_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂཽ࠭").format(bstack111l1ll1ll_opy_));
  except Exception as e:
    logger.debug(bstack111ll11ll_opy_.format(str(e)))
def bstack1llll11111_opy_(bstack1ll1l1llll_opy_):
  global CONFIG
  try:
    bstack1l1lll1l1l_opy_ = datetime.datetime.now()
    host = bstack11l1l1l_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧཾ") if bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱࠩཿ") in CONFIG else bstack11l1l1l_opy_ (u"࠭ࡡࡱ࡫ྀࠪ")
    user = CONFIG[bstack11l1l1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦཱྀࠩ")]
    key = CONFIG[bstack11l1l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫྂ")]
    bstack11llll1111_opy_ = bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨྃ") if bstack11l1l1l_opy_ (u"ࠪࡥࡵࡶ྄ࠧ") in CONFIG else (bstack11l1l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ྅") if CONFIG.get(bstack11l1l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ྆")) else bstack11l1l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ྇"))
    url = bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬྈ").format(user, key, host, bstack11llll1111_opy_,
                                                                                bstack1ll1l1llll_opy_)
    headers = {
      bstack11l1l1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧྉ"): bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬྊ"),
    }
    proxies = bstack1l1lll1ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      cli.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡩࡨࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹ࡟࡭࡫ࡶࡸࠧྋ"), datetime.datetime.now() - bstack1l1lll1l1l_opy_)
      return list(map(lambda session: session[bstack11l1l1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩྌ")], response.json()))
  except Exception as e:
    logger.debug(bstack1lll1l1lll_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l1l1llll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def get_build_link():
  global CONFIG
  global bstack1l1111111_opy_
  try:
    if bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨྍ") in CONFIG:
      bstack1l1lll1l1l_opy_ = datetime.datetime.now()
      host = bstack11l1l1l_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩྎ") if bstack11l1l1l_opy_ (u"ࠧࡢࡲࡳࠫྏ") in CONFIG else bstack11l1l1l_opy_ (u"ࠨࡣࡳ࡭ࠬྐ")
      user = CONFIG[bstack11l1l1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫྑ")]
      key = CONFIG[bstack11l1l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ྒ")]
      bstack11llll1111_opy_ = bstack11l1l1l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪྒྷ") if bstack11l1l1l_opy_ (u"ࠬࡧࡰࡱࠩྔ") in CONFIG else bstack11l1l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨྕ")
      url = bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠰࡭ࡷࡴࡴࠧྖ").format(user, key, host, bstack11llll1111_opy_)
      headers = {
        bstack11l1l1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧྗ"): bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ྘"),
      }
      if bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬྙ") in CONFIG:
        params = {bstack11l1l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩྚ"): CONFIG[bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨྛ")], bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩྜ"): CONFIG[bstack11l1l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩྜྷ")]}
      else:
        params = {bstack11l1l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ྞ"): CONFIG[bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬྟ")]}
      proxies = bstack1l1lll1ll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack111llll111_opy_ = response.json()[0][bstack11l1l1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡣࡷ࡬ࡰࡩ࠭ྠ")]
        if bstack111llll111_opy_:
          bstack1lllll1l1l_opy_ = bstack111llll111_opy_[bstack11l1l1l_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨྡ")].split(bstack11l1l1l_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧ࠲ࡨࡵࡪ࡮ࡧࠫྡྷ"))[0] + bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠵ࠧྣ") + bstack111llll111_opy_[
            bstack11l1l1l_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪྤ")]
          logger.info(bstack11l1lll11l_opy_.format(bstack1lllll1l1l_opy_))
          bstack1l1111111_opy_ = bstack111llll111_opy_[bstack11l1l1l_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫྥ")]
          bstack1l1lll11l_opy_ = CONFIG[bstack11l1l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬྦ")]
          if bstack11l1l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬྦྷ") in CONFIG:
            bstack1l1lll11l_opy_ += bstack11l1l1l_opy_ (u"ࠫࠥ࠭ྨ") + CONFIG[bstack11l1l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧྩ")]
          if bstack1l1lll11l_opy_ != bstack111llll111_opy_[bstack11l1l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫྪ")]:
            logger.debug(bstack1ll1111l11_opy_.format(bstack111llll111_opy_[bstack11l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬྫ")], bstack1l1lll11l_opy_))
          cli.bstack1ll1l1lll_opy_(bstack11l1l1l_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡦࡺ࡯࡬ࡥࡡ࡯࡭ࡳࡱࠢྫྷ"), datetime.datetime.now() - bstack1l1lll1l1l_opy_)
          return [bstack111llll111_opy_[bstack11l1l1l_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬྭ")], bstack1lllll1l1l_opy_]
    else:
      logger.warn(bstack1l1l111ll1_opy_)
  except Exception as e:
    logger.debug(bstack1lllllll1l_opy_.format(str(e)))
  return [None, None]
def bstack111llllll_opy_(url, bstack11111lll1_opy_=False):
  global CONFIG
  global bstack1llllll1l1_opy_
  if not bstack1llllll1l1_opy_:
    hostname = bstack11ll1ll1ll_opy_(url)
    is_private = bstack11l1l1lll_opy_(hostname)
    if (bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧྮ") in CONFIG and not bstack1l1llllll1_opy_(CONFIG[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨྯ")])) and (is_private or bstack11111lll1_opy_):
      bstack1llllll1l1_opy_ = hostname
def bstack11ll1ll1ll_opy_(url):
  return urlparse(url).hostname
def bstack11l1l1lll_opy_(hostname):
  for bstack1ll1ll1l11_opy_ in bstack1lll11llll_opy_:
    regex = re.compile(bstack1ll1ll1l11_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack111lll111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1111l1111_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1ll1l1l11l_opy_
  bstack1ll1l11l1_opy_ = not (bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩྰ"), None) and bstack11llll1l_opy_(
          threading.current_thread(), bstack11l1l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬྱ"), None))
  bstack111llllll1_opy_ = getattr(driver, bstack11l1l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧྲ"), None) != True
  if not bstack111lllll_opy_.bstack1lll11lll1_opy_(CONFIG, bstack1ll1l1l11l_opy_) or (bstack111llllll1_opy_ and bstack1ll1l11l1_opy_):
    logger.warning(bstack11l1l1l_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦླ"))
    return {}
  try:
    logger.debug(bstack11l1l1l_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ྴ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1111111l1_opy_.bstack1ll111lll1_opy_)
    return results
  except Exception:
    logger.error(bstack11l1l1l_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡸࡧࡵࡩࠥ࡬࡯ࡶࡰࡧ࠲ࠧྵ"))
    return {}
@measure(event_name=EVENTS.bstack1l111111ll_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1ll1l1l11l_opy_
  bstack1ll1l11l1_opy_ = not (bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨྶ"), None) and bstack11llll1l_opy_(
          threading.current_thread(), bstack11l1l1l_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫྷ"), None))
  bstack111llllll1_opy_ = getattr(driver, bstack11l1l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ྸ"), None) != True
  if not bstack111lllll_opy_.bstack1lll11lll1_opy_(CONFIG, bstack1ll1l1l11l_opy_) or (bstack111llllll1_opy_ and bstack1ll1l11l1_opy_):
    logger.warning(bstack11l1l1l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻ࠱ࠦྐྵ"))
    return {}
  try:
    logger.debug(bstack11l1l1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠭ྺ"))
    logger.debug(perform_scan(driver))
    bstack1l1l1l1ll1_opy_ = driver.execute_async_script(bstack1111111l1_opy_.bstack11111l1l1_opy_)
    return bstack1l1l1l1ll1_opy_
  except Exception:
    logger.error(bstack11l1l1l_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡵ࡮࡯ࡤࡶࡾࠦࡷࡢࡵࠣࡪࡴࡻ࡮ࡥ࠰ࠥྻ"))
    return {}
@measure(event_name=EVENTS.bstack11lllll1l_opy_, stage=STAGE.SINGLE, bstack11ll11ll11_opy_=bstack11l1ll111_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1ll1l1l11l_opy_
  bstack1ll1l11l1_opy_ = not (bstack11llll1l_opy_(threading.current_thread(), bstack11l1l1l_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧྼ"), None) and bstack11llll1l_opy_(
          threading.current_thread(), bstack11l1l1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ྽"), None))
  bstack111llllll1_opy_ = getattr(driver, bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ྾"), None) != True
  if not bstack111lllll_opy_.bstack1lll11lll1_opy_(CONFIG, bstack1ll1l1l11l_opy_) or (bstack111llllll1_opy_ and bstack1ll1l11l1_opy_):
    logger.warning(bstack11l1l1l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡵ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮ࠣ྿"))
    return {}
  try:
    bstack111l11111_opy_ = driver.execute_async_script(bstack1111111l1_opy_.perform_scan, {bstack11l1l1l_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧ࿀"): kwargs.get(bstack11l1l1l_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡥࡲࡱࡲࡧ࡮ࡥࠩ࿁"), None) or bstack11l1l1l_opy_ (u"ࠩࠪ࿂")})
    return bstack111l11111_opy_
  except Exception:
    logger.error(bstack11l1l1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡲࡶࡰࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡨࡧ࡮࠯ࠤ࿃"))
    return {}