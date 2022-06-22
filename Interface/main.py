#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Felipe Mendoza Giraldo
# Created Date: date/month/time ..etc
# version ='1.0'
# ---------------------------------------------------------------------------
"""A one-line description or name.
A longer description that spans multiple lines.  Explain the purpose of the
file and provide a short list of the key classes/functions it contains.  This
is the docstring shown when some does 'import foo;foo?' in IPython, so it
should be reasonably useful and informative.
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, the IPython Development Team and José Fonseca.
#
# Distributed under the terms of the Creative Commons License.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#
#
# REFERENCES:
#
# -----------------------------------------------------------------------------
'''
OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script
ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script
'''

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# stdlib imports -------------------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QRectF, QPointF
from PyQt5.QtGui import QColor, QBrush, QPaintEvent, QPainter, QPen
from PyQt5.QtWidgets import (QToolBar, QToolButton, QCheckBox, QComboBox,
                             QPushButton, QFileDialog)
import pyqtgraph as pg
import serial
import serial.tools.list_ports
import time
import json
import itertools
import csv
from guiLoop import guiLoop  # https://gist.github.com/niccokunzmann/8673951
from os.path import exists

# Third-party imports -----------------------------------------------

# Our own imports ---------------------------------------------------


# -----------------------------------------------------------------------------
# GLOBALS
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# LOCAL UTILITIES
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 10, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 10, 1)
        self.current = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current.sizePolicy().hasHeightForWidth())
        self.current.setSizePolicy(sizePolicy)
        self.current.setMaximumSize(QtCore.QSize(60, 16777215))
        self.current.setReadOnly(True)
        self.current.setObjectName("current")
        self.gridLayout.addWidget(self.current, 6, 2, 1, 1)
        self.irradiance = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.irradiance.sizePolicy().hasHeightForWidth())
        self.irradiance.setSizePolicy(sizePolicy)
        self.irradiance.setMaximumSize(QtCore.QSize(60, 16777215))
        self.irradiance.setObjectName("irradiance")
        self.gridLayout.addWidget(self.irradiance, 3, 2, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 9, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.iterations = QtWidgets.QSpinBox(self.centralwidget)
        self.iterations.setMinimum(1)
        self.iterations.setMaximum(5)
        self.iterations.setObjectName("iterations")
        self.gridLayout.addWidget(self.iterations, 1, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plt = PlotWidget(self.groupBox)
        self.plt.setObjectName("plt")
        self.horizontalLayout.addWidget(self.plt)
        self.gridLayout.addWidget(self.groupBox, 1, 3, 8, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setObjectName("browse")
        self.gridLayout.addWidget(self.browse, 9, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font: 36pt \"Bahnschrift\";")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 4)
        self.voltage = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voltage.sizePolicy().hasHeightForWidth())
        self.voltage.setSizePolicy(sizePolicy)
        self.voltage.setMaximumSize(QtCore.QSize(60, 16777215))
        self.voltage.setReadOnly(True)
        self.voltage.setObjectName("voltage")
        self.gridLayout.addWidget(self.voltage, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.resolution = QtWidgets.QSpinBox(self.centralwidget)
        self.resolution.setMinimum(10)
        self.resolution.setMaximum(25)
        self.resolution.setObjectName("resolution")
        self.gridLayout.addWidget(self.resolution, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Current [mA]:"))
        self.label_3.setText(_translate("MainWindow", "Solar irradiance [W/m^2]:"))
        self.label_4.setText(_translate("MainWindow", "Voltage [V]:"))
        self.groupBox.setTitle(_translate("MainWindow", "VI curve"))
        self.label.setText(_translate("MainWindow", "Number of iterations:"))
        self.browse.setText(_translate("MainWindow", "Open"))
        self.label_5.setText(_translate("MainWindow", "Scientific intrumentation project"))
        self.label_6.setText(_translate("MainWindow", "Resolution:"))
        # ----------------------------
        self.plt.setLabel('bottom', 'Voltage', units='V')
        self.plt.setLabel('left', 'Current', units='A')
        self.plt.setTitle('VI curve')
        self.plt.setBackground('w')
        self.plt.showGrid(x=True, y=True)


from pyqtgraph import PlotWidget


class Solar_radiation(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        BaudRates = ['2400', '4800', '9600', '19200', '57600', '115200']
        # ***** Tool bar declaration ********
        self.toolBar = QToolBar("Tool bar")

        # ******** Text "Select COM" declaration ********
        self.select_com = QToolButton()
        self.select_com.setText("Select COM: ")
        self.select_com.setCheckable(False)
        self.toolBar.addWidget(self.select_com)

        # ******** ComboBox for selecting the COM port ***
        self.combo = QComboBox(self)
        Coms = GetComPorts()
        for element in Coms:
            self.combo.addItem(element)
        self.toolBar.addWidget(self.combo)

        # ******** Text "Select BaudRate" declaration ****
        self.toolButton = QToolButton()
        self.toolButton.setText(" Select BaudRate: ")
        self.toolButton.setCheckable(False)
        self.toolBar.addWidget(self.toolButton)

        # ******** ComboBox for selecting the BaudRate ****
        self.combo1 = QComboBox(self)
        for element in BaudRates:
            self.combo1.addItem(element)
        self.toolBar.addWidget(self.combo1)

        # ******** Open Button *****************************
        self.openCOM = QPushButton()
        self.openCOM.setText("Open")
        self.openCOM.clicked.connect(self.uSerial)
        self.toolBar.addWidget(self.openCOM)

        self.toolButton = QToolButton()
        self.toolButton.setText("IV curve")
        self.toolButton.setCheckable(False)
        self.toolBar.addWidget(self.toolButton)
        self.startButton = Start()
        self.startButton.clicked.connect(self.readSerial)
        self.toolBar.addWidget(self.startButton)
        self.addToolBar(self.toolBar)
        self.MainWindow = Ui_MainWindow()
        self.MainWindow.setupUi(self)
        self.serialPort = serial.Serial()
        self.info = {"rx": False, "i": 1, "r": 10}
        self.listC = []
        self.listV = []
        self.folder = ''
        self.MainWindow.browse.clicked.connect(self.browse_files)

    def browse_files(self):
        f_name = QFileDialog.getExistingDirectory(self, "Open Directory", './')
        self.folder = f_name+"/"
        print(self.folder)

    def UpdateSerial(self, COMport, BaudRate):
        try:
            if self.serialPort.isOpen():
                self.serialPort.close()
            self.serialPort = serial.Serial(COMport, BaudRate)
            print(COMport, BaudRate)
        except Exception as e:
            print(e)

    def readSerial(self):
        if not self.startButton.isChecked:
            if self.serialPort.isOpen():
                self.serialPort.write("Start\n".encode())
        else:
            if self.serialPort.isOpen():
                self.serialPort.write("Stop\n".encode())
                time.sleep(0.1)

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def closeEvent(self, event):
        self.serialPort.close()
        print('El programa ha terminado!')

    def uSerial(self):
        self.UpdateSerial(self.combo.currentText(), int(self.combo1.currentText()))
        print("Connect")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_E:
            self.toggle_fullscreen()
        return super().keyPressEvent(event)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def event(self, e):
        if not isinstance(e, (
                QtCore.QEvent,
                QtCore.QChildEvent,
                QtCore.QDynamicPropertyChangeEvent,
                QtGui.QPaintEvent,
                QtGui.QHoverEvent,
                QtGui.QMoveEvent,
                QtGui.QEnterEvent,
                QtGui.QResizeEvent,
                QtGui.QShowEvent,
                QtGui.QPlatformSurfaceEvent,
                QtGui.QWindowStateChangeEvent,
                QtGui.QKeyEvent,
                QtGui.QWheelEvent,
                QtGui.QMouseEvent,
                QtGui.QFocusEvent,
                QtGui.QHelpEvent,
                QtGui.QHideEvent,
                QtGui.QCloseEvent,
                QtGui.QInputMethodQueryEvent,
                QtGui.QContextMenuEvent,
        )):
            print("unknown event: %r %r", e.type(), e)
        return super().event(e)


class Start(QtWidgets.QPushButton):
    _transparent_pen = QPen(Qt.transparent)
    _light_grey_pen = QPen(Qt.lightGray)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.isChecked = False
        self.handle_state_change()
        self.setContentsMargins(0, 0, 0, 0)
        self.clicked.connect(self.handle_state_change)

    def sizeHint(self):
        return QSize(25, 25)

    def handle_state_change(self):
        if self.isChecked:
            self.isChecked = False
            self.setStyleSheet("border-image :url(\\\"stop.png\\\");\n"
                               "background-repeat: no-repeat;\n"
                               "background-position: center;\n"
                               "\n"
                               "")
        else:
            self.isChecked = True
            self.setStyleSheet("border-image :url(\\\"play.png\\\");\n"
                               "background-repeat: no-repeat;\n"
                               "background-position: center;\n"
                               "\n"
                               "")


# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

# FUNCTION CATEGORY 1 -----------------------------------------
def GetComPorts():
    com_list = serial.tools.list_ports.comports()
    connected = []
    for element in com_list:
        connected.append(element.device)
    return connected


@guiLoop
def Main_loop():
    state = 0
    rx = ""
    while True:
        if ui.serialPort.isOpen():
            if ui.serialPort.in_waiting:
                rx = ui.serialPort.readline().decode("utf-8").rstrip('\r\n')
                print(rx)
            if rx == "Stop":
                state = 0
            if state == 0:
                if rx == "Receive":
                    # Send message with the information of the curve
                    ui.info["rx"] = True
                    ui.info["i"] = ui.MainWindow.iterations.value()
                    ui.info["r"] = ui.MainWindow.resolution.value()
                    ui.serialPort.write((json.dumps(ui.info)+'\n').encode())
                    # Reset the I-V curve
                    ui.MainWindow.plt.clear()
                    ui.listC = []
                    ui.listV = []
                    state = 1
            elif state == 1:
                try:
                    data = json.loads(rx)
                    v = data["V"]
                    c = data["C"]
                    ui.listV.append(v)
                    ui.listC.append(c)
                    ui.MainWindow.voltage.setText(str(v))
                    ui.MainWindow.current.setText(str(c))
                    ui.MainWindow.plt.clear()
                    ui.MainWindow.plt.plot(ui.listV, ui.listC, pen=pg.mkPen('b', width=2), name=
                    ui.MainWindow.irradiance)
                    ui.MainWindow.plt.autoRange()
                    if not data["rx"]:
                        state = 2
                except Exception as e:
                    pass
            elif state == 2:
                file_name = ui.MainWindow.file_name.text()
                file_name = "measures/IV_measure" if file_name == "" else file_name
                irradiance = ui.MainWindow.irradiance.text()
                file_name = file_name + ("" if irradiance == "" else ("_" + irradiance))
                path = ui.folder + file_name + ".csv"
                cont = 1
                while exists(path):
                    path = ui.folder + file_name + "({})".format(cont) + ".csv"
                    cont += 1
                with open(path, 'w', newline='') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    # write a row to the csv file
                    for (i, j) in zip(ui.listV, ui.listC):
                        writer.writerow([i, j])
                ui.startButton.animateClick(1)
                state = 0
        yield 0.1


# FUNCTION CATEGORY 2 -----------------------------------------


# FUNCTION CATEGORY n -----------------------------------------


# -----------------------------------------------------------------------------
# RUNTIME PROCEDURE
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Solar_radiation()
    ui.show()
    Main_loop(ui)
    sys.exit(app.exec_())
