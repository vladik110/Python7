#!/usr/bin/env python3
# coding=utf-8
import sys
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QButtonGroup

answers = ['', '', '']  # 1 - form2, 2 - form3, 3 - form4


class Form1(QtWidgets.QMainWindow):
    # аргумент str говорит о том, что сигнал должен быть строкового типа
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form1, self).__init__()
        uic.loadUi('uis/form1.ui', self)

        self.setWindowTitle('Приветствие')

        self.btn_exit.clicked.connect(self.close)
        self.btn_begin.clicked.connect(self.next)

    def next(self):
        self.switch_window.emit('1>2')


class Form2(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form2, self).__init__()
        uic.loadUi('uis/form2.ui', self)

        self.setWindowTitle('Детство')

        self.label_img.setPixmap(QPixmap('images/picture1.jpg'))

        self.label_img.setScaledContents(True)

        answers[0] = self.radioButton_1.text()
        if answers[0] is not None:
            self.label_selected.setText('Выбрано: ' + answers[0])

        self.radioButton_1.toggled.connect(
            lambda: self.onToggled(self.radioButton_1))
        self.radioButton_2.toggled.connect(
            lambda: self.onToggled(self.radioButton_2))
        self.radioButton_3.toggled.connect(
            lambda: self.onToggled(self.radioButton_3))
        self.radioButton_4.toggled.connect(
            lambda: self.onToggled(self.radioButton_4))

        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def onToggled(self, radiobutton):
        if radiobutton.isChecked():
            answers[0] = radiobutton.text()
            self.label_selected.setText('Выбрано: ' + answers[0])

    def back(self):
        self.switch_window.emit('1<2')

    def next(self):
        self.switch_window.emit('2>3')


class Form3(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form3, self).__init__()
        uic.loadUi('uis/form3.ui', self)

        self.setWindowTitle('Отрочество')
        self.label_img.setPixmap(QPixmap('images/picture2.jpg'))
        self.label_img.setScaledContents(True)

        answers[1] = self.comboBox.itemText(0)

        if answers[1] is not None:
            self.label_selected.setText('Выбрано: ' + answers[1])

        self.comboBox.activated.connect(self.handleActivated)
        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def handleActivated(self, index):
        answers[1] = self.comboBox.itemText(index)
        self.label_selected.setText('Выбрано: ' + answers[1])

    def back(self):
        self.switch_window.emit('2<3')

    def next(self):
        self.switch_window.emit('3>4')


class Form4(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form4, self).__init__()
        uic.loadUi('uis/form4.ui', self)

        self.setWindowTitle('Юность')

        self.label_img.setPixmap(QPixmap('images/picture3.jpg'))
        self.label_img.setScaledContents(True)

        answers[2] = self.checkBox_1.text()

        if answers[2] is not None:
            self.label_selected.setText('Выбрано: ' + answers[2])

        self.button_group = QButtonGroup()

        self.button_group.addButton(self.checkBox_1, 1)
        self.button_group.addButton(self.checkBox_2, 2)
        self.button_group.addButton(self.checkBox_3, 3)
        self.button_group.addButton(self.checkBox_4, 4)

        self.checkBox_1.stateChanged.connect(
            lambda: self.onToggled(self.checkBox_1))
        self.checkBox_2.stateChanged.connect(
            lambda: self.onToggled(self.checkBox_2))
        self.checkBox_3.stateChanged.connect(
            lambda: self.onToggled(self.checkBox_3))
        self.checkBox_4.stateChanged.connect(
            lambda: self.onToggled(self.checkBox_4))

        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def onToggled(self, checkbox):
        if checkbox.isChecked():
            answers[2] = checkbox.text()
            self.label_selected.setText('Выбрано: ' + answers[2])

    def back(self):
        self.switch_window.emit('3<4')

    def next(self):
        self.switch_window.emit('4>5')


class Form5(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form5, self).__init__()
        uic.loadUi('uis/form5.ui', self)

        self.setWindowTitle('Результат')

        self.lineEdit_1.setText("Ваша любимая каша: " + answers[0])
        self.lineEdit_2.setText("Вы учились в 5 классе на: " + answers[1])
        self.lineEdit_3.setText("У вас " + answers[2] + " образование")

        self.btn_back.clicked.connect(self.back)
        self.btn_exit.clicked.connect(self.close)

    def back(self):
        self.switch_window.emit("4<5")


class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()

        if text == '1>2':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form1.close()

        if text == '2>3':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form2.close()

        if text == '3>4':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form3.close()

        if text == '4>5':
            self.form5 = Form5()
            self.form5.switch_window.connect(self.select_forms)
            self.form5.show()
            self.form4.close()

        if text == '4<5':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form5.close()

        if text == '3<4':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form4.close()

        if text == '2<3':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form3.close()

        if text == '1<2':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
            self.form2.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
