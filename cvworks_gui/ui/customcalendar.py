import datetime
import platform

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QPixmap, QPalette
from PyQt6.QtWidgets import QCalendarWidget

from cvworks_gui import OFF_ICON, WORKS_ICON
from schedule import schedule


def _to_python_date(d: QDate):
    return datetime.date(d.year(), d.month(), d.day())


class CustomCalendar(QCalendarWidget):
    FONT_WEIGHT = 1000

    def __init__(self, parent=None):
        super().__init__(parent)
        self._off_indicator = QPixmap(OFF_ICON)
        self._works_indicator = QPixmap(WORKS_ICON)

        if platform.system() == "Windows":
            self.date_background_color = self.palette().color(
                QPalette.ColorGroup.Normal, QPalette.ColorRole.Shadow
            )
        else:
            self.date_background_color = self.palette().color(
                QPalette.ColorGroup.Normal, QPalette.ColorRole.Base
            )

    def paintCell(self, painter, rect, date: QDate):
        if date == self.selectedDate():
            working = schedule.working_this_day(_to_python_date(date))
            if working:
                indicator = self._works_indicator
            else:
                indicator = self._off_indicator

            font = painter.font()
            font.setWeight(self.FONT_WEIGHT)
            painter.setFont(font)
            painter.setPen(Qt.GlobalColor.yellow)
            alignment = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight
            painter.fillRect(rect, self.date_background_color)
            painter.drawPixmap(rect, indicator)
            painter.drawText(
                rect,
                alignment,
                f"{date.day()}",
            )
            return

        super().paintCell(painter, rect, date)
