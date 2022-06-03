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
import pyqtgraph as pg

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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.plt = PlotWidget(self.centralwidget)
        self.plt.setObjectName("plt")
        self.gridLayout.addWidget(self.plt, 0, 1, 4, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
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
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))

        # ----------------------------
        self.plt.setLabel('left', '<font size="5">Voltage</font>', units='<font size="5">V</font>')
        self.plt.setLabel('bottom', '<font size="5">Current</font>', units='<font size="5">mA</font>')
        self.plt.setTitle('<font size="5">VI curve</font>')
        self.plt.setBackground('w')
        self.plt.showGrid(x=True, y=True)
        self.plt.addLegend()
        y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        y2 = [0, 1, 2, 4, 12, 14, 16, 17, 14, 22]
        x = range(0, 10)
        self.plt.plot(x, y, pen=pg.mkPen('b', width=2), name='<font size="5">Red</font>')
        self.plt.plot(x, y2, pen='r', symbol='o', symbolPen='r', symbolBrush=0.5, name='blue')


from pyqtgraph import PlotWidget


# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

# FUNCTION CATEGORY 1 -----------------------------------------
def foo(arg1, arg2):
    '''
    Complete description of the method, what it does and how it should be used
    :param arg1: type - description of the 1st argument
    :param arg2: type - description of the 2nd argument
    :return: type - description of the value returned
    :timeComplexityTerm TERM_X: type - term used in the Complexity formula
    :timeComplexityDominantOperation  OP_X: type - operation considered to
        calculate the time complexity of this method
    :timeComplexity: O(OP_X*TERM_X²)
    '''
    # what this variable means and how it is calculated
    stall = arg1
    # what is being calculated, and what are the parameters and values used
    stall = arg2 - foo(arg1, stall)

    return None


# FUNCTION CATEGORY 2 -----------------------------------------


# FUNCTION CATEGORY n -----------------------------------------


# -----------------------------------------------------------------------------
# RUNTIME PROCEDURE
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
