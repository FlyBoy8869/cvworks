from PyQt6.QtCore import QDate, Qt, pyqtSignal, QSettings, QSize, QPoint
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox

from cvworks_gui.styling import *
from cvworks_gui.ui.calendar_ui import Ui_Form

settings = QSettings("CharlesIndustries", "CVWorks")


class CalendarView(QWidget, Ui_Form):
    show_today: pyqtSignal = pyqtSignal(QDate)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"CVWorks")

        # hook up signals
        self.show_today.connect(self._go_to_today)

        self.show()

    def closeEvent(self, event):
        settings.setValue("calendarView/size", self.size())
        settings.setValue("calendarView/position", self.pos())
        event.accept()

    def keyReleaseEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_A:
                self._show_about_dialog()
                return
            if event.key() == Qt.Key.Key_T:
                self.show_today.emit(QDate.currentDate())
                return
        event.ignore()

    def showEvent(self, event):
        self.move(settings.value("calendarView/position", QPoint(100, 100)))
        self.resize(settings.value("calendarView/size", QSize(400, 400)))
        event.accept()

    def _go_to_today(self, current_date: QDate):
        self.calendarWidget.setSelectedDate(current_date)

    def _show_about_dialog(self):
        text = (
            f"{AUTHOR_HEADING}"
            f"{AUTHOR_NAME}"
            f"{AUTHOR_EMAIL}"
            f"{VERSION_HEADING}"
            f"{OPERATING_SYSTEM}"
            f"{PROGRAM_VERSION}"
        )

        msg_box = QMessageBox(parent=self)
        msg_box.setIconPixmap(QPixmap(INFO_ICON))
        msg_box.setWindowTitle("About CVWorks")
        msg_box.setText(text)
        msg_box.exec()
