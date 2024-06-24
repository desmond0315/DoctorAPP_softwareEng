from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1224, 667)
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(-10, 0, 1241, 681))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("C:\\Users\\60111\\PycharmProjects\\DoctorApp\\doctorlogin.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.login_label = QtWidgets.QLabel(Dialog)
        self.login_label.setGeometry(QtCore.QRect(770, 120, 401, 451))
        self.login_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.login_label.setText("")
        self.login_label.setObjectName("login_label")
        self.welcome = QtWidgets.QLabel(Dialog)
        self.welcome.setGeometry(QtCore.QRect(880, 190, 181, 41))
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
        self.back_btn = QtWidgets.QPushButton(Dialog)
        self.back_btn.setGeometry(QtCore.QRect(1080, 490, 81, 71))
        self.back_btn.setStyleSheet("border-radius: 40px;")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\60111\\PycharmProjects\\DoctorApp\\back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(40, 40))
        self.back_btn.setCheckable(False)
        self.back_btn.setObjectName("back_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.back_btn.clicked.connect(lambda: self.back_action(Dialog))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome.setText(_translate("Dialog", "Doctor Login"))
        self.username.setPlaceholderText(_translate("Dialog", "   Username"))
        self.password.setPlaceholderText(_translate("Dialog", "   Password"))
        self.login_btn.setText(_translate("Dialog", "Login"))

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
