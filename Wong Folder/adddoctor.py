from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QFrame, QLabel, QTextEdit, QPushButton, QDialogButtonBox, \
    QFileDialog, QMessageBox
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
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1461, 731)
        Dialog.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.name_input = QTextEdit(Dialog)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(640, 200, 491, 41))
        self.name_input.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.language_input = QTextEdit(Dialog)
        self.language_input.setObjectName(u"language_input")
        self.language_input.setGeometry(QRect(640, 270, 491, 41))
        self.language_input.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.specialty_input = QTextEdit(Dialog)
        self.specialty_input.setObjectName(u"specialty_input")
        self.specialty_input.setGeometry(QRect(640, 340, 491, 41))
        self.specialty_input.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.summary_input = QTextEdit(Dialog)
        self.summary_input.setObjectName(u"summary_input")
        self.summary_input.setGeometry(QRect(640, 410, 491, 41))
        self.summary_input.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 200, 81, 31))
        self.label.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 270, 191, 31))
        self.label_2.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 340, 191, 31))
        self.label_3.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.profile_summary = QLabel(Dialog)
        self.profile_summary.setObjectName(u"profile_summary")
        self.profile_summary.setGeometry(QRect(350, 410, 191, 31))
        self.profile_summary.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(90, 60, 1301, 621))
        self.frame.setStyleSheet(u"background: rgb(0, 255, 255)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 110, 1161, 441))
        self.frame_2.setStyleSheet(u"background:  rgb(217, 255, 254);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.buttonBox = QDialogButtonBox(self.frame_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(760, 400, 341, 32))
        self.buttonBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.raise_()
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 50, 451, 51))
        self.label_5.setStyleSheet(u"\n"
                                   "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                   "font-style: \"bold\";")
        self.frame.raise_()
        self.name_input.raise_()
        self.language_input.raise_()
        self.specialty_input.raise_()
        self.summary_input.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.profile_summary.raise_()

        self.retranslateUi(Dialog)

        # Connect the OK and Cancel buttons
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.clearData)

        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Spoken Language"))
        self.label_3.setText(_translate("Dialog", "Specialty"))
        self.profile_summary.setText(_translate("Dialog", "Profile Summary"))
        self.label_5.setText(_translate("Dialog", "Doctor Information Form"))
        #self.label_5.setText(QCoreApplication.translate("Dialog", u"Doctor Information Form", None))


    def clearData(self):
        # self.label.setText('Data Deleted')
        self.name_input.clear()
        self.language_input.clear()
        self.summary_input.clear()
        self.specialty_input.clear()

        # self.done(0)

#    def browse_picture(self):
#       options = QFileDialog.Options()
#        file_name, _ = QFileDialog.getOpenFileName(None, "Select Picture", "",
#                                                   "Images (.png *.xpm *.jpg *.jpeg *.bmp);;All Files ()",
#                                                   options=options)
#        if file_name:
#            pixmap = QPixmap(file_name)
#            self.labelPicture.setPixmap(pixmap.scaled(self.labelPicture.size(), Qt.KeepAspectRatio))

    def accept(self):
        # Check if all text fields are filled
        if not self.name_input.toPlainText().strip():
            self.show_error_message("Name field must be filled.")
        elif not self.language_input.toPlainText().strip():
            self.show_error_message("Spoken Language field must be filled.")
        elif not self.specialty_input.toPlainText().strip():
            self.show_error_message("Specialty field must be filled.")
        elif not self.summary_input.toPlainText().strip():
            self.show_error_message("Profile Summary field must be filled.")
        else:
            data = {"name": self.name_input.toPlainText(), "spoken_lg": self.language_input.toPlainText(), "specialty": self.specialty_input.toPlainText(), "summary": self.summary_input.toPlainText()}
            db.child("doctor").child(self.name_input.toPlainText()).set(data)

            QtWidgets.QMessageBox.information(Dialog, "Success", "Doctor information added successfully.")

    def show_error_message(self, message):
        error_message = QMessageBox()
        error_message.setIcon(QMessageBox.Warning)
        error_message.setWindowTitle("Input Error")
        error_message.setText(message)
        error_message.setStandardButtons(QMessageBox.Ok)
        error_message.exec_()

    def show_success_message(self, message):
        success_message = QMessageBox()
        success_message.setIcon(QMessageBox.Accepted)
        success_message.setWindowTitle("Success")
        success_message.setText(message)
        success_message.setStandardButtons(QMessageBox.Ok)
        success_message.exec_()

# class DoctorProfileForm(QDialog, Ui_Dialog):
#     def _init_(self, parent=None):
#         super(DoctorProfileForm, self)._init_(parent)
#         self.setupUi(self)
#
#
#         # Connect the OK and Cancel buttons
#         self.buttonBox.accepted.connect(self.accept)
#         self.buttonBox.rejected.connect(self.clearData)
#
#     def clearData(self):
#         self.label.setText('Data Deleted')
#         self.name_input.QTextEdit("")
#         self.language_input.clear()
#         self.summary_input.clear()
#         self.specialty_input.clear()
#         self.done(0)
#
#     def accept(self):
#         # Check if all text fields are filled
#         if not self.name_input.toPlainText().strip():
#             self.show_error_message("Name field must be filled.")
#         elif not self.language_input.toPlainText().strip():
#             self.show_error_message("Spoken Language field must be filled.")
#         elif not self.specialty_input.toPlainText().strip():
#             self.show_error_message("Specialty field must be filled.")
#         elif not self.summary_input.toPlainText().strip():
#             self.show_error_message("Profile Summary field must be filled.")
#         else:
#             super().accept()  # If all fields are filled, accept the dialog
#
#     def show_error_message(self, message):
#         error_message = QMessageBox()
#         error_message.setIcon(QMessageBox.Warning)
#         error_message.setWindowTitle("Input Error")
#         error_message.setText(message)
#         error_message.setStandardButtons(QMessageBox.Ok)
#         error_message.exec_()



if _name_ == "_main_":
    import sys

    app = QApplication(sys.argv)
    # Dialog = DoctorProfileForm()
    #Dialog.show()
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


