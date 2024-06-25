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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1393, 2822))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 2800))
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
        self.logo.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\Doctor2u (1).png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")


        self.doctorframe = QtWidgets.QFrame(self.frame)
        self.doctorframe.setGeometry(QtCore.QRect(40, 110, 1291, 301))
        self.doctorframe.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe.setObjectName("doctorframe")
        self.doctor_desc = QtWidgets.QTextEdit(self.doctorframe)
        self.doctor_desc.setGeometry(QtCore.QRect(270, 70, 1011, 221))
        self.doctor_desc.setObjectName("doctor_desc")
        self.doctorname = QtWidgets.QTextEdit(self.doctorframe)
        self.doctorname.setGeometry(QtCore.QRect(270, 10, 331, 41))
        self.doctorname.setObjectName("doctorname")
        self.doctorpic = QtWidgets.QLabel(self.doctorframe)
        self.doctorpic.setGeometry(QtCore.QRect(30, 70, 211, 211))
        self.doctorpic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctorpic.setText("")
        self.doctorpic.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\docpic2.jpg"))
        self.doctorpic.setScaledContents(True)
        self.doctorpic.setObjectName("doctorpic")
        self.doctorframe_2 = QtWidgets.QFrame(self.frame)
        self.doctorframe_2.setGeometry(QtCore.QRect(40, 440, 1291, 301))
        self.doctorframe_2.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe_2.setObjectName("doctorframe_2")
        self.doctor_desc_3 = QtWidgets.QTextEdit(self.doctorframe_2)
        self.doctor_desc_3.setGeometry(QtCore.QRect(270, 70, 1011, 221))
        self.doctor_desc_3.setObjectName("doctor_desc_3")
        self.doctorname_3 = QtWidgets.QTextEdit(self.doctorframe_2)
        self.doctorname_3.setGeometry(QtCore.QRect(270, 10, 301, 41))
        self.doctorname_3.setObjectName("doctorname_3")
        self.doctorpic_3 = QtWidgets.QLabel(self.doctorframe_2)
        self.doctorpic_3.setGeometry(QtCore.QRect(30, 80, 211, 211))
        self.doctorpic_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctorpic_3.setText("")
        self.doctorpic_3.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\docpic1.jpg"))
        self.doctorpic_3.setScaledContents(True)
        self.doctorpic_3.setObjectName("doctorpic_3")
        self.doctorframe_3 = QtWidgets.QFrame(self.frame)
        self.doctorframe_3.setGeometry(QtCore.QRect(40, 770, 1291, 301))
        self.doctorframe_3.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe_3.setObjectName("doctorframe_3")
        self.doctorpic_4 = QtWidgets.QLabel(self.doctorframe_3)
        self.doctorpic_4.setGeometry(QtCore.QRect(30, 70, 211, 211))
        self.doctorpic_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctorpic_4.setText("")
        self.doctorpic_4.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\docpic3.jpg"))
        self.doctorpic_4.setScaledContents(True)
        self.doctorpic_4.setObjectName("doctorpic_4")
        self.doctor_desc_4 = QtWidgets.QTextEdit(self.doctorframe_3)
        self.doctor_desc_4.setGeometry(QtCore.QRect(270, 70, 1011, 221))
        self.doctor_desc_4.setObjectName("doctor_desc_4")
        self.doctorname_4 = QtWidgets.QTextEdit(self.doctorframe_3)
        self.doctorname_4.setGeometry(QtCore.QRect(270, 10, 301, 41))
        self.doctorname_4.setObjectName("doctorname_4")
        self.doctorframe_4 = QtWidgets.QFrame(self.frame)
        self.doctorframe_4.setGeometry(QtCore.QRect(40, 1100, 1291, 301))
        self.doctorframe_4.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe_4.setObjectName("doctorframe_4")
        self.doctor_desc_5 = QtWidgets.QTextEdit(self.doctorframe_4)
        self.doctor_desc_5.setGeometry(QtCore.QRect(270, 70, 1011, 221))
        self.doctor_desc_5.setObjectName("doctor_desc_5")
        self.doctorname_5 = QtWidgets.QTextEdit(self.doctorframe_4)
        self.doctorname_5.setGeometry(QtCore.QRect(270, 10, 311, 41))
        self.doctorname_5.setObjectName("doctorname_5")
        self.doctorpic_5 = QtWidgets.QLabel(self.doctorframe_4)
        self.doctorpic_5.setGeometry(QtCore.QRect(30, 70, 211, 211))
        self.doctorpic_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctorpic_5.setText("")
        self.doctorpic_5.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\docpic4.jpg"))
        self.doctorpic_5.setScaledContents(True)
        self.doctorpic_5.setObjectName("doctorpic_5")
        self.doctorframe_5 = QtWidgets.QFrame(self.frame)
        self.doctorframe_5.setGeometry(QtCore.QRect(40, 1430, 1291, 301))
        self.doctorframe_5.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe_5.setObjectName("doctorframe_5")
        self.doctor_desc_6 = QtWidgets.QTextEdit(self.doctorframe_5)
        self.doctor_desc_6.setGeometry(QtCore.QRect(270, 70, 1011, 221))
        self.doctor_desc_6.setObjectName("doctor_desc_6")
        self.doctorname_6 = QtWidgets.QTextEdit(self.doctorframe_5)
        self.doctorname_6.setGeometry(QtCore.QRect(270, 10, 341, 41))
        self.doctorname_6.setObjectName("doctorname_6")
        self.doctorpic_6 = QtWidgets.QLabel(self.doctorframe_5)
        self.doctorpic_6.setGeometry(QtCore.QRect(30, 70, 211, 211))
        self.doctorpic_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctorpic_6.setText("")
        self.doctorpic_6.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\doctor5.jpg"))
        self.doctorpic_6.setScaledContents(True)
        self.doctorpic_6.setObjectName("doctorpic_6")
        self.doctorframe_6 = QtWidgets.QFrame(self.frame)
        self.doctorframe_6.setGeometry(QtCore.QRect(40, 1760, 1291, 301))
        self.doctorframe_6.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe_6.setObjectName("doctorframe_6")
        self.doctor_desc_7 = QtWidgets.QTextEdit(self.doctorframe_6)
        self.doctor_desc_7.setGeometry(QtCore.QRect(270, 70, 1011, 221))
        self.doctor_desc_7.setObjectName("doctor_desc_7")
        self.doctorname_7 = QtWidgets.QTextEdit(self.doctorframe_6)
        self.doctorname_7.setGeometry(QtCore.QRect(270, 10, 301, 41))
        self.doctorname_7.setObjectName("doctorname_7")
        self.doctorpic_7 = QtWidgets.QLabel(self.doctorframe_6)
        self.doctorpic_7.setGeometry(QtCore.QRect(30, 70, 211, 211))
        self.doctorpic_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctorpic_7.setText("")
        self.doctorpic_7.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\doctor6.jpg"))
        self.doctorpic_7.setScaledContents(True)
        self.doctorpic_7.setObjectName("doctorpic_7")
        self.doctorframe_7 = QtWidgets.QFrame(self.frame)
        self.doctorframe_7.setGeometry(QtCore.QRect(40, 2090, 1291, 301))
        self.doctorframe_7.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe_7.setObjectName("doctorframe_7")
        self.doctor_desc_8 = QtWidgets.QTextEdit(self.doctorframe_7)
        self.doctor_desc_8.setGeometry(QtCore.QRect(270, 70, 1011, 221))
        self.doctor_desc_8.setObjectName("doctor_desc_8")
        self.doctorname_8 = QtWidgets.QTextEdit(self.doctorframe_7)
        self.doctorname_8.setGeometry(QtCore.QRect(270, 10, 331, 41))
        self.doctorname_8.setObjectName("doctorname_8")
        self.doctorpic_8 = QtWidgets.QLabel(self.doctorframe_7)
        self.doctorpic_8.setGeometry(QtCore.QRect(30, 70, 211, 211))
        self.doctorpic_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctorpic_8.setText("")
        self.doctorpic_8.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\doctor7.jpg"))
        self.doctorpic_8.setScaledContents(True)
        self.doctorpic_8.setObjectName("doctorpic_8")
        self.doctorframe_8 = QtWidgets.QFrame(self.frame)
        self.doctorframe_8.setGeometry(QtCore.QRect(40, 2420, 1291, 301))
        self.doctorframe_8.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.doctorframe_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.doctorframe_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.doctorframe_8.setObjectName("doctorframe_8")
        self.doctor_desc_9 = QtWidgets.QTextEdit(self.doctorframe_8)
        self.doctor_desc_9.setGeometry(QtCore.QRect(270, 70, 1011, 221))
        self.doctor_desc_9.setObjectName("doctor_desc_9")
        self.doctorname_9 = QtWidgets.QTextEdit(self.doctorframe_8)
        self.doctorname_9.setGeometry(QtCore.QRect(270, 10, 301, 41))
        self.doctorname_9.setObjectName("doctorname_9")
        self.doctorpic_9 = QtWidgets.QLabel(self.doctorframe_8)
        self.doctorpic_9.setGeometry(QtCore.QRect(30, 70, 211, 211))
        self.doctorpic_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doctorpic_9.setText("")
        self.doctorpic_9.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\doctor8.jpg"))
        self.doctorpic_9.setScaledContents(True)
        self.doctorpic_9.setObjectName("doctorpic_9")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.doctor_desc.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Specialization:</span><span style=\" font-size:14pt;\"> Cardiology</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Languages Spoken:</span><span style=\" font-size:14pt;\"> English, Malay, Mandarin</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Profile Summary:</span><span style=\" font-size:14pt;\"> Dr. Lim Wei Peng is a renowned cardiologist with over 15 years of experience. He specializes in interventional cardiology and has a particular interest in treating coronary artery disease.</span></p></body></html>"))
        self.doctorname.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Dr Lim Wei Peng -- Island Hospital</span></p></body></html>"))
        self.doctor_desc_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Specialization:</span><span style=\" font-size:14pt;\"> Obstetrics and Gynecology</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Languages Spoken:</span><span style=\" font-size:14pt;\"> English, Malay, Tamil</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Profile Summary:</span><span style=\" font-size:14pt;\"> Dr. Anjali Menon is a highly respected obstetrician and gynecologist with over 18 years of experience. She is dedicated to providing comprehensive care for women, including prenatal and postnatal care, and managing reproductive health issues.</span></p></body></html>"))
        self.doctorname_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Dr Anjali Menon -- Gleneagles</span></p></body></html>"))
        self.doctor_desc_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Specialization:</span><span style=\" font-size:14pt;\"> Pediatrics</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Languages Spoken:</span><span style=\" font-size:14pt;\"> English, Malay, Cantonese, Mandarin</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Profile Summary:</span><span style=\" font-size:14pt;\"> Dr. Tan Siew Lee has been a pediatrician for over 10 years. She is dedicated to providing comprehensive healthcare for children and adolescents, including preventive health services and managing acute and chronic diseases.</span></p></body></html>"))
        self.doctorname_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Dr Tan Siew Lee -- Gleneagles</span></p></body></html>"))
        self.doctor_desc_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Specialization:</span><span style=\" font-size:14pt;\"> Cardiology</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Languages Spoken:</span><span style=\" font-size:14pt;\"> English, Malay, Tamil, Hindi</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Profile Summary:</span><span style=\" font-size:14pt;\"> Dr. Ramesh Kumar is a distinguished cardiologist with over 15 years of experience. He specializes in interventional cardiology and has a particular interest in treating coronary artery disease.</span></p></body></html>"))
        self.doctorname_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Dr Ramesh Kumar -- Gleneagles</span></p></body></html>"))
        self.doctor_desc_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Specialization:</span><span style=\" font-size:14pt;\"> Orthopedic Surgery</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Languages Spoken:</span><span style=\" font-size:14pt;\"> English, Malay, Mandarin, Cantonese</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Profile Summary:</span><span style=\" font-size:14pt;\"> Dr. Lee Chong Wei is an experienced orthopedic surgeon with over 15 years in the field. He specializes in joint replacement and sports injuries. Dr. Lee is dedicated to helping his patients regain mobility and improve their quality of life.</span></p></body></html>"))
        self.doctorname_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Dr Lee Chong Wei -- Island Hospital</span></p></body></html>"))
        self.doctor_desc_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Specialization:</span><span style=\" font-size:14pt;\"> Rheumatology</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Languages Spoken:</span><span style=\" font-size:14pt;\"> English, Malay, Mandarin, Hokkien</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Profile Summary:</span><span style=\" font-size:14pt;\"> Dr. Wong Li Hua has been practicing rheumatology for over 10 years. She focuses on diagnosing and treating autoimmune diseases and arthritis. Dr. Wong is known for her compassionate care and patient education.</span></p></body></html>"))
        self.doctorname_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Dr Wong Li Hua -- Gleneagles</span></p></body></html>"))
        self.doctor_desc_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Specialization:</span><span style=\" font-size:14pt;\"> Ophthalmology</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Languages Spoken:</span><span style=\" font-size:14pt;\"> English, Malay, Mandarin</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Profile Summary:</span><span style=\" font-size:14pt;\"> Dr. Tan Chia Ying is a skilled ophthalmologist with over 12 years of experience. She specializes in cataract surgery and treating various eye conditions, including glaucoma and diabetic retinopathy. Dr. Tan is committed to providing comprehensive eye care to her patients.</span></p></body></html>"))
        self.doctorname_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Dr Tan Chia Ying -- Island Hospital</span></p></body></html>"))
        self.doctor_desc_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Specialization:</span><span style=\" font-size:14pt;\"> Pulmonology</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Languages Spoken:</span><span style=\" font-size:14pt;\"> English, Malay, Tamil, Hindi</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Profile Summary:</span><span style=\" font-size:14pt;\"> Dr. Anand Raj has over 18 years of experience in pulmonology. He specializes in treating respiratory conditions such as asthma, COPD, and lung infections. Dr. Anand is known for his thorough diagnostic approach and personalized treatment plans.</span></p></body></html>"))
        self.doctorname_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Dr Anand Raj -- Island Hospital</span></p></body></html>"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())