# Hide Welcome Panels
# 在开始页面画出来之前，就把"开始"栏和"新闻"栏隐藏掉，避免闪烁。
# 兼容 Krita 5.3 (PyQt5) 和 Krita 6.0 (PyQt6)。

from krita import Extension

try:
    from PyQt6.QtCore import QObject, QEvent
    from PyQt6.QtWidgets import QApplication, QWidget
except ImportError:
    from PyQt5.QtCore import QObject, QEvent
    from PyQt5.QtWidgets import QApplication, QWidget

# 要隐藏的栏（对象名来自 Krita 源码 libs/ui/forms/KisWelcomePage.ui）
# 想连最近文件也隐藏，加上 "widgetRecentImagesColumn"
HIDE_NAMES = {"widgetCenter", "widgetRight"}
PAGE_NAME = "KisWelcomePage"


def _on_welcome_page(widget):
    p = widget.parentWidget()
    while p is not None:
        if p.objectName() == PAGE_NAME:
            return True
        p = p.parentWidget()
    return False


class _Filter(QObject):
    def eventFilter(self, obj, event):
        # Show 事件在控件第一次显示之前发出，这时隐藏就不会闪
        if event.type() in (QEvent.Type.Show, QEvent.Type.Polish) \
                and isinstance(obj, QWidget) \
                and obj.objectName() in HIDE_NAMES \
                and _on_welcome_page(obj):
            obj.hide()
            return event.type() == QEvent.Type.Show
        return False


class HideWelcomePanels(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self._filter = None

    def setup(self):
        # setup() 在主窗口创建之前调用，比样式表早
        self._filter = _Filter()
        QApplication.instance().installEventFilter(self._filter)

    def createActions(self, window):
        pass
