from .hide_welcome_panels import HideWelcomePanels
from krita import Krita

app = Krita.instance()
app.addExtension(HideWelcomePanels(app))
