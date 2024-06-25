from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import pyrebase
from PyQt5.QtCore import QDate

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
        MainWindow.resize(1438, 789)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.setupHeader()
        self.setupCenterFrame()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupHeader(self):
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 1441, 80))
        self.header.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")

        self.logo = QtWidgets.QLabel(self.header)
        self.logo.setGeometry(QtCore.QRect(-10, 0, 191, 61))
        self.logo.setStyleSheet("QLabel {\n"
                                "    background-repeat: no-repeat;\n"
                                "    background-position: center;\n"
                                "    background-size: contain;\n"
                                "}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("C:\\Users\\60111\\PycharmProjects\\DoctorApp\\Doctor2u (1).png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

    def setupCenterFrame(self):
        self.center_frame = QtWidgets.QFrame(self.centralwidget)
        self.center_frame.setGeometry(QtCore.QRect(-10, 60, 1461, 751))
        self.center_frame.setStyleSheet("background-color: rgb(217, 255, 254);")
        self.center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame.setObjectName("center_frame")

        self.setupMapFrame()
        self.setupForm()

    def setupMapFrame(self):
        self.mapframe = QtWidgets.QFrame(self.center_frame)
        self.mapframe.setGeometry(QtCore.QRect(50, 60, 751, 561))
        self.mapframe.setStyleSheet("QFrame {\n"
                                    "    background-color: #ffffff;\n"
                                    "    border: 2px solid #000000;\n"
                                    "    border-radius: 15px;\n"
                                    "}")
        self.mapframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mapframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mapframe.setObjectName("mapframe")

        self.webview = QtWebEngineWidgets.QWebEngineView(self.mapframe)
        self.webview.setGeometry(QtCore.QRect(0, 0, 751, 561))
        self.webview.load(
            QtCore.QUrl("https://www.google.com.my/maps/search/hospitals+in+penang/@5.4104848,100.3421989,12.8z?hl=en"))

    def setupForm(self):
        self.title = QtWidgets.QLabel(self.center_frame)
        self.title.setGeometry(QtCore.QRect(870, 50, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(38, 208, 0);")
        self.title.setObjectName("title")

        self.medical_input = QtWidgets.QLineEdit(self.center_frame)
        self.medical_input.setGeometry(QtCore.QRect(1160, 120, 261, 301))
        self.medical_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.medical_input.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.medical_input.setObjectName("medical_input")

        self.date_select = QtWidgets.QDateEdit(self.center_frame)
        self.date_select.setGeometry(QtCore.QRect(870, 390, 261, 31))
        self.date_select.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_select.setObjectName("date_select")
        self.date_select.setCalendarPopup(True)
        self.date_select.setDisplayFormat("yyyy-MM-dd")

        # Set the minimum date to today
        today = QDate.currentDate()
        self.date_select.setMinimumDate(today)

        self.setupComboboxes()
        self.setupButton()

        self.age_input = QtWidgets.QLineEdit(self.center_frame)
        self.age_input.setGeometry(QtCore.QRect(870, 470, 261, 31))
        self.age_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.age_input.setObjectName("age_input")
        self.age_input.setPlaceholderText("Enter age...")

    def setupComboboxes(self):
        self.hospital_select = QtWidgets.QComboBox(self.center_frame)
        self.hospital_select.setGeometry(QtCore.QRect(870, 120, 261, 31))
        self.hospital_select.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hospital_select.setObjectName("hospital_select")
        self.hospital_select.addItem("--SELECT HOSPITAL--")
        self.hospital_select.addItem("Island Hospital Penang")
        self.hospital_select.addItem("Gleneagles Penang")

        self.hospital_select.currentIndexChanged.connect(self.update_doctor_list)

        self.doctor_select = QtWidgets.QComboBox(self.center_frame)
        self.doctor_select.setGeometry(QtCore.QRect(870, 210, 261, 31))
        self.doctor_select.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctor_select.setObjectName("doctor_select")

        self.time_select = QtWidgets.QComboBox(self.center_frame)
        self.time_select.setGeometry(QtCore.QRect(870, 300, 261, 31))
        self.time_select.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_select.setObjectName("time_select")
        self.time_select.addItem("--SELECT TIME--")
        self.time_select.addItem("12:00 PM")
        self.time_select.addItem("12:30 PM")
        self.time_select.addItem("01:00 PM")
        self.time_select.addItem("01:30 PM")
        self.time_select.addItem("02:00 PM")
        self.time_select.addItem("02:30 PM")
        self.time_select.addItem("03:00 PM")
        self.time_select.addItem("03:30 PM")
        self.time_select.addItem("04:00 PM")
        self.time_select.addItem("04:30 PM")

    def setupButton(self):
        self.pushButton = QtWidgets.QPushButton(self.center_frame)
        self.pushButton.setGeometry(QtCore.QRect(1000, 540, 271, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 15pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Make Appointment")
        self.pushButton.clicked.connect(self.make_appointment)


    def update_doctor_list(self):
        hospital = self.hospital_select.currentText()
        self.doctor_select.clear()
        self.doctor_select.addItem("--SELECT DOCTOR--")

        doctors = {
            "Island Hospital Penang": [
                "Dr. Lim Wei Peng (Island Hospital)",
                "Dr. Lee Chong Wei (Island Hospital)",
                "Dr. Tan Chia Ying (Island Hospital)",
                "Dr. Anand Raj (Island Hospital)"
            ],
            "Gleneagles Penang": [
                "Dr. Anjali Menon (Gleneagles Hospital)",
                "Dr. Tan Siew Lee (Gleneagles Hospital)",
                "Dr. Ramesh Kumar (Gleneagles Hospital)",
                "Dr. Wong Lee Hua (Gleneagles Hospital)"
            ]
        }

        if hospital in doctors:
            for doctor in doctors[hospital]:
                self.doctor_select.addItem(doctor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Doctor's Appointment Details"))
        self.medical_input.setPlaceholderText(_translate("MainWindow", "Medical Request..."))

    def make_appointment(self):
        hospital = self.hospital_select.currentText()
        doctor = self.doctor_select.currentText()
        time = self.time_select.currentText()
        date = self.date_select.date().toString("yyyy-MM-dd")
        medical_request = self.medical_input.text()
        age = self.age_input.text()

        if hospital == "--SELECT HOSPITAL--" or doctor == "--SELECT DOCTOR--" or time == "--SELECT TIME--" or not medical_request or not age:
            QtWidgets.QMessageBox.warning(None, "Incomplete Data", "Please fill all fields to make an appointment.")
        else:
            appointment_details = f"Appointment made with {doctor} at {hospital} on {date} at {time}.\nMedical Request: {medical_request}"
            QtWidgets.QMessageBox.information(None, "Appointment Confirmed", appointment_details)

        # Get logged in user email
        loggedin = db.child("loggedin").get()
        l_email = loggedin.val()["email"]

        user = db.child("user").get()
        for users in user.each():
            u_firstname = users.val()["firstname"]
            u_lastname = users.val()["lastname"]
            u_mobilenumber = users.val()["mobilenumber"]
            u_email = users.val()["email"]
            u_gender = users.val()["gender"]
            u_ic_number = users.val()["ic_number"]
            u_username = users.val()["username"]
            if u_email == l_email:
                break

        data = {"firstname": u_firstname, "lastname": u_lastname, "username": u_username, "hospital": hospital, "doctor": doctor, "time": time, "date": date, "medreq": medical_request, "email": u_email, "age": age, "ic_number": u_ic_number}
        db.child("appointment_pending").child(u_username).set(data)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
