# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHBoxLayout, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)

from cvworks_gui.ui.customcalendar import CustomCalendar

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QSize(500, 500))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_about = QToolButton(Form)
        self.tb_about.setObjectName(u"tb_about")
        self.tb_about.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.tb_about)

        self.tb_today = QToolButton(Form)
        self.tb_today.setObjectName(u"tb_today")
        self.tb_today.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.tb_today)

        self.tb_reset = QToolButton(Form)
        self.tb_reset.setObjectName(u"tb_reset")
        self.tb_reset.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.tb_reset)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.calendarWidget = CustomCalendar(Form)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SelectionMode.SingleSelection)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setDateEditEnabled(False)

        self.verticalLayout.addWidget(self.calendarWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tb_about.setText(QCoreApplication.translate("Form", u"About", None))
        self.tb_today.setText(QCoreApplication.translate("Form", u"Today", None))
        self.tb_reset.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

