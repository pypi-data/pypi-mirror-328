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
class RobotHandler():
    def __init__(self, args, logger, bstack1111llll_opy_, bstack111l1111_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111llll_opy_ = bstack1111llll_opy_
        self.bstack111l1111_opy_ = bstack111l1111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1l11ll_opy_(bstack111l1ll11l_opy_):
        bstack111l1l1ll1_opy_ = []
        if bstack111l1ll11l_opy_:
            tokens = str(os.path.basename(bstack111l1ll11l_opy_)).split(bstack11l1l1l_opy_ (u"ࠦࡤࠨ࿄"))
            camelcase_name = bstack11l1l1l_opy_ (u"ࠧࠦࠢ࿅").join(t.title() for t in tokens)
            suite_name, bstack111l1l1lll_opy_ = os.path.splitext(camelcase_name)
            bstack111l1l1ll1_opy_.append(suite_name)
        return bstack111l1l1ll1_opy_
    @staticmethod
    def bstack111l1ll111_opy_(typename):
        if bstack11l1l1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤ࿆") in typename:
            return bstack11l1l1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣ࿇")
        return bstack11l1l1l_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤ࿈")