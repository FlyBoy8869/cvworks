import datetime
import platform

import darkdetect
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QPixmap, QPalette
from PyQt6.QtWidgets import QCalendarWidget

from cvworks_gui import OFF_ICON, WORKS_ICON
from schedule import schedule


class CustomCalendar(QCalendarWidget):
    FONT_WEIGHT = 1000

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._off_indicator = QPixmap(OFF_ICON)
        self._works_indicator = QPixmap(WORKS_ICON)

    def paintCell(self, painter, rect, date: QDate) -> None:
        if date == self.selectedDate():
            if darkdetect.theme() == "Dark":
                selected_date_pen_color = Qt.GlobalColor.white
                if platform.system() == "Windows":
                    date_background_color = self.palette().color(
                        QPalette.ColorGroup.Normal, QPalette.ColorRole.Shadow
                    )
                else:
                    date_background_color = self.palette().color(
                        QPalette.ColorGroup.Normal, QPalette.ColorRole.Base
                    )
            else:
                selected_date_pen_color = Qt.GlobalColor.black
                if platform.system() == "Windows":
                    date_background_color = self.palette().color(
                        QPalette.ColorGroup.Normal, QPalette.ColorRole.Base
                    )
                else:
                    date_background_color = self.palette().color(
                        QPalette.ColorGroup.Normal, QPalette.ColorRole.Base
                    )

            if date.dayOfWeek() in (6, 7):
                selected_date_pen_color = Qt.GlobalColor.red

            font = painter.font()
            font.setWeight(self.FONT_WEIGHT)
            painter.setFont(font)
            painter.setPen(selected_date_pen_color)
            painter.fillRect(rect, date_background_color)
            painter.drawPixmap(rect, self._get_indicator(date))
            painter.drawText(
                rect,
                Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight,
                f"{date.day()}",
            )
            return

        super().paintCell(painter, rect, date)

    def _get_indicator(self, date) -> QPixmap:
        working = schedule.working_this_day(self._to_python_date(date))
        if working:
            return self._works_indicator

        return self._off_indicator

    @staticmethod
    def _to_python_date(d: QDate) -> datetime.date:
        return datetime.date(d.year(), d.month(), d.day())
