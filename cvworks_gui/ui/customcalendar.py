import datetime

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QPixmap, QColor, QPalette
from PyQt6.QtWidgets import QCalendarWidget

from cvworks_gui.ui import off_icon, works_icon
from schedule import schedule


def to_python_date(d: QDate):
    return datetime.date(d.year(), d.month(), d.day())


class CustomCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._off_indicator = QPixmap(off_icon)
        self._works_indicator = QPixmap(works_icon)
        self.date_background_color = self.palette().color(
            QPalette.ColorGroup.Normal, QPalette.ColorRole.Base
        )

    def paintCell(self, painter, rect, date: QDate):
        if date == self.selectedDate():
            working = schedule.working_this_day(to_python_date(date))
            if working:
                painter.setPen(Qt.GlobalColor.yellow)
                alignment = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight
                complication = self._works_indicator
            else:
                painter.setPen(Qt.GlobalColor.yellow)
                alignment = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight
                complication = self._off_indicator

            font = painter.font()
            font.setWeight(1000)
            # font.setBold(True)

            painter.setFont(font)

            painter.fillRect(rect, self.date_background_color)
            painter.drawPixmap(rect, complication)
            painter.drawText(
                rect,
                alignment,
                f"{date.day()}",
            )

            return

        super().paintCell(painter, rect, date)
