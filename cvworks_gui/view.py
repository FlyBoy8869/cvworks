from PySide6.QtCore import (
    QDate,
    Qt,
    Signal,
    QSize,
    QPoint,
)
from PySide6.QtGui import QPixmap, QKeyEvent
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication

import cvworks_gui.styling as styling
from cvworks_gui.ui.calendar_ui import Ui_Form
from cvworks_gui.ui.customcalendar import CustomCalendarViewMode
import settings


class CalendarView(QWidget, Ui_Form):
    show_today: Signal = Signal(QDate)

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"CVWorks")

        # noinspection PyUnresolvedReferences
        self.show_today.connect(self._go_to_today)

        self.tb_about.clicked.connect(
            lambda _: self.keyReleaseEvent(
                self.create_ctrl_key_release_event(Qt.Key.Key_A)
            )
        )

        self.tb_reset.clicked.connect(
            lambda _: self.keyReleaseEvent(
                self.create_ctrl_key_release_event(Qt.Key.Key_R)
            )
        )

        self.tb_today.clicked.connect(
            lambda _: self.keyReleaseEvent(
                self.create_ctrl_key_release_event(Qt.Key.Key_T)
            )
        )

        # used with qtmodern window wrapper
        self._self = None

    def closeEvent(self, event) -> None:
        settings.settings.setValue("calendarView/size", self._self.size())
        settings.settings.setValue("calendarView/position", self._self.pos())
        settings.settings.setValue("calendarView/viewMode", self.calendarWidget.mode)
        event.accept()

    def keyReleaseEvent(self, event) -> None:
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_A:
                self._show_about_dialog()
                return
            if event.key() == Qt.Key.Key_M:
                self.calendarWidget.mode = (
                    CustomCalendarViewMode.Graphical
                    if self.calendarWidget.mode == CustomCalendarViewMode.Text
                    else CustomCalendarViewMode.Text
                )
            if event.key() == Qt.Key.Key_R:
                self._center_on_screen()
                return
            if event.key() == Qt.Key.Key_T:
                # noinspection PyUnresolvedReferences
                self.show_today.emit(QDate.currentDate())
                return
            if event.key() == Qt.Key.Key_D:
                print(f"geometry: {self.geometry()}")
                return

        event.ignore()

    def set_qtmodern_window_reference(self, window_reference):
        self._self = window_reference

    def showEvent(self, event) -> None:
        self._self.resize(settings.settings.value("calendarView/size", QSize(400, 428)))
        self._self.move(settings.settings.value("calendarView/position", QPoint(100, 100)))
        self.calendarWidget.mode = settings.settings.value(
            "calendarView/viewMode", CustomCalendarViewMode.Graphical
        )
        event.accept()

    def _center_on_screen(self) -> None:
        screen = QApplication.screenAt(QPoint(self.x(), self.y()))
        self._self.resize(500, 500)
        self._self.move(
            int((screen.geometry().width() - self._self.geometry().width()) / 2),
            int((screen.geometry().height() - self._self.geometry().height()) / 2),
        )

    def _go_to_today(self, current_date: QDate) -> None:
        self.calendarWidget.setSelectedDate(current_date)

    def _show_about_dialog(self) -> None:
        text = (
            f"{styling.ABOUT_AUTHOR_HEADING}"
            f"{styling.ABOUT_AUTHOR_NAME}"
            f"{styling.ABOUT_AUTHOR_EMAIL}"
            f"{styling.ABOUT_VERSION_HEADING}"
            f"{styling.ABOUT_OPERATING_SYSTEM}"
            f"{styling.ABOUT_PROGRAM_VERSION}"
            f"{styling.ABOUT_PROGRAM_BUILD}"
        )

        msg_box = QMessageBox(parent=self)
        msg_box.setIconPixmap(QPixmap(styling.ABOUT_INFO_ICON))
        msg_box.setWindowTitle("About CVWorks")
        msg_box.setText(text)
        msg_box.exec()

    @staticmethod
    def create_ctrl_key_release_event(key) -> QKeyEvent:
        return QKeyEvent(
            QKeyEvent.Type.KeyRelease, key, Qt.KeyboardModifier.ControlModifier
        )
