from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1393, 1472))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 800))
        self.frame.setStyleSheet("background-color: rgb(217, 255, 254);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1371, 71))
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
        self.logo.setPixmap(QtGui.QPixmap("C:\\Users\\60111\\PycharmProjects\\DoctorApp\\Doctor2u (1).png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(590, 20, 281, 41))
        self.label.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.doctorframe = QtWidgets.QFrame(self.frame)
        self.doctorframe.setGeometry(QtCore.QRect(40, 110, 1291, 301))
        self.doctorframe.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe.setObjectName("doctorframe")
        self.approve_btn = QtWidgets.QPushButton(self.doctorframe)
        self.approve_btn.setGeometry(QtCore.QRect(1070, 20, 81, 28))
        self.approve_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.approve_btn.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.approve_btn.setObjectName("approve_btn")
        self.reject_btn = QtWidgets.QPushButton(self.doctorframe)
        self.reject_btn.setGeometry(QtCore.QRect(1190, 20, 81, 28))
        self.reject_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reject_btn.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.reject_btn.setObjectName("reject_btn")
        self.hospital_desc = QtWidgets.QTextEdit(self.doctorframe)
        self.hospital_desc.setGeometry(QtCore.QRect(20, 70, 1251, 221))
        self.hospital_desc.setObjectName("hospital_desc")
        self.hospitalname = QtWidgets.QTextEdit(self.doctorframe)
        self.hospitalname.setGeometry(QtCore.QRect(20, 10, 341, 41))
        self.hospitalname.setObjectName("hospitalname")
        self.hospitalcontact = QtWidgets.QTextEdit(self.doctorframe)
        self.hospitalcontact.setGeometry(QtCore.QRect(380, 10, 351, 41))
        self.hospitalcontact.setObjectName("hospitalcontact")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect signals to slots
        self.approve_btn.clicked.connect(self.approve_action)
        self.reject_btn.clicked.connect(self.reject_action)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ADMIN PAGE"))
        self.approve_btn.setText(_translate("MainWindow", "APPROVE"))
        self.reject_btn.setText(_translate("MainWindow", "REJECT"))

    def approve_action(self):
        # Show message box for approval
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Approval Status")
        msg_box.setText("Successfully Approved!")
        msg_box.exec_()

        # Hide the doctorframe
        self.doctorframe.hide()

    def reject_action(self):
        # Show message box for rejection
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Rejection Status")
        msg_box.setText("Successfully Rejected!")
        msg_box.exec_()

        # Hide the doctorframe
        self.doctorframe.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())