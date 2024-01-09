import datetime

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import QWidget, QMessageBox

import schedule.schedule as schedule
from cvworks_gui.ui.calendar_ui import Ui_Form

from version import VERSION


WORKS = {True: "WORKING", False: "OFF"}

WORKS_STYLESHEET = (
    "background-color: red; color: yellow; "
    "border: 2px solid yellow; border-radius: 6px; font-weight: bold;"
)
OFF_STYLESHEET = (
    "background-color: green; color: white; "
    "border: 2px solid white; border-radius: 6px; font-weight: bold;"
)
STYLESHEET = {True: WORKS_STYLESHEET, False: OFF_STYLESHEET}

# About Dialog
INFO_DIALOG_HEADING_WEIGHT = 500
INFO_DIALOG_TEXT_SIZE = 10
INFO_DIALOG_TEXT_FONT_WEIGHT = 300

AUTHOR_HEADING = f"<p><span style='font-weight: {INFO_DIALOG_HEADING_WEIGHT};'>Written by:</span><br>"
AUTHOR_NAME = (
    f"<span style='font-weight: {INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {INFO_DIALOG_TEXT_SIZE}px;'>Charles Cognato</span><br>"
)
AUTHOR_EMAIL = (
    f"<span style='font-weight: {INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {INFO_DIALOG_TEXT_SIZE}px;'>charlescognato@gmail.com</span></p>"
)
VERSION_HEADING = (
    f"<p><span style='font-weight: {INFO_DIALOG_HEADING_WEIGHT};'>Version:</span><br>"
)
PROGRAM_VERSION = (
    f"<span style='font-weight: {INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {INFO_DIALOG_TEXT_SIZE}px;'>{VERSION}</span></p>"
)


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
            f"{PROGRAM_VERSION}"
        )

        QMessageBox(
            QMessageBox.Icon.Information,
            "About CVWorks",
            text,
            parent=self,
        ).exec()
