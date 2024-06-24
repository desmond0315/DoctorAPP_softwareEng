from PyQt5 import QtCore, QtWidgets
from adddoctor import Ui_Dialog as AddDoctorUi_Dialog
from requestsdoctor import Ui_Dialog as RequestsDoctorUI_Dialog
from list_of_doctor import Ui_Dialog as ListOfDoctorUI_Dialog
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(1463, 731)
        Dialog.setSizeIncrement(QtCore.QSize(1461, 471))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QtCore.QRect(200, 100, 1041, 541))
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(450, 20, 171, 51))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(410, 370, 231, 61))
        self.pushButton.setStyleSheet("background-color: rgb(26, 221, 238);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(410, 150, 231, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(26, 221, 238);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QtCore.QRect(410, 260, 231, 61))
        self.pushButton_3.setStyleSheet("background-color: rgb(26, 221, 238);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.navigate_to_add_doctor_page)
        self.pushButton_3.clicked.connect(self.navigate_to_list_of_doctor_page) #list of doctor
        self.pushButton_2.clicked.connect(self.navigate_to_requestsdoctor_page) #requests

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Dialog", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", "Admin Page", None))
        self.pushButton.setText(QtCore.QCoreApplication.translate("Dialog", "Add Doctor", None))
        self.pushButton_2.setText(QtCore.QCoreApplication.translate("Dialog", "Incoming Request", None))
        self.pushButton_3.setText(QtCore.QCoreApplication.translate("Dialog", "List of Doctor", None))

    def navigate_to_add_doctor_page(self):
        try:
            print("Navigating to add doctor page...")
            #create an instance of the add doctor page UI
            self.adddoctor_dialog = QtWidgets.QDialog()
            self.adddoctor_ui = AddDoctorUi_Dialog()
            self.adddoctor_ui.setupUi(self.adddoctor_dialog)
            self.adddoctor_dialog.show()

            # self.Dialog.close()
        except Exception as e:
            print("Error", e)

    def navigate_to_requestsdoctor_page(self):
        try:
            print("Navigating to request doctor page...")
            # create an instance of the request doctor page UI
            self.requestsdoctor_dialog = QtWidgets.QDialog()
            self.requestsdoctor_ui = RequestsDoctorUI_Dialog()
            self.requestsdoctor_ui.setupUi(self.requestsdoctor_dialog)
            self.requestsdoctor_dialog.show()

            # self.Dialog.close()
        except Exception as e:
            print("Error", e)

    def navigate_to_list_of_doctor_page(self):
        try:
            print("Navigating to list of doctor page...")
            self.list_of_doctor_dialog = QtWidgets.QDialog()
            self.list_of_doctor_ui = ListOfDoctorUI_Dialog()
            self.list_of_doctor_ui.setupUi(self.list_of_doctor_dialog)
            self.list_of_doctor_dialog.show()
        except Exception as e:
            print("Error",e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
