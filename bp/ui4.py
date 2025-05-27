# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui4.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_NabtewStudio(object):
    def setupUi(self, NabtewStudio):
        if not NabtewStudio.objectName():
            NabtewStudio.setObjectName(u"NabtewStudio")
        NabtewStudio.setWindowModality(Qt.NonModal)
        NabtewStudio.resize(1219, 758)
        NabtewStudio.setMinimumSize(QSize(1219, 758))
        NabtewStudio.setMaximumSize(QSize(1219, 758))
        NabtewStudio.setStyleSheet(u"")
        self.centralwidget = QWidget(NabtewStudio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Main_layOut = QHBoxLayout()
        self.Main_layOut.setSpacing(15)
        self.Main_layOut.setObjectName(u"Main_layOut")
        self.Main_layOut.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.Main_layOut.setContentsMargins(10, 25, 10, 25)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(180, 200))
        self.label_2.setMaximumSize(QSize(180, 200))
        self.label_2.setSizeIncrement(QSize(0, 0))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-image: url(:/test/logo.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.label_2.setPixmap(QPixmap(u":/test/C:/Users/bbnat/Desktop/really_bin/gggggggggggggggggggggggg.jpg"))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(5)
        self.label_2.setOpenExternalLinks(False)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(180, 20))
        self.label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(14)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Storage_box = QComboBox(self.centralwidget)
        self.Storage_box.setObjectName(u"Storage_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Storage_box.sizePolicy().hasHeightForWidth())
        self.Storage_box.setSizePolicy(sizePolicy1)
        self.Storage_box.setMinimumSize(QSize(10, 40))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei Light"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.Storage_box.setFont(font1)
        self.Storage_box.setFocusPolicy(Qt.WheelFocus)
        self.Storage_box.setLayoutDirection(Qt.LeftToRight)
        self.Storage_box.setStyleSheet(u"QComboBox {\n"
"    font-size: 18px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e02\u0e19\u0e32\u0e14\u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23\u0e43\u0e19\u0e41\u0e17\u0e47\u0e1a */\n"
"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"}\n"
"")
        self.Storage_box.setEditable(True)
        self.Storage_box.setCurrentText(u"")
        self.Storage_box.setInsertPolicy(QComboBox.InsertAtBottom)
        self.Storage_box.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_3.addWidget(self.Storage_box, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.project_box = QComboBox(self.centralwidget)
        self.project_box.setObjectName(u"project_box")
        self.project_box.setMinimumSize(QSize(150, 40))
        self.project_box.setMaximumSize(QSize(150, 16777215))
        self.project_box.setFont(font1)
        self.project_box.setStyleSheet(u"QComboBox {\n"
"    font-size: 18px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e02\u0e19\u0e32\u0e14\u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23\u0e43\u0e19\u0e41\u0e17\u0e47\u0e1a */\n"
"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"}\n"
"")
        self.project_box.setEditable(True)

        self.horizontalLayout_13.addWidget(self.project_box)

        self.addProject_button = QPushButton(self.centralwidget)
        self.addProject_button.setObjectName(u"addProject_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addProject_button.sizePolicy().hasHeightForWidth())
        self.addProject_button.setSizePolicy(sizePolicy2)
        self.addProject_button.setMinimumSize(QSize(20, 40))
        self.addProject_button.setMaximumSize(QSize(20, 40))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei Light"])
        font2.setPointSize(12)
        self.addProject_button.setFont(font2)

        self.horizontalLayout_13.addWidget(self.addProject_button)

        self.delProject_button = QPushButton(self.centralwidget)
        self.delProject_button.setObjectName(u"delProject_button")
        sizePolicy2.setHeightForWidth(self.delProject_button.sizePolicy().hasHeightForWidth())
        self.delProject_button.setSizePolicy(sizePolicy2)
        self.delProject_button.setMinimumSize(QSize(20, 40))
        self.delProject_button.setMaximumSize(QSize(20, 40))
        self.delProject_button.setFont(font2)

        self.horizontalLayout_13.addWidget(self.delProject_button)


        self.gridLayout_3.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)


        self.Main_layOut.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabList = QTabWidget(self.centralwidget)
        self.tabList.setObjectName(u"tabList")
        self.tabList.setEnabled(True)
        self.tabList.setMaximumSize(QSize(16777215, 16777215))
        self.tabList.setFont(font2)
        self.tabList.setFocusPolicy(Qt.WheelFocus)
        self.tabList.setContextMenuPolicy(Qt.NoContextMenu)
        self.tabList.setLayoutDirection(Qt.LeftToRight)
        self.tabList.setStyleSheet(u"QTabBar::tab {\n"
"    height: 50px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e39\u0e07\u0e02\u0e2d\u0e07\u0e41\u0e17\u0e47\u0e1a */\n"
"    width: 140px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e01\u0e27\u0e49\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e41\u0e17\u0e47\u0e1a */\n"
"    font-size: 18px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e02\u0e19\u0e32\u0e14\u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23\u0e43\u0e19\u0e41\u0e17\u0e47\u0e1a */\n"
"}\n"
"")
        self.tabList.setIconSize(QSize(30, 30))
        self.tabList.setElideMode(Qt.ElideMiddle)
        self.tabList.setTabsClosable(False)
        self.Assets_tab = QWidget()
        self.Assets_tab.setObjectName(u"Assets_tab")
        self.label_10 = QLabel(self.Assets_tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 80, 61, 20))
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12 = QLabel(self.Assets_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(470, 80, 298, 20))
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.asset_list_box = QListWidget(self.Assets_tab)
        self.asset_list_box.setObjectName(u"asset_list_box")
        self.asset_list_box.setGeometry(QRect(20, 110, 441, 431))
        self.asset_list_box.setFont(font2)
        self.asset_list_box.setStyleSheet(u"QListWidget {\n"
"	background-color: rgb(38, 38, 38);\n"
"}")
        self.asset_list_box.setFrameShape(QFrame.NoFrame)
        self.asset_search_box = QLineEdit(self.Assets_tab)
        self.asset_search_box.setObjectName(u"asset_search_box")
        self.asset_search_box.setGeometry(QRect(20, 550, 211, 41))
        self.asset_search_box.setFont(font2)
        self.asset_search_box.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(38, 38, 38);\n"
"}")
        self.asset_search_box.setFrame(False)
        self.asset_ver_box = QListWidget(self.Assets_tab)
        self.asset_ver_box.setObjectName(u"asset_ver_box")
        self.asset_ver_box.setGeometry(QRect(470, 110, 231, 431))
        self.asset_ver_box.setFont(font2)
        self.asset_ver_box.setStyleSheet(u"QListWidget {\n"
"	background-color: rgb(38, 38, 38);\n"
"}")
        self.asset_ver_box.setFrameShape(QFrame.NoFrame)
        self.department1_box = QComboBox(self.Assets_tab)
        self.department1_box.setObjectName(u"department1_box")
        self.department1_box.setEnabled(True)
        self.department1_box.setGeometry(QRect(200, 20, 151, 41))
        self.department1_box.setStyleSheet(u"QComboBox {\n"
"    font-size: 18px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e02\u0e19\u0e32\u0e14\u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23\u0e43\u0e19\u0e41\u0e17\u0e47\u0e1a */\n"
"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"}\n"
"")
        self.department1_box.setEditable(True)
        self.type_box = QComboBox(self.Assets_tab)
        self.type_box.setObjectName(u"type_box")
        self.type_box.setEnabled(True)
        self.type_box.setGeometry(QRect(30, 20, 151, 41))
        self.type_box.setStyleSheet(u"QComboBox {\n"
"    font-size: 18px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e02\u0e19\u0e32\u0e14\u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23\u0e43\u0e19\u0e41\u0e17\u0e47\u0e1a */\n"
"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"}\n"
"")
        self.type_box.setEditable(True)
        self.addAsset_button = QPushButton(self.Assets_tab)
        self.addAsset_button.setObjectName(u"addAsset_button")
        self.addAsset_button.setEnabled(False)
        self.addAsset_button.setGeometry(QRect(240, 550, 50, 45))
        sizePolicy2.setHeightForWidth(self.addAsset_button.sizePolicy().hasHeightForWidth())
        self.addAsset_button.setSizePolicy(sizePolicy2)
        self.addAsset_button.setMinimumSize(QSize(50, 45))
        self.addAsset_button.setMaximumSize(QSize(50, 45))
        self.addAsset_button.setFont(font2)
        self.delAsset_button = QPushButton(self.Assets_tab)
        self.delAsset_button.setObjectName(u"delAsset_button")
        self.delAsset_button.setEnabled(False)
        self.delAsset_button.setGeometry(QRect(300, 550, 50, 45))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.delAsset_button.sizePolicy().hasHeightForWidth())
        self.delAsset_button.setSizePolicy(sizePolicy3)
        self.delAsset_button.setMinimumSize(QSize(50, 45))
        self.delAsset_button.setMaximumSize(QSize(50, 45))
        self.delAsset_button.setFont(font2)
        self.tabList.addTab(self.Assets_tab, "")
        self.model_tab = QWidget()
        self.model_tab.setObjectName(u"model_tab")
        self.label_14 = QLabel(self.model_tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 80, 71, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_15 = QLabel(self.model_tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(470, 80, 298, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scene_list_box = QListWidget(self.model_tab)
        self.scene_list_box.setObjectName(u"scene_list_box")
        self.scene_list_box.setGeometry(QRect(20, 110, 441, 431))
        self.scene_list_box.setFont(font2)
        self.scene_list_box.setStyleSheet(u"QListWidget {\n"
"	background-color: rgb(38, 38, 38);\n"
"}")
        self.scene_list_box.setFrameShape(QFrame.NoFrame)
        self.scene_ver_box = QListWidget(self.model_tab)
        self.scene_ver_box.setObjectName(u"scene_ver_box")
        self.scene_ver_box.setGeometry(QRect(470, 110, 231, 431))
        self.scene_ver_box.setFont(font2)
        self.scene_ver_box.setStyleSheet(u"QListWidget {\n"
"	background-color: rgb(38, 38, 38);\n"
"}")
        self.scene_ver_box.setFrameShape(QFrame.NoFrame)
        self.scene_search_box = QLineEdit(self.model_tab)
        self.scene_search_box.setObjectName(u"scene_search_box")
        self.scene_search_box.setGeometry(QRect(20, 550, 211, 41))
        self.scene_search_box.setFont(font2)
        self.scene_search_box.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(38, 38, 38);\n"
"}")
        self.scene_search_box.setFrame(False)
        self.section_box = QComboBox(self.model_tab)
        self.section_box.setObjectName(u"section_box")
        self.section_box.setEnabled(True)
        self.section_box.setGeometry(QRect(30, 20, 151, 41))
        self.section_box.setStyleSheet(u"QComboBox {\n"
"    font-size: 18px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e02\u0e19\u0e32\u0e14\u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23\u0e43\u0e19\u0e41\u0e17\u0e47\u0e1a */\n"
"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"}\n"
"")
        self.section_box.setEditable(True)
        self.department2_box = QComboBox(self.model_tab)
        self.department2_box.setObjectName(u"department2_box")
        self.department2_box.setEnabled(True)
        self.department2_box.setGeometry(QRect(200, 20, 151, 41))
        self.department2_box.setStyleSheet(u"QComboBox {\n"
"    font-size: 18px;  /* \u0e1b\u0e23\u0e31\u0e1a\u0e02\u0e19\u0e32\u0e14\u0e15\u0e31\u0e27\u0e2d\u0e31\u0e01\u0e29\u0e23\u0e43\u0e19\u0e41\u0e17\u0e47\u0e1a */\n"
"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"}\n"
"")
        self.department2_box.setEditable(True)
        self.addScene_button = QPushButton(self.model_tab)
        self.addScene_button.setObjectName(u"addScene_button")
        self.addScene_button.setEnabled(False)
        self.addScene_button.setGeometry(QRect(240, 550, 50, 45))
        sizePolicy2.setHeightForWidth(self.addScene_button.sizePolicy().hasHeightForWidth())
        self.addScene_button.setSizePolicy(sizePolicy2)
        self.addScene_button.setMinimumSize(QSize(50, 45))
        self.addScene_button.setMaximumSize(QSize(50, 45))
        self.addScene_button.setFont(font2)
        self.delScene_button = QPushButton(self.model_tab)
        self.delScene_button.setObjectName(u"delScene_button")
        self.delScene_button.setEnabled(False)
        self.delScene_button.setGeometry(QRect(300, 550, 50, 45))
        sizePolicy3.setHeightForWidth(self.delScene_button.sizePolicy().hasHeightForWidth())
        self.delScene_button.setSizePolicy(sizePolicy3)
        self.delScene_button.setMinimumSize(QSize(50, 45))
        self.delScene_button.setMaximumSize(QSize(50, 45))
        self.delScene_button.setFont(font2)
        self.addSection_button = QPushButton(self.model_tab)
        self.addSection_button.setObjectName(u"addSection_button")
        self.addSection_button.setEnabled(False)
        self.addSection_button.setGeometry(QRect(130, 70, 25, 25))
        sizePolicy2.setHeightForWidth(self.addSection_button.sizePolicy().hasHeightForWidth())
        self.addSection_button.setSizePolicy(sizePolicy2)
        self.addSection_button.setMinimumSize(QSize(25, 25))
        self.addSection_button.setMaximumSize(QSize(20, 20))
        self.addSection_button.setFont(font2)
        self.delSection_button = QPushButton(self.model_tab)
        self.delSection_button.setObjectName(u"delSection_button")
        self.delSection_button.setEnabled(False)
        self.delSection_button.setGeometry(QRect(160, 70, 25, 25))
        sizePolicy2.setHeightForWidth(self.delSection_button.sizePolicy().hasHeightForWidth())
        self.delSection_button.setSizePolicy(sizePolicy2)
        self.delSection_button.setMinimumSize(QSize(25, 25))
        self.delSection_button.setMaximumSize(QSize(20, 20))
        self.delSection_button.setFont(font2)
        self.tabList.addTab(self.model_tab, "")

        self.verticalLayout.addWidget(self.tabList)


        self.Main_layOut.addLayout(self.verticalLayout)

        self.R_layOut_A = QVBoxLayout()
        self.R_layOut_A.setSpacing(10)
        self.R_layOut_A.setObjectName(u"R_layOut_A")
        self.R_layOut_A.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.R_layOut_A.setContentsMargins(15, 15, 5, 15)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/test/logo.jpg"))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.R_layOut_A.addWidget(self.label_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(5)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(5, 20))
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setFont(font2)
        self.label_8.setFocusPolicy(Qt.WheelFocus)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_9)

        self.verticalSpacer_4 = QSpacerItem(10, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)


        self.R_layOut_A.addLayout(self.verticalLayout_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.open_button = QPushButton(self.centralwidget)
        self.open_button.setObjectName(u"open_button")
        sizePolicy2.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy2)
        self.open_button.setMinimumSize(QSize(100, 45))
        self.open_button.setMaximumSize(QSize(100, 45))
        self.open_button.setFont(font2)

        self.horizontalLayout_12.addWidget(self.open_button)

        self.publish_button = QPushButton(self.centralwidget)
        self.publish_button.setObjectName(u"publish_button")
        self.publish_button.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.publish_button.sizePolicy().hasHeightForWidth())
        self.publish_button.setSizePolicy(sizePolicy3)
        self.publish_button.setMinimumSize(QSize(100, 45))
        self.publish_button.setMaximumSize(QSize(100, 45))
        self.publish_button.setFont(font2)

        self.horizontalLayout_12.addWidget(self.publish_button)

        self.horizontalSpacer_5 = QSpacerItem(10, 10, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.R_layOut_A.addLayout(self.horizontalLayout_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(10, 10, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.export_button = QPushButton(self.centralwidget)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy2)
        self.export_button.setMinimumSize(QSize(100, 45))
        self.export_button.setMaximumSize(QSize(100, 45))
        self.export_button.setFont(font2)

        self.horizontalLayout.addWidget(self.export_button)

        self.data_button = QPushButton(self.centralwidget)
        self.data_button.setObjectName(u"data_button")
        sizePolicy3.setHeightForWidth(self.data_button.sizePolicy().hasHeightForWidth())
        self.data_button.setSizePolicy(sizePolicy3)
        self.data_button.setMinimumSize(QSize(100, 45))
        self.data_button.setMaximumSize(QSize(100, 45))
        self.data_button.setFont(font2)

        self.horizontalLayout.addWidget(self.data_button)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.R_layOut_A.addLayout(self.horizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.R_layOut_A.addItem(self.verticalSpacer_5)


        self.Main_layOut.addLayout(self.R_layOut_A)


        self.verticalLayout_3.addLayout(self.Main_layOut)

        NabtewStudio.setCentralWidget(self.centralwidget)

        self.retranslateUi(NabtewStudio)

        self.Storage_box.setCurrentIndex(-1)
        self.project_box.setCurrentIndex(-1)
        self.tabList.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(NabtewStudio)
    # setupUi

    def retranslateUi(self, NabtewStudio):
        NabtewStudio.setWindowTitle(QCoreApplication.translate("NabtewStudio", u"Nabtew Studio", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("NabtewStudio", u"SHIBBON", None))
        self.project_box.setCurrentText("")
        self.addProject_button.setText(QCoreApplication.translate("NabtewStudio", u"+", None))
        self.delProject_button.setText(QCoreApplication.translate("NabtewStudio", u"-", None))
        self.label_10.setText(QCoreApplication.translate("NabtewStudio", u"Assets", None))
        self.label_12.setText(QCoreApplication.translate("NabtewStudio", u"Versions", None))
        self.asset_search_box.setInputMask("")
        self.asset_search_box.setText("")
        self.asset_search_box.setPlaceholderText(QCoreApplication.translate("NabtewStudio", u"Search", None))
        self.department1_box.setCurrentText("")
        self.type_box.setCurrentText("")
        self.addAsset_button.setText(QCoreApplication.translate("NabtewStudio", u"+", None))
        self.delAsset_button.setText(QCoreApplication.translate("NabtewStudio", u"-", None))
        self.tabList.setTabText(self.tabList.indexOf(self.Assets_tab), QCoreApplication.translate("NabtewStudio", u"Assets", None))
        self.label_14.setText(QCoreApplication.translate("NabtewStudio", u"Scenes", None))
        self.label_15.setText(QCoreApplication.translate("NabtewStudio", u"Versions", None))
        self.scene_search_box.setInputMask("")
        self.scene_search_box.setText("")
        self.scene_search_box.setPlaceholderText(QCoreApplication.translate("NabtewStudio", u"Search", None))
        self.section_box.setCurrentText("")
        self.department2_box.setCurrentText("")
        self.addScene_button.setText(QCoreApplication.translate("NabtewStudio", u"+", None))
        self.delScene_button.setText(QCoreApplication.translate("NabtewStudio", u"-", None))
        self.addSection_button.setText(QCoreApplication.translate("NabtewStudio", u"+", None))
        self.delSection_button.setText(QCoreApplication.translate("NabtewStudio", u"-", None))
        self.tabList.setTabText(self.tabList.indexOf(self.model_tab), QCoreApplication.translate("NabtewStudio", u"Scenes", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("NabtewStudio", u"Name : Nabtew", None))
        self.label_7.setText(QCoreApplication.translate("NabtewStudio", u"Date : 01/11/1111", None))
        self.label_9.setText(QCoreApplication.translate("NabtewStudio", u"Last update : --/--/----", None))
        self.open_button.setText(QCoreApplication.translate("NabtewStudio", u"OPEN", None))
        self.publish_button.setText(QCoreApplication.translate("NabtewStudio", u"PUBLISH", None))
        self.export_button.setText(QCoreApplication.translate("NabtewStudio", u"EXPORT", None))
        self.data_button.setText(QCoreApplication.translate("NabtewStudio", u"DATA", None))
    # retranslateUi

