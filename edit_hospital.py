from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys

class Ui_edit_form_hospital(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_edit_form_hospital, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("edit_form_hospital")
        self.resize(506, 396)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.setWindowIcon(QtGui.QIcon("./icon/edit.png"))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_id_edit_hospital = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_id_edit_hospital.setGeometry(QtCore.QRect(140, 31, 341, 31))
        self.txt_id_edit_hospital.setReadOnly(True)
        self.txt_id_edit_hospital.setObjectName("txt_id_edit_hospital")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 185, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_name_edit_hospital = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_edit_hospital.setGeometry(QtCore.QRect(140, 70, 341, 31))
        self.txt_name_edit_hospital.setReadOnly(False)
        self.txt_name_edit_hospital.setObjectName("txt_name_edit_hospital")
        self.txt_phone_edit_hospital = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_phone_edit_hospital.setGeometry(QtCore.QRect(140, 110, 341, 31))
        self.txt_phone_edit_hospital.setReadOnly(False)
        self.txt_phone_edit_hospital.setObjectName("txt_phone_edit_hospital")
        self.txt_address_edit_hospital = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_address_edit_hospital.setGeometry(QtCore.QRect(140, 150, 341, 31))
        self.txt_address_edit_hospital.setReadOnly(False)
        self.txt_address_edit_hospital.setObjectName("txt_address_edit_hospital")
        self.txt_description_edit_hospital = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_description_edit_hospital.setGeometry(QtCore.QRect(30, 220, 441, 111))
        self.txt_description_edit_hospital.setReadOnly(False)
        self.txt_description_edit_hospital.setObjectName("txt_description_edit_hospital")
        self.btn_save_edit_hospital = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_edit_hospital.setGeometry(QtCore.QRect(110, 340, 89, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save_edit_hospital.setFont(font)
        self.btn_save_edit_hospital.setObjectName("btn_save_edit_hospital")
        self.btn_cancel_edit_hospital = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel_edit_hospital.setGeometry(QtCore.QRect(270, 340, 89, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cancel_edit_hospital.setFont(font)
        self.btn_cancel_edit_hospital.setObjectName("btn_cancel_edit_hospital")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(edit_form_hospital)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("edit_form_hospital", "Edit Information Hospital"))
        self.label.setText(_translate("edit_form_hospital", "Id:"))
        self.label_2.setText(_translate("edit_form_hospital", "Name:"))
        self.label_3.setText(_translate("edit_form_hospital", "Phone:"))
        self.label_4.setText(_translate("edit_form_hospital", "Address:"))
        self.label_5.setText(_translate("edit_form_hospital", "Description:"))
        self.btn_save_edit_hospital.setText(_translate("edit_form_hospital", "Save"))
        self.btn_cancel_edit_hospital.setText(_translate("edit_form_hospital", "Cancel"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_edit_form_hospital()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())