# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mahasiswa.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(566, 398)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 71, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 10, 311, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.editNPM = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editNPM.setObjectName("editNPM")
        self.verticalLayout_2.addWidget(self.editNPM)
        self.editNama = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editNama.setObjectName("editNama")
        self.verticalLayout_2.addWidget(self.editNama)
        self.editKelas = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editKelas.setObjectName("editKelas")
        self.verticalLayout_2.addWidget(self.editKelas)
        self.editJurusan = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editJurusan.setObjectName("editJurusan")
        self.verticalLayout_2.addWidget(self.editJurusan)
        self.editLahir = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.editLahir.setObjectName("editLahir")
        self.verticalLayout_2.addWidget(self.editLahir)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 381, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bSimpan = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bSimpan.setObjectName("bSimpan")
        self.horizontalLayout.addWidget(self.bSimpan)
        self.bEdit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bEdit.setObjectName("bEdit")
        self.horizontalLayout.addWidget(self.bEdit)
        self.bHapus = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bHapus.setObjectName("bHapus")
        self.horizontalLayout.addWidget(self.bHapus)
        self.bData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bData.setObjectName("bData")
        self.horizontalLayout.addWidget(self.bData)
        self.widget_data = QtWidgets.QTableWidget(Form)
        self.widget_data.setGeometry(QtCore.QRect(10, 200, 381, 121))
        self.widget_data.setObjectName("widget_data")
        self.widget_data.setColumnCount(5)
        self.widget_data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.widget_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_data.setHorizontalHeaderItem(4, item)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 330, 371, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editCari = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.editCari.setObjectName("editCari")
        self.horizontalLayout_2.addWidget(self.editCari)
        self.bCari = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bCari.setObjectName("bCari")
        self.horizontalLayout_2.addWidget(self.bCari)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "NPM"))
        self.label_2.setText(_translate("Form", "Nama"))
        self.label_3.setText(_translate("Form", "Kelas"))
        self.label_4.setText(_translate("Form", "Jurusan"))
        self.label_5.setText(_translate("Form", "Tanggal Lahir"))
        self.bSimpan.setText(_translate("Form", "Simpan"))
        self.bEdit.setText(_translate("Form", "Edit"))
        self.bHapus.setText(_translate("Form", "Hapus"))
        self.bData.setText(_translate("Form", "Load Data"))
        item = self.widget_data.horizontalHeaderItem(0)
        item.setText(_translate("Form", "NPM"))
        item = self.widget_data.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama"))
        item = self.widget_data.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Kelas"))
        item = self.widget_data.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Jurusan"))
        item = self.widget_data.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tanggal Lahir"))
        self.bCari.setText(_translate("Form", "Cari"))
        self.bSimpan.clicked.connect(self.simpan_data)
        self.bEdit.clicked.connect(self.edit_data)
        self.bHapus.clicked.connect(self.hapus_data)
        self.bData.clicked.connect(self.load_data)
        self.bCari.clicked.connect(self.cari_data)

    def simpan_data(self):
        try:
            db = mc.connect(

            host ="localhost",
            user ="root",
            password ="",
            database ="kampus"
            )
            cursor = db.cursor()
            npm = self.editNPM.text()
            nama = self.editNama.text()
            kelas = self.editKelas.text()
            jurusan = self.editJurusan.text()
            tanggal_lahir = self.editLahir.text()
            sql = "INSERT INTO mahasiswa (npm,nama, kelas, jurusan, tanggal_lahir) VALUES (%s,%s,%s,%s,%s)"
            val = (npm,nama,kelas,jurusan,tanggal_lahir)
            cursor.execute(sql,val)
            db.commit()
            self.labeldata_result.setText("Data Berhasil Disimpan")

            self.editNPM.setText("")
            self.editNama.setText("")
            self.editKelas.setText("")
            self.editJurusan.setText("")
            self.editLahir.setText("")
        except mc.Error as e:
            self.labeldata_result.setText("Data Gagal")

    def edit_data(self):
        try:
            db = mc.connect(

            host ="localhost",
            user ="root",
            password ="",
            database ="kampus"
            )
            cursor = db.cursor()
            npm = self.editNPM.text()
            nama = self.editNama.text()
            kelas = self.editKelas.text()
            jurusan = self.editJurusan.text()
            tanggal_lahir = self.editLahir.text()
            which_npm = self.editCari.text()
            sql = "UPDATE mahasiswa set npm =%s, nama=%s,kelas=%s,jurusan=%s,tanggal_lahir=%s WHERE npm=%s"
            val = (npm,nama,kelas,jurusan,tanggal_lahir,which_npm)
            cursor.execute(sql,val)
            db.commit()
            self.labeldata_result.setText("Data Berhasil Diupate")
            self.editNPM.setText("")
            self.editNama.setText("")
            self.editKelas.setText("")
            self.editJurusan.setText("")
            self.editLahir.setText("")
            self.editCari.setText("")
            
        except mc.Error as e:
            self.labeldata_result.setText("Data Gagal Diupdate")

    def hapus_data(self):
        try:
            db = mc.connect(

            host ="localhost",
            user ="root",
            password ="",
            database ="kampus"
            )
            cursor = db.cursor()
            npm = self.editNPM.text()
            sql = "DELETE FROM mahasiswa WHERE npm=%s"
            val = (npm,)
            cursor.execute(sql,val)
            db.commit()
            self.labeldata_result.setText("Data Berhasil Dihapus")
            self.editNPM.setText("")
            
        except mc.Error as e:
            self.labeldata_result.setText("Data Gagal Dihapus")

    def load_data(self):
        try:
            db = mc.connect(
            host ="localhost",
            user ="root",
            password ="",
            database ="kampus"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM mahasiswa ORDER BY npm ASC")
            result = cursor.fetchall()
            self.widget_data.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.widget_data.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.widget_data.setItem(row_number,column_number,
            QTableWidgetItem(str(data)))
            self.labeldata_result.setText("Data Berhasil Ditampilkan")
        except mc.Error as err:
            self.labeldata_result.setText("Data Gagal DiLoad")

    def cari_data(self):
        try:
            db = mc.connect(
            host ="localhost",
            user ="root",
            password ="",
            database ="kampus"
            )
            cursor = db.cursor()
            npm = self.editNPM.text()
            sql = "SELECT * FROM mahasiswa WHERE npm=%s"
            val = (npm,)
            cursor.execute(sql,val)
            result = cursor.fetchall()
            self.widget_data.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.widget_data.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.widget_data.setItem(row_number,column_number,
            QTableWidgetItem(str(data)))
            self.labeldata_result.setText("Data Berhasil Di Filter")
            self.editNPM.setText("")
            
        except mc.Error as err:
            self.labeldata_result.setText("Data Gagal Di Filter")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
