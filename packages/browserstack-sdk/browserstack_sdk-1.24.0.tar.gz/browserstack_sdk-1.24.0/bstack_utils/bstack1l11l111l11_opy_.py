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
import threading
import logging
logger = logging.getLogger(__name__)
bstack1l1111l1lll_opy_ = 1000
bstack1l1111l1l11_opy_ = 2
class bstack1l1111lll11_opy_:
    def __init__(self, handler, bstack1l1111l1ll1_opy_=bstack1l1111l1lll_opy_, bstack1l1111ll111_opy_=bstack1l1111l1l11_opy_):
        self.queue = []
        self.handler = handler
        self.bstack1l1111l1ll1_opy_ = bstack1l1111l1ll1_opy_
        self.bstack1l1111ll111_opy_ = bstack1l1111ll111_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1lll11111ll_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack1l1111ll1ll_opy_()
    def bstack1l1111ll1ll_opy_(self):
        self.bstack1lll11111ll_opy_ = threading.Event()
        def bstack1l1111l1l1l_opy_():
            self.bstack1lll11111ll_opy_.wait(self.bstack1l1111ll111_opy_)
            if not self.bstack1lll11111ll_opy_.is_set():
                self.bstack1l1111l11ll_opy_()
        self.timer = threading.Thread(target=bstack1l1111l1l1l_opy_, daemon=True)
        self.timer.start()
    def bstack1l1111ll11l_opy_(self):
        try:
            if self.bstack1lll11111ll_opy_ and not self.bstack1lll11111ll_opy_.is_set():
                self.bstack1lll11111ll_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack11l1l1l_opy_ (u"ࠧ࡜ࡵࡷࡳࡵࡥࡴࡪ࡯ࡨࡶࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࠫ៟") + (str(e) or bstack11l1l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡧࡴࡴࡶࡦࡴࡷࡩࡩࠦࡴࡰࠢࡶࡸࡷ࡯࡮ࡨࠤ០")))
        finally:
            self.timer = None
    def bstack1l1111ll1l1_opy_(self):
        if self.timer:
            self.bstack1l1111ll11l_opy_()
        self.bstack1l1111ll1ll_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack1l1111l1ll1_opy_:
                threading.Thread(target=self.bstack1l1111l11ll_opy_).start()
    def bstack1l1111l11ll_opy_(self, source = bstack11l1l1l_opy_ (u"ࠩࠪ១")):
        with self.lock:
            if not self.queue:
                self.bstack1l1111ll1l1_opy_()
                return
            data = self.queue[:self.bstack1l1111l1ll1_opy_]
            del self.queue[:self.bstack1l1111l1ll1_opy_]
        self.handler(data)
        if source != bstack11l1l1l_opy_ (u"ࠪࡷ࡭ࡻࡴࡥࡱࡺࡲࠬ២"):
            self.bstack1l1111ll1l1_opy_()
    def shutdown(self):
        self.bstack1l1111ll11l_opy_()
        while self.queue:
            self.bstack1l1111l11ll_opy_(source=bstack11l1l1l_opy_ (u"ࠫࡸ࡮ࡵࡵࡦࡲࡻࡳ࠭៣"))