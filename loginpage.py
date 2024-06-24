from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1224, 667)
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(-10, 0, 1241, 681))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("C:\\Users\\60111\\PycharmProjects\\DoctorApp\\docbackground2.jpg"))
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
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(810, 280, 331, 41))
        self.username.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 229);\n"
"border-radius: 10px;")
        self.username.setInputMask("")
        self.username.setText("")
        self.username.setObjectName("username")
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
        self.username.setPlaceholderText(_translate("Dialog", "   Username"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
