import datetime

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox

import schedule.schedule as schedule
from cvworks_gui.ui.calendar_ui import Ui_Form
from cvworks_gui.styling import *


class CalendarView(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"CVWorks")
        self.date_clicked(datetime.date.today())
        self.calendarWidget.clicked.connect(
            lambda d: self.date_clicked(self.to_python_date(d))
        )
        self.show()

    def date_clicked(self, d: datetime.date):
        works = schedule.working_this_day(d)
        self.label.setText(f"{WORKS[works]}")
        self.label.setStyleSheet(STYLESHEET[works])

    def keyReleaseEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_A:
                self._show_about_dialog()
                return

        event.ignore()

    @staticmethod
    def to_python_date(d: QDate):
        return datetime.date(d.year(), d.month(), d.day())

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
