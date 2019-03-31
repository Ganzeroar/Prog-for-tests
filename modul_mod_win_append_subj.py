import sys
import json
import time
import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class mod_win_append_subj(QWidget):
    def __init__(self, number,list_for_theme_buttons,self_2, parent=None):
        super(mod_win_append_subj, self).__init__(parent)
        self.initUI()
        #list_for_theme_buttons
        
        self.number = number
        self.list_for_theme_buttons = list_for_theme_buttons
        self.self_2 = self_2
    def initUI(self):
        
        self.setFixedSize(631, 342)
        self.setWindowTitle('Добавление предмета')
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        #self.setParent(self_2)
        #self.setWindowModality(self_2)
        
        self.label_and_text()
        #self.test_func()
        self.show()
        
        
        global ultra_dict
        ultra_dict = {}
        try:
            with open('database.json', 'r',encoding="utf-8", ) as file_db:
                ultra_dict = json.load(file_db)
        except:
            None
         
    def test_func(self):
        def save_name_subj_test():
            print(2)
        label_name_win = QtWidgets.QLabel("Создание нового предмета", self)
        font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 15)
        label_name_win.setFont(font_obj_for_label)
        label_name_win.move(142, 20)
        label_name_win.show()
        
        btn_save_subj = QtWidgets.QPushButton('Сохранить', self)
        btn_save_subj.setFixedSize(225, 53)
        btn_save_subj.move(347, 257)
        btn_save_subj.clicked.connect(save_name_subj_test)
        
        
        print(1)
        print(self)
        print(1)
              
    def paintEvent(self, e):
        
        new_pen = QPen(Qt.black, 2, Qt.SolidLine)
        
        painter_1 = QPainter()
        painter_1.begin(self)
        
        col = QColor(0, 0, 0)
        col.setNamedColor('#676767')
        
        painter_1.setPen(col)
        painter_1.setBrush(QColor(103, 103, 103))
        painter_1.drawRect(0, 0, 631, 76)
        
        
    def label_and_text(self):
        label_name_win = QtWidgets.QLabel("Создание нового предмета", self)
        font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 15)
        label_name_win.setFont(font_obj_for_label)
        label_name_win.move(142, 20)
        label_name_win.show()
        
        def cancel_add_subj():
            #print(1)
            self.close()
        def save_name_subj():
            print(1)
            
            if bool(name_subj.toPlainText().strip()) != True:
                
                modalWindowError = QtWidgets.QWidget(self, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(300, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(self.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Заполните все ячейки', modalWindowError)
                label_of_error.move(80, 100)
                
                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(modalWindowError.close)
                modalWindowError.show()
            
            elif name_subj.toPlainText().strip() in ultra_dict.keys():
                
                modalWindowError = QtWidgets.QWidget(modalWindowAppSubj, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(400, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(modalWindowAppSubj.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Такой предмет уже существует.\nСоздавать предметы с одинаковыми названиями нельзя.', modalWindowError)
                label_of_error.move(20, 100)
                
                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(modalWindowError.close)
                modalWindowError.show()
                
            else:
                string_name_subj = name_subj.toPlainText().strip()
                ultra_dict[string_name_subj] = {}
                with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                    file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                for btn_theme in self.list_for_theme_buttons:
                    btn_theme.hide()
                # очень важная конструкция, активирует метод в мейн классе
                self.self_2.creator_subj_buttons()
                self.close()
        
                    
        label_name_new_subj = QtWidgets.QLabel("Введите название предмета", self)
        font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 15)
        label_name_new_subj.setFont(font_obj_for_label)
        label_name_new_subj.move(41, 143)
        
        name_subj = QTextEdit(self)
        name_subj.move(404,141)
        name_subj.setFixedSize(190, 86)
        global btn_exit
        btn_exit = QtWidgets.QPushButton('Отмена', self)
        btn_exit.setStyleSheet("QPushButton {background-color: rgb(232,236,942); color: White; border-radius: 27px 27px 27px 27px;}"
                           "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        btn_exit.setFixedSize(225, 53)
        btn_exit.move(59, 257)
        btn_exit.clicked.connect(cancel_add_subj)
        
        btn_save_subj = QtWidgets.QPushButton('Сохранить', self)
        btn_save_subj.setFixedSize(225, 53)
        btn_save_subj.move(347, 257)
        btn_save_subj.clicked.connect(save_name_subj)
        










'''
class mod_win_append_subj(QWidget):
    def __init__(self, number,list_for_theme_buttons, parent=None):
        super(mod_win_append_subj, self).__init__(parent)
        self.initUI()
        #list_for_theme_buttons
        
        self.number = number
        self.list_for_theme_buttons = list_for_theme_buttons
    def initUI(self):
        
        self.setFixedSize(400, 400)
        self.setWindowTitle('Добавление предмета')
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        
        self.label_and_text()
        #self.labels()
        #self.buttons()
        #self.creator_subj_buttons()
        #self.creator_theme_buttons()
        
        self.show()
        
        
        global ultra_dict
        ultra_dict = {}
            
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
        
    def paintEvent(self, e):
        print(1)
        print(self.number)
        new_pen = QPen(Qt.black, 2, Qt.SolidLine)
        
        painter_1 = QPainter()
        painter_1.begin(self)
        
        painter_1.setPen(new_pen)
        painter_1.drawLine(4,4,100,10)
        painter_1.end()
   # paintEvent(modalWindowAppSubj)
    def label_and_text(self):
        def cancel_add_subj():
            print(2)
            self.close()
        def save_name_subj():
            
            if bool(name_subj.toPlainText().strip()) != True:
                
                modalWindowError = QtWidgets.QWidget(self, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(300, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(self.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Заполните все ячейки', modalWindowError)
                label_of_error.move(80, 100)
                
                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(modalWindowError.close)
                modalWindowError.show()
            elif name_subj.toPlainText().strip() in ultra_dict.keys():
                
                modalWindowError = QtWidgets.QWidget(modalWindowAppSubj, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(400, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(modalWindowAppSubj.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Такой предмет уже существует.\nСоздавать предметы с одинаковыми названиями нельзя.', modalWindowError)
                label_of_error.move(20, 100)
                
                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(modalWindowError.close)
                modalWindowError.show()
            else:
                string_name_subj = name_subj.toPlainText().strip()
                ultra_dict[string_name_subj] = {}
                with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                    file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                for btn_theme in self.list_for_theme_buttons:
                    btn_theme.hide()
                #MainCodeClass.creator_subj_buttons()
                bd_edit_test_1.MainCodeClass()
                #self.creator_subj_buttons()
                self.close()    
        label_name_new_subj = QtWidgets.QLabel("Введите название предмета", self)
        label_name_new_subj.move(10, 10)
        
        name_subj = QTextEdit(self)
        name_subj.move(20,40)
        global btn_exit
        btn_exit = QtWidgets.QPushButton('Отмена', self)
        btn_exit.move(20,350)
        btn_exit.clicked.connect(cancel_add_subj)
        
        btn_save_subj = QtWidgets.QPushButton('Сохранить', self)
        btn_save_subj.move(200, 350)
        btn_save_subj.clicked.connect(save_name_subj)
                
        
        # Кнопка для сохранения предмета в окне создания предмета
        def save_name_subj():
            
            if bool(name_subj.toPlainText().strip()) != True:
                
                modalWindowError = QtWidgets.QWidget(self, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(300, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(self.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Заполните все ячейки', modalWindowError)
                label_of_error.move(80, 100)
                
                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(modalWindowError.close)
                modalWindowError.show()
            elif name_subj.toPlainText().strip() in ultra_dict.keys():
                
                modalWindowError = QtWidgets.QWidget(modalWindowAppSubj, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(400, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(modalWindowAppSubj.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Такой предмет уже существует.\nСоздавать предметы с одинаковыми названиями нельзя.', modalWindowError)
                label_of_error.move(20, 100)
                
                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(modalWindowError.close)
                modalWindowError.show()
            else:
                string_name_subj = name_subj.toPlainText().strip()
                ultra_dict[string_name_subj] = {}
                with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                    file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                for btn_theme in list_for_theme_buttons:
                    btn_theme.hide()
                self.creator_subj_buttons()
                modalWindowAppSubj.close()
        '''    
       # btn_exit.clicked.connect(cancel_add_subj)
            
       # btn_save_subj = QtWidgets.QPushButton('Сохранить', modalWindowAppSubj)
       # btn_save_subj.move(200, 350)
       # btn_save_subj.clicked.connect(save_name_subj)
                
    
    
    
