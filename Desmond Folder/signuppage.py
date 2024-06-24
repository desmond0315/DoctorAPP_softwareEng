from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import re
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1224, 671)
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(-10, -10, 1241, 681))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(
            "D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\docbackground4.jpg"))
        self.background.setObjectName("background")
        self.right_label = QtWidgets.QLabel(Dialog)
        self.right_label.setGeometry(QtCore.QRect(770, 0, 461, 681))
        self.right_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.right_label.setText("")
        self.right_label.setObjectName("right_label")
        self.WelcomeText = QtWidgets.QLabel(Dialog)
        self.WelcomeText.setGeometry(QtCore.QRect(830, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeText.setFont(font)
        self.WelcomeText.setObjectName("WelcomeText")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(830, 200, 331, 41))
        self.username.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.username.setInputMask("")
        self.username.setText("")
        self.username.setObjectName("username")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(830, 320, 331, 41))
        self.email.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.email.setInputMask("")
        self.email.setText("")
        self.email.setObjectName("email")
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(920, 620, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(830, 500, 331, 41))
        self.password.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setObjectName("password")
        self.confirmpassword = QtWidgets.QLineEdit(Dialog)
        self.confirmpassword.setGeometry(QtCore.QRect(830, 560, 331, 41))
        self.confirmpassword.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.confirmpassword.setInputMask("")
        self.confirmpassword.setText("")
        self.confirmpassword.setObjectName("confirmpassword")
        self.back_btn = QtWidgets.QPushButton(Dialog)
        self.back_btn.setGeometry(QtCore.QRect(1140, 10, 81, 71))
        self.back_btn.setStyleSheet("border-radius: 40px;")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\back.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(40, 40))
        self.back_btn.setCheckable(False)
        self.back_btn.setObjectName("back_btn")
        self.view_btn = QtWidgets.QPushButton(Dialog)
        self.view_btn.setGeometry(QtCore.QRect(1120, 510, 31, 28))
        self.view_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\view2.jpg"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_btn.setIcon(icon1)
        self.view_btn.setObjectName("view_btn")
        self.view2_btn = QtWidgets.QPushButton(Dialog)
        self.view2_btn.setGeometry(QtCore.QRect(1120, 570, 31, 28))
        self.view2_btn.setText("")
        self.view2_btn.setIcon(icon1)
        self.view2_btn.setObjectName("view2_btn")
        self.ic_number = QtWidgets.QLineEdit(Dialog)
        self.ic_number.setGeometry(QtCore.QRect(830, 380, 331, 41))
        self.ic_number.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.ic_number.setInputMask("")
        self.ic_number.setText("")
        self.ic_number.setObjectName("ic_number")
        self.gender = QtWidgets.QLineEdit(Dialog)
        self.gender.setGeometry(QtCore.QRect(830, 440, 331, 41))
        self.gender.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.gender.setInputMask("")
        self.gender.setText("")
        self.gender.setObjectName("gender")
        self.lastname = QtWidgets.QLineEdit(Dialog)
        self.lastname.setGeometry(QtCore.QRect(830, 140, 331, 41))
        self.lastname.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.lastname.setInputMask("")
        self.lastname.setText("")
        self.lastname.setObjectName("lastname")
        self.firstname = QtWidgets.QLineEdit(Dialog)
        self.firstname.setGeometry(QtCore.QRect(830, 80, 331, 41))
        self.firstname.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.firstname.setInputMask("")
        self.firstname.setText("")
        self.firstname.setObjectName("firstname")
        self.mobilenumber = QtWidgets.QLineEdit(Dialog)
        self.mobilenumber.setGeometry(QtCore.QRect(830, 260, 331, 41))
        self.mobilenumber.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.mobilenumber.setInputMask("")
        self.mobilenumber.setText("")
        self.mobilenumber.setObjectName("mobilenumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect signals
        self.back_btn.clicked.connect(lambda: self.back_action(Dialog))
        self.signup_btn.clicked.connect(self.signup_action)
        self.view_btn.clicked.connect(self.toggle_password_visibility)
        self.view_btn.setCheckable(True)  # Set to checkable so it retains its state
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.view_btn.clicked.connect(self.toggle_password_visibility)
        self.view2_btn.clicked.connect(self.toggle_confirm_password_visibility)
        self.view2_btn.setCheckable(True)  # Set to checkable so it retains its state
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.WelcomeText.setText(_translate("Dialog", "WELCOME DOCTOR2U"))
        self.username.setPlaceholderText(_translate("Dialog", "   Username"))
        self.email.setPlaceholderText(_translate("Dialog", "   Email"))
        self.signup_btn.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#13827d;\">Sign Up</span></p></body></html>"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.password.setPlaceholderText(_translate("Dialog", "   Password"))
        self.confirmpassword.setPlaceholderText(_translate("Dialog", "   Confirm Password"))
        self.ic_number.setPlaceholderText(_translate("Dialog", "   IC Number (no -)"))
        self.gender.setPlaceholderText(_translate("Dialog", "   Gender (male/female)"))
        self.lastname.setPlaceholderText(_translate("Dialog", "   Last Name"))
        self.firstname.setPlaceholderText(_translate("Dialog", "   First Name"))
        self.mobilenumber.setPlaceholderText(_translate("Dialog", "   Mobile Number"))

    def back_action(self, Dialog):
        try:
            import loginpage  # Assuming loginpage is the name of the login dialog module
            self.new_page = QtWidgets.QDialog()
            self.ui = loginpage.Ui_Dialog()
            self.ui.setupUi(self.new_page)
            self.new_page.show()
            Dialog.close()  # Close the current dialog
        except ImportError as e:
            print("Failed to import loginpage module:", e)
        except Exception as e:
            print("An error occurred:", e)

    def signup_action(self):
        firstname = self.firstname.text().strip()
        lastname = self.lastname.text().strip()
        username = self.username.text().strip()
        email = self.email.text().strip()
        password = self.password.text().strip()
        confirmpassword = self.confirmpassword.text().strip()
        mobilenumber = self.mobilenumber.text().strip()
        ic_number = self.ic_number.text().strip()
        gender = self.gender.text().strip().lower()

        if not self.validate_inputs(firstname, lastname, username, email, password, confirmpassword, mobilenumber, ic_number, gender):
            return

        # Show success message and clear inputs
        self.show_message("Success", "Signup successful!")

        # Enroll user data into firebase database
        auth.create_user_with_email_and_password(email, password)
        data = {"firstname": firstname, "lastname": lastname, "username": username, "email": email, "password": password, "mobilenumber": mobilenumber, "ic_number": ic_number, "gender": gender}
        db.child("user").child(username).set(data)
        self.clear_inputs()
        try:
            import loginpage  # Assuming loginpage is the name of the login dialog module
            self.new_page = QtWidgets.QDialog()
            self.ui = loginpage.Ui_Dialog()
            self.ui.setupUi(self.new_page)
            self.new_page.show()
            Dialog.close()  # Close the current dialog

        except ImportError as e:
            print("Failed to import loginpage module:", e)
        except Exception as e:
            print("An error occurred:", e)

    def validate_inputs(self, firstname, lastname, username, email, password, confirmpassword, mobilenumber, ic_number, gender):
        # Validate first name and last name
        if not firstname:
            self.show_message("Error", "Please enter First Name.")
            return False
        if not lastname:
            self.show_message("Error", "Please enter Last Name.")
            return False

        # Validate username
        if not username:
            self.show_message("Error", "Please enter Username.")
            return False

        # Validate email
        if not self.validate_email(email):
            self.show_message("Error", "Invalid email format.")
            return False

        # Validate password
        if not password or len(password) < 8:
            self.show_message("Error", "Password must be at least 8 characters long.")
            return False

        # Confirm password
        if password != confirmpassword:
            self.show_message("Error", "Passwords do not match!")
            return False

        # Validate mobile number format (e.g., 60124100450)
        if not re.match(r'^(\+?601)?\d{9,10}$', mobilenumber):
            self.show_message("Error", "Invalid mobile number format.")
            return False

        # Validate IC number (simple validation for numeric characters only)
        if not ic_number.isdigit():
            self.show_message("Error", "IC Number must be numeric.")
            return False

        # Validate gender (should be either "male" or "female")
        if gender not in ("male", "female"):
            self.show_message("Error", "Gender must be either 'male' or 'female'.")
            return False

        return True

    def validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def show_message(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information if title == "Success" else QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def clear_inputs(self):
        self.username.clear()
        self.email.clear()
        self.password.clear()
        self.confirmpassword.clear()
        self.mobilenumber.clear()
        self.firstname.clear()
        self.lastname.clear()
        self.ic_number.clear()
        self.gender.clear()

    def toggle_password_visibility(self):
        if self.view_btn.isChecked():
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def toggle_password_visibility(self):
        print("Toggle password visibility method called")  # Debug message
        if self.view_btn.isChecked():
            print("Show password")  # Debug message
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            print("Hide password")  # Debug message
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def toggle_confirm_password_visibility(self):
        if self.view2_btn.isChecked():
            self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)


def exit_handler():
    db.child("loggedin").remove()


atexit.register(exit_handler)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
