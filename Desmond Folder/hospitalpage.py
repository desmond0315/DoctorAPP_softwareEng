from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -720, 1393, 2722))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 2700))
        self.frame.setStyleSheet("background-color: rgb(214, 255, 192);")
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
        self.hospitalframe = QtWidgets.QFrame(self.frame)
        self.hospitalframe.setGeometry(QtCore.QRect(40, 110, 1291, 721))
        self.hospitalframe.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.hospitalframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hospitalframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hospitalframe.setObjectName("hospitalframe")
        self.hospital_desc = QtWidgets.QTextEdit(self.hospitalframe)
        self.hospital_desc.setGeometry(QtCore.QRect(10, 350, 1271, 361))
        self.hospital_desc.setObjectName("hospital_desc")
        self.hospital_pic1 = QtWidgets.QLabel(self.hospitalframe)
        self.hospital_pic1.setGeometry(QtCore.QRect(20, 20, 381, 311))
        self.hospital_pic1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hospital_pic1.setText("")
        self.hospital_pic1.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\islandhospital.jpg"))
        self.hospital_pic1.setScaledContents(True)
        self.hospital_pic1.setObjectName("hospital_pic1")
        self.hospital_pic1_2 = QtWidgets.QLabel(self.hospitalframe)
        self.hospital_pic1_2.setGeometry(QtCore.QRect(450, 20, 401, 311))
        self.hospital_pic1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hospital_pic1_2.setText("")
        self.hospital_pic1_2.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\islandhospital2.jpg"))
        self.hospital_pic1_2.setScaledContents(True)
        self.hospital_pic1_2.setObjectName("hospital_pic1_2")
        self.hospital_pic1_3 = QtWidgets.QLabel(self.hospitalframe)
        self.hospital_pic1_3.setGeometry(QtCore.QRect(900, 20, 371, 311))
        self.hospital_pic1_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hospital_pic1_3.setText("")
        self.hospital_pic1_3.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\islandhospital3.jpg"))
        self.hospital_pic1_3.setScaledContents(True)
        self.hospital_pic1_3.setObjectName("hospital_pic1_3")
        self.hospitalframe_2 = QtWidgets.QFrame(self.frame)
        self.hospitalframe_2.setGeometry(QtCore.QRect(40, 1400, 1291, 721))
        self.hospitalframe_2.setStyleSheet("border: 0.6px solid #000000; /* Border width and color */\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;       /* Border radius for rounded corners */")
        self.hospitalframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hospitalframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hospitalframe_2.setObjectName("hospitalframe_2")
        self.hospital_desc_2 = QtWidgets.QTextEdit(self.hospitalframe_2)
        self.hospital_desc_2.setGeometry(QtCore.QRect(10, 350, 1271, 361))
        self.hospital_desc_2.setObjectName("hospital_desc_2")
        self.hospital_pic1_4 = QtWidgets.QLabel(self.hospitalframe_2)
        self.hospital_pic1_4.setGeometry(QtCore.QRect(20, 20, 381, 311))
        self.hospital_pic1_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hospital_pic1_4.setText("")
        self.hospital_pic1_4.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\gleneagle.jpg"))
        self.hospital_pic1_4.setScaledContents(True)
        self.hospital_pic1_4.setObjectName("hospital_pic1_4")
        self.hospital_pic1_5 = QtWidgets.QLabel(self.hospitalframe_2)
        self.hospital_pic1_5.setGeometry(QtCore.QRect(430, 20, 441, 311))
        self.hospital_pic1_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hospital_pic1_5.setText("")
        self.hospital_pic1_5.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\gleneagles2.jpg"))
        self.hospital_pic1_5.setScaledContents(True)
        self.hospital_pic1_5.setObjectName("hospital_pic1_5")
        self.hospital_pic1_6 = QtWidgets.QLabel(self.hospitalframe_2)
        self.hospital_pic1_6.setGeometry(QtCore.QRect(900, 20, 371, 311))
        self.hospital_pic1_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hospital_pic1_6.setText("")
        self.hospital_pic1_6.setPixmap(QtGui.QPixmap("D:\\Documents (Extras)\\Additional Program Files\\PycharmProjects\\DoctorApp\\gmc.jpg"))
        self.hospital_pic1_6.setScaledContents(True)
        self.hospital_pic1_6.setObjectName("hospital_pic1_6")
        self.mapframe1 = QtWidgets.QFrame(self.frame)
        self.mapframe1.setGeometry(QtCore.QRect(60, 870, 1271, 491))
        self.mapframe1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mapframe1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mapframe1.setObjectName("mapframe1")
        self.mapframe2 = QtWidgets.QFrame(self.frame)
        self.mapframe2.setGeometry(QtCore.QRect(50, 2160, 1271, 491))
        self.mapframe2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mapframe2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mapframe2.setObjectName("mapframe2")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.webView = QtWebEngineWidgets.QWebEngineView(self.mapframe1)
        self.webView.setGeometry(QtCore.QRect(0, 0, 1271, 491))
        self.webView.setUrl(QtCore.QUrl("https://www.google.com/maps/place/Island+Hospital+Penang/@5.4216189,100.3116082,16z/data=!4m6!3m5!1s0x304ac3afb9bfdbe1:0xba3e0b947e6c8e77!8m2!3d5.4220563!4d100.3137875!16s%2Fg%2F11gg9f8573?entry=ttu"))
        self.webView.setObjectName("webView")

        self.webView = QtWebEngineWidgets.QWebEngineView(self.mapframe2)
        self.webView.setGeometry(QtCore.QRect(0, 0, 1271, 491))
        self.webView.setUrl(QtCore.QUrl(
            "https://www.google.com/maps/place/Gleneagles+Hospital+Penang/@5.4267879,100.3199707,17z/data=!4m6!3m5!1s0x304ac3a67d318bdd:0xe54f46ee3c79f8fe!8m2!3d5.4267879!4d100.3199707!16s%2Fg%2F11b75j_h11?entry=ttu"))
        self.webView.setObjectName("webView")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hospital_desc.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Island Hospital                                                                                                              Contact: </span><a href=\"https://www.google.com/search?q=gleneagles+hospital+penang+contact&amp;sca_esv=9808eceaba48aaa9&amp;bih=776&amp;biw=1536&amp;rlz=1C1ONGR_enMY1035MY1035&amp;hl=en&amp;ei=rIlxZqKkNpzz4-EPnM6HgA4&amp;ved=0ahUKEwiiqomYn-WGAxWc-TgGHRznAeAQ4dUDCBA&amp;uact=5&amp;oq=gleneagles+hospital+penang+contact&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIiJnbGVuZWFnbGVzIGhvc3BpdGFsIHBlbmFuZyBjb250YWN0MgUQABiABDIGEAAYFhgeMgYQABgWGB4yAhAmMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESPEJUABYvwdwAHgAkAEAmAFvoAGDBaoBAzYuMbgBA8gBAPgBAZgCB6ACrgXCAgkQABgWGIsDGB7CAgUQJhiLA8ICCxAAGKIEGIkFGIsDwgILEAAYgAQYogQYiwPCAggQABiiBBiJBZgDAJIHAzUuMqAHkis&amp;sclient=gws-wiz-serp#\"><span style=\" font-family:\'arial,sans-serif\'; font-size:14pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">04-238-3388</span></a><span style=\" font-size:14pt; font-weight:600;\">                                                        </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">Island Hospital, founded in 1996, is a 600-bed hospital located in Penang, Malaysia. The hospital is recognised as one of the leading healthcare providers in Malaysia, serving patients from around the region. Island Hospital offers a wide range of healthcare services and is committed to providing best-in-class care to deliver care in the best interest of the patient and “to comfort always.”</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Lato-Regular\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">Island Hospital has over 80 full-time specialists across 9 Centres of Excellence, offering a wide range of treatment services that are supported by cutting-edge medical equipment and technology. The hospital’s specialists are highly experienced and renowned in their dedicated fields, with an average of 24.4 years of practice and international exposure in their medical careers. Its commitment to providing excellent patient care has earned it recognition as one of the best hospitals in its class. As part of its ongoing efforts to improve the quality of care it provides, Island Hospital has expanded its services to aim towards becoming a Regional Quaternary Care hospital. This expansion has allowed it to offer patients an advanced level of specialised and niche treatments.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Lato-Regular\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato-Regular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">As a testament to its dedication to providing high-quality healthcare services, Island Hospital was shortlisted by the Malaysia Healthcare Travel Council (MHTC) as the only hospital in Penang in the Flagship Medical Tourism Hospital Programme. The Flagship Medical Tourism Hospital Programme is an innovative initiative that aims to establish new standards in global healthcare travel, spearheaded by the Malaysia Healthcare Travel Council (MHTC) in 2022. Fully endorsed by the Government of Malaysia and the Ministry of Health, this collaborative effort with international bodies IQVIA and Joint Commission International (JCI) aims to position Malaysia as a globally renowned icon for healthcare travel, delivering exceptional end-to-end patient experiences anchored on medical and service excellence best practices and international branding. The programme is a critical component of the five-year Malaysia Healthcare Travel Industry blueprint, which seeks to provide the Best Malaysia Healthcare Travel Experience by 2025.</span></p></body></html>"))
        self.hospital_desc_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Gleneagles Hospital                                                                                                         Contact: </span><a href=\"https://www.google.com/search?q=gleneagles+hospital+penang+contact&amp;sca_esv=9808eceaba48aaa9&amp;bih=776&amp;biw=1536&amp;rlz=1C1ONGR_enMY1035MY1035&amp;hl=en&amp;ei=rIlxZqKkNpzz4-EPnM6HgA4&amp;ved=0ahUKEwiiqomYn-WGAxWc-TgGHRznAeAQ4dUDCBA&amp;uact=5&amp;oq=gleneagles+hospital+penang+contact&amp;gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIiJnbGVuZWFnbGVzIGhvc3BpdGFsIHBlbmFuZyBjb250YWN0MgUQABiABDIGEAAYFhgeMgYQABgWGB4yAhAmMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESPEJUABYvwdwAHgAkAEAmAFvoAGDBaoBAzYuMbgBA8gBAPgBAZgCB6ACrgXCAgkQABgWGIsDGB7CAgUQJhiLA8ICCxAAGKIEGIkFGIsDwgILEAAYgAQYogQYiwPCAggQABiiBBiJBZgDAJIHAzUuMqAHkis&amp;sclient=gws-wiz-serp#\"><span style=\" font-family:\'arial,sans-serif\'; font-size:14pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">04-222 9111</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:160%;\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; font-weight:600; color:#202122; background-color:#ffffff;\">Gleneagles Hospital Penang (GPG)</span><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122; background-color:#ffffff;\"> is a </span><a href=\"https://en.wikipedia.org/wiki/Private_hospital\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">private hospital</span></a><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122; background-color:#ffffff;\"> in </span><a href=\"https://en.wikipedia.org/wiki/George_Town,_Penang\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">George Town</span></a><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122; background-color:#ffffff;\"> within the </span><a href=\"https://en.wikipedia.org/wiki/States_and_federal_territories_of_Malaysia\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">Malaysian state</span></a><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122; background-color:#ffffff;\"> of </span><a href=\"https://en.wikipedia.org/wiki/Penang\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">Penang</span></a><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122; background-color:#ffffff;\">. Established in 1973, the 360-bed tertiary care provider houses over 85 doctors which cover a wide array of medical specialties, supported by more than 1,100 employees (nurses, allied health personnel and support staff). The hospital now consists of its original six-storey building and a 19-storey annex.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:160%;\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122; background-color:#ffffff;\">The Gleneagles Hospital Penang was established in 1973 and was originally a three-storey hospital with 70 beds.</span><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122;\"> It was located at the junction of Jalan Cantonment and Jalan Bell. The hospital was subsequently expanded to six floors in 1977, housing 132 beds. In 1989, </span><a href=\"https://en.wikipedia.org/wiki/Parkway_Pantai\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; text-decoration: underline; color:#000000;\">Parkway Pantai</span></a><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122;\">, a </span><a href=\"https://en.wikipedia.org/wiki/Singapore_Exchange\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; text-decoration: underline; color:#000000;\">Singapore</span></a><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122;\">-listed healthcare firm, acquired the majority control of the hospital, which was then renamed the Gleneagles Medical Centre. The hospital was expanded again in 2013, with the completion of a 19-storey annex. Today it is known as Gleneagles Hospital Penang and accommodates 360 beds. The CEO of Gleneagles Hospital Penang is Mr. Ivan Loh.</span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:19px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122; background-color:#ffffff;\">Gleneagles Hospital Penang is one of 16 hospitals operated by Pantai Holdings Sdn Bhd (Pantai Group), which is part of Parkway Pantai Limited, a subsidiary of</span><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122;\"> </span><a href=\"https://en.wikipedia.org/wiki/IHH_Healthcare\"><span style=\" font-family:\'sans-serif\'; font-size:10pt; text-decoration: underline; color:#000000;\">IHH Healthcare</span></a><span style=\" font-family:\'sans-serif\'; font-size:10pt; color:#202122;\"> Berhad (IHH).</span><span style=\" font-size:10pt;\"><br /></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
