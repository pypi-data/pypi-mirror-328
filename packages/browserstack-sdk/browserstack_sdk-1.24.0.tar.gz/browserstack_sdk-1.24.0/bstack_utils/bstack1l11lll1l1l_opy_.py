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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack1l11lll111l_opy_
from browserstack_sdk.bstack111l11l1_opy_ import bstack111lll1l_opy_
def _1l11lll11l1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1l11llll11l_opy_:
    def __init__(self, handler):
        self._1l11lll1111_opy_ = {}
        self._1l11llll1ll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack111lll1l_opy_.version()
        if bstack1l11lll111l_opy_(pytest_version, bstack11l1l1l_opy_ (u"ࠢ࠹࠰࠴࠲࠶ࠨᐧ")) >= 0:
            self._1l11lll1111_opy_[bstack11l1l1l_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᐨ")] = Module._register_setup_function_fixture
            self._1l11lll1111_opy_[bstack11l1l1l_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᐩ")] = Module._register_setup_module_fixture
            self._1l11lll1111_opy_[bstack11l1l1l_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᐪ")] = Class._register_setup_class_fixture
            self._1l11lll1111_opy_[bstack11l1l1l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᐫ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack1l11lllll11_opy_(bstack11l1l1l_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᐬ"))
            Module._register_setup_module_fixture = self.bstack1l11lllll11_opy_(bstack11l1l1l_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᐭ"))
            Class._register_setup_class_fixture = self.bstack1l11lllll11_opy_(bstack11l1l1l_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᐮ"))
            Class._register_setup_method_fixture = self.bstack1l11lllll11_opy_(bstack11l1l1l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᐯ"))
        else:
            self._1l11lll1111_opy_[bstack11l1l1l_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᐰ")] = Module._inject_setup_function_fixture
            self._1l11lll1111_opy_[bstack11l1l1l_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᐱ")] = Module._inject_setup_module_fixture
            self._1l11lll1111_opy_[bstack11l1l1l_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᐲ")] = Class._inject_setup_class_fixture
            self._1l11lll1111_opy_[bstack11l1l1l_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᐳ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack1l11lllll11_opy_(bstack11l1l1l_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᐴ"))
            Module._inject_setup_module_fixture = self.bstack1l11lllll11_opy_(bstack11l1l1l_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᐵ"))
            Class._inject_setup_class_fixture = self.bstack1l11lllll11_opy_(bstack11l1l1l_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᐶ"))
            Class._inject_setup_method_fixture = self.bstack1l11lllll11_opy_(bstack11l1l1l_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᐷ"))
    def bstack1l11lllll1l_opy_(self, bstack1l11lll1ll1_opy_, hook_type):
        bstack1l11ll1lll1_opy_ = id(bstack1l11lll1ll1_opy_.__class__)
        if (bstack1l11ll1lll1_opy_, hook_type) in self._1l11llll1ll_opy_:
            return
        meth = getattr(bstack1l11lll1ll1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1l11llll1ll_opy_[(bstack1l11ll1lll1_opy_, hook_type)] = meth
            setattr(bstack1l11lll1ll1_opy_, hook_type, self.bstack1l11llll111_opy_(hook_type, bstack1l11ll1lll1_opy_))
    def bstack1l11ll1llll_opy_(self, instance, bstack1l11lll11ll_opy_):
        if bstack1l11lll11ll_opy_ == bstack11l1l1l_opy_ (u"ࠥࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪࠨᐸ"):
            self.bstack1l11lllll1l_opy_(instance.obj, bstack11l1l1l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧᐹ"))
            self.bstack1l11lllll1l_opy_(instance.obj, bstack11l1l1l_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤᐺ"))
        if bstack1l11lll11ll_opy_ == bstack11l1l1l_opy_ (u"ࠨ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᐻ"):
            self.bstack1l11lllll1l_opy_(instance.obj, bstack11l1l1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࠨᐼ"))
            self.bstack1l11lllll1l_opy_(instance.obj, bstack11l1l1l_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠥᐽ"))
        if bstack1l11lll11ll_opy_ == bstack11l1l1l_opy_ (u"ࠤࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠤᐾ"):
            self.bstack1l11lllll1l_opy_(instance.obj, bstack11l1l1l_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠣᐿ"))
            self.bstack1l11lllll1l_opy_(instance.obj, bstack11l1l1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠧᑀ"))
        if bstack1l11lll11ll_opy_ == bstack11l1l1l_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࠨᑁ"):
            self.bstack1l11lllll1l_opy_(instance.obj, bstack11l1l1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠧᑂ"))
            self.bstack1l11lllll1l_opy_(instance.obj, bstack11l1l1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠤᑃ"))
    @staticmethod
    def bstack1l11llll1l1_opy_(hook_type, func, args):
        if hook_type in [bstack11l1l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᑄ"), bstack11l1l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᑅ")]:
            _1l11lll11l1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1l11llll111_opy_(self, hook_type, bstack1l11ll1lll1_opy_):
        def bstack1l11llllll1_opy_(arg=None):
            self.handler(hook_type, bstack11l1l1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪᑆ"))
            result = None
            try:
                bstack1l1l1ll1ll1_opy_ = self._1l11llll1ll_opy_[(bstack1l11ll1lll1_opy_, hook_type)]
                self.bstack1l11llll1l1_opy_(hook_type, bstack1l1l1ll1ll1_opy_, (arg,))
                result = Result(result=bstack11l1l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᑇ"))
            except Exception as e:
                result = Result(result=bstack11l1l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᑈ"), exception=e)
                self.handler(hook_type, bstack11l1l1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᑉ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l1l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᑊ"), result)
        def bstack1l11lll1lll_opy_(this, arg=None):
            self.handler(hook_type, bstack11l1l1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨᑋ"))
            result = None
            exception = None
            try:
                self.bstack1l11llll1l1_opy_(hook_type, self._1l11llll1ll_opy_[hook_type], (this, arg))
                result = Result(result=bstack11l1l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᑌ"))
            except Exception as e:
                result = Result(result=bstack11l1l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᑍ"), exception=e)
                self.handler(hook_type, bstack11l1l1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᑎ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l1l1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᑏ"), result)
        if hook_type in [bstack11l1l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬᑐ"), bstack11l1l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᑑ")]:
            return bstack1l11lll1lll_opy_
        return bstack1l11llllll1_opy_
    def bstack1l11lllll11_opy_(self, bstack1l11lll11ll_opy_):
        def bstack1l11lll1l11_opy_(this, *args, **kwargs):
            self.bstack1l11ll1llll_opy_(this, bstack1l11lll11ll_opy_)
            self._1l11lll1111_opy_[bstack1l11lll11ll_opy_](this, *args, **kwargs)
        return bstack1l11lll1l11_opy_