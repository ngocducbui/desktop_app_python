from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
import common as cm
import datetime


class Ui_edit_schedule(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_edit_schedule, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("edit_schedule")
        self.resize(502, 422)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 55, 16))
        self.setWindowIcon(QtGui.QIcon("./icon/edit.png"))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btn_save_edit_schedule = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_edit_schedule.setGeometry(QtCore.QRect(140, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save_edit_schedule.setFont(font)
        self.btn_save_edit_schedule.setObjectName("btn_save_edit_schedule")
        self.btn_cancel_edit_schedule = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel_edit_schedule.setGeometry(QtCore.QRect(270, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_cancel_edit_schedule.setFont(font)
        self.btn_cancel_edit_schedule.setObjectName("btn_cancel_edit_schedule")
        self.txt_id_edit_schedule = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_id_edit_schedule.setGeometry(QtCore.QRect(100, 20, 371, 31))
        self.txt_id_edit_schedule.setReadOnly(True)
        self.txt_id_edit_schedule.setObjectName("txt_id_edit_schedule")
        self.txt_name_edit_schedule = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_edit_schedule.setGeometry(QtCore.QRect(100, 70, 371, 31))
        self.txt_name_edit_schedule.setReadOnly(False)
        self.txt_name_edit_schedule.setObjectName("txt_name_edit_schedule")
        self.txt_result_edit_schedule = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_result_edit_schedule.setGeometry(QtCore.QRect(100, 270, 371, 31))
        self.txt_result_edit_schedule.setReadOnly(False)
        self.txt_result_edit_schedule.setObjectName("txt_result_edit_schedule")
        self.combo_patient_edit_schedule = QtWidgets.QComboBox(self.centralwidget)
        wordlist = cm.select_table_name('patient').tolist()
        wordList_1 = []
        for i in wordlist:
            t = ' '.join(i)
            wordList_1.append(t)
        self.combo_patient_edit_schedule.addItems(wordList_1)
        self.combo_patient_edit_schedule.setEditable(True)
        self.combo_patient_edit_schedule.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combo_patient_edit_schedule.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.combo_patient_edit_schedule.setGeometry(QtCore.QRect(100, 220, 211, 31))
        self.combo_patient_edit_schedule.setObjectName("combo_patient_edit_schedule")

        self.combo_doctor_edit_schedule = QtWidgets.QComboBox(self.centralwidget)
        wordlist = cm.select_table_name('doctor').tolist()
        wordList_1 = []
        for i in wordlist:
            t = ' '.join(i)
            wordList_1.append(t)
        self.combo_doctor_edit_schedule.addItems(wordList_1)
        self.combo_doctor_edit_schedule.setEditable(True)
        self.combo_doctor_edit_schedule.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combo_doctor_edit_schedule.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.combo_doctor_edit_schedule.setGeometry(QtCore.QRect(100, 170, 211, 31))
        self.combo_doctor_edit_schedule.setObjectName("combo_doctor_edit_schedule")
        self.date_time_edit_schedule = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.date_time_edit_schedule.setGeometry(QtCore.QRect(100, 120, 311, 31))
        self.date_time_edit_schedule.setObjectName("date_time_edit_schedule")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(edit_schedule)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("edit_schedule", "Edit Schedule"))
        self.label.setText(_translate("edit_schedule", "Id:"))
        self.label_2.setText(_translate("edit_schedule", "Name:"))
        self.label_3.setText(_translate("edit_schedule", "Date:"))
        self.label_4.setText(_translate("edit_schedule", "Doctor:"))
        self.label_5.setText(_translate("edit_schedule", "Patient:"))
        self.label_6.setText(_translate("edit_schedule", "Result:"))
        self.btn_save_edit_schedule.setText(_translate("edit_schedule", "Save"))
        self.btn_cancel_edit_schedule.setText(_translate("edit_schedule", "Cancel"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_edit_schedule()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
