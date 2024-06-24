from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox  # Add this line to import QMessageBox
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
        MainWindow.resize(1438, 789)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1414, 765))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("background-color: rgb(214, 255, 192);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1391, 71))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.logo = QtWidgets.QLabel(self.frame_2)
        self.logo.setGeometry(QtCore.QRect(10, 10, 191, 61))
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

        self.title = QtWidgets.QLabel(self.frame_2)
        self.title.setGeometry(QtCore.QRect(400, 0, 671, 61))
        self.title.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";")
        self.title.setObjectName("title")

        self.hospital_frame = QtWidgets.QFrame(self.frame)
        self.hospital_frame.setGeometry(QtCore.QRect(680, 110, 691, 601))
        self.hospital_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    background-color: #ffffff; /* Optional: set a background color */\n"
"    border: 2px solid #000000; /* Border width and color */\n"
"    border-radius: 15px;       /* Border radius for rounded corners */\n"
"")
        self.hospital_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hospital_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hospital_frame.setObjectName("hospital_frame")

        self.hospitalname = QtWidgets.QLabel(self.hospital_frame)
        self.hospitalname.setGeometry(QtCore.QRect(20, 10, 171, 41))
        self.hospitalname.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"border: no\n"
"")
        self.hospitalname.setObjectName("hospitalname")

        self.hospitaldescription = QtWidgets.QLabel(self.hospital_frame)
        self.hospitaldescription.setGeometry(QtCore.QRect(20, 240, 231, 41))
        self.hospitaldescription.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"border: no\n"
"")
        self.hospitaldescription.setObjectName("hospitaldescription")
        self.hospitalcontact = QtWidgets.QLabel(self.hospital_frame)
        self.hospitalcontact.setGeometry(QtCore.QRect(20, 120, 191, 41))
        self.hospitalcontact.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"border: no\n"
"")
        self.hospitalcontact.setObjectName("hospitalcontact")
        self.hospitaldesc_input = QtWidgets.QLineEdit(self.hospital_frame)
        self.hospitaldesc_input.setGeometry(QtCore.QRect(20, 280, 651, 251))
        self.hospitaldesc_input.setStyleSheet(" border: 1px solid #000000; /* Border width and color */\n"
"    border-radius: 0px;       /* Border radius for rounded corners */\n"
"background-color: rgb(226, 226, 226);\n"
"")
        self.hospitaldesc_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hospitaldesc_input.setObjectName("hospitaldesc_input")
        self.hospitalname_input = QtWidgets.QLineEdit(self.hospital_frame)
        self.hospitalname_input.setGeometry(QtCore.QRect(20, 50, 651, 71))
        self.hospitalname_input.setStyleSheet(" border: 1px solid #000000; /* Border width and color */\n"
"background-color: rgb(226, 226, 226);\n"
"    border-radius: 0px;       /* Border radius for rounded corners */")
        self.hospitalname_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hospitalname_input.setObjectName("hospitalname_input")
        self.hospitalcontact_input = QtWidgets.QLineEdit(self.hospital_frame)
        self.hospitalcontact_input.setGeometry(QtCore.QRect(20, 160, 651, 71))
        self.hospitalcontact_input.setStyleSheet(" border: 1px solid #000000; /* Border width and color */\n"
"    border-radius: 0px;       /* Border radius for rounded corners */\n"
"background-color: rgb(226, 226, 226);\n"
"")
        self.hospitalcontact_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hospitalcontact_input.setObjectName("hospitalcontact_input")
        self.submit_btn = QtWidgets.QPushButton(self.hospital_frame)
        self.submit_btn.setGeometry(QtCore.QRect(270, 550, 191, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.submit_btn.setFont(font)
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_btn.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(80, 229, 0);\n"
"")
        self.submit_btn.setAutoDefault(False)
        self.submit_btn.setObjectName("submit_btn")
        self.picture = QtWidgets.QLabel(self.frame)
        self.picture.setGeometry(QtCore.QRect(40, 120, 581, 581))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\doctorcute.jpg"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.submit_btn.clicked.connect(self.showMessageBox)

    def showMessageBox(self):
        # Check if any of the fields are empty
        hospital_name = self.hospitalname_input.text()
        hospital_contact = self.hospitalcontact_input.text()
        hospital_description = self.hospitaldesc_input.text()

        if hospital_name == '' or hospital_contact == '' or hospital_description == '':
            # Display a warning message box
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("All fields are required!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            # Display a success message box
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Form submitted successfully!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

            data = {"hospital_name": hospital_name, "hospital_contact": hospital_contact, "hospital_description": hospital_description}
            db.child("new_hospital").child(hospital_name).set(data)

            # Clear input fields after successful submission
            self.hospitalname_input.clear()
            self.hospitalcontact_input.clear()
            self.hospitaldesc_input.clear()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "New Hospital Registration Form"))
        self.hospitalname.setText(_translate("MainWindow", "Hospital Name :"))
        self.hospitaldescription.setText(_translate("MainWindow", "Hospital Description :"))
        self.hospitalcontact.setText(_translate("MainWindow", "Hospital Contact :"))
        self.hospitaldesc_input.setPlaceholderText(_translate("MainWindow", "Hospital Description...."))
        self.hospitalname_input.setPlaceholderText(_translate("MainWindow", "Hospital Name...."))
        self.hospitalcontact_input.setPlaceholderText(_translate("MainWindow", "Hospital Contact...."))
        self.submit_btn.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
