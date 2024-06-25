from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pyrebase


firebaseConfig = {
    'apiKey': "AIzaSyCVw3U9mV4RZsv4ByZf8bYUHicSbtdqLpo",
    'authDomain': "doctorapp-5009cem.firebaseapp.com",
    'databaseURL': "https://doctorapp-5009cem-default-rtdb.firebaseio.com",
    'projectId': "doctorapp-5009cem",
    'storageBucket': "doctorapp-5009cem.appspot.com",
    'messagingSenderId': "534087094334",
    'appId': "1:534087094334:web:90a701b5db96341b32416f",
    'measurementId': "G-K3CERXJ1VT"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


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
        self.add_doctor_btn.clicked.connect(lambda: self.add_doctor_action(MainWindow))

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
        self.logo.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\Doctor2u (1).png"))
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

        self.add_doctor_btn = QtWidgets.QPushButton(self.center_frame)
        self.add_doctor_btn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.add_doctor_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_doctor_btn.setObjectName("add_doctor_btn")
        self.add_doctor_btn.setText("Add Doctor")

        self.setupTableWidget()

    def setupTableWidget(self):
        self.tableWidget = QtWidgets.QTableWidget(self.center_frame)
        self.tableWidget.setGeometry(QtCore.QRect(140, 60, 1281, 601))
        self.tableWidget.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")

        headers = ["Name", "Spoken Language", "Specialty", "Summary", ""]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.populateTable()

    def populateTable(self):
        doctor = db.child("doctor").get()
        if doctor and doctor.each():
            self.tableWidget.setRowCount(0)  # Clear existing rows
            for doctors in doctor.each():
                d_key = doctors.key()
                d_name = doctors.val().get("name", "")
                d_spoken_lg = doctors.val().get("spoken_lg", "")
                d_specialty = doctors.val().get("specialty", "")
                d_summary = doctors.val().get("summary", "")

                delete_btn = QtWidgets.QPushButton(self.tableWidget)
                delete_btn.setText("Delete")

                rowPosition = self.tableWidget.rowCount()
                delete_btn.clicked.connect(lambda _, key=d_key, row=rowPosition: self.deleteRow(key, row))

                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(d_name))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(d_spoken_lg))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(d_specialty))
                self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(d_summary))

                self.tableWidget.setCellWidget(rowPosition, 4, delete_btn)

    def add_doctor_action(self, Dialog):
        try:
            import adddoctor
            self.new_page = QtWidgets.QDialog()
            self.ui = adddoctor.Ui_Dialog()
            self.ui.setupUi(self.new_page)
            self.new_page.show()

        except Exception as e:
            print("An error occurred:", e)

    def deleteRow(self, key, row):
        # Delete from QTableWidget
        self.tableWidget.removeRow(row)

        # Delete from Firebase
        db.child("doctor").child(key).remove()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LIST OF DOCTORS"))
        self.label.setGeometry(QtCore.QRect(180, 0, 1461, 60))


if _name_ == "_main_":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


