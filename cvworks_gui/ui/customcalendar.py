import datetime

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import QCalendarWidget

from schedule import schedule


def to_python_date(d: QDate):
    return datetime.date(d.year(), d.month(), d.day())


class CustomCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintCell(self, painter, rect, date: QDate):
        if date == self.selectedDate():
            working = schedule.working_this_day(to_python_date(date))
            if working:
                background_color = Qt.GlobalColor.red
                painter.setPen(Qt.GlobalColor.yellow)
            else:
                background_color = Qt.GlobalColor.darkGreen

            painter.fillRect(rect, background_color)
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, f"{date.day()}")
            return

        super().paintCell(painter, rect, date)
