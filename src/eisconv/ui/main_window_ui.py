# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowmJkhxT.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint,
    QRect, QSize, QTime, QUrl, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap,
    QRadialGradient, QTransform
)
from PySide6.QtWidgets import (
    QApplication, QComboBox, QGroupBox, QHBoxLayout, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget
)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(528, 312)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBoxImport = QGroupBox(self.centralwidget)
        self.groupBoxImport.setObjectName(u"groupBoxImport")
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxImport)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBoxImport = QComboBox(self.groupBoxImport)
        self.comboBoxImport.setObjectName(u"comboBoxImport")

        self.verticalLayout_3.addWidget(self.comboBoxImport)

        self.pushButtonImport = QPushButton(self.groupBoxImport)
        self.pushButtonImport.setObjectName(u"pushButtonImport")

        self.verticalLayout_3.addWidget(self.pushButtonImport)

        self.verticalLayout_5.addWidget(self.groupBoxImport)

        self.groupBoxExport = QGroupBox(self.centralwidget)
        self.groupBoxExport.setObjectName(u"groupBoxExport")
        self.verticalLayout_4 = QVBoxLayout(self.groupBoxExport)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBoxExport = QComboBox(self.groupBoxExport)
        self.comboBoxExport.setObjectName(u"comboBoxExport")

        self.verticalLayout_4.addWidget(self.comboBoxExport)

        self.pushButtonExport = QPushButton(self.groupBoxExport)
        self.pushButtonExport.setObjectName(u"pushButtonExport")

        self.verticalLayout_4.addWidget(self.pushButtonExport)

        self.verticalLayout_5.addWidget(self.groupBoxExport)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout.setStretch(0, 60)
        self.horizontalLayout.setStretch(1, 40)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 528, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", u"Impedance data converter", None
            )
        )
        self.groupBoxImport.setTitle(
            QCoreApplication.translate("MainWindow", u"Import data", None)
        )
        self.pushButtonImport.setText(
            QCoreApplication.translate("MainWindow", u"Load", None)
        )
        self.groupBoxExport.setTitle(
            QCoreApplication.translate("MainWindow", u"Export data", None)
        )
        self.pushButtonExport.setText(
            QCoreApplication.translate("MainWindow", u"Export", None)
        )

    # retranslateUi
