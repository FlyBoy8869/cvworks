from PyQt6.QtCore import QSettings

from cvworks_gui import ORGANIZATION, APPLICATION

settings = QSettings(QSettings.Scope.UserScope, ORGANIZATION, APPLICATION)
