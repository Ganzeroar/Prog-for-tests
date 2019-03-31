import sys
import json
import time
import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


# Доделать класс
class mod_win_append_theme(QWidget):
    def __init__(self, self_2, list_for_subj_buttons, list_for_theme_buttons, parent = None):
        super(mod_win_append_theme, self).__init__(parent)
        self.initUI()
        
        self.self_2 = self_2
        self.list_for_subj_buttons = list_for_subj_buttons
        self.list_for_theme_buttons = list_for_theme_buttons
        
    def initUI(self):
    
        
        #modalWindowAppTheme = QtWidgets.QWidget(self, QtCore.Qt.Window)
        self.setWindowTitle("Добавление темы")
        self.setFixedSize(631, 342)
        self.setWindowFlags(QtCore.Qt.Dialog)
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        #self.move(self.self_2.geometry().center() - modalWindowAppTheme.rect().center() - QtCore.QPoint(4, 30))
        
        self.label_and_text()
        
        self.show()
        
        global ultra_dict
        ultra_dict = {}
        try:
            with open('database.json', 'r',encoding="utf-8", ) as file_db:
                ultra_dict = json.load(file_db)
        except:
            None
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
        
        label_name_new_theme = QtWidgets.QLabel("Создание новой темы", self)
        font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 15)
        label_name_new_theme.setFont(font_obj_for_label)
        label_name_new_theme.move(142, 20)
        
        
        
        
        def cancel_add_theme():
            self.close()
        # Кнопка для сохранения предмета в окне создания предмета
        def save_name_theme():
            for btn in self.list_for_subj_buttons:
                if btn.isChecked():
                    name_of_subj = btn.text()
            string_name_theme = name_theme.toPlainText().strip()
            list_of_themes_for_check = [] 
            for subj in ultra_dict:
                for theme in ultra_dict[subj]:
                    list_of_themes_for_check.append(theme)
            modalWindowError = QtWidgets.QWidget(self, QtCore.Qt.Window)
            if bool(name_theme.toPlainText().strip()) != True:
                
                #modalWindowError = QtWidgets.QWidget(modalWindowAppTheme, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(300, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(self.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Заполните все ячейки', self)
                label_of_error.move(80, 100)
                
            
                
                btn_ok = QtWidgets.QPushButton('Ок', self)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(self.close)
                modalWindowError.show()
              
            
            elif string_name_theme in list_of_themes_for_check and modalWindowError.isVisible() != True: 
                # ultra_dict[name_of_subj].keys():
                
                modalWindowError = QtWidgets.QWidget(self, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(400, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(self.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Такая тема уже существует.\nСоздавать темы с одинаковыми названиями нельзя.', modalWindowError)
                label_of_error.move(20, 100)
                
                btn_ok = QtWidgets.QPushButton('Ок', self)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(self.close)
                modalWindowError.show()
                
            else:
              #  name_of_subj = ''
              #  for btn in list_for_subj_buttons:
              #      if btn.isChecked():
              #          name_of_subj = btn.text()
              #  string_name_theme = name_theme.toPlainText()
                
                ultra_dict[name_of_subj][string_name_theme] = {}
             
                with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                    file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                for btn_theme_1 in self.list_for_theme_buttons:
                    btn_theme_1.hide()
                self.list_for_theme_buttons.clear()
                self.self_2.creator_theme_buttons()
               ### метод из мейн кода
                self.self_2.click_subj_choose_themes_local_for_add_theme()
                self.close()
                
        name_theme = QTextEdit(self)
        name_theme.move(404,141)
        name_theme.setFixedSize(190, 86)
        
        btn_exit = QtWidgets.QPushButton('Отмена', self)
        btn_exit.setFixedSize(225, 53)
        btn_exit.move(59, 257)
        btn_exit.clicked.connect(cancel_add_theme)
            
        btn_save_subj = QtWidgets.QPushButton('Сохранить', self)
        btn_save_subj.setFixedSize(225, 53)
        btn_save_subj.move(347, 257)
        btn_save_subj.clicked.connect(save_name_theme)
        
        
        
