import datetime

from PyQt6.QtCore import QDate, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox

import schedule.schedule as schedule
from cvworks_gui.ui.calendar_ui import Ui_Form
from cvworks_gui.styling import *


class CalendarView(QWidget, Ui_Form):
    show_today: pyqtSignal = pyqtSignal(QDate)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"CVWorks")
        self.date_clicked(QDate.currentDate())
        self.calendarWidget.clicked.connect(self.date_clicked)
        self.show_today.connect(self._go_to_today)
        self.show()

    def keyReleaseEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_A:
                self._show_about_dialog()
                return
            if event.key() == Qt.Key.Key_T:
                self.show_today.emit(QDate.currentDate())
                return

        event.ignore()

    def date_clicked(self, d: QDate):
        def to_python_date(d: QDate):
            return datetime.date(d.year(), d.month(), d.day())

        works = schedule.working_this_day(to_python_date(d))
        self.label.setText(f"{WORKS[works]}")
        self.label.setStyleSheet(STYLESHEET[works])

    def _go_to_today(self, current_date: QDate):
        self.calendarWidget.setSelectedDate(current_date)
        self.date_clicked(current_date)

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
