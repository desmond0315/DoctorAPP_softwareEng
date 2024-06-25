from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
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
        Dialog.resize(1224, 667)
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(-10, 0, 1241, 681))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\docbackground2.jpg"))
        self.background.setObjectName("background")
        self.login_label = QtWidgets.QLabel(Dialog)
        self.login_label.setGeometry(QtCore.QRect(770, 120, 401, 451))
        self.login_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.login_label.setText("")
        self.login_label.setObjectName("login_label")
        self.welcome = QtWidgets.QLabel(Dialog)
        self.welcome.setGeometry(QtCore.QRect(900, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(810, 280, 331, 41))
        self.email.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.email.setInputMask("")
        self.email.setText("")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(810, 340, 331, 41))
        self.password.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setObjectName("password")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(920, 410, 111, 31))
        self.login_btn.setObjectName("login_btn")
        self.Signup_btn = QtWidgets.QPushButton(Dialog)
        self.Signup_btn.setGeometry(QtCore.QRect(880, 450, 191, 28))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.Signup_btn.setFont(font)
        self.Signup_btn.setStyleSheet("QPushButton { color: blue; border: none; }")
        self.Signup_btn.setObjectName("Signup_btn")
        self.doctorlogin_btn = QtWidgets.QPushButton(Dialog)
        self.doctorlogin_btn.setGeometry(QtCore.QRect(880, 500, 191, 28))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.doctorlogin_btn.setFont(font)
        self.doctorlogin_btn.setStyleSheet("QPushButton { color: blue; border: none; }")

        self.doctorlogin_btn.setObjectName("doctorlogin_btn")

        # Connect the clicked signal of signup_btn to the signup_action method
        self.Signup_btn.clicked.connect(lambda: self.signup_action(Dialog))
        self.doctorlogin_btn.clicked.connect(lambda: self.doctor_action(Dialog))
        self.login_btn.clicked.connect(lambda: self.login_action(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Signup_btn.enterEvent = self.signup_btn_enter_event
        self.Signup_btn.leaveEvent = self.signup_btn_leave_event

    def signup_btn_enter_event(self, event):
        self.Signup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def signup_btn_leave_event(self, event):
        self.Signup_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome.setText(_translate("Dialog", "WELCOME"))
        self.email.setPlaceholderText(_translate("Dialog", "   Email"))
        self.password.setPlaceholderText(_translate("Dialog", "   Password"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.Signup_btn.setText(_translate("Dialog", "Dont Have Account? Signup"))
        self.doctorlogin_btn.setText(_translate("Dialog", "Login For Doctor"))

    def signup_action(self, Dialog):
        try:
            import signuppage
            self.new_page = QtWidgets.QDialog()
            self.ui = signuppage.Ui_Dialog()
            self.ui.setupUi(self.new_page)
            self.new_page.show()
            Dialog.close()  # Close the current dialog
        except ImportError as e:
            print("Failed to import signuppage module:", e)
        except Exception as e:
            print("An error occurred:", e)

    def doctor_action(self, Dialog):
        try:
            import doctorloginpage
            self.new_page = QtWidgets.QDialog()
            self.ui = doctorloginpage.Ui_Dialog()
            self.ui.setupUi(self.new_page)
            self.new_page.show()
            Dialog.close()  # Close the current dialog
        except ImportError as e:
            print("Failed to import doctorloginpage module:", e)
        except Exception as e:
            print("An error occurred:", e)

    def login_action(self, Dialog):
        email = self.email.text()
        password = self.password.text()

        admin = db.child("admin").get()
        for adminusername in admin.each():
            if email == (adminusername.val()["email"]):
                for adminpassword in admin.each():
                    if password == (adminpassword.val()["password"]):
                        try:
                            try:
                                import adminmainpage
                                self.new_page = QtWidgets.QDialog()
                                self.ui = adminmainpage.Ui_Dialog()
                                self.ui.setupUi(self.new_page)
                                self.new_page.show()
                                Dialog.close()  # Close the current dialog

                                data = {"email": email}
                                db.child("loggedin").set(data)

                            except Exception as e:
                                print("An error occurred:", e)

                        except Exception as e:
                            print("An error occurred:", e)

                    else:
                        QMessageBox.warning(Dialog, "Login Failed", "Invalid username or password.")

            else:
                try:
                    auth.sign_in_with_email_and_password(email, password)
                    try:
                        import doctor_mainpage2
                        # from doctor_mainpage2 import Ui_MainWindow
                        self.new_page = QtWidgets.QMainWindow()
                        self.ui = doctor_mainpage2.Ui_MainWindow()
                        self.ui.setupUi(self.new_page)
                        # self.ui.Profile_btn.setText(email)
                        self.new_page.show()
                        Dialog.close()  # Close the current dialog

                        data = {"email": email}
                        db.child("loggedin").set(data)

                    except Exception as e:
                        print("An error occurred:", e)

                except Exception as e:
                    print("An error occurred:", e)
                    # Show a warning message box
                    QMessageBox.warning(Dialog, "Login Failed", "Invalid username or password.")

def exit_handler():
    db.child("loggedin").remove()


atexit.register(exit_handler)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
