from PyQt5 import QtCore, QtGui, QtWidgets
import re
from PyQt5.QtWidgets import QMessageBox

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
        self.logo = QtWidgets.QLabel(self.header)
        self.logo.setGeometry(QtCore.QRect(40, 10, 191, 61))
        self.logo.setStyleSheet("QLabel {\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size: contain; /* or \'cover\' depending on how you want it to fit */\n"
"}\n"
"")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("C:\\Users\\60111\\PycharmProjects\\DoctorApp\\Doctor2u (1).png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.center_frame = QtWidgets.QFrame(self.centralwidget)
        self.center_frame.setGeometry(QtCore.QRect(-10, 80, 1461, 731))
        self.center_frame.setStyleSheet("background-color: rgb(217, 255, 254);")
        self.center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame.setObjectName("center_frame")
        self.frame_2 = QtWidgets.QFrame(self.center_frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 1421, 651))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftframe = QtWidgets.QFrame(self.frame_2)
        self.leftframe.setStyleSheet("background-color: rgb(255, 229, 229);")
        self.leftframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftframe.setObjectName("leftframe")
        self.username_show = QtWidgets.QLabel(self.leftframe)
        self.username_show.setGeometry(QtCore.QRect(110, 220, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.username_show.setFont(font)
        self.username_show.setObjectName("username_show")
        self.user_pic = QtWidgets.QLabel(self.leftframe)
        self.user_pic.setGeometry(QtCore.QRect(140, 50, 171, 161))
        self.user_pic.setText("")
        self.user_pic.setPixmap(QtGui.QPixmap("C:\\Users\\60111\\PycharmProjects\\DoctorApp\\profile 2.png"))
        self.user_pic.setScaledContents(True)
        self.user_pic.setObjectName("user_pic")
        self.horizontalLayout.addWidget(self.leftframe)
        self.middleframe = QtWidgets.QFrame(self.frame_2)
        self.middleframe.setStyleSheet("background-color: rgb(255, 229, 229);")
        self.middleframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middleframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middleframe.setObjectName("middleframe")
        self.profile_title = QtWidgets.QLabel(self.middleframe)
        self.profile_title.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.profile_title.setFont(font)
        self.profile_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.profile_title.setObjectName("profile_title")
        self.FirstName = QtWidgets.QLabel(self.middleframe)
        self.FirstName.setGeometry(QtCore.QRect(30, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.FirstName.setFont(font)
        self.FirstName.setObjectName("FirstName")
        self.LastName = QtWidgets.QLabel(self.middleframe)
        self.LastName.setGeometry(QtCore.QRect(250, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LastName.setFont(font)
        self.LastName.setObjectName("LastName")
        self.FirstName_input = QtWidgets.QLineEdit(self.middleframe)
        self.FirstName_input.setGeometry(QtCore.QRect(30, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FirstName_input.setFont(font)
        self.FirstName_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.FirstName_input.setObjectName("FirstName_input")
        self.LastName_input = QtWidgets.QLineEdit(self.middleframe)
        self.LastName_input.setGeometry(QtCore.QRect(250, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LastName_input.setFont(font)
        self.LastName_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.LastName_input.setObjectName("LastName_input")
        self.MobileNumber_input = QtWidgets.QLineEdit(self.middleframe)
        self.MobileNumber_input.setGeometry(QtCore.QRect(30, 210, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.MobileNumber_input.setFont(font)
        self.MobileNumber_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.MobileNumber_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.MobileNumber_input.setObjectName("MobileNumber_input")
        self.MobileNumber = QtWidgets.QLabel(self.middleframe)
        self.MobileNumber.setGeometry(QtCore.QRect(30, 180, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MobileNumber.setFont(font)
        self.MobileNumber.setObjectName("MobileNumber")
        self.Email = QtWidgets.QLabel(self.middleframe)
        self.Email.setGeometry(QtCore.QRect(30, 280, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.Email_input = QtWidgets.QLineEdit(self.middleframe)
        self.Email_input.setGeometry(QtCore.QRect(30, 310, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Email_input.setFont(font)
        self.Email_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Email_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Email_input.setObjectName("Email_input")
        self.horizontalLayout.addWidget(self.middleframe)
        self.rightframe = QtWidgets.QFrame(self.frame_2)
        self.rightframe.setStyleSheet("background-color: rgb(255, 229, 229);")
        self.rightframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightframe.setObjectName("rightframe")
        self.Gender = QtWidgets.QLabel(self.rightframe)
        self.Gender.setGeometry(QtCore.QRect(50, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Gender.setFont(font)
        self.Gender.setObjectName("Gender")
        self.save_profile_button = QtWidgets.QPushButton(self.rightframe)
        self.save_profile_button.setGeometry(QtCore.QRect(190, 550, 93, 28))
        self.save_profile_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.save_profile_button.setObjectName("save_profile_button")
        self.Gender_input = QtWidgets.QLineEdit(self.rightframe)
        self.Gender_input.setGeometry(QtCore.QRect(50, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Gender_input.setFont(font)
        self.Gender_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Gender_input.setObjectName("Gender_input")
        self.horizontalLayout.addWidget(self.rightframe)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.save_profile_button.clicked.connect(lambda: self.save_profile(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_show.setText(_translate("MainWindow", "User Name Show"))
        self.profile_title.setText(_translate("MainWindow", "Profile Setting "))
        self.FirstName.setText(_translate("MainWindow", "First Name"))
        self.LastName.setText(_translate("MainWindow", "Last Name"))
        self.FirstName_input.setPlaceholderText(_translate("MainWindow", "first name"))
        self.LastName_input.setPlaceholderText(_translate("MainWindow", "surname"))
        self.MobileNumber_input.setPlaceholderText(_translate("MainWindow", "enter phone number"))
        self.MobileNumber.setText(_translate("MainWindow", "Mobile Number"))
        self.Email.setText(_translate("MainWindow", "Email"))
        self.Email_input.setPlaceholderText(_translate("MainWindow", "enter email"))
        self.Gender.setText(_translate("MainWindow", "Gender"))
        self.save_profile_button.setText(_translate("MainWindow", "save profile"))
        self.Gender_input.setPlaceholderText(_translate("MainWindow", "male/female"))

    def save_profile(self, MainWindow):
        # Get input values
        first_name = self.FirstName_input.text().strip()
        last_name = self.LastName_input.text().strip()
        mobile_number = self.MobileNumber_input.text().strip()
        email = self.Email_input.text().strip()
        gender = self.Gender_input.text().strip()

        # Assuming you have a database connection or some method to save data
        # Example: Saving to a file
        profile_data = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile_number': mobile_number,
            'email': email,
            'gender': gender
        }

        try:
            with open('profile_data.txt', 'a') as file:
                file.write(str(profile_data) + '\n')
            QMessageBox.information(MainWindow, 'Success', 'Profile saved successfully.')
        except Exception as e:
            QMessageBox.critical(MainWindow, 'Error', f'Failed to save profile: {str(e)}')


            # Validate input
            #if not (first_name and last_name and mobile_number and address and email and date_of_birth):
                    #QtWidgets.QMessageBox.warning(MainWindow, "Warning", "All fields are required.")
                    #return

            # Validate email format
            #if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    #QtWidgets.QMessageBox.warning(MainWindow, "Warning", "Invalid email format.")
                    #return

            # Validate phone number format
            #if not re.match(r'^(\+?601)?\d{9,10}$', mobile_number):
                    #QtWidgets.QMessageBox.warning(MainWindow, "Warning",
                                                  #"Invalid phone number format. Please use +60123456789 format.")
                    #return

                    # Validate gender
            #if Gender not in ["male", "female", "other"]:
                    #QtWidgets.QMessageBox.warning(MainWindow, "Warning",
                                                  #"Invalid gender. Please enter male, female, or other.")
                    #return

            #QtWidgets.QMessageBox.information(MainWindow, "Success", "Profile saved successfully.")
            #MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
