from PyQt5 import QtCore, QtGui, QtWidgets
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

        #self.backmain_btn = QtWidgets.QPushButton(self.center_frame)
        #self.backmain_btn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        #self.backmain_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.backmain_btn.setObjectName("backmain_btn")
        #self.backmain_btn.setHidden(True)

        #self.edit_table_btn = QtWidgets.QPushButton(self.center_frame)
        #self.edit_table_btn.setGeometry(QtCore.QRect(110, 20, 100, 23))
        #self.edit_table_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.edit_table_btn.setObjectName("edit_table_btn")
        #self.edit_table_btn.setText("Edit Table")
        #self.edit_table_btn.clicked.connect(self.enableTableEditing)

        self.setupTableWidget()

    def setupTableWidget(self):
        self.tableWidget = QtWidgets.QTableWidget(self.center_frame)
        self.tableWidget.setGeometry(QtCore.QRect(140, 60, 1281, 601))
        self.tableWidget.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")

        headers = ["Name", "Age", "IC", "Last visit date", "Last visit time", "Med Req", "Doctor Name", "", ""]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.populateTable()

    def populateTable(self):
        appointment_pending = db.child("appointment_pending").get()
        if appointment_pending and appointment_pending.each():
            self.tableWidget.setRowCount(0)  # Clear existing rows
            for appointments_pending in appointment_pending.each():
                ap_key = appointments_pending.key()
                ap_firstname = appointments_pending.val().get("firstname", "")
                ap_lastname = appointments_pending.val().get("lastname", "")
                ap_age = appointments_pending.val().get("age", "")
                ap_ic_number = appointments_pending.val().get("ic_number", "")
                ap_date = appointments_pending.val().get("date", "")
                ap_time = appointments_pending.val().get("time", "")
                ap_medreq = appointments_pending.val().get("medreq", "")
                ap_doctor = appointments_pending.val().get("doctor", "")

                ap_fullname = f"{ap_firstname} {ap_lastname}"

                approve_btn = QtWidgets.QPushButton(self.tableWidget)
                approve_btn.setText("Approve")

                delete_btn = QtWidgets.QPushButton(self.tableWidget)
                delete_btn.setText("Delete")

                rowPosition = self.tableWidget.rowCount()
                approve_btn.clicked.connect(lambda _, key=ap_key, row=rowPosition: self.approveRow(key, row))
                delete_btn.clicked.connect(lambda _, key=ap_key, row=rowPosition: self.deleteRow(key, row))

                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(ap_fullname))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(ap_age))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(ap_ic_number))
                self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(ap_date))
                self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(ap_time))
                self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(ap_medreq))
                self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(ap_doctor))
                self.tableWidget.setCellWidget(rowPosition, 7, approve_btn)
                self.tableWidget.setCellWidget(rowPosition, 8, delete_btn)

    def approveRow(self, key, row):
        data = db.child("appointment_pending").child(key).get().val()
        db.child("appointment").child(key).update(data)

        # Delete from QTableWidget
        self.tableWidget.removeRow(row)

        # Delete from Firebase
        db.child("appointment_pending").child(key).remove()

    def deleteRow(self, key, row):
        # Delete from QTableWidget
        self.tableWidget.removeRow(row)

        # Delete from Firebase
        db.child("appointment_pending").child(key).remove()
        self.populateTable()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PATIENT REQUEST APPROVAL"))
        self.label.setGeometry(QtCore.QRect(180, 0, 1461, 60))
        #self.backmain_btn.setText(_translate("MainWindow", "BACK"))


if _name_ == "_main_":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())