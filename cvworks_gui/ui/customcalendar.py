import datetime
import platform
from enum import Enum

import darkdetect
from PySide6.QtCore import QDate, Qt, QRect
from PySide6.QtGui import QPixmap, QPalette, QFont, QFontMetrics
from PySide6.QtWidgets import QCalendarWidget

from cvworks_gui import OFF_ICON, WORKS_ICON
from schedule import schedule


class CustomCalendarViewMode(Enum):
    Graphical = 1
    Text = 2


class CustomCalendar(QCalendarWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._off_indicator = QPixmap(OFF_ICON)
        self._works_indicator = QPixmap(WORKS_ICON)
        self._mode = CustomCalendarViewMode.Graphical

    @property
    def mode(self) -> CustomCalendarViewMode:
        return self._mode

    @mode.setter
    def mode(self, mode: CustomCalendarViewMode) -> None:
        self._mode = mode
        self.updateCells()

    def paintCell(self, painter, rect, date: QDate) -> None:
        if self.mode == CustomCalendarViewMode.Graphical:
            self._do_graphical_stuff(painter, rect, date)
        else:
            self._do_text_stuff(painter, rect, date)

    def _do_graphical_stuff(self, painter, rect, date):
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
        font.setWeight(QFont.Weight.Black)
        painter.setFont(font)
        painter.setPen(selected_date_pen_color)
        painter.fillRect(rect, date_background_color)

        rect.setWidth(rect.width() - 30)
        rect.setHeight(rect.height() - 30)
        painter.drawPixmap(
            rect,
            self._get_indicator(date)[1],
        )

        painter.drawText(
            rect,
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight,
            f"{date.day()}",
        )
        return

    def _do_text_stuff(self, painter, rect, date):
        pen_color = (
            Qt.GlobalColor.yellow
            if darkdetect.theme() == "Dark"
            else Qt.GlobalColor.black
        )
        painter.setPen(pen_color)
        super().paintCell(painter, rect, date)

        font = painter.font()
        fm = QFontMetrics(font)
        font.setWeight(QFont.Weight.Thin)

        painter.setFont(font)
        new_rect = QRect(
            rect.x(),
            rect.y(),
            rect.width(),
            int(rect.height() / 2) + (fm.height() + fm.descent() + 3),
        )

        text_indicator = self._get_indicator(date)[0]
        painter.drawText(
            new_rect,
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter,
            text_indicator,
        )

    def _get_indicator(self, date) -> tuple[str, QPixmap]:
        working = schedule.working_this_day(self._to_python_date(date))
        if working:
            return "Working", self._works_indicator

        return "Off", self._off_indicator

    @staticmethod
    def _to_python_date(d: QDate) -> datetime.date:
        return datetime.date(d.year(), d.month(), d.day())
