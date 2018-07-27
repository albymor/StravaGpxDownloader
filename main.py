from PyQt5 import QtCore, QtGui, QtWidgets
import GUI


class StravaGpxDownloader(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(StravaGpxDownloader, self).__init__(parent)
        self.setupUi(self)
        self.activityIdField.setText("0123456789")
        self.filenameField.setText("stravaOut.gpx")
        self.downloadButton.clicked.connect(self.downloadGpx)


    def downloadGpx(self):
        import gpxDownloader
        activityID = self.activityIdField.text().strip()
        filename = self.filenameField.text().strip()
        if len(activityID) != 10 or not activityID.isdigit():
            QtWidgets.QMessageBox.information(
                self, "Error", "Wrong ActivityID format")
        else:
            gpxDownloader.downloader(activityID, filename)
            QtWidgets.QMessageBox.information(
                self, "Done!", "Done dowloading gpx!")


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = StravaGpxDownloader()
    form.show()
    app.exec_()


if __name__ == "__main__":
    import sys
    main()