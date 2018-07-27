# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 70)
        MainWindow.setMinimumSize(QtCore.QSize(290, 70))
        MainWindow.setMaximumSize(QtCore.QSize(290, 70))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 41, 47, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 10, 51, 21))
        self.label.setObjectName("label")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(210, 12, 71, 21))
        self.downloadButton.setObjectName("downloadButton")
        self.activityIdField = QtWidgets.QLineEdit(self.centralwidget)
        self.activityIdField.setGeometry(QtCore.QRect(70, 11, 131, 20))
        self.activityIdField.setInputMethodHints(QtCore.Qt.ImhNone)
        self.activityIdField.setObjectName("activityIdField")
        self.filenameField = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameField.setGeometry(QtCore.QRect(70, 40, 211, 21))
        self.filenameField.setObjectName("filenameField")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Strava Gpx Downloader"))
        self.label_2.setText(_translate("MainWindow", "Filename"))
        self.label.setText(_translate("MainWindow", "Activity ID"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

