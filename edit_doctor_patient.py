from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import common as cm
import sys
class Ui_edit_form_doctor_patient(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_edit_form_doctor_patient, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("edit_form_doctor_patient")
        self.resize(508, 402)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 55, 16))
        self.setWindowIcon(QtGui.QIcon("./icon/edit.png"))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btn_save_edit_doctor_patient = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_edit_doctor_patient.setGeometry(QtCore.QRect(150, 340, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save_edit_doctor_patient.setFont(font)
        self.btn_save_edit_doctor_patient.setObjectName("btn_save_edit_doctor_patient")
        self.btn_cancel_edit_doctor_patient = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel_edit_doctor_patient.setGeometry(QtCore.QRect(280, 340, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cancel_edit_doctor_patient.setFont(font)
        self.btn_cancel_edit_doctor_patient.setObjectName("btn_cancel_edit_doctor_patient")
        self.txt_id_edit_doctor_patient = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_id_edit_doctor_patient.setGeometry(QtCore.QRect(110, 30, 371, 31))
        self.txt_id_edit_doctor_patient.setReadOnly(True)
        self.txt_id_edit_doctor_patient.setObjectName("txt_id_edit_doctor_patient")
        self.txt_name_edit_doctor_patient = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_edit_doctor_patient.setGeometry(QtCore.QRect(110, 80, 371, 31))
        self.txt_name_edit_doctor_patient.setReadOnly(False)
        self.txt_name_edit_doctor_patient.setObjectName("txt_name_edit_doctor_patient")
        self.txt_phone_edit_doctor_patient = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_phone_edit_doctor_patient.setGeometry(QtCore.QRect(110, 130, 371, 31))
        self.txt_phone_edit_doctor_patient.setReadOnly(False)
        self.txt_phone_edit_doctor_patient.setObjectName("txt_phone_edit_doctor_patient")
        self.txt_email_edit_doctor_patient = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_email_edit_doctor_patient.setGeometry(QtCore.QRect(110, 180, 371, 31))
        self.txt_email_edit_doctor_patient.setReadOnly(False)
        self.txt_email_edit_doctor_patient.setObjectName("txt_email_edit_doctor_patient")
        self.txt_address_edit_doctor_patient = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_address_edit_doctor_patient.setGeometry(QtCore.QRect(110, 230, 371, 31))
        self.txt_address_edit_doctor_patient.setReadOnly(False)
        self.txt_address_edit_doctor_patient.setObjectName("txt_address_edit_doctor_patient")
        self.combo_edit_doctor_patient = QtWidgets.QComboBox(self.centralwidget)

        wordlist = cm.select_table_name('hospital').tolist()
        wordList_1 = []
        for i in wordlist:
            t = ' '.join(i)
            wordList_1.append(t)
        self.combo_edit_doctor_patient.addItems(wordList_1)
        self.combo_edit_doctor_patient.setEditable(True)
        self.combo_edit_doctor_patient.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combo_edit_doctor_patient.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        self.combo_edit_doctor_patient.setGeometry(QtCore.QRect(110, 280, 251, 31))
        self.combo_edit_doctor_patient.setObjectName("combo_edit_doctor_patient")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("edit_form_doctor_patient", "Edit Infromation"))
        self.label.setText(_translate("edit_form_doctor_patient", "Id:"))
        self.label_2.setText(_translate("edit_form_doctor_patient", "Name:"))
        self.label_3.setText(_translate("edit_form_doctor_patient", "Phone:"))
        self.label_4.setText(_translate("edit_form_doctor_patient", "Address:"))
        self.label_5.setText(_translate("edit_form_doctor_patient", "Email:"))
        self.label_6.setText(_translate("edit_form_doctor_patient", "Hospital:"))
        self.btn_save_edit_doctor_patient.setText(_translate("edit_form_doctor_patient", "Save"))
        self.btn_cancel_edit_doctor_patient.setText(_translate("edit_form_doctor_patient", "Cancel"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_edit_form_doctor_patient()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
