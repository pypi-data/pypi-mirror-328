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
import abc
from browserstack_sdk.sdk_cli.bstack11111ll1l1_opy_ import bstack11111ll11l_opy_
class bstack1111l1ll11_opy_(abc.ABC):
    bin_session_id: str
    bstack11111ll1l1_opy_: bstack11111ll11l_opy_
    def __init__(self):
        self.bstack1111l11ll1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack11111ll1l1_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack11111ll111_opy_(self):
        return (self.bstack1111l11ll1_opy_ != None and self.bin_session_id != None and self.bstack11111ll1l1_opy_ != None)
    def configure(self, bstack1111l11ll1_opy_, config, bin_session_id: str, bstack11111ll1l1_opy_: bstack11111ll11l_opy_):
        self.bstack1111l11ll1_opy_ = bstack1111l11ll1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack11111ll1l1_opy_ = bstack11111ll1l1_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11l1l1l_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࡪࠠ࡮ࡱࡧࡹࡱ࡫ࠠࡼࡵࡨࡰ࡫࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠ࠰ࡢࡣࡳࡧ࡭ࡦࡡࡢࢁ࠿ࠦࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠽ࠣဘ") + str(self.bin_session_id) + bstack11l1l1l_opy_ (u"ࠧࠨမ"))
    def bstack1111l11l1l_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11l1l1l_opy_ (u"ࠨࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡒࡴࡴࡥࠣယ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False