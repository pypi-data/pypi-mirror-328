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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1l11l1llll1_opy_, bstack1lll11llll_opy_, bstack111lll11l_opy_, bstack1ll11lll1_opy_,
                                    bstack1l11l1ll11l_opy_, bstack1l11ll1l11l_opy_, bstack1l11l1l11l1_opy_, bstack1l11ll1l111_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111llll1l_opy_, bstack1l11l11l1l_opy_
from bstack_utils.proxy import bstack1l1lll1ll_opy_, bstack1lll1111l1_opy_
from bstack_utils.constants import *
from bstack_utils import bstack111111l1l_opy_
from browserstack_sdk._version import __version__
bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
logger = bstack111111l1l_opy_.get_logger(__name__, bstack111111l1l_opy_.bstack1ll1l1l111l_opy_())
def bstack11ll1llllll_opy_(config):
    return config[bstack11l1l1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ៤")]
def bstack11lll11lll1_opy_(config):
    return config[bstack11l1l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ៥")]
def bstack1l1ll11111_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11lll1ll1l1_opy_(obj):
    values = []
    bstack11lll111ll1_opy_ = re.compile(bstack11l1l1l_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦ៦"), re.I)
    for key in obj.keys():
        if bstack11lll111ll1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11lllll1111_opy_(config):
    tags = []
    tags.extend(bstack11lll1ll1l1_opy_(os.environ))
    tags.extend(bstack11lll1ll1l1_opy_(config))
    return tags
def bstack11lllll1l11_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack11lllll11l1_opy_(bstack11ll1ll1lll_opy_):
    if not bstack11ll1ll1lll_opy_:
        return bstack11l1l1l_opy_ (u"ࠨࠩ៧")
    return bstack11l1l1l_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾࠫࠥ៨").format(bstack11ll1ll1lll_opy_.name, bstack11ll1ll1lll_opy_.email)
def bstack1l111111l11_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack11llll1l1l1_opy_ = repo.common_dir
        info = {
            bstack11l1l1l_opy_ (u"ࠥࡷ࡭ࡧࠢ៩"): repo.head.commit.hexsha,
            bstack11l1l1l_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢ៪"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l1l1l_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧ៫"): repo.active_branch.name,
            bstack11l1l1l_opy_ (u"ࠨࡴࡢࡩࠥ៬"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l1l1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥ៭"): bstack11lllll11l1_opy_(repo.head.commit.committer),
            bstack11l1l1l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤ៮"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l1l1l_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤ៯"): bstack11lllll11l1_opy_(repo.head.commit.author),
            bstack11l1l1l_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣ៰"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l1l1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧ៱"): repo.head.commit.message,
            bstack11l1l1l_opy_ (u"ࠧࡸ࡯ࡰࡶࠥ៲"): repo.git.rev_parse(bstack11l1l1l_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣ៳")),
            bstack11l1l1l_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣ៴"): bstack11llll1l1l1_opy_,
            bstack11l1l1l_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦ៵"): subprocess.check_output([bstack11l1l1l_opy_ (u"ࠤࡪ࡭ࡹࠨ៶"), bstack11l1l1l_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨ៷"), bstack11l1l1l_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢ៸")]).strip().decode(
                bstack11l1l1l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ៹")),
            bstack11l1l1l_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣ៺"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l1l1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤ៻"): repo.git.rev_list(
                bstack11l1l1l_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣ៼").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11lll1l1l11_opy_ = []
        for remote in remotes:
            bstack1l11111l111_opy_ = {
                bstack11l1l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ៽"): remote.name,
                bstack11l1l1l_opy_ (u"ࠥࡹࡷࡲࠢ៾"): remote.url,
            }
            bstack11lll1l1l11_opy_.append(bstack1l11111l111_opy_)
        bstack11lll1111l1_opy_ = {
            bstack11l1l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ៿"): bstack11l1l1l_opy_ (u"ࠧ࡭ࡩࡵࠤ᠀"),
            **info,
            bstack11l1l1l_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹࠢ᠁"): bstack11lll1l1l11_opy_
        }
        bstack11lll1111l1_opy_ = bstack11ll1lll1ll_opy_(bstack11lll1111l1_opy_)
        return bstack11lll1111l1_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l1l1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥ᠂").format(err))
        return {}
def bstack11ll1lll1ll_opy_(bstack11lll1111l1_opy_):
    bstack11ll1lll1l1_opy_ = bstack11llll1lll1_opy_(bstack11lll1111l1_opy_)
    if bstack11ll1lll1l1_opy_ and bstack11ll1lll1l1_opy_ > bstack1l11l1ll11l_opy_:
        bstack11lll111lll_opy_ = bstack11ll1lll1l1_opy_ - bstack1l11l1ll11l_opy_
        bstack1l1111l11l1_opy_ = bstack11llll1l111_opy_(bstack11lll1111l1_opy_[bstack11l1l1l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤ᠃")], bstack11lll111lll_opy_)
        bstack11lll1111l1_opy_[bstack11l1l1l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥ᠄")] = bstack1l1111l11l1_opy_
        logger.info(bstack11l1l1l_opy_ (u"ࠥࡘ࡭࡫ࠠࡤࡱࡰࡱ࡮ࡺࠠࡩࡣࡶࠤࡧ࡫ࡥ࡯ࠢࡷࡶࡺࡴࡣࡢࡶࡨࡨ࠳ࠦࡓࡪࡼࡨࠤࡴ࡬ࠠࡤࡱࡰࡱ࡮ࡺࠠࡢࡨࡷࡩࡷࠦࡴࡳࡷࡱࡧࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡻࡾࠢࡎࡆࠧ᠅")
                    .format(bstack11llll1lll1_opy_(bstack11lll1111l1_opy_) / 1024))
    return bstack11lll1111l1_opy_
def bstack11llll1lll1_opy_(json_data):
    try:
        if json_data:
            bstack11lll111111_opy_ = json.dumps(json_data)
            bstack11llll1ll11_opy_ = sys.getsizeof(bstack11lll111111_opy_)
            return bstack11llll1ll11_opy_
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠦࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡦࡲࡣࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡵ࡬ࡾࡪࠦ࡯ࡧࠢࡍࡗࡔࡔࠠࡰࡤ࡭ࡩࡨࡺ࠺ࠡࡽࢀࠦ᠆").format(e))
    return -1
def bstack11llll1l111_opy_(field, bstack1l1111111ll_opy_):
    try:
        bstack11lll11111l_opy_ = len(bytes(bstack1l11ll1l11l_opy_, bstack11l1l1l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫ᠇")))
        bstack1l111111111_opy_ = bytes(field, bstack11l1l1l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬ᠈"))
        bstack1l1111l111l_opy_ = len(bstack1l111111111_opy_)
        bstack11lll111l11_opy_ = ceil(bstack1l1111l111l_opy_ - bstack1l1111111ll_opy_ - bstack11lll11111l_opy_)
        if bstack11lll111l11_opy_ > 0:
            bstack11llll11l11_opy_ = bstack1l111111111_opy_[:bstack11lll111l11_opy_].decode(bstack11l1l1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭᠉"), errors=bstack11l1l1l_opy_ (u"ࠨ࡫ࡪࡲࡴࡸࡥࠨ᠊")) + bstack1l11ll1l11l_opy_
            return bstack11llll11l11_opy_
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡵࡴࡸࡲࡨࡧࡴࡪࡰࡪࠤ࡫࡯ࡥ࡭ࡦ࠯ࠤࡳࡵࡴࡩ࡫ࡱ࡫ࠥࡽࡡࡴࠢࡷࡶࡺࡴࡣࡢࡶࡨࡨࠥ࡮ࡥࡳࡧ࠽ࠤࢀࢃࠢ᠋").format(e))
    return field
def bstack1ll1l111l_opy_():
    env = os.environ
    if (bstack11l1l1l_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣ᠌") in env and len(env[bstack11l1l1l_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠤ᠍")]) > 0) or (
            bstack11l1l1l_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦ᠎") in env and len(env[bstack11l1l1l_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠧ᠏")]) > 0):
        return {
            bstack11l1l1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᠐"): bstack11l1l1l_opy_ (u"ࠣࡌࡨࡲࡰ࡯࡮ࡴࠤ᠑"),
            bstack11l1l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᠒"): env.get(bstack11l1l1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᠓")),
            bstack11l1l1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᠔"): env.get(bstack11l1l1l_opy_ (u"ࠧࡐࡏࡃࡡࡑࡅࡒࡋࠢ᠕")),
            bstack11l1l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᠖"): env.get(bstack11l1l1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ᠗"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠣࡅࡌࠦ᠘")) == bstack11l1l1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ᠙") and bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡆࡍࠧ᠚"))):
        return {
            bstack11l1l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᠛"): bstack11l1l1l_opy_ (u"ࠧࡉࡩࡳࡥ࡯ࡩࡈࡏࠢ᠜"),
            bstack11l1l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᠝"): env.get(bstack11l1l1l_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ᠞")),
            bstack11l1l1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᠟"): env.get(bstack11l1l1l_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡍࡓࡇࠨᠠ")),
            bstack11l1l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᠡ"): env.get(bstack11l1l1l_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࠢᠢ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠧࡉࡉࠣᠣ")) == bstack11l1l1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᠤ") and bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙ࠢᠥ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᠦ"): bstack11l1l1l_opy_ (u"ࠤࡗࡶࡦࡼࡩࡴࠢࡆࡍࠧᠧ"),
            bstack11l1l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᠨ"): env.get(bstack11l1l1l_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢ࡛ࡊࡈ࡟ࡖࡔࡏࠦᠩ")),
            bstack11l1l1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᠪ"): env.get(bstack11l1l1l_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᠫ")),
            bstack11l1l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᠬ"): env.get(bstack11l1l1l_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᠭ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠤࡆࡍࠧᠮ")) == bstack11l1l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᠯ") and env.get(bstack11l1l1l_opy_ (u"ࠦࡈࡏ࡟ࡏࡃࡐࡉࠧᠰ")) == bstack11l1l1l_opy_ (u"ࠧࡩ࡯ࡥࡧࡶ࡬࡮ࡶࠢᠱ"):
        return {
            bstack11l1l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᠲ"): bstack11l1l1l_opy_ (u"ࠢࡄࡱࡧࡩࡸ࡮ࡩࡱࠤᠳ"),
            bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᠴ"): None,
            bstack11l1l1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᠵ"): None,
            bstack11l1l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᠶ"): None
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡔࡄࡒࡈࡎࠢᠷ")) and env.get(bstack11l1l1l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡅࡒࡑࡒࡏࡔࠣᠸ")):
        return {
            bstack11l1l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᠹ"): bstack11l1l1l_opy_ (u"ࠢࡃ࡫ࡷࡦࡺࡩ࡫ࡦࡶࠥᠺ"),
            bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᠻ"): env.get(bstack11l1l1l_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡍࡉࡕࡡࡋࡘ࡙ࡖ࡟ࡐࡔࡌࡋࡎࡔࠢᠼ")),
            bstack11l1l1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᠽ"): None,
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᠾ"): env.get(bstack11l1l1l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᠿ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠨࡃࡊࠤᡀ")) == bstack11l1l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᡁ") and bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠣࡆࡕࡓࡓࡋࠢᡂ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᡃ"): bstack11l1l1l_opy_ (u"ࠥࡈࡷࡵ࡮ࡦࠤᡄ"),
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᡅ"): env.get(bstack11l1l1l_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡐࡎࡔࡋࠣᡆ")),
            bstack11l1l1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᡇ"): None,
            bstack11l1l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᡈ"): env.get(bstack11l1l1l_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᡉ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠤࡆࡍࠧᡊ")) == bstack11l1l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᡋ") and bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋࠢᡌ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᡍ"): bstack11l1l1l_opy_ (u"ࠨࡓࡦ࡯ࡤࡴ࡭ࡵࡲࡦࠤᡎ"),
            bstack11l1l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᡏ"): env.get(bstack11l1l1l_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡔࡘࡇࡂࡐࡌ࡞ࡆ࡚ࡉࡐࡐࡢ࡙ࡗࡒࠢᡐ")),
            bstack11l1l1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᡑ"): env.get(bstack11l1l1l_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᡒ")),
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᡓ"): env.get(bstack11l1l1l_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡏࡄࠣᡔ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠨࡃࡊࠤᡕ")) == bstack11l1l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᡖ") and bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠣࡉࡌࡘࡑࡇࡂࡠࡅࡌࠦᡗ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᡘ"): bstack11l1l1l_opy_ (u"ࠥࡋ࡮ࡺࡌࡢࡤࠥᡙ"),
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᡚ"): env.get(bstack11l1l1l_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤ࡛ࡒࡍࠤᡛ")),
            bstack11l1l1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᡜ"): env.get(bstack11l1l1l_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᡝ")),
            bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᡞ"): env.get(bstack11l1l1l_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡌࡈࠧᡟ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠥࡇࡎࠨᡠ")) == bstack11l1l1l_opy_ (u"ࠦࡹࡸࡵࡦࠤᡡ") and bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࠣᡢ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᡣ"): bstack11l1l1l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡱࡩࡵࡧࠥᡤ"),
            bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᡥ"): env.get(bstack11l1l1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᡦ")),
            bstack11l1l1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᡧ"): env.get(bstack11l1l1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡍࡃࡅࡉࡑࠨᡨ")) or env.get(bstack11l1l1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅࠣᡩ")),
            bstack11l1l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᡪ"): env.get(bstack11l1l1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᡫ"))
        }
    if bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥᡬ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᡭ"): bstack11l1l1l_opy_ (u"࡚ࠥ࡮ࡹࡵࡢ࡮ࠣࡗࡹࡻࡤࡪࡱࠣࡘࡪࡧ࡭ࠡࡕࡨࡶࡻ࡯ࡣࡦࡵࠥᡮ"),
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᡯ"): bstack11l1l1l_opy_ (u"ࠧࢁࡽࡼࡿࠥᡰ").format(env.get(bstack11l1l1l_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩᡱ")), env.get(bstack11l1l1l_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࡎࡊࠧᡲ"))),
            bstack11l1l1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᡳ"): env.get(bstack11l1l1l_opy_ (u"ࠤࡖ࡝ࡘ࡚ࡅࡎࡡࡇࡉࡋࡏࡎࡊࡖࡌࡓࡓࡏࡄࠣᡴ")),
            bstack11l1l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᡵ"): env.get(bstack11l1l1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦᡶ"))
        }
    if bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘࠢᡷ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᡸ"): bstack11l1l1l_opy_ (u"ࠢࡂࡲࡳࡺࡪࡿ࡯ࡳࠤ᡹"),
            bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᡺"): bstack11l1l1l_opy_ (u"ࠤࡾࢁ࠴ࡶࡲࡰ࡬ࡨࡧࡹ࠵ࡻࡾ࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠣ᡻").format(env.get(bstack11l1l1l_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤ࡛ࡒࡍࠩ᡼")), env.get(bstack11l1l1l_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡁࡄࡅࡒ࡙ࡓ࡚࡟ࡏࡃࡐࡉࠬ᡽")), env.get(bstack11l1l1l_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡕࡏ࡙ࡌ࠭᡾")), env.get(bstack11l1l1l_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ᡿"))),
            bstack11l1l1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᢀ"): env.get(bstack11l1l1l_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᢁ")),
            bstack11l1l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᢂ"): env.get(bstack11l1l1l_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᢃ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠦࡆࡠࡕࡓࡇࡢࡌ࡙࡚ࡐࡠࡗࡖࡉࡗࡥࡁࡈࡇࡑࡘࠧᢄ")) and env.get(bstack11l1l1l_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢᢅ")):
        return {
            bstack11l1l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᢆ"): bstack11l1l1l_opy_ (u"ࠢࡂࡼࡸࡶࡪࠦࡃࡊࠤᢇ"),
            bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᢈ"): bstack11l1l1l_opy_ (u"ࠤࡾࢁࢀࢃ࠯ࡠࡤࡸ࡭ࡱࡪ࠯ࡳࡧࡶࡹࡱࡺࡳࡀࡤࡸ࡭ࡱࡪࡉࡥ࠿ࡾࢁࠧᢉ").format(env.get(bstack11l1l1l_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭ᢊ")), env.get(bstack11l1l1l_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࠩᢋ")), env.get(bstack11l1l1l_opy_ (u"ࠬࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠬᢌ"))),
            bstack11l1l1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᢍ"): env.get(bstack11l1l1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᢎ")),
            bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᢏ"): env.get(bstack11l1l1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᢐ"))
        }
    if any([env.get(bstack11l1l1l_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᢑ")), env.get(bstack11l1l1l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡓࡇࡖࡓࡑ࡜ࡅࡅࡡࡖࡓ࡚ࡘࡃࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥᢒ")), env.get(bstack11l1l1l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤᢓ"))]):
        return {
            bstack11l1l1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᢔ"): bstack11l1l1l_opy_ (u"ࠢࡂ࡙ࡖࠤࡈࡵࡤࡦࡄࡸ࡭ࡱࡪࠢᢕ"),
            bstack11l1l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᢖ"): env.get(bstack11l1l1l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡖࡕࡃࡎࡌࡇࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᢗ")),
            bstack11l1l1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᢘ"): env.get(bstack11l1l1l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᢙ")),
            bstack11l1l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᢚ"): env.get(bstack11l1l1l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᢛ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧᢜ")):
        return {
            bstack11l1l1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᢝ"): bstack11l1l1l_opy_ (u"ࠤࡅࡥࡲࡨ࡯ࡰࠤᢞ"),
            bstack11l1l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᢟ"): env.get(bstack11l1l1l_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡕࡩࡸࡻ࡬ࡵࡵࡘࡶࡱࠨᢠ")),
            bstack11l1l1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᢡ"): env.get(bstack11l1l1l_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡳࡩࡱࡵࡸࡏࡵࡢࡏࡣࡰࡩࠧᢢ")),
            bstack11l1l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᢣ"): env.get(bstack11l1l1l_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡎࡶ࡯ࡥࡩࡷࠨᢤ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࠥᢥ")) or env.get(bstack11l1l1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡒࡇࡉࡏࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡘ࡚ࡁࡓࡖࡈࡈࠧᢦ")):
        return {
            bstack11l1l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᢧ"): bstack11l1l1l_opy_ (u"ࠧ࡝ࡥࡳࡥ࡮ࡩࡷࠨᢨ"),
            bstack11l1l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᢩ"): env.get(bstack11l1l1l_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᢪ")),
            bstack11l1l1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᢫"): bstack11l1l1l_opy_ (u"ࠤࡐࡥ࡮ࡴࠠࡑ࡫ࡳࡩࡱ࡯࡮ࡦࠤ᢬") if env.get(bstack11l1l1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡒࡇࡉࡏࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡘ࡚ࡁࡓࡖࡈࡈࠧ᢭")) else None,
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᢮"): env.get(bstack11l1l1l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡇࡊࡖࡢࡇࡔࡓࡍࡊࡖࠥ᢯"))
        }
    if any([env.get(bstack11l1l1l_opy_ (u"ࠨࡇࡄࡒࡢࡔࡗࡕࡊࡆࡅࡗࠦᢰ")), env.get(bstack11l1l1l_opy_ (u"ࠢࡈࡅࡏࡓ࡚ࡊ࡟ࡑࡔࡒࡎࡊࡉࡔࠣᢱ")), env.get(bstack11l1l1l_opy_ (u"ࠣࡉࡒࡓࡌࡒࡅࡠࡅࡏࡓ࡚ࡊ࡟ࡑࡔࡒࡎࡊࡉࡔࠣᢲ"))]):
        return {
            bstack11l1l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᢳ"): bstack11l1l1l_opy_ (u"ࠥࡋࡴࡵࡧ࡭ࡧࠣࡇࡱࡵࡵࡥࠤᢴ"),
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᢵ"): None,
            bstack11l1l1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᢶ"): env.get(bstack11l1l1l_opy_ (u"ࠨࡐࡓࡑࡍࡉࡈ࡚࡟ࡊࡆࠥᢷ")),
            bstack11l1l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᢸ"): env.get(bstack11l1l1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᢹ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࠧᢺ")):
        return {
            bstack11l1l1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᢻ"): bstack11l1l1l_opy_ (u"ࠦࡘ࡮ࡩࡱࡲࡤࡦࡱ࡫ࠢᢼ"),
            bstack11l1l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᢽ"): env.get(bstack11l1l1l_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᢾ")),
            bstack11l1l1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᢿ"): bstack11l1l1l_opy_ (u"ࠣࡌࡲࡦࠥࠩࡻࡾࠤᣀ").format(env.get(bstack11l1l1l_opy_ (u"ࠩࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈࠬᣁ"))) if env.get(bstack11l1l1l_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡊࡐࡄࡢࡍࡉࠨᣂ")) else None,
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᣃ"): env.get(bstack11l1l1l_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᣄ"))
        }
    if bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠨࡎࡆࡖࡏࡍࡋ࡟ࠢᣅ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᣆ"): bstack11l1l1l_opy_ (u"ࠣࡐࡨࡸࡱ࡯ࡦࡺࠤᣇ"),
            bstack11l1l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᣈ"): env.get(bstack11l1l1l_opy_ (u"ࠥࡈࡊࡖࡌࡐ࡛ࡢ࡙ࡗࡒࠢᣉ")),
            bstack11l1l1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᣊ"): env.get(bstack11l1l1l_opy_ (u"࡙ࠧࡉࡕࡇࡢࡒࡆࡓࡅࠣᣋ")),
            bstack11l1l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᣌ"): env.get(bstack11l1l1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤᣍ"))
        }
    if bstack1l1llllll1_opy_(env.get(bstack11l1l1l_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡃࡆࡘࡎࡕࡎࡔࠤᣎ"))):
        return {
            bstack11l1l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᣏ"): bstack11l1l1l_opy_ (u"ࠥࡋ࡮ࡺࡈࡶࡤࠣࡅࡨࡺࡩࡰࡰࡶࠦᣐ"),
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᣑ"): bstack11l1l1l_opy_ (u"ࠧࢁࡽ࠰ࡽࢀ࠳ࡦࡩࡴࡪࡱࡱࡷ࠴ࡸࡵ࡯ࡵ࠲ࡿࢂࠨᣒ").format(env.get(bstack11l1l1l_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡓࡆࡔ࡙ࡉࡗࡥࡕࡓࡎࠪᣓ")), env.get(bstack11l1l1l_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡇࡓࡓࡘࡏࡔࡐࡔ࡜ࠫᣔ")), env.get(bstack11l1l1l_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠨᣕ"))),
            bstack11l1l1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᣖ"): env.get(bstack11l1l1l_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢ࡛ࡔࡘࡋࡇࡎࡒ࡛ࠧᣗ")),
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᣘ"): env.get(bstack11l1l1l_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠧᣙ"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠨࡃࡊࠤᣚ")) == bstack11l1l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᣛ") and env.get(bstack11l1l1l_opy_ (u"ࠣࡘࡈࡖࡈࡋࡌࠣᣜ")) == bstack11l1l1l_opy_ (u"ࠤ࠴ࠦᣝ"):
        return {
            bstack11l1l1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᣞ"): bstack11l1l1l_opy_ (u"࡛ࠦ࡫ࡲࡤࡧ࡯ࠦᣟ"),
            bstack11l1l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᣠ"): bstack11l1l1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࡻࡾࠤᣡ").format(env.get(bstack11l1l1l_opy_ (u"ࠧࡗࡇࡕࡇࡊࡒ࡟ࡖࡔࡏࠫᣢ"))),
            bstack11l1l1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᣣ"): None,
            bstack11l1l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᣤ"): None,
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤ࡜ࡅࡓࡕࡌࡓࡓࠨᣥ")):
        return {
            bstack11l1l1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᣦ"): bstack11l1l1l_opy_ (u"࡚ࠧࡥࡢ࡯ࡦ࡭ࡹࡿࠢᣧ"),
            bstack11l1l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᣨ"): None,
            bstack11l1l1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᣩ"): env.get(bstack11l1l1l_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢࡔࡗࡕࡊࡆࡅࡗࡣࡓࡇࡍࡆࠤᣪ")),
            bstack11l1l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᣫ"): env.get(bstack11l1l1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᣬ"))
        }
    if any([env.get(bstack11l1l1l_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋࠢᣭ")), env.get(bstack11l1l1l_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡕࡐࠧᣮ")), env.get(bstack11l1l1l_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡘࡗࡊࡘࡎࡂࡏࡈࠦᣯ")), env.get(bstack11l1l1l_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢࡘࡊࡇࡍࠣᣰ"))]):
        return {
            bstack11l1l1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᣱ"): bstack11l1l1l_opy_ (u"ࠤࡆࡳࡳࡩ࡯ࡶࡴࡶࡩࠧᣲ"),
            bstack11l1l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᣳ"): None,
            bstack11l1l1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᣴ"): env.get(bstack11l1l1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᣵ")) or None,
            bstack11l1l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᣶"): env.get(bstack11l1l1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤ᣷"), 0)
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨ᣸")):
        return {
            bstack11l1l1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᣹"): bstack11l1l1l_opy_ (u"ࠥࡋࡴࡉࡄࠣ᣺"),
            bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᣻"): None,
            bstack11l1l1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᣼"): env.get(bstack11l1l1l_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ᣽")),
            bstack11l1l1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᣾"): env.get(bstack11l1l1l_opy_ (u"ࠣࡉࡒࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡃࡐࡗࡑࡘࡊࡘࠢ᣿"))
        }
    if env.get(bstack11l1l1l_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᤀ")):
        return {
            bstack11l1l1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᤁ"): bstack11l1l1l_opy_ (u"ࠦࡈࡵࡤࡦࡈࡵࡩࡸ࡮ࠢᤂ"),
            bstack11l1l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᤃ"): env.get(bstack11l1l1l_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᤄ")),
            bstack11l1l1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᤅ"): env.get(bstack11l1l1l_opy_ (u"ࠣࡅࡉࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦᤆ")),
            bstack11l1l1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᤇ"): env.get(bstack11l1l1l_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᤈ"))
        }
    return {bstack11l1l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᤉ"): None}
def get_host_info():
    return {
        bstack11l1l1l_opy_ (u"ࠧ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠢᤊ"): platform.node(),
        bstack11l1l1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣᤋ"): platform.system(),
        bstack11l1l1l_opy_ (u"ࠢࡵࡻࡳࡩࠧᤌ"): platform.machine(),
        bstack11l1l1l_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤᤍ"): platform.version(),
        bstack11l1l1l_opy_ (u"ࠤࡤࡶࡨ࡮ࠢᤎ"): platform.architecture()[0]
    }
def bstack1l11l111ll_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack11lll1l1lll_opy_():
    if bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫᤏ")):
        return bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᤐ")
    return bstack11l1l1l_opy_ (u"ࠬࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠫᤑ")
def bstack11ll1ll111l_opy_(driver):
    info = {
        bstack11l1l1l_opy_ (u"࠭ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᤒ"): driver.capabilities,
        bstack11l1l1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫᤓ"): driver.session_id,
        bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩᤔ"): driver.capabilities.get(bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᤕ"), None),
        bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᤖ"): driver.capabilities.get(bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᤗ"), None),
        bstack11l1l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࠧᤘ"): driver.capabilities.get(bstack11l1l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬᤙ"), None),
    }
    if bstack11lll1l1lll_opy_() == bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᤚ"):
        if bstack1l11ll1l1_opy_():
            info[bstack11l1l1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᤛ")] = bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨᤜ")
        elif driver.capabilities.get(bstack11l1l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᤝ"), {}).get(bstack11l1l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᤞ"), False):
            info[bstack11l1l1l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭᤟")] = bstack11l1l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᤠ")
        else:
            info[bstack11l1l1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᤡ")] = bstack11l1l1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᤢ")
    return info
def bstack1l11ll1l1_opy_():
    if bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᤣ")):
        return True
    if bstack1l1llllll1_opy_(os.environ.get(bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫᤤ"), None)):
        return True
    return False
def bstack1l11llll1l_opy_(bstack11lll11l111_opy_, url, data, config):
    headers = config.get(bstack11l1l1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᤥ"), None)
    proxies = bstack1l1lll1ll_opy_(config, url)
    auth = config.get(bstack11l1l1l_opy_ (u"ࠬࡧࡵࡵࡪࠪᤦ"), None)
    response = requests.request(
            bstack11lll11l111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l11111ll_opy_(bstack1111ll1ll_opy_, size):
    bstack11l11ll11_opy_ = []
    while len(bstack1111ll1ll_opy_) > size:
        bstack111ll111l_opy_ = bstack1111ll1ll_opy_[:size]
        bstack11l11ll11_opy_.append(bstack111ll111l_opy_)
        bstack1111ll1ll_opy_ = bstack1111ll1ll_opy_[size:]
    bstack11l11ll11_opy_.append(bstack1111ll1ll_opy_)
    return bstack11l11ll11_opy_
def bstack11lllll1ll1_opy_(message, bstack11llll1111l_opy_=False):
    os.write(1, bytes(message, bstack11l1l1l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᤧ")))
    os.write(1, bytes(bstack11l1l1l_opy_ (u"ࠧ࡝ࡰࠪᤨ"), bstack11l1l1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᤩ")))
    if bstack11llll1111l_opy_:
        with open(bstack11l1l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨᤪ") + os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᤫ")] + bstack11l1l1l_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩ᤬"), bstack11l1l1l_opy_ (u"ࠬࡧࠧ᤭")) as f:
            f.write(message + bstack11l1l1l_opy_ (u"࠭࡜࡯ࠩ᤮"))
def bstack1l1llll111l_opy_():
    return os.environ[bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ᤯")].lower() == bstack11l1l1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᤰ")
def bstack1lll111l1l_opy_(bstack1l11111lll1_opy_):
    return bstack11l1l1l_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨᤱ").format(bstack1l11l1llll1_opy_, bstack1l11111lll1_opy_)
def bstack11llllll_opy_():
    return bstack1ll1l1l1_opy_().replace(tzinfo=None).isoformat() + bstack11l1l1l_opy_ (u"ࠪ࡞ࠬᤲ")
def bstack11lll11ll11_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l1l1l_opy_ (u"ࠫ࡟࠭ᤳ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l1l1l_opy_ (u"ࠬࡠࠧᤴ")))).total_seconds() * 1000
def bstack1l11111l1ll_opy_(timestamp):
    return bstack11ll1ll1l11_opy_(timestamp).isoformat() + bstack11l1l1l_opy_ (u"࡚࠭ࠨᤵ")
def bstack11llll11l1l_opy_(bstack11llllll11l_opy_):
    date_format = bstack11l1l1l_opy_ (u"࡛ࠧࠦࠨࡱࠪࡪࠠࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪࠬᤶ")
    bstack11lll1l11ll_opy_ = datetime.datetime.strptime(bstack11llllll11l_opy_, date_format)
    return bstack11lll1l11ll_opy_.isoformat() + bstack11l1l1l_opy_ (u"ࠨ࡜ࠪᤷ")
def bstack11ll1lllll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l1l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᤸ")
    else:
        return bstack11l1l1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦ᤹ࠪ")
def bstack1l1llllll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l1l1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ᤺")
def bstack11llllll1ll_opy_(val):
    return val.__str__().lower() == bstack11l1l1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨ᤻ࠫ")
def bstack1ll111l1_opy_(bstack11lll11l1ll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack11lll11l1ll_opy_ as e:
                print(bstack11l1l1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨ᤼").format(func.__name__, bstack11lll11l1ll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1l11111l11l_opy_(bstack11lllll1lll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11lllll1lll_opy_(cls, *args, **kwargs)
            except bstack11lll11l1ll_opy_ as e:
                print(bstack11l1l1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢ᤽").format(bstack11lllll1lll_opy_.__name__, bstack11lll11l1ll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1l11111l11l_opy_
    else:
        return decorator
def bstack11l1111ll1_opy_(bstack1111llll_opy_):
    if os.getenv(bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ᤾")) is not None:
        return bstack1l1llllll1_opy_(os.getenv(bstack11l1l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬ᤿")))
    if bstack11l1l1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ᥀") in bstack1111llll_opy_ and bstack11llllll1ll_opy_(bstack1111llll_opy_[bstack11l1l1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᥁")]):
        return False
    if bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ᥂") in bstack1111llll_opy_ and bstack11llllll1ll_opy_(bstack1111llll_opy_[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᥃")]):
        return False
    return True
def bstack11l1ll111l_opy_():
    try:
        from pytest_bdd import reporting
        bstack11llll1ll1l_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠢ᥄"), None)
        return bstack11llll1ll1l_opy_ is None or bstack11llll1ll1l_opy_ == bstack11l1l1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧ᥅")
    except Exception as e:
        return False
def bstack1llll111l1_opy_(hub_url, CONFIG):
    if bstack1ll1l1111l_opy_() <= version.parse(bstack11l1l1l_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ᥆")):
        if hub_url:
            return bstack11l1l1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ᥇") + hub_url + bstack11l1l1l_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ᥈")
        return bstack111lll11l_opy_
    if hub_url:
        return bstack11l1l1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢ᥉") + hub_url + bstack11l1l1l_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢ᥊")
    return bstack1ll11lll1_opy_
def bstack11lll1ll111_opy_():
    return isinstance(os.getenv(bstack11l1l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭᥋")), str)
def bstack11ll1ll1ll_opy_(url):
    return urlparse(url).hostname
def bstack11l1l1lll_opy_(hostname):
    for bstack1ll1ll1l11_opy_ in bstack1lll11llll_opy_:
        regex = re.compile(bstack1ll1ll1l11_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack1l1l111l111_opy_(bstack11lllllllll_opy_, file_name, logger):
    bstack1lll1l1111_opy_ = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠨࢀࠪ᥌")), bstack11lllllllll_opy_)
    try:
        if not os.path.exists(bstack1lll1l1111_opy_):
            os.makedirs(bstack1lll1l1111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠩࢁࠫ᥍")), bstack11lllllllll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l1l1l_opy_ (u"ࠪࡻࠬ᥎")):
                pass
            with open(file_path, bstack11l1l1l_opy_ (u"ࠦࡼ࠱ࠢ᥏")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111llll1l_opy_.format(str(e)))
def bstack1l1l111ll11_opy_(file_name, key, value, logger):
    file_path = bstack1l1l111l111_opy_(bstack11l1l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᥐ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111l1l1l1_opy_ = json.load(open(file_path, bstack11l1l1l_opy_ (u"࠭ࡲࡣࠩᥑ")))
        else:
            bstack111l1l1l1_opy_ = {}
        bstack111l1l1l1_opy_[key] = value
        with open(file_path, bstack11l1l1l_opy_ (u"ࠢࡸ࠭ࠥᥒ")) as outfile:
            json.dump(bstack111l1l1l1_opy_, outfile)
def bstack1l1lllll11_opy_(file_name, logger):
    file_path = bstack1l1l111l111_opy_(bstack11l1l1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᥓ"), file_name, logger)
    bstack111l1l1l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l1l1l_opy_ (u"ࠩࡵࠫᥔ")) as bstack11l1lll1l_opy_:
            bstack111l1l1l1_opy_ = json.load(bstack11l1lll1l_opy_)
    return bstack111l1l1l1_opy_
def bstack1l111l11ll_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩ࠿ࠦࠧᥕ") + file_path + bstack11l1l1l_opy_ (u"ࠫࠥ࠭ᥖ") + str(e))
def bstack1ll1l1111l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l1l1l_opy_ (u"ࠧࡂࡎࡐࡖࡖࡉ࡙ࡄࠢᥗ")
def bstack1l11ll1lll_opy_(config):
    if bstack11l1l1l_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᥘ") in config:
        del (config[bstack11l1l1l_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᥙ")])
        return False
    if bstack1ll1l1111l_opy_() < version.parse(bstack11l1l1l_opy_ (u"ࠨ࠵࠱࠸࠳࠶ࠧᥚ")):
        return False
    if bstack1ll1l1111l_opy_() >= version.parse(bstack11l1l1l_opy_ (u"ࠩ࠷࠲࠶࠴࠵ࠨᥛ")):
        return True
    if bstack11l1l1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪᥜ") in config and config[bstack11l1l1l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᥝ")] is False:
        return False
    else:
        return True
def bstack11l11l11l_opy_(args_list, bstack11lllll11ll_opy_):
    index = -1
    for value in bstack11lllll11ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1llll111_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1llll111_opy_ = bstack1llll111_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l1l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᥞ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l1l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᥟ"), exception=exception)
    def bstack111l1ll111_opy_(self):
        if self.result != bstack11l1l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᥠ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l1l1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦᥡ") in self.exception_type:
            return bstack11l1l1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥᥢ")
        return bstack11l1l1l_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦᥣ")
    def bstack11lll11ll1l_opy_(self):
        if self.result != bstack11l1l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᥤ"):
            return None
        if self.bstack1llll111_opy_:
            return self.bstack1llll111_opy_
        return bstack11lll1lllll_opy_(self.exception)
def bstack11lll1lllll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack11ll1lll11l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack11llll1l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1lllllll_opy_(config, logger):
    try:
        import playwright
        bstack11lllll1l1l_opy_ = playwright.__file__
        bstack11lll1l11l1_opy_ = os.path.split(bstack11lllll1l1l_opy_)
        bstack11lll111l1l_opy_ = bstack11lll1l11l1_opy_[0] + bstack11l1l1l_opy_ (u"ࠬ࠵ࡤࡳ࡫ࡹࡩࡷ࠵ࡰࡢࡥ࡮ࡥ࡬࡫࠯࡭࡫ࡥ࠳ࡨࡲࡩ࠰ࡥ࡯࡭࠳ࡰࡳࠨᥥ")
        os.environ[bstack11l1l1l_opy_ (u"࠭ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠩᥦ")] = bstack1lll1111l1_opy_(config)
        with open(bstack11lll111l1l_opy_, bstack11l1l1l_opy_ (u"ࠧࡳࠩᥧ")) as f:
            file_content = f.read()
            bstack11ll1llll11_opy_ = bstack11l1l1l_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧᥨ")
            bstack11lllllll11_opy_ = file_content.find(bstack11ll1llll11_opy_)
            if bstack11lllllll11_opy_ == -1:
              process = subprocess.Popen(bstack11l1l1l_opy_ (u"ࠤࡱࡴࡲࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹࠨᥩ"), shell=True, cwd=bstack11lll1l11l1_opy_[0])
              process.wait()
              bstack11llll1l11l_opy_ = bstack11l1l1l_opy_ (u"ࠪࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴࠣ࠽ࠪᥪ")
              bstack11llllllll1_opy_ = bstack11l1l1l_opy_ (u"ࠦࠧࠨࠠ࡝ࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࡢࠢ࠼ࠢࡦࡳࡳࡹࡴࠡࡽࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵࠦࡽࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫ࠮ࡁࠠࡪࡨࠣࠬࡵࡸ࡯ࡤࡧࡶࡷ࠳࡫࡮ࡷ࠰ࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝࠮ࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠪࠬ࠿ࠥࠨࠢࠣᥫ")
              bstack11llll1l1ll_opy_ = file_content.replace(bstack11llll1l11l_opy_, bstack11llllllll1_opy_)
              with open(bstack11lll111l1l_opy_, bstack11l1l1l_opy_ (u"ࠬࡽࠧᥬ")) as f:
                f.write(bstack11llll1l1ll_opy_)
    except Exception as e:
        logger.error(bstack1l11l11l1l_opy_.format(str(e)))
def bstack11l111l1ll_opy_():
  try:
    bstack11lllllll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᥭ"))
    bstack11ll1ll1ll1_opy_ = []
    if os.path.exists(bstack11lllllll1l_opy_):
      with open(bstack11lllllll1l_opy_) as f:
        bstack11ll1ll1ll1_opy_ = json.load(f)
      os.remove(bstack11lllllll1l_opy_)
    return bstack11ll1ll1ll1_opy_
  except:
    pass
  return []
def bstack1l11ll11ll_opy_(bstack1llll1111l_opy_):
  try:
    bstack11ll1ll1ll1_opy_ = []
    bstack11lllllll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧ᥮"))
    if os.path.exists(bstack11lllllll1l_opy_):
      with open(bstack11lllllll1l_opy_) as f:
        bstack11ll1ll1ll1_opy_ = json.load(f)
    bstack11ll1ll1ll1_opy_.append(bstack1llll1111l_opy_)
    with open(bstack11lllllll1l_opy_, bstack11l1l1l_opy_ (u"ࠨࡹࠪ᥯")) as f:
        json.dump(bstack11ll1ll1ll1_opy_, f)
  except:
    pass
def bstack11ll11ll1l_opy_(logger, bstack11lll1111ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l1l1l_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᥰ"), bstack11l1l1l_opy_ (u"ࠪࠫᥱ"))
    if test_name == bstack11l1l1l_opy_ (u"ࠫࠬᥲ"):
        test_name = threading.current_thread().__dict__.get(bstack11l1l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡇࡪࡤࡠࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠫᥳ"), bstack11l1l1l_opy_ (u"࠭ࠧᥴ"))
    bstack11ll1ll11l1_opy_ = bstack11l1l1l_opy_ (u"ࠧ࠭ࠢࠪ᥵").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11lll1111ll_opy_:
        bstack1l11lll11_opy_ = os.environ.get(bstack11l1l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ᥶"), bstack11l1l1l_opy_ (u"ࠩ࠳ࠫ᥷"))
        bstack1llll1111_opy_ = {bstack11l1l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ᥸"): test_name, bstack11l1l1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ᥹"): bstack11ll1ll11l1_opy_, bstack11l1l1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ᥺"): bstack1l11lll11_opy_}
        bstack1l111111lll_opy_ = []
        bstack11ll1lll111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡰࡱࡲࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ᥻"))
        if os.path.exists(bstack11ll1lll111_opy_):
            with open(bstack11ll1lll111_opy_) as f:
                bstack1l111111lll_opy_ = json.load(f)
        bstack1l111111lll_opy_.append(bstack1llll1111_opy_)
        with open(bstack11ll1lll111_opy_, bstack11l1l1l_opy_ (u"ࠧࡸࠩ᥼")) as f:
            json.dump(bstack1l111111lll_opy_, f)
    else:
        bstack1llll1111_opy_ = {bstack11l1l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭᥽"): test_name, bstack11l1l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ᥾"): bstack11ll1ll11l1_opy_, bstack11l1l1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ᥿"): str(multiprocessing.current_process().name)}
        if bstack11l1l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨᦀ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1llll1111_opy_)
  except Exception as e:
      logger.warn(bstack11l1l1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡱࡻࡷࡩࡸࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᦁ").format(e))
def bstack1lll1ll1l1_opy_(error_message, test_name, index, logger):
  try:
    bstack11lll1ll1ll_opy_ = []
    bstack1llll1111_opy_ = {bstack11l1l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᦂ"): test_name, bstack11l1l1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᦃ"): error_message, bstack11l1l1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᦄ"): index}
    bstack11ll1ll1111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᦅ"))
    if os.path.exists(bstack11ll1ll1111_opy_):
        with open(bstack11ll1ll1111_opy_) as f:
            bstack11lll1ll1ll_opy_ = json.load(f)
    bstack11lll1ll1ll_opy_.append(bstack1llll1111_opy_)
    with open(bstack11ll1ll1111_opy_, bstack11l1l1l_opy_ (u"ࠪࡻࠬᦆ")) as f:
        json.dump(bstack11lll1ll1ll_opy_, f)
  except Exception as e:
    logger.warn(bstack11l1l1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡲࡰࡤࡲࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᦇ").format(e))
def bstack11l111l1l1_opy_(bstack11l1l1ll1l_opy_, name, logger):
  try:
    bstack1llll1111_opy_ = {bstack11l1l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᦈ"): name, bstack11l1l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᦉ"): bstack11l1l1ll1l_opy_, bstack11l1l1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᦊ"): str(threading.current_thread()._name)}
    return bstack1llll1111_opy_
  except Exception as e:
    logger.warn(bstack11l1l1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡦࡪ࡮ࡡࡷࡧࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᦋ").format(e))
  return
def bstack1l11111llll_opy_():
    return platform.system() == bstack11l1l1l_opy_ (u"࡚ࠩ࡭ࡳࡪ࡯ࡸࡵࠪᦌ")
def bstack1l11l1l11_opy_(bstack11llll1llll_opy_, config, logger):
    bstack11lll1ll11l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack11llll1llll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪ࡮ࡷࡩࡷࠦࡣࡰࡰࡩ࡭࡬ࠦ࡫ࡦࡻࡶࠤࡧࡿࠠࡳࡧࡪࡩࡽࠦ࡭ࡢࡶࡦ࡬࠿ࠦࡻࡾࠤᦍ").format(e))
    return bstack11lll1ll11l_opy_
def bstack1l11lll111l_opy_(bstack11lll1llll1_opy_, bstack1l11111111l_opy_):
    bstack11llll111l1_opy_ = version.parse(bstack11lll1llll1_opy_)
    bstack11llllll1l1_opy_ = version.parse(bstack1l11111111l_opy_)
    if bstack11llll111l1_opy_ > bstack11llllll1l1_opy_:
        return 1
    elif bstack11llll111l1_opy_ < bstack11llllll1l1_opy_:
        return -1
    else:
        return 0
def bstack1ll1l1l1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack11ll1ll1l11_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack11lll11l11l_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack11ll1111ll_opy_(options, framework, bstack1lll11l11_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l1l1l_opy_ (u"ࠫ࡬࡫ࡴࠨᦎ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack11l1ll1l1_opy_ = caps.get(bstack11l1l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᦏ"))
    bstack1l1111111l1_opy_ = True
    bstack1ll1l1l11_opy_ = os.environ[bstack11l1l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᦐ")]
    if bstack11llllll1ll_opy_(caps.get(bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧ࡚࠷ࡈ࠭ᦑ"))) or bstack11llllll1ll_opy_(caps.get(bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡶࡵࡨࡣࡼ࠹ࡣࠨᦒ"))):
        bstack1l1111111l1_opy_ = False
    if bstack1l11ll1lll_opy_({bstack11l1l1l_opy_ (u"ࠤࡸࡷࡪ࡝࠳ࡄࠤᦓ"): bstack1l1111111l1_opy_}):
        bstack11l1ll1l1_opy_ = bstack11l1ll1l1_opy_ or {}
        bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬᦔ")] = bstack11lll11l11l_opy_(framework)
        bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᦕ")] = bstack1l1llll111l_opy_()
        bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨᦖ")] = bstack1ll1l1l11_opy_
        bstack11l1ll1l1_opy_[bstack11l1l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨᦗ")] = bstack1lll11l11_opy_
        if getattr(options, bstack11l1l1l_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨᦘ"), None):
            options.set_capability(bstack11l1l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᦙ"), bstack11l1ll1l1_opy_)
        else:
            options[bstack11l1l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᦚ")] = bstack11l1ll1l1_opy_
    else:
        if getattr(options, bstack11l1l1l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫᦛ"), None):
            options.set_capability(bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬᦜ"), bstack11lll11l11l_opy_(framework))
            options.set_capability(bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᦝ"), bstack1l1llll111l_opy_())
            options.set_capability(bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨᦞ"), bstack1ll1l1l11_opy_)
            options.set_capability(bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨᦟ"), bstack1lll11l11_opy_)
        else:
            options[bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᦠ")] = bstack11lll11l11l_opy_(framework)
            options[bstack11l1l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᦡ")] = bstack1l1llll111l_opy_()
            options[bstack11l1l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᦢ")] = bstack1ll1l1l11_opy_
            options[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᦣ")] = bstack1lll11l11_opy_
    return options
def bstack11lll1lll11_opy_(ws_endpoint, framework):
    bstack1lll11l11_opy_ = bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢᦤ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11l1l1l_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᦥ"))) > 1:
        ws_url = ws_endpoint.split(bstack11l1l1l_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᦦ"))[0]
        if bstack11l1l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫᦧ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack11lll1l1111_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11l1l1l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᦨ"))[1]))
            bstack11lll1l1111_opy_ = bstack11lll1l1111_opy_ or {}
            bstack1ll1l1l11_opy_ = os.environ[bstack11l1l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᦩ")]
            bstack11lll1l1111_opy_[bstack11l1l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬᦪ")] = str(framework) + str(__version__)
            bstack11lll1l1111_opy_[bstack11l1l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᦫ")] = bstack1l1llll111l_opy_()
            bstack11lll1l1111_opy_[bstack11l1l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ᦬")] = bstack1ll1l1l11_opy_
            bstack11lll1l1111_opy_[bstack11l1l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ᦭")] = bstack1lll11l11_opy_
            ws_endpoint = ws_endpoint.split(bstack11l1l1l_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧ᦮"))[0] + bstack11l1l1l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨ᦯") + urllib.parse.quote(json.dumps(bstack11lll1l1111_opy_))
    return ws_endpoint
def bstack111l11lll_opy_():
    global bstack111ll11ll1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack111ll11ll1_opy_ = BrowserType.connect
    return bstack111ll11ll1_opy_
def bstack11lll1lll1_opy_(framework_name):
    global bstack11l1ll11l1_opy_
    bstack11l1ll11l1_opy_ = framework_name
    return framework_name
def bstack1lll11ll1l_opy_(self, *args, **kwargs):
    global bstack111ll11ll1_opy_
    try:
        global bstack11l1ll11l1_opy_
        if bstack11l1l1l_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᦰ") in kwargs:
            kwargs[bstack11l1l1l_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨᦱ")] = bstack11lll1lll11_opy_(
                kwargs.get(bstack11l1l1l_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩᦲ"), None),
                bstack11l1ll11l1_opy_
            )
    except Exception as e:
        logger.error(bstack11l1l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡨࡧࡰࡴ࠼ࠣࡿࢂࠨᦳ").format(str(e)))
    return bstack111ll11ll1_opy_(self, *args, **kwargs)
def bstack11lll1l1ll1_opy_(bstack11ll1ll1l1l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1l1lll1ll_opy_(bstack11ll1ll1l1l_opy_, bstack11l1l1l_opy_ (u"ࠢࠣᦴ"))
        if proxies and proxies.get(bstack11l1l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢᦵ")):
            parsed_url = urlparse(proxies.get(bstack11l1l1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣᦶ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l1l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ᦷ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l1l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧᦸ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l1l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨᦹ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l1l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩᦺ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1ll1l1ll1_opy_(bstack11ll1ll1l1l_opy_):
    bstack11llll111ll_opy_ = {
        bstack1l11ll1l111_opy_[bstack1l111111l1l_opy_]: bstack11ll1ll1l1l_opy_[bstack1l111111l1l_opy_]
        for bstack1l111111l1l_opy_ in bstack11ll1ll1l1l_opy_
        if bstack1l111111l1l_opy_ in bstack1l11ll1l111_opy_
    }
    bstack11llll111ll_opy_[bstack11l1l1l_opy_ (u"ࠢࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠢᦻ")] = bstack11lll1l1ll1_opy_(bstack11ll1ll1l1l_opy_, bstack11111l11_opy_.get_property(bstack11l1l1l_opy_ (u"ࠣࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠣᦼ")))
    bstack1l11111l1l1_opy_ = [element.lower() for element in bstack1l11l1l11l1_opy_]
    bstack11lllll111l_opy_(bstack11llll111ll_opy_, bstack1l11111l1l1_opy_)
    return bstack11llll111ll_opy_
def bstack11lllll111l_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l1l1l_opy_ (u"ࠤ࠭࠮࠯࠰ࠢᦽ")
    for value in d.values():
        if isinstance(value, dict):
            bstack11lllll111l_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack11lllll111l_opy_(item, keys)
def bstack11lll11llll_opy_():
    bstack11ll1ll11ll_opy_ = [os.environ.get(bstack11l1l1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡍࡑࡋࡓࡠࡆࡌࡖࠧᦾ")), os.path.join(os.path.expanduser(bstack11l1l1l_opy_ (u"ࠦࢃࠨᦿ")), bstack11l1l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᧀ")), os.path.join(bstack11l1l1l_opy_ (u"࠭࠯ࡵ࡯ࡳࠫᧁ"), bstack11l1l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᧂ"))]
    for path in bstack11ll1ll11ll_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11l1l1l_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࠧࠣᧃ") + str(path) + bstack11l1l1l_opy_ (u"ࠤࠪࠤࡪࡾࡩࡴࡶࡶ࠲ࠧᧄ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11l1l1l_opy_ (u"ࠥࡋ࡮ࡼࡩ࡯ࡩࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠡࡨࡲࡶࠥ࠭ࠢᧅ") + str(path) + bstack11l1l1l_opy_ (u"ࠦࠬࠨᧆ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11l1l1l_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࠫࠧᧇ") + str(path) + bstack11l1l1l_opy_ (u"ࠨࠧࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡫ࡥࡸࠦࡴࡩࡧࠣࡶࡪࡷࡵࡪࡴࡨࡨࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯ࡵ࠱ࠦᧈ"))
            else:
                logger.debug(bstack11l1l1l_opy_ (u"ࠢࡄࡴࡨࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠࠨࠤᧉ") + str(path) + bstack11l1l1l_opy_ (u"ࠣࠩࠣࡻ࡮ࡺࡨࠡࡹࡵ࡭ࡹ࡫ࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱ࠲ࠧ᧊"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11l1l1l_opy_ (u"ࠤࡒࡴࡪࡸࡡࡵ࡫ࡲࡲࠥࡹࡵࡤࡥࡨࡩࡩ࡫ࡤࠡࡨࡲࡶࠥ࠭ࠢ᧋") + str(path) + bstack11l1l1l_opy_ (u"ࠥࠫ࠳ࠨ᧌"))
            return path
        except Exception as e:
            logger.debug(bstack11l1l1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡺࡶࠠࡧ࡫࡯ࡩࠥ࠭ࡻࡱࡣࡷ࡬ࢂ࠭࠺ࠡࠤ᧍") + str(e) + bstack11l1l1l_opy_ (u"ࠧࠨ᧎"))
    logger.debug(bstack11l1l1l_opy_ (u"ࠨࡁ࡭࡮ࠣࡴࡦࡺࡨࡴࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠥ᧏"))
    return None
@measure(event_name=EVENTS.bstack1l11l11ll11_opy_, stage=STAGE.SINGLE)
def bstack1ll1l11ll11_opy_(binary_path, bstack1ll11ll1lll_opy_, bs_config):
    logger.debug(bstack11l1l1l_opy_ (u"ࠢࡄࡷࡵࡶࡪࡴࡴࠡࡅࡏࡍࠥࡖࡡࡵࡪࠣࡪࡴࡻ࡮ࡥ࠼ࠣࡿࢂࠨ᧐").format(binary_path))
    bstack11llll11111_opy_ = bstack11l1l1l_opy_ (u"ࠨࠩ᧑")
    bstack11lll11l1l1_opy_ = {
        bstack11l1l1l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ᧒"): __version__,
        bstack11l1l1l_opy_ (u"ࠥࡳࡸࠨ᧓"): platform.system(),
        bstack11l1l1l_opy_ (u"ࠦࡴࡹ࡟ࡢࡴࡦ࡬ࠧ᧔"): platform.machine(),
        bstack11l1l1l_opy_ (u"ࠧࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠥ᧕"): bstack11l1l1l_opy_ (u"࠭࠰ࠨ᧖"),
        bstack11l1l1l_opy_ (u"ࠢࡴࡦ࡮ࡣࡱࡧ࡮ࡨࡷࡤ࡫ࡪࠨ᧗"): bstack11l1l1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ᧘")
    }
    try:
        if binary_path:
            bstack11lll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ᧙")] = subprocess.check_output([binary_path, bstack11l1l1l_opy_ (u"ࠥࡺࡪࡸࡳࡪࡱࡱࠦ᧚")]).strip().decode(bstack11l1l1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᧛"))
        response = requests.request(
            bstack11l1l1l_opy_ (u"ࠬࡍࡅࡕࠩ᧜"),
            url=bstack1lll111l1l_opy_(bstack1l11ll11111_opy_),
            headers=None,
            auth=(bs_config[bstack11l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ᧝")], bs_config[bstack11l1l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ᧞")]),
            json=None,
            params=bstack11lll11l1l1_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11l1l1l_opy_ (u"ࠨࡷࡵࡰࠬ᧟") in data.keys() and bstack11l1l1l_opy_ (u"ࠩࡸࡴࡩࡧࡴࡦࡦࡢࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ᧠") in data.keys():
            logger.debug(bstack11l1l1l_opy_ (u"ࠥࡒࡪ࡫ࡤࠡࡶࡲࠤࡺࡶࡤࡢࡶࡨࠤࡧ࡯࡮ࡢࡴࡼ࠰ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡢࡪࡰࡤࡶࡾࠦࡶࡦࡴࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠦ᧡").format(bstack11lll11l1l1_opy_[bstack11l1l1l_opy_ (u"ࠫࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ᧢")]))
            bstack1l11111ll1l_opy_ = bstack1l111111ll1_opy_(data[bstack11l1l1l_opy_ (u"ࠬࡻࡲ࡭ࠩ᧣")], bstack1ll11ll1lll_opy_)
            bstack11llll11111_opy_ = os.path.join(bstack1ll11ll1lll_opy_, bstack1l11111ll1l_opy_)
            os.chmod(bstack11llll11111_opy_, 0o777) # bstack11ll1llll1l_opy_ permission
            return bstack11llll11111_opy_
    except Exception as e:
        logger.debug(bstack11l1l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡱࡩࡼࠦࡓࡅࡍࠣࡿࢂࠨ᧤").format(e))
    return binary_path
@measure(event_name=EVENTS.bstack1l11l1l1lll_opy_, stage=STAGE.SINGLE)
def bstack1l111111ll1_opy_(bstack11lll1lll1l_opy_, bstack1l1111l1111_opy_):
    logger.debug(bstack11l1l1l_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳ࠺ࠡࠤ᧥") + str(bstack11lll1lll1l_opy_) + bstack11l1l1l_opy_ (u"ࠣࠤ᧦"))
    zip_path = os.path.join(bstack1l1111l1111_opy_, bstack11l1l1l_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࡥࡦࡪ࡮ࡨ࠲ࡿ࡯ࡰࠣ᧧"))
    bstack1l11111ll1l_opy_ = bstack11l1l1l_opy_ (u"ࠪࠫ᧨")
    with requests.get(bstack11lll1lll1l_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11l1l1l_opy_ (u"ࠦࡼࡨࠢ᧩")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11l1l1l_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾ࠴ࠢ᧪"))
    with zipfile.ZipFile(zip_path, bstack11l1l1l_opy_ (u"࠭ࡲࠨ᧫")) as zip_ref:
        bstack11lll1l111l_opy_ = zip_ref.namelist()
        if len(bstack11lll1l111l_opy_) > 0:
            bstack1l11111ll1l_opy_ = bstack11lll1l111l_opy_[0] # bstack11lll1l1l1l_opy_ bstack1l11l1ll111_opy_ will be bstack1l11111ll11_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1l1111l1111_opy_)
        logger.debug(bstack11l1l1l_opy_ (u"ࠢࡇ࡫࡯ࡩࡸࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥ࡫ࡸࡵࡴࡤࡧࡹ࡫ࡤࠡࡶࡲࠤࠬࠨ᧬") + str(bstack1l1111l1111_opy_) + bstack11l1l1l_opy_ (u"ࠣࠩࠥ᧭"))
    os.remove(zip_path)
    return bstack1l11111ll1l_opy_
def get_cli_dir():
    bstack11llll11ll1_opy_ = bstack11lll11llll_opy_()
    if bstack11llll11ll1_opy_:
        bstack1ll11ll1lll_opy_ = os.path.join(bstack11llll11ll1_opy_, bstack11l1l1l_opy_ (u"ࠤࡦࡰ࡮ࠨ᧮"))
        if not os.path.exists(bstack1ll11ll1lll_opy_):
            os.makedirs(bstack1ll11ll1lll_opy_, mode=0o777, exist_ok=True)
        return bstack1ll11ll1lll_opy_
    else:
        raise FileNotFoundError(bstack11l1l1l_opy_ (u"ࠥࡒࡴࠦࡷࡳ࡫ࡷࡥࡧࡲࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽ࠳ࠨ᧯"))
def bstack1ll1ll11l11_opy_(bstack1ll11ll1lll_opy_):
    bstack11l1l1l_opy_ (u"ࠦࠧࠨࡇࡦࡶࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡲࠥࡧࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠳ࠨࠢࠣ᧰")
    bstack11llll11lll_opy_ = [
        os.path.join(bstack1ll11ll1lll_opy_, f)
        for f in os.listdir(bstack1ll11ll1lll_opy_)
        if os.path.isfile(os.path.join(bstack1ll11ll1lll_opy_, f)) and f.startswith(bstack11l1l1l_opy_ (u"ࠧࡨࡩ࡯ࡣࡵࡽ࠲ࠨ᧱"))
    ]
    if len(bstack11llll11lll_opy_) > 0:
        return max(bstack11llll11lll_opy_, key=os.path.getmtime) # get bstack11llllll111_opy_ binary
    return bstack11l1l1l_opy_ (u"ࠨࠢ᧲")