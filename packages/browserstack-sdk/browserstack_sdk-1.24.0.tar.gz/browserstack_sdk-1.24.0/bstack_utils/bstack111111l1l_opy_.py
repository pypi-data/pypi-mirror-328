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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack1l11l11l11l_opy_, bstack1l11l1l11l1_opy_
import tempfile
import json
bstack11ll1l11111_opy_ = os.getenv(bstack11l1l1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡋࡤࡌࡉࡍࡇࠥᨻ"), None) or os.path.join(tempfile.gettempdir(), bstack11l1l1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠧᨼ"))
bstack11ll1l11ll1_opy_ = os.path.join(bstack11l1l1l_opy_ (u"ࠦࡱࡵࡧࠣᨽ"), bstack11l1l1l_opy_ (u"ࠬࡹࡤ࡬࠯ࡦࡰ࡮࠳ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠩᨾ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l1l1l_opy_ (u"࠭ࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩᨿ"),
      datefmt=bstack11l1l1l_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࡞ࠬᩀ"),
      stream=sys.stdout
    )
  return logger
def bstack1ll1l1l111l_opy_():
  bstack11ll1l111ll_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡅࡇࡅ࡙ࡌࠨᩁ"), bstack11l1l1l_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣᩂ"))
  return logging.DEBUG if bstack11ll1l111ll_opy_.lower() == bstack11l1l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᩃ") else logging.INFO
def bstack1lll11l111l_opy_():
  global bstack11ll1l11111_opy_
  if os.path.exists(bstack11ll1l11111_opy_):
    os.remove(bstack11ll1l11111_opy_)
  if os.path.exists(bstack11ll1l11ll1_opy_):
    os.remove(bstack11ll1l11ll1_opy_)
def bstack1l111ll1ll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack11ll111lll_opy_(config, log_level):
  bstack11ll11lllll_opy_ = log_level
  if bstack11l1l1l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᩄ") in config and config[bstack11l1l1l_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᩅ")] in bstack1l11l11l11l_opy_:
    bstack11ll11lllll_opy_ = bstack1l11l11l11l_opy_[config[bstack11l1l1l_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᩆ")]]
  if config.get(bstack11l1l1l_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩᩇ"), False):
    logging.getLogger().setLevel(bstack11ll11lllll_opy_)
    return bstack11ll11lllll_opy_
  global bstack11ll1l11111_opy_
  bstack1l111ll1ll_opy_()
  bstack11ll1l111l1_opy_ = logging.Formatter(
    fmt=bstack11l1l1l_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫᩈ"),
    datefmt=bstack11l1l1l_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧᩉ"),
  )
  bstack11ll1l1l111_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11ll1l11111_opy_)
  file_handler.setFormatter(bstack11ll1l111l1_opy_)
  bstack11ll1l1l111_opy_.setFormatter(bstack11ll1l111l1_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11ll1l1l111_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l1l1l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡴࡨࡱࡴࡺࡥ࠯ࡴࡨࡱࡴࡺࡥࡠࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬᩊ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11ll1l1l111_opy_.setLevel(bstack11ll11lllll_opy_)
  logging.getLogger().addHandler(bstack11ll1l1l111_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11ll11lllll_opy_
def bstack11ll1l1l1ll_opy_(config):
  try:
    bstack11ll11ll1l1_opy_ = set(bstack1l11l1l11l1_opy_)
    bstack11ll11llll1_opy_ = bstack11l1l1l_opy_ (u"ࠫࠬᩋ")
    with open(bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨᩌ")) as bstack11ll11ll1ll_opy_:
      bstack11ll1l11l1l_opy_ = bstack11ll11ll1ll_opy_.read()
      bstack11ll11llll1_opy_ = re.sub(bstack11l1l1l_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠤ࠰࠭ࠨࡡࡴࠧᩍ"), bstack11l1l1l_opy_ (u"ࠧࠨᩎ"), bstack11ll1l11l1l_opy_, flags=re.M)
      bstack11ll11llll1_opy_ = re.sub(
        bstack11l1l1l_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠫࠫᩏ") + bstack11l1l1l_opy_ (u"ࠩࡿࠫᩐ").join(bstack11ll11ll1l1_opy_) + bstack11l1l1l_opy_ (u"ࠪ࠭࠳࠰ࠤࠨᩑ"),
        bstack11l1l1l_opy_ (u"ࡶࠬࡢ࠲࠻ࠢ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ᩒ"),
        bstack11ll11llll1_opy_, flags=re.M | re.I
      )
    def bstack11ll1l1l11l_opy_(dic):
      bstack11ll1l1l1l1_opy_ = {}
      for key, value in dic.items():
        if key in bstack11ll11ll1l1_opy_:
          bstack11ll1l1l1l1_opy_[key] = bstack11l1l1l_opy_ (u"ࠬࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩᩓ")
        else:
          if isinstance(value, dict):
            bstack11ll1l1l1l1_opy_[key] = bstack11ll1l1l11l_opy_(value)
          else:
            bstack11ll1l1l1l1_opy_[key] = value
      return bstack11ll1l1l1l1_opy_
    bstack11ll1l1l1l1_opy_ = bstack11ll1l1l11l_opy_(config)
    return {
      bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩᩔ"): bstack11ll11llll1_opy_,
      bstack11l1l1l_opy_ (u"ࠧࡧ࡫ࡱࡥࡱࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪᩕ"): json.dumps(bstack11ll1l1l1l1_opy_)
    }
  except Exception as e:
    return {}
def bstack11ll1l11l11_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11l1l1l_opy_ (u"ࠨ࡮ࡲ࡫ࠬᩖ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11ll1l11lll_opy_ = os.path.join(log_dir, bstack11l1l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵࠪᩗ"))
  if not os.path.exists(bstack11ll1l11lll_opy_):
    bstack11ll11lll11_opy_ = {
      bstack11l1l1l_opy_ (u"ࠥ࡭ࡳ࡯ࡰࡢࡶ࡫ࠦᩘ"): str(inipath),
      bstack11l1l1l_opy_ (u"ࠦࡷࡵ࡯ࡵࡲࡤࡸ࡭ࠨᩙ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫᩚ")), bstack11l1l1l_opy_ (u"࠭ࡷࠨᩛ")) as bstack11ll11ll11l_opy_:
      bstack11ll11ll11l_opy_.write(json.dumps(bstack11ll11lll11_opy_))
def bstack11ll1l1111l_opy_():
  try:
    bstack11ll1l11lll_opy_ = os.path.join(os.getcwd(), bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡪࠫᩜ"), bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧᩝ"))
    if os.path.exists(bstack11ll1l11lll_opy_):
      with open(bstack11ll1l11lll_opy_, bstack11l1l1l_opy_ (u"ࠩࡵࠫᩞ")) as bstack11ll11ll11l_opy_:
        bstack11ll11ll111_opy_ = json.load(bstack11ll11ll11l_opy_)
      return bstack11ll11ll111_opy_.get(bstack11l1l1l_opy_ (u"ࠪ࡭ࡳ࡯ࡰࡢࡶ࡫ࠫ᩟"), bstack11l1l1l_opy_ (u"᩠ࠫࠬ")), bstack11ll11ll111_opy_.get(bstack11l1l1l_opy_ (u"ࠬࡸ࡯ࡰࡶࡳࡥࡹ࡮ࠧᩡ"), bstack11l1l1l_opy_ (u"࠭ࠧᩢ"))
  except:
    pass
  return None, None
def bstack11ll11l1lll_opy_():
  try:
    bstack11ll1l11lll_opy_ = os.path.join(os.getcwd(), bstack11l1l1l_opy_ (u"ࠧ࡭ࡱࡪࠫᩣ"), bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧᩤ"))
    if os.path.exists(bstack11ll1l11lll_opy_):
      os.remove(bstack11ll1l11lll_opy_)
  except:
    pass
def bstack1ll1111l_opy_(config):
  from bstack_utils.helper import bstack11111l11_opy_
  global bstack11ll1l11111_opy_
  try:
    if config.get(bstack11l1l1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫᩥ"), False):
      return
    uuid = os.getenv(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᩦ")) if os.getenv(bstack11l1l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᩧ")) else bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢᩨ"))
    if not uuid or uuid == bstack11l1l1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᩩ"):
      return
    bstack11ll11l1ll1_opy_ = [bstack11l1l1l_opy_ (u"ࠧࡳࡧࡴࡹ࡮ࡸࡥ࡮ࡧࡱࡸࡸ࠴ࡴࡹࡶࠪᩪ"), bstack11l1l1l_opy_ (u"ࠨࡒ࡬ࡴ࡫࡯࡬ࡦࠩᩫ"), bstack11l1l1l_opy_ (u"ࠩࡳࡽࡵࡸ࡯࡫ࡧࡦࡸ࠳ࡺ࡯࡮࡮ࠪᩬ"), bstack11ll1l11111_opy_, bstack11ll1l11ll1_opy_]
    bstack11ll11l1l1l_opy_, root_path = bstack11ll1l1111l_opy_()
    if bstack11ll11l1l1l_opy_ != None:
      bstack11ll11l1ll1_opy_.append(bstack11ll11l1l1l_opy_)
    if root_path != None:
      bstack11ll11l1ll1_opy_.append(os.path.join(root_path, bstack11l1l1l_opy_ (u"ࠪࡧࡴࡴࡦࡵࡧࡶࡸ࠳ࡶࡹࠨᩭ")))
    bstack1l111ll1ll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡱࡵࡧࡴ࠯ࠪᩮ") + uuid + bstack11l1l1l_opy_ (u"ࠬ࠴ࡴࡢࡴ࠱࡫ࡿ࠭ᩯ"))
    with tarfile.open(output_file, bstack11l1l1l_opy_ (u"ࠨࡷ࠻ࡩࡽࠦᩰ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11ll11l1ll1_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11ll1l1l1ll_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11ll11lll1l_opy_ = data.encode()
        tarinfo.size = len(bstack11ll11lll1l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11ll11lll1l_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11l1l1l_opy_ (u"ࠧࡥࡣࡷࡥࠬᩱ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l1l1l_opy_ (u"ࠨࡴࡥࠫᩲ")), bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯ࡹ࠯ࡪࡾ࡮ࡶࠧᩳ")),
        bstack11l1l1l_opy_ (u"ࠪࡧࡱ࡯ࡥ࡯ࡶࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᩴ"): uuid
      }
    )
    response = requests.post(
      bstack11l1l1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡻࡰ࡭ࡱࡤࡨ࠲ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡥ࡯࡭ࡪࡴࡴ࠮࡮ࡲ࡫ࡸ࠵ࡵࡱ࡮ࡲࡥࡩࠨ᩵"),
      data=multipart_data,
      headers={bstack11l1l1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ᩶"): multipart_data.content_type},
      auth=(config[bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ᩷")], config[bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ᩸")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l1l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲ࡯ࡳࡦࡪࠠ࡭ࡱࡪࡷ࠿ࠦࠧ᩹") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l1l1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹ࠺ࠨ᩺") + str(e))
  finally:
    try:
      bstack1lll11l111l_opy_()
      bstack11ll11l1lll_opy_()
    except:
      pass