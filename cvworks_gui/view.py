from PyQt6.QtCore import (
    QDate,
    Qt,
    pyqtSignal,
    QSize,
    QPoint,
)
from PyQt6.QtGui import QPixmap, QKeyEvent
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication

import cvworks_gui.styling as styling
from cvworks_gui.ui.calendar_ui import Ui_Form
import settings


class CalendarView(QWidget, Ui_Form):
    show_today: pyqtSignal = pyqtSignal(QDate)

    def __init__(self):
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

        self.tb_today.clicked.connect(
            lambda _: self.keyReleaseEvent(
                self.create_ctrl_key_release_event(Qt.Key.Key_T)
            )
        )

        self.tb_reset.clicked.connect(
            lambda _: self.keyReleaseEvent(
                self.create_ctrl_key_release_event(Qt.Key.Key_R)
            )
        )

        self.show()

    def closeEvent(self, event):
        settings.settings.setValue("calendarView/size", self.size())
        settings.settings.setValue("calendarView/position", self.pos())
        event.accept()

    def keyReleaseEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_A:
                self._show_about_dialog()
                return
            if event.key() == Qt.Key.Key_T:
                # noinspection PyUnresolvedReferences
                self.show_today.emit(QDate.currentDate())
                return
            if event.key() == Qt.Key.Key_R:
                screen = QApplication.screenAt(QPoint(self.x(), self.y()))
                self.resize(400, 428)
                self.move(
                    int((screen.geometry().width() - self.geometry().width()) / 2),
                    int((screen.geometry().height() - self.geometry().height()) / 2),
                )
                return

        event.ignore()

    def showEvent(self, event):
        self.resize(settings.settings.value("calendarView/size", QSize(400, 400)))
        self.move(settings.settings.value("calendarView/position", QPoint(100, 100)))
        event.accept()

    def _go_to_today(self, current_date: QDate):
        self.calendarWidget.setSelectedDate(current_date)

    def _show_about_dialog(self):
        text = (
            f"{styling.ABOUT_AUTHOR_HEADING}"
            f"{styling.ABOUT_AUTHOR_NAME}"
            f"{styling.ABOUT_AUTHOR_EMAIL}"
            f"{styling.ABOUT_VERSION_HEADING}"
            f"{styling.ABOUT_OPERATING_SYSTEM}"
            f"{styling.ABOUT_PROGRAM_VERSION}"
        )

        msg_box = QMessageBox(parent=self)
        msg_box.setIconPixmap(QPixmap(styling.ABOUT_INFO_ICON))
        msg_box.setWindowTitle("About CVWorks")
        msg_box.setText(text)
        msg_box.exec()

    @staticmethod
    def create_ctrl_key_release_event(key):
        return QKeyEvent(
            QKeyEvent.Type.KeyRelease, key, Qt.KeyboardModifier.ControlModifier
        )
