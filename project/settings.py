from irekua_dev_settings.settings import *
from irekua_database.settings import *
from selia_visualizers.settings import *


INSTALLED_APPS = (
    SELIA_VISUALIZERS_APPS +
    IREKUA_DATABASE_APPS +
    IREKUA_BASE_APPS
)
