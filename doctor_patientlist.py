from PyQt5 import QtCore, QtGui, QtWidgets
from doctorloginpage import Ui_Dialog as doctorlogin_MainWindow



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1461, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.setupHeader(MainWindow)
        self.setupCenterFrame(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupHeader(self, MainWindow):
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 1461, 80))
        self.header.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")

        self.logo = QtWidgets.QLabel(self.header)
        self.logo.setGeometry(QtCore.QRect(-10, 0, 191, 61))
        self.logo.setStyleSheet(
            "QLabel { background-repeat: no-repeat; background-position: center; background-size: contain; }")
        self.logo.setPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\New folder\\Doctor2u (1).png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.label = QtWidgets.QLabel(self.header)
        self.label.setGeometry(QtCore.QRect(30, 10, 211, 41))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

    def setupCenterFrame(self, MainWindow):
        self.center_frame = QtWidgets.QFrame(self.centralwidget)
        self.center_frame.setGeometry(QtCore.QRect(0, 60, 1471, 751))
        self.center_frame.setStyleSheet(
            "background-color: rgb(217, 255, 254); border-bottom-color: rgb(255, 255, 255);")
        self.center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame.setObjectName("center_frame")

        self.backmain_btn = QtWidgets.QPushButton(self.center_frame)
        self.backmain_btn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.backmain_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backmain_btn.setObjectName("backmain_btn")

        self.edit_table_btn = QtWidgets.QPushButton(self.center_frame)
        self.edit_table_btn.setGeometry(QtCore.QRect(110, 20, 100, 23))
        self.edit_table_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_table_btn.setObjectName("edit_table_btn")
        self.edit_table_btn.setText("Edit Table")
        self.edit_table_btn.clicked.connect(self.enableTableEditing)

        self.setupTableWidget()
        self.backmain_btn.clicked.connect(self.navigate_to_doctor_login_page)


    def setupTableWidget(self):
        self.tableWidget = QtWidgets.QTableWidget(self.center_frame)
        self.tableWidget.setGeometry(QtCore.QRect(140, 60, 1281, 601))
        self.tableWidget.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(4)

        headers = ["Name", "Age", "IC", "Last visit date", "Last visit time", "Meds"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item.setText(header)

        patients = [
            ["Potato", "87", "020305-07-0325", "1 April 2011", "1200", "-"],
            ["Johny", "69", "04124-04-4204", "2May 2044", "1400", "-"],
            ["Adeline", "30", "870807-08-0087", "6 Sept 2012", "1800", "-"]
        ]

        for row, patient in enumerate(patients, start=1):
            for col, detail in enumerate(patient):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(row, col, item)
                item.setText(detail)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def enableTableEditing(self):
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.AllEditTriggers)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PATIENT LIST"))
        self.backmain_btn.setText(_translate("MainWindow", "BACK"))

    def navigate_to_doctor_login_page(self):
        try:
            print("Navigating to login page...")
            # Create an instance of the login page UI
            self.doctorlogin_window = QtWidgets.QMainWindow()
            self.doctorlogin_ui = doctorlogin_MainWindow()
            self.doctorlogin_ui.setupUi(self.doctorlogin_window)
            self.doctorlogin_window.show()

            # Close the main window of the previous page
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
