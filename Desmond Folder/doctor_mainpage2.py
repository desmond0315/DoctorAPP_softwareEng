from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from appoinmentpage import Ui_MainWindow as AppointmentUi_MainWindow
from profilepage import Ui_MainWindow as Ui_ProfileWindow  # Import the Ui_ProfileWindow class
from finddoctorpage import Ui_MainWindow as FindDoctorUi_MainWindow
from hospitalpage import Ui_MainWindow as HospitalUi_MainWindow
from new_hospital_join import Ui_MainWindow as joinUi_MainWindow
import pyrebase
import atexit


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
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 1441, 80))
        self.header.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.FindDoc_btn = QtWidgets.QPushButton(self.header)
        self.FindDoc_btn.setGeometry(QtCore.QRect(540, 30, 101, 28))
        self.FindDoc_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FindDoc_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(98, 98, 98);\n"
"    font-size: 17px;\n"
"    border: none;\n"
"\n"
"}\n"
"")
        self.FindDoc_btn.setObjectName("FindDoc_btn")
        self.Profile_btn = QtWidgets.QPushButton(self.header)
        self.Profile_btn.setGeometry(QtCore.QRect(700, 30, 93, 28))
        self.Profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Profile_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(98, 98, 98);\n"
"    font-size: 17px;\n"
"    border: none;\n"
"\n"
"}\n"
"")
        self.Profile_btn.setObjectName("Profile_btn")
        self.Appoinment_btn = QtWidgets.QPushButton(self.header)
        self.Appoinment_btn.setGeometry(QtCore.QRect(860, 30, 93, 28))
        self.Appoinment_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Appoinment_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(98, 98, 98);\n"
"    font-size: 17px;\n"
"    border: none;\n"
"\n"
"}\n"
"")
        self.Appoinment_btn.setObjectName("Appoinment_btn")
        self.Hospital_btn = QtWidgets.QPushButton(self.header)
        self.Hospital_btn.setGeometry(QtCore.QRect(1010, 30, 131, 28))
        self.Hospital_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Hospital_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(98, 98, 98);\n"
"    font-size: 17px;\n"
"    border: none;\n"
"\n"
"}\n"
"")
        self.Hospital_btn.setObjectName("Hospital_btn")
        self.logo = QtWidgets.QLabel(self.header)
        self.logo.setGeometry(QtCore.QRect(40, 10, 191, 61))
        self.logo.setStyleSheet("QLabel {\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size: contain; /* or \'cover\' depending on how you want it to fit */\n"
"}\n"
"")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\Doctor2u (1).png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.request_btn = QtWidgets.QPushButton(self.header)
        self.request_btn.setGeometry(QtCore.QRect(1220, 10, 81, 71))
        self.request_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.request_btn.setStyleSheet("border-radius: 40px;")
        self.request_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\request.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.request_btn.setIcon(icon)
        self.request_btn.setIconSize(QtCore.QSize(40, 40))
        self.request_btn.setCheckable(False)
        self.request_btn.setObjectName("request_btn")
        self.join_btn = QtWidgets.QPushButton(self.header)
        self.join_btn.setGeometry(QtCore.QRect(300, 30, 121, 28))
        self.join_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.join_btn.setStyleSheet("QPushButton {\n"
"    font-size: 17px;\n"
"    color: rgb(232, 0, 0);\n"
"    border: none;\n"
"\n"
"}\n"
"")
        self.join_btn.setObjectName("join_btn")
        self.center_frame = QtWidgets.QFrame(self.centralwidget)
        self.center_frame.setGeometry(QtCore.QRect(-10, 80, 1461, 731))
        self.center_frame.setStyleSheet("background-color: rgb(217, 255, 254);")
        self.center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame.setObjectName("center_frame")
        self.title = QtWidgets.QLabel(self.center_frame)
        self.title.setGeometry(QtCore.QRect(330, 30, 871, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.left_frame = QtWidgets.QFrame(self.center_frame)
        self.left_frame.setGeometry(QtCore.QRect(230, 130, 431, 491))
        self.left_frame.setStyleSheet("QFrame {\n"
"    background-color: #ffffff; /* Optional: set a background color */\n"
"    border: 2px solid #000000; /* Border width and color */\n"
"    border-radius: 15px;       /* Border radius for rounded corners */\n"
"}\n"
"")
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
        self.left_title = QtWidgets.QLabel(self.left_frame)
        self.left_title.setGeometry(QtCore.QRect(30, 310, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.left_title.setFont(font)
        self.left_title.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"")
        self.left_title.setObjectName("left_title")
        self.left_desc = QtWidgets.QLabel(self.left_frame)
        self.left_desc.setGeometry(QtCore.QRect(20, 370, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.left_desc.setFont(font)
        self.left_desc.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"")
        self.left_desc.setObjectName("left_desc")
        self.left_search = QtWidgets.QPushButton(self.left_frame)
        self.left_search.setGeometry(QtCore.QRect(110, 427, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.left_search.setFont(font)
        self.left_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_search.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"    color: rgb(85, 0, 255);\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.left_search.setCheckable(False)
        self.left_search.setFlat(False)
        self.left_search.setObjectName("left_search")
        self.leftphoto = QtWidgets.QLabel(self.left_frame)
        self.leftphoto.setGeometry(QtCore.QRect(70, 40, 301, 271))
        self.leftphoto.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.leftphoto.setText("")
        self.leftphoto.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\doctorleftframe.jpg"))
        self.leftphoto.setScaledContents(True)
        self.leftphoto.setObjectName("leftphoto")
        self.right_frame = QtWidgets.QFrame(self.center_frame)
        self.right_frame.setGeometry(QtCore.QRect(870, 130, 431, 491))
        self.right_frame.setStyleSheet("QFrame {\n"
"    background-color: #ffffff; /* Optional: set a background color */\n"
"    border: 2px solid #000000; /* Border width and color */\n"
"    border-radius: 15px;       /* Border radius for rounded corners */\n"
"}\n"
"")
        self.right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame.setObjectName("right_frame")
        self.right_title = QtWidgets.QLabel(self.right_frame)
        self.right_title.setGeometry(QtCore.QRect(20, 310, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.right_title.setFont(font)
        self.right_title.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"")
        self.right_title.setObjectName("right_title")
        self.right_desc = QtWidgets.QLabel(self.right_frame)
        self.right_desc.setGeometry(QtCore.QRect(80, 370, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.right_desc.setFont(font)
        self.right_desc.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"")
        self.right_desc.setObjectName("right_desc")
        self.right_search = QtWidgets.QPushButton(self.right_frame)
        self.right_search.setGeometry(QtCore.QRect(140, 427, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.right_search.setFont(font)
        self.right_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.right_search.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"    color: rgb(85, 0, 255);\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.right_search.setCheckable(False)
        self.right_search.setFlat(False)
        self.right_search.setObjectName("right_search")
        self.rightphoto = QtWidgets.QLabel(self.right_frame)
        self.rightphoto.setGeometry(QtCore.QRect(70, 20, 301, 311))
        self.rightphoto.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.rightphoto.setText("")
        self.rightphoto.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\doctorrightframe.jpg"))
        self.rightphoto.setScaledContents(True)
        self.rightphoto.setObjectName("rightphoto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.left_search.clicked.connect(self.navigate_to_appointment_page)
        self.request_btn.clicked.connect(self.show_small_window)
        self.Profile_btn.clicked.connect(self.navigate_to_profile_page)
        self.FindDoc_btn.clicked.connect(self.navigate_to_find_doctor_page)
        self.Appoinment_btn.clicked.connect(self.navigate_to_appointment_page)
        self.right_search.clicked.connect(self.navigate_to_find_doctor_page)
        self.Hospital_btn.clicked.connect(self.navigate_to_hospital_page)
        self.join_btn.clicked.connect(self.navigate_to_join_page)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FindDoc_btn.setText(_translate("MainWindow", "Find A Doctor"))
        self.Profile_btn.setText(_translate("MainWindow", "Profile"))
        self.Appoinment_btn.setText(_translate("MainWindow", "Appointment"))
        self.Hospital_btn.setText(_translate("MainWindow", "Hospital"))
        self.join_btn.setText(_translate("MainWindow", "JOIN US !"))
        self.title.setText(_translate("MainWindow", "Book your consultation with your doctor anywhere !"))
        self.left_title.setText(_translate("MainWindow", "Locate Your Best Healthcare Provider"))
        self.left_desc.setText(_translate("MainWindow", "Discover and connect with the best healthcare providers in your area."))
        self.left_search.setText(_translate("MainWindow", "Make Appointment Now"))
        self.right_title.setText(_translate("MainWindow", "Search And Discover Your Ideal Doctor"))
        self.right_desc.setText(_translate("MainWindow", "Discover Healthcare Professionals in Your Area"))
        self.right_search.setText(_translate("MainWindow", "View Doctor Now"))

    def navigate_to_join_page(self):
        try:
            print("Navigating to join page...")
            # Create an instance of the appointment page UI
            self.join_window = QtWidgets.QMainWindow()
            self.join_ui = joinUi_MainWindow()
            self.join_ui.setupUi(self.join_window)
            self.join_window.show()

            # Close the main window of the previous page
        except Exception as e:
            print("Error:", e)
    def navigate_to_appointment_page(self):
        try:
            print("Navigating to appointment page...")
            # Create an instance of the appointment page UI
            self.appointment_window = QtWidgets.QMainWindow()
            self.appointment_ui = AppointmentUi_MainWindow()
            self.appointment_ui.setupUi(self.appointment_window)
            self.appointment_window.show()

            # Close the main window of the previous page
        except Exception as e:
            print("Error:", e)

    def navigate_to_hospital_page(self):
        try:
            print("Navigating to hospital page...")
            # Create an instance of the appointment page UI
            self.hospital_window = QtWidgets.QMainWindow()
            self.hospital_ui = HospitalUi_MainWindow()
            self.hospital_ui.setupUi(self.hospital_window)
            self.hospital_window.show()

            # Close the main window of the previous page
        except Exception as e:
            print("Error:", e)


    def navigate_to_profile_page(self):
        try:
            print("Navigating to profile page...")
            # Create an instance of the profile page UI
            self.profile_window = QtWidgets.QMainWindow()
            self.profile_ui = Ui_ProfileWindow()
            self.profile_ui.setupUi(self.profile_window)
            self.profile_window.show()

            # Close the main window of the previous page
        except Exception as e:
            print("Error:", e)

    def navigate_to_find_doctor_page(self):
        try:
            print("Navigating to find doctor page...")
            # Create an instance of the find doctor page UI
            self.find_doctor_window = QtWidgets.QMainWindow()
            self.find_doctor_ui = FindDoctorUi_MainWindow()
            self.find_doctor_ui.setupUi(self.find_doctor_window)
            self.find_doctor_window.show()

            # Close the main window of the previous page
            self.MainWindow.close()
        except Exception as e:
            print("Error:", e)

    def show_small_window(self):
        x_offset = 850
        y_offset = 430
        self.small_window = SmallWindow()
        self.small_window.show_at_location(x_offset, y_offset)


class SmallWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SmallWindow, self).__init__(parent)
        self.setWindowTitle("Patient History")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        # Get logged in user email
        loggedin = db.child("loggedin").get()
        l_email = loggedin.val()["email"]

        appointment = db.child("appointment").get()
        for appointments in appointment.each():
            a_firstname = appointments.val()["firstname"]
            a_lastname = appointments.val()["lastname"]
            a_username = appointments.val()["username"]
            a_hospital = appointments.val()["hospital"]
            a_doctor = appointments.val()["doctor"]
            a_time = appointments.val()["time"]
            a_date = appointments.val()["date"]
            a_medreq = appointments.val()["medreq"]
            a_email = appointments.val()["email"]
            if a_email == l_email:
                break

        # Example label for Patient's Name (replace with dynamic data)
        self.name_label = QtWidgets.QLabel("Name: ", self)
        layout.addWidget(self.name_label)
        self.name_label.setText(f"Name: {a_firstname} {a_lastname}")

        # Table for Recent Appointments (replace with dynamic data)
        self.recent_appointments_label = QtWidgets.QLabel("Pending Appointments:", self)
        layout.addWidget(self.recent_appointments_label)
        self.appointments_table = QtWidgets.QTableWidget(self)
        self.appointments_table.setColumnCount(3)
        self.appointments_table.setHorizontalHeaderLabels(["Date", "Doctor", "Hospital"])

        layout.addWidget(self.appointments_table)

        self.appointments_table.setRowCount(1)
        self.appointments_table.setItem(0, 0, QtWidgets.QTableWidgetItem(a_date))
        self.appointments_table.setItem(0, 1, QtWidgets.QTableWidgetItem(a_doctor))
        self.appointments_table.setItem(0, 2, QtWidgets.QTableWidgetItem(a_hospital))

        # Close button
        self.close_button = QtWidgets.QPushButton("Close", self)
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def set_patient_name(self, patient_name):
        self.name_label.setText(f"Name: {patient_name}")

    def load_appointments_data(self, appointments):
        self.appointments_table.setRowCount(len(appointments))
        for row, (date, doctor, hospital) in enumerate(appointments):
            self.appointments_table.setItem(row, 0, QtWidgets.QTableWidgetItem(date))
            self.appointments_table.setItem(row, 1, QtWidgets.QTableWidgetItem(doctor))
            self.appointments_table.setItem(row, 2, QtWidgets.QTableWidgetItem(hospital))


    def show_at_location(self, x, y):
        self.move(x, y)
        self.show()

def exit_handler():
    db.child("loggedin").remove()


atexit.register(exit_handler)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
