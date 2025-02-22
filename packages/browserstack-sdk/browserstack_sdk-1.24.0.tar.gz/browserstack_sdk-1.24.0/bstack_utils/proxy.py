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
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack1l11lllllll_opy_
bstack11111l11_opy_ = Config.bstack111ll1ll_opy_()
def bstack1l1l1111111_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1l1l1111l11_opy_(bstack1l1l1111ll1_opy_, bstack1l1l11111ll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1l1l1111ll1_opy_):
        with open(bstack1l1l1111ll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1l1l1111111_opy_(bstack1l1l1111ll1_opy_):
        pac = get_pac(url=bstack1l1l1111ll1_opy_)
    else:
        raise Exception(bstack11l1l1l_opy_ (u"ࠫࡕࡧࡣࠡࡨ࡬ࡰࡪࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠺ࠡࡽࢀࠫᐁ").format(bstack1l1l1111ll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l1l1l_opy_ (u"ࠧ࠾࠮࠹࠰࠻࠲࠽ࠨᐂ"), 80))
        bstack1l1l11111l1_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1l1l11111l1_opy_ = bstack11l1l1l_opy_ (u"࠭࠰࠯࠲࠱࠴࠳࠶ࠧᐃ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1l1l11111ll_opy_, bstack1l1l11111l1_opy_)
    return proxy_url
def bstack1ll11l1111_opy_(config):
    return bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᐄ") in config or bstack11l1l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᐅ") in config
def bstack1lll1111l1_opy_(config):
    if not bstack1ll11l1111_opy_(config):
        return
    if config.get(bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᐆ")):
        return config.get(bstack11l1l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᐇ"))
    if config.get(bstack11l1l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᐈ")):
        return config.get(bstack11l1l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᐉ"))
def bstack1l1lll1ll_opy_(config, bstack1l1l11111ll_opy_):
    proxy = bstack1lll1111l1_opy_(config)
    proxies = {}
    if config.get(bstack11l1l1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᐊ")) or config.get(bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᐋ")):
        if proxy.endswith(bstack11l1l1l_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ᐌ")):
            proxies = bstack1lll11l11l_opy_(proxy, bstack1l1l11111ll_opy_)
        else:
            proxies = {
                bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᐍ"): proxy
            }
    bstack11111l11_opy_.set_property(bstack11l1l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪᐎ"), proxies)
    return proxies
def bstack1lll11l11l_opy_(bstack1l1l1111ll1_opy_, bstack1l1l11111ll_opy_):
    proxies = {}
    global bstack1l1l1111l1l_opy_
    if bstack11l1l1l_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧᐏ") in globals():
        return bstack1l1l1111l1l_opy_
    try:
        proxy = bstack1l1l1111l11_opy_(bstack1l1l1111ll1_opy_, bstack1l1l11111ll_opy_)
        if bstack11l1l1l_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧᐐ") in proxy:
            proxies = {}
        elif bstack11l1l1l_opy_ (u"ࠨࡈࡕࡖࡓࠦᐑ") in proxy or bstack11l1l1l_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨᐒ") in proxy or bstack11l1l1l_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢᐓ") in proxy:
            bstack1l1l111111l_opy_ = proxy.split(bstack11l1l1l_opy_ (u"ࠤࠣࠦᐔ"))
            if bstack11l1l1l_opy_ (u"ࠥ࠾࠴࠵ࠢᐕ") in bstack11l1l1l_opy_ (u"ࠦࠧᐖ").join(bstack1l1l111111l_opy_[1:]):
                proxies = {
                    bstack11l1l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᐗ"): bstack11l1l1l_opy_ (u"ࠨࠢᐘ").join(bstack1l1l111111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᐙ"): str(bstack1l1l111111l_opy_[0]).lower() + bstack11l1l1l_opy_ (u"ࠣ࠼࠲࠳ࠧᐚ") + bstack11l1l1l_opy_ (u"ࠤࠥᐛ").join(bstack1l1l111111l_opy_[1:])
                }
        elif bstack11l1l1l_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤᐜ") in proxy:
            bstack1l1l111111l_opy_ = proxy.split(bstack11l1l1l_opy_ (u"ࠦࠥࠨᐝ"))
            if bstack11l1l1l_opy_ (u"ࠧࡀ࠯࠰ࠤᐞ") in bstack11l1l1l_opy_ (u"ࠨࠢᐟ").join(bstack1l1l111111l_opy_[1:]):
                proxies = {
                    bstack11l1l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᐠ"): bstack11l1l1l_opy_ (u"ࠣࠤᐡ").join(bstack1l1l111111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᐢ"): bstack11l1l1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᐣ") + bstack11l1l1l_opy_ (u"ࠦࠧᐤ").join(bstack1l1l111111l_opy_[1:])
                }
        else:
            proxies = {
                bstack11l1l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᐥ"): proxy
            }
    except Exception as e:
        print(bstack11l1l1l_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥᐦ"), bstack1l11lllllll_opy_.format(bstack1l1l1111ll1_opy_, str(e)))
    bstack1l1l1111l1l_opy_ = proxies
    return proxies