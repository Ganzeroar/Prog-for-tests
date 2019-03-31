import sys
import json
import time
import copy
#from test_mod_app_subj.py import xxx
import modul_mod_win_append_subj
import modul_mod_win_append_theme
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


#print('a')
#print(000111110000)
'''
class mod_win_append_subj(QWidget):
    def __init__(self, number,list_for_theme_buttons,self_2, parent=None):
        super(mod_win_append_subj, self).__init__(parent)
        self.initUI()
        #list_for_theme_buttons
        
        self.number = number
        self.list_for_theme_buttons = list_for_theme_buttons
        self.self_2 = self_2
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
                #app_2 = QApplication(sys.argv)
                #import main_file
                #sys.exit()
                #smth_2 = MainCodeClass()
                print(22222)
                #sys.exit(app_2.exec_())
                #MainCodeClass()
                #bd_edit_test_1.MainCodeClass()
                self.self_2.creator_subj_buttons()
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

'''











class MainCodeClass(QWidget):
    #global MainCodeClass
    def __init__(self, parent=None):
        super(MainCodeClass, self).__init__(parent)
        self.initUI()
        
    
    #app = QtWidgets.QApplication(sys.argv)   
    #window = QtWidgets.QWidget()
    #window.setWindowTitle('Редактирование')
    #window.setFixedSize(1024, 758)
    
    def initUI(self):
        print(444444)
        self.setFixedSize(1024, 758)
        self.setWindowTitle('Редактирование')
        print(self)
        self.labels()
        self.buttons()
        self.creator_subj_buttons()
        self.creator_theme_buttons()
        
        self.show()
        print(3333333333)
       # widget_theme_scroll = QtWidgets.QWidget(self)
        #widget_theme_scroll.size(700,100)
       # widget_theme_scroll.move(522, 157)
      #  btn_test = QtWidgets.QPushButton('Добавить предмет', widget_theme_scroll)
      #  widget_theme_scroll.show()
    global ultra_dict
    ultra_dict = {}

    try:
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
    except:
        with open('database.json', 'w',encoding="utf-8",  ) as file_1:
            file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
    global list_of_checked_subj_button_for_edit
    list_of_checked_subj_button_for_edit = []
    global list_for_checked_subj_button
    list_for_checked_subj_button = []
    global list_for_subj_buttons
    list_for_subj_buttons = []
    #global list_for_subj_buttons
    global list_for_theme_buttons
    list_for_theme_buttons = []
    global list_of_subj_buttons_for_edit
    list_of_subj_buttons_for_edit = []
    global list_of_theme_buttons_for_edit
    list_of_theme_buttons_for_edit = []


    dict_for_theme_btn_textofbtn_and_label = {}

    def paintEvent(self, e):
            
        
        painter_1 = QPainter()
        painter_1.begin(self)
        
        col = QColor(0, 0, 0)
        col.setNamedColor('#676767')
        
        painter_1.setPen(col)
        painter_1.setBrush(QColor(103, 103, 103))
        painter_1.drawRect(0, 0, 1024, 80)
        #painter_1.drawLine(4,4,10,10)
        painter_1.setBrush(QColor(232, 236, 242))
        painter_1.drawRect(15, 96, 490, 61)
        painter_1.drawRect(520, 96, 490, 61)
        painter_1.drawLine(15, 157, 15, 748)
        painter_1.drawLine(505, 157, 505, 748)
        painter_1.drawLine(15, 748, 505, 748)
         
        
        painter_1.end()

    def labels(self):
        label_subject = QtWidgets.QLabel("Выбор предмета", self)
        font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 15)
        label_subject.setFont(font_obj_for_label)
        label_subject.move(110, 103)
        label_subject.show()
        label_theme = QtWidgets.QLabel("Выбор темы", self)
        font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 15)
        label_theme.setFont(font_obj_for_label)
        label_theme.move(550, 100)
        label_theme.show()

    def buttons(self):
        try:
            with open('database.json', 'r',encoding="utf-8", ) as file_db:
                ultra_dict = json.load(file_db)
        except:
            None    
        
        
        font_obj_for_btn = QtGui.QFont('times new roman',pointSize = 10)
        icon_for_btn = QtGui.QIcon('icons8_add_96.png')
        size_obj = QtCore.QSize(40, 40)
        
        btn_add_subject = QtWidgets.QPushButton('', self)
        btn_add_subject.setFont(font_obj_for_btn)
        btn_add_subject.setIcon(icon_for_btn)
        btn_add_subject.setIconSize(size_obj)
        btn_add_subject.setFlat(True)
        btn_add_subject.move(451, 104)
        btn_add_subject.setFixedSize(40, 40)
        btn_add_subject.clicked.connect(self.mod_win_append_subj)
        btn_add_subject.show() 

        global btn_add_theme
        btn_add_theme = QtWidgets.QPushButton('', self)
        btn_add_theme.setFont(font_obj_for_btn)
        btn_add_theme.setIcon(icon_for_btn)
        btn_add_theme.setIconSize(size_obj)
        btn_add_theme.setFlat(True)
        btn_add_theme.move(959, 104)
        btn_add_theme.setFixedSize(40, 40)
        btn_add_theme.clicked.connect(self.mod_win_append_theme)
        btn_add_theme.hide()

        global btn_for_delete_subj
        btn_for_delete_subj = QtWidgets.QPushButton('Удалить выбранный предмет', self)
        btn_for_delete_subj.setFixedSize(300, 100)
        btn_for_delete_subj.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 50px 50px 50px 50px;}"
                           "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        btn_for_delete_subj.move(110,630)
        btn_for_delete_subj.clicked.connect(self.final_deleter_subj)
        btn_for_delete_subj.hide()
        
     

    def final_deleter_subj(self):
        modalWindowDeleter = QtWidgets.QWidget(self, QtCore.Qt.Window)
        modalWindowDeleter.setWindowTitle('Удаление вопроса')
        modalWindowDeleter.setFixedSize(300, 250)
        modalWindowDeleter.setWindowFlags(QtCore.Qt.Dialog)
        modalWindowDeleter.setWindowModality(QtCore.Qt.WindowModal)
        modalWindowDeleter.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modalWindowDeleter.move(self.geometry().center() - modalWindowDeleter.rect().center() - QtCore.QPoint(4, 30))
                    
        label_of_attention = QtWidgets.QLabel('Вы уверены, что хотите удалить предмет?', modalWindowDeleter)
        label_of_attention.move(40, 100)
                    
                    
        def final_delete_quest():
            btn_add_theme.hide()
            with open('database.json', 'r',encoding="utf-8", ) as file_db:
                ultra_dict = json.load(file_db)
            for button_1 in list_for_subj_buttons:
                if button_1.isChecked():
                    var_for_delete = button_1.text()
                    ultra_dict.pop(var_for_delete)
                    with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                        file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                    self.creator_subj_buttons()
                    
                    for btn in list_for_theme_buttons:
                        btn.hide()
                    btn_for_delete_subj.hide()   
                    modalWindowDeleter.close() 
                    #app = QtWidgets.QApplication(sys.argv)
                    #smth = MainCodeClass()
                    #sys.exit(app.exec_())        
        def cancel_from_delete_window():
            modalWindowDeleter.close()
                                
        btn_no = QtWidgets.QPushButton('нет', modalWindowDeleter)
        btn_no.move(20, 200)
        btn_no.clicked.connect(cancel_from_delete_window)
        
        
        btn_yes = QtWidgets.QPushButton('да', modalWindowDeleter)
        btn_yes.move(140, 200)
        btn_yes.clicked.connect(final_delete_quest)
        
        

        modalWindowDeleter.show()
    '''   
        btn_add_theme.hide()
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
        for button_1 in list_for_subj_buttons:
            if button_1.isChecked():
                var_for_delete = button_1.text()
                ultra_dict.pop(var_for_delete)
                with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                    file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                creator_subj_buttons()
                
                for btn in list_for_theme_buttons:
                    btn.hide()
                btn_for_delete_subj.hide()
    '''                
         
    def mod_win_append_theme(self):
        modul_mod_win_append_theme.mod_win_append_theme(self, list_for_subj_buttons, list_for_theme_buttons)
        '''
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
        modalWindowAppTheme = QtWidgets.QWidget(self, QtCore.Qt.Window)
        modalWindowAppTheme.setWindowTitle("Добавление темы")
        modalWindowAppTheme.setFixedSize(400, 400)
        modalWindowAppTheme.setWindowFlags(QtCore.Qt.Dialog)
        
        modalWindowAppTheme.setWindowModality(QtCore.Qt.WindowModal)
        modalWindowAppTheme.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modalWindowAppTheme.move(self.geometry().center() - modalWindowAppTheme.rect().center() - QtCore.QPoint(4, 30))
        label_name_new_theme = QtWidgets.QLabel("Введите название темы", modalWindowAppTheme)
        label_name_new_theme.move(10, 10)
        
        name_theme = QTextEdit(modalWindowAppTheme)
        name_theme.move(20,40)
        
        btn_exit = QtWidgets.QPushButton('Отмена', modalWindowAppTheme)
        btn_exit.move(20,350)
        
        def cancel_add_theme():
            modalWindowAppTheme.close()
        # Кнопка для сохранения предмета в окне создания предмета
        def save_name_theme():
            for btn in list_for_subj_buttons:
                if btn.isChecked():
                    name_of_subj = btn.text()
            string_name_theme = name_theme.toPlainText().strip()
            list_of_themes_for_check = [] 
            for subj in ultra_dict:
                for theme in ultra_dict[subj]:
                    list_of_themes_for_check.append(theme)
            modalWindowError = QtWidgets.QWidget(modalWindowAppTheme, QtCore.Qt.Window)
            if bool(name_theme.toPlainText().strip()) != True:
                
                #modalWindowError = QtWidgets.QWidget(modalWindowAppTheme, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(300, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(modalWindowAppTheme.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Заполните все ячейки', modalWindowError)
                label_of_error.move(80, 100)
                
            
                
                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(modalWindowError.close)
                modalWindowError.show()
              
            
            elif string_name_theme in list_of_themes_for_check and modalWindowError.isVisible() != True: 
                # ultra_dict[name_of_subj].keys():
                
                modalWindowError = QtWidgets.QWidget(modalWindowAppTheme, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(400, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(modalWindowAppTheme.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
                label_of_error = QtWidgets.QLabel('Такая тема уже существует.\nСоздавать темы с одинаковыми названиями нельзя.', modalWindowError)
                label_of_error.move(20, 100)
                
                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                btn_ok.move(80, 200)
                btn_ok.clicked.connect(modalWindowError.close)
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
                for btn_theme_1 in list_for_theme_buttons:
                    btn_theme_1.hide()
                list_for_theme_buttons.clear()
                self.creator_theme_buttons()
               
                self.click_subj_choose_themes_local_for_add_theme()
                modalWindowAppTheme.close()
            
        btn_exit.clicked.connect(cancel_add_theme)
            
        btn_save_subj = QtWidgets.QPushButton('Сохранить', modalWindowAppTheme)
        btn_save_subj.move(200, 350)
        btn_save_subj.clicked.connect(save_name_theme)
        
        
        modalWindowAppTheme.show()
    #class two_k(MainCodeClass):
     #   print(1)
    '''
    
    def mod_win_append_subj(self):
        
        #self.close()
        modul_mod_win_append_subj.mod_win_append_subj(5, list_for_theme_buttons, self)
        #self.creator_subj_buttons()
        #self.close()
        #app = QtWidgets.QApplication(sys.argv)
        #smth = MainCodeClass()
        #sys.exit(app.exec_())
       # mod_win_append_subj()
    '''
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
        modalWindowAppSubj = QtWidgets.QWidget(self, QtCore.Qt.Window)
        #class mod_win_append_subj_class():
         #   def paintEvent(modalWindowAppSubj, e):
            #print(1)
          #      new_pen = QPen(Qt.black, 2, Qt.SolidLine)
                
          #      painter_1 = QPainter()
          #      painter_1.begin(modalWindowAppSubj)
                
          #      painter_1.setPen(new_pen)
          #      painter_1.drawLine(4,4,10,10)
          #      painter_1.end()
          #  paintEvent(modalWindowAppSubj)
        #modalWindowAppSubj = QtWidgets.QWidget(self, QtCore.Qt.Window)
        modalWindowAppSubj.setWindowTitle("Добавление предмета")
        modalWindowAppSubj.setFixedSize(400, 400)
        modalWindowAppSubj.setWindowFlags(QtCore.Qt.Dialog)
        
        modalWindowAppSubj.setWindowModality(QtCore.Qt.WindowModal)
        modalWindowAppSubj.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modalWindowAppSubj.move(self.geometry().center() - modalWindowAppSubj.rect().center() - QtCore.QPoint(4, 30))
        
        def paintEvent(modalWindowAppSubj, e):
            #print(1)
            new_pen = QPen(Qt.black, 2, Qt.SolidLine)
            
            painter_1 = QPainter()
            painter_1.begin(modalWindowAppSubj)
            
            painter_1.setPen(new_pen)
            painter_1.drawLine(4,4,400,400)
            painter_1.end()
       # paintEvent(modalWindowAppSubj)
        label_name_new_subj = QtWidgets.QLabel("Введите название предмета", modalWindowAppSubj)
        label_name_new_subj.move(10, 10)
        
        name_subj = QTextEdit(modalWindowAppSubj)
        name_subj.move(20,40)
        
        btn_exit = QtWidgets.QPushButton('Отмена', modalWindowAppSubj)
        btn_exit.move(20,350)
        
        def cancel_add_subj():
            modalWindowAppSubj.hide()
        # Кнопка для сохранения предмета в окне создания предмета
        def save_name_subj():
            if bool(name_subj.toPlainText().strip()) != True:
                
                modalWindowError = QtWidgets.QWidget(modalWindowAppSubj, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(300, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(modalWindowAppSubj.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
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
            
        btn_exit.clicked.connect(cancel_add_subj)
            
        btn_save_subj = QtWidgets.QPushButton('Сохранить', modalWindowAppSubj)
        btn_save_subj.move(200, 350)
        btn_save_subj.clicked.connect(save_name_subj)
                
        
        modalWindowAppSubj.show()
    '''
    '''
    def mod_win_append_subj(self):
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
        
        modalWindowAppSubj = QtWidgets.QWidget(self, QtCore.Qt.Window)
        modalWindowAppSubj.setWindowTitle("Добавление предмета")
        modalWindowAppSubj.setFixedSize(400, 400)
        modalWindowAppSubj.setWindowFlags(QtCore.Qt.Dialog)
        
        modalWindowAppSubj.setWindowModality(QtCore.Qt.WindowModal)
        modalWindowAppSubj.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modalWindowAppSubj.move(self.geometry().center() - modalWindowAppSubj.rect().center() - QtCore.QPoint(4, 30))
        
        def paintEvent(modalWindowAppSubj):
            #print(1)
            new_pen = QPen(Qt.black, 2, Qt.SolidLine)
            
            painter_1 = QPainter()
            painter_1.begin(modalWindowAppSubj)
            
            painter_1.setPen(new_pen)
            painter_1.drawLine(4,4,10,10)
            painter_1.end()
        paintEvent(modalWindowAppSubj)
        label_name_new_subj = QtWidgets.QLabel("Введите название предмета", modalWindowAppSubj)
        label_name_new_subj.move(10, 10)
        
        name_subj = QTextEdit(modalWindowAppSubj)
        name_subj.move(20,40)
        
        btn_exit = QtWidgets.QPushButton('Отмена', modalWindowAppSubj)
        btn_exit.move(20,350)
        
        def cancel_add_subj():
            modalWindowAppSubj.hide()
        # Кнопка для сохранения предмета в окне создания предмета
        def save_name_subj():
            if bool(name_subj.toPlainText().strip()) != True:
                
                modalWindowError = QtWidgets.QWidget(modalWindowAppSubj, QtCore.Qt.Window)
                modalWindowError.setWindowTitle('Ошибка')
                modalWindowError.setFixedSize(300, 250)
                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                modalWindowError.move(modalWindowAppSubj.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                
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
                creator_subj_buttons()
                modalWindowAppSubj.close()
            
        btn_exit.clicked.connect(cancel_add_subj)
            
        btn_save_subj = QtWidgets.QPushButton('Сохранить', modalWindowAppSubj)
        btn_save_subj.move(200, 350)
        btn_save_subj.clicked.connect(save_name_subj)
        
        
        
        
        modalWindowAppSubj.show()
    '''
    var_for_number_index_of_checked_button = 0

    def click_subj_choose_themes_local_for_add_theme(self):
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
       
        try:
            for button_2 in list_for_changed_btn_for_text_wrap:
                var_name = dict_for_theme_btn_textofbtn_and_label[button_2][0]
                button_2.setText(dict_for_theme_btn_textofbtn_and_label[button_2][0])
                dict_for_theme_btn_textofbtn_and_label[button_2][1].setText('')
        except:
            None
        list_for_changed_btn_for_text_wrap.clear()
        
        
        for button_1 in list_for_subj_buttons:
            if button_1.isChecked():
                for btn in list_for_theme_buttons:
                    btn.hide()
                    if btn.text() in ultra_dict[button_1.text()]:
                        
                        btn.setText('')
                        dict_for_theme_btn_textofbtn_and_label[btn][1].setText(dict_for_theme_btn_textofbtn_and_label[btn][0])
                   
                        list_for_changed_btn_for_text_wrap.append(btn)     
                        btn.show()



    global list_for_text_of_btn_for_wrap
    list_for_text_of_btn_for_wrap = []
    global list_for_changed_btn_for_text_wrap
    list_for_changed_btn_for_text_wrap = []
    global dict_of_btn_label_for_text_wrap
    dict_of_btn_label_for_text_wrap = {}



    def click_subj_choose_themes(self):
        btn_for_delete_subj.show()
        for btn_theme in list_for_theme_buttons:
            btn_theme.hide()
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
        list_for_check_or_no_btn = []
        for btn in list_for_checked_subj_button:
            btn.setChecked(False)
            list_for_checked_subj_button.pop()
        for h in list_for_theme_buttons:
            h.hide()
            
        try:
            for button_2 in list_for_changed_btn_for_text_wrap:
                button_2.setText(dict_for_theme_btn_textofbtn_and_label[button_2][0])
                dict_for_theme_btn_textofbtn_and_label[button_2][1].setText('')
        except:
            None
        list_for_changed_btn_for_text_wrap.clear()
        
        
        for button_1 in list_for_subj_buttons:
            if button_1.isChecked():
                var_for_number_index_of_checked_button = list_for_subj_buttons.index(button_1)
                
                list_for_check_or_no_btn.append(True)
                list_for_checked_subj_button.append(button_1)
                for btn in list_for_theme_buttons:
                    if btn.text() in ultra_dict[button_1.text()]:

                        btn.setText('')
                        dict_for_theme_btn_textofbtn_and_label[btn][1].setText(dict_for_theme_btn_textofbtn_and_label[btn][0])
                   
                        list_for_changed_btn_for_text_wrap.append(btn)   
                                       
                        btn.show()
                        
                
            else:
                list_for_check_or_no_btn.append(False)
        if True in list_for_check_or_no_btn:
            btn_add_theme.show()
        else:
            btn_add_theme.hide()
            
    #   def final_deleter_subj():
    #        for button_1 in list_for_subj_buttons:
    #            if button_1.isChecked():
    #                var_for_delete = button_1.text()
    #                ultra_dict.pop(var_for_delete)
    #                with open('database.json', 'w',encoding="utf-8",  ) as file_1:
    #                    file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
    #                creator_subj_buttons()
    #                
    #                for btn in list_for_theme_buttons:
    #                    btn.hide()
    #                btn_for_delete_subj.hide()
                    
                
        
    #    btn_for_delete_subj = QtWidgets.QPushButton('Удалить выбранный предмет', window)
    #    btn_for_delete_subj.setFixedSize(200, 50)
    #    btn_for_delete_subj.move(50,50)
    #    btn_for_delete_subj.clicked.connect(final_deleter_subj)
    #    btn_for_delete_subj.show()
        
        var_for_hidder_btn = True
        for button_2 in list_for_subj_buttons:
            if button_2.isChecked():
                var_for_hidder_btn = False
        if var_for_hidder_btn:
            btn_for_delete_subj.hide()


    def creator_subj_buttons(self):
        
        try:
            for btn in list_for_subj_buttons:
                btn.hide()
                btn.destroy()
        except:
            None
        try:
            with open('database.json', 'r',encoding="utf-8", ) as file_db:
                ultra_dict = json.load(file_db)
        except:
            None
       # for btn in list_for_subj_buttons:
        #    btn.destroy()
            
        list_for_subj_buttons.clear()
        y_coord_for_btn_subj = 170
        # Создаёт кнопки предметов 
        
        for subj in ultra_dict.items():
            
            button_of_subject = QtWidgets.QPushButton(str(subj[0]), self)
            font_obj_for_btn = QtGui.QFont('Segoe UI', pointSize = 15)
            button_of_subject.setFont(font_obj_for_btn)
            button_of_subject.setCheckable(True)
            button_of_subject.clicked.connect(self.click_subj_choose_themes)
            button_of_subject.move(26, y_coord_for_btn_subj)
            button_of_subject.setFixedSize(469, 44)
            #button_of_subject.setFlat(True)
            #button_of_subject.setStyleSheet("QPushButton {white-space: pre-line;}")
            button_of_subject.show()
            list_for_subj_buttons.append(button_of_subject)
            y_coord_for_btn_subj += 50   
            print(10)
        print(list_for_subj_buttons)
        for btn_3 in list_for_subj_buttons:
            print(btn_3.isHidden())
    global list_for_text_of_dict_of_btn
    list_for_text_of_dict_of_btn = []
    #list_for_pressed_btn_for_repaint = []
    def click_theme_start_edit(self):
        print(1212121212) 
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
        
        list_for_pressed_btn_for_repaint = []
        
        list_of_all_text_field = []
        list_of_all_radiobtn = []
        list_of_answers_text_field = []
        list_of_text_field_answers = []
        list_of_all_quest_field = []
        global var_for_subj
        global var_for_theme
        var_for_subj = ''
        var_for_theme = ''
        list_for_btn_subj = []
        list_for_btn_theme = []
        list_for_field_of_theme = []
        
        for btn_subj in list_for_subj_buttons:
            if btn_subj.isChecked():
                list_for_btn_subj.append(btn_subj)
        
        modalWindowEdit = QtWidgets.QWidget(self, QtCore.Qt.Window)
        modalWindowEdit.setWindowTitle('Редактирование')
        modalWindowEdit.setFixedSize(1024, 758)
        modalWindowEdit.setWindowFlags(QtCore.Qt.Dialog)
        modalWindowEdit.setWindowModality(QtCore.Qt.WindowModal)
        modalWindowEdit.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modalWindowEdit.move(self.geometry().center() - modalWindowEdit.rect().center() - QtCore.QPoint(4, 30))
        
        scrollArea = QtWidgets.QScrollArea()
        widget = QtWidgets.QWidget()
        #widget_for_theme_scroll.move(522, 157)
        #def closeEvent(modalWindowEdit):
        #    print(1)
        #modalWindowEdit.closeEvent( )
       # def closeEvent(modalWindowEdit):
        #    print(1)
        
        list_for_text_of_dict_of_btn.clear()
        for button in list_for_theme_buttons:
            if button.isChecked():
                list_for_text_of_dict_of_btn.append(dict_for_theme_btn_textofbtn_and_label[button][0])

                list_for_btn_theme.append(button.text())
                list_for_pressed_btn_for_repaint.append(button)
                vbox = QtWidgets.QVBoxLayout()
                
                hbox_1 = QtWidgets.QHBoxLayout()
                hbox_2 = QtWidgets.QHBoxLayout()
                
                
                label_subj = QtWidgets.QLabel('Название предмета: ', widget)
                hbox_1.addWidget(label_subj)
                
                field_of_subj = QTextEdit(str(list_for_btn_subj[0].text()), widget)
                field_of_subj.setFixedSize(300, 50)
                text_of_subj_before_edit = field_of_subj.toPlainText().rstrip()
                hbox_1.addWidget(field_of_subj)
                vbox.addLayout(hbox_1)
                
                label_theme = QtWidgets.QLabel('Название темы: ', widget)
                hbox_2.addWidget(label_theme)
                
                field_of_theme = QTextEdit(str(dict_for_theme_btn_textofbtn_and_label[button][0]), widget)
                field_of_theme.setFixedSize(300, 50)
                text_of_theme_before_edit = field_of_theme.toPlainText().rstrip()
                list_for_field_of_theme.append(field_of_theme.toPlainText())
                hbox_2.addWidget(field_of_theme)
                vbox.addLayout(hbox_2)
                
                
                list_of_questions = []
                list_for_answers = []
                list_for_delete_quest_button = []
                # for subject in ultra_dict.keys():
                   # try:
                
                for btn_subj in list_for_subj_buttons:
                    if btn_subj.isChecked():
                        subject = btn_subj.text()
                        
                        for theme_2 in dict_for_theme_btn_textofbtn_and_label:
                           # print(dict_for_theme_btn_textofbtn_and_label[theme_2][0])
                            if dict_for_theme_btn_textofbtn_and_label[button][0] == dict_for_theme_btn_textofbtn_and_label[theme_2][0]:
                                #print(dict_for_theme_btn_textofbtn_and_label)
                                var_for_subj = subject
                                var_for_theme = dict_for_theme_btn_textofbtn_and_label[theme_2][0]

                                dict_of_questions = ultra_dict[subject][dict_for_theme_btn_textofbtn_and_label[theme_2][0]]
                                
                                for quests in dict_of_questions.keys():
                                    list_of_questions.append(quests)
                                    local_answ_list = []
                                    for answer in dict_of_questions[quests]:
                                        #if answer[-1] == ' ':
                                        #    answer = answer[0:-1]
                                        local_answ_list.append(answer)
                                    list_for_answers.append(local_answ_list)

                       # break
                            
                    #except:
                    #    None
                def func_for_delete_quest():
                    modalWindowChoose = QtWidgets.QWidget(modalWindowEdit, QtCore.Qt.Window)
                    modalWindowChoose.setWindowTitle('Удаление вопроса')
                    modalWindowChoose.setFixedSize(300, 250)
                    modalWindowChoose.setWindowFlags(QtCore.Qt.Dialog)
                    modalWindowChoose.setWindowModality(QtCore.Qt.WindowModal)
                    modalWindowChoose.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                    modalWindowChoose.move(modalWindowEdit.geometry().center() - modalWindowChoose.rect().center() - QtCore.QPoint(4, 30))
                    
                    label_of_error = QtWidgets.QLabel('Вы уверены, что хотите удалить вопрос?', modalWindowChoose)
                    label_of_error.move(40, 100)
                    
                    for button in list_for_delete_quest_button:
                        if button.isChecked():
                            index_of_delete_btn = list_for_delete_quest_button.index(button)
                    
                    for button in list_for_delete_quest_button:
                        button.setChecked(False)
                    
                    def final_delete_quest():
                       # for button in list_for_delete_quest_button:
                       #     if button.isChecked():
                       #         index_of_delete_btn = list_for_delete_quest_button.index(button)
                        list_of_questions = list(ultra_dict[var_for_subj][var_for_theme].keys())
                        elem_for_delete = list_of_questions[index_of_delete_btn]
                        
                        ultra_dict[var_for_subj][var_for_theme].pop(elem_for_delete)
                        with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                            file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                        modalWindowEdit.close()
                        modalWindowChoose.close()
                        for theme_button in list_for_theme_buttons:
                            
                            if theme_button == list_for_pressed_btn_for_repaint[0]:
                                
                                theme_button.click()
                             #   for button in list_for_delete_quest_button:
                             #       button.setChecked(False)
                        
                        # list_for_pressed_btn_for_repaint
                        #click_theme_start_edit()
                    
                    def cancel_from_delete_window():
                      #  for button in list_for_delete_quest_button:
                      #      button.setChecked(False)
                        modalWindowChoose.close()
                                
                    btn_no = QtWidgets.QPushButton('нет', modalWindowChoose)
                    btn_no.move(20, 200)
                    btn_no.clicked.connect(cancel_from_delete_window)
                    
                    
                    btn_yes = QtWidgets.QPushButton('да', modalWindowChoose)
                    btn_yes.move(140, 200)
                    btn_yes.clicked.connect(final_delete_quest)
                    
                    #for button in list_for_delete_quest_button:
                    #    button.setChecked(False)
                
                    modalWindowChoose.show()
                    
                for num in range(1,len(list_of_questions)+1):
                    

                    
                    hbox_for_cycle_1 = QtWidgets.QHBoxLayout()
                    hbox_for_cycle_2 = QtWidgets.QHBoxLayout()
                    hbox_for_cycle_3 = QtWidgets.QHBoxLayout()
                    
                    hbox_for_answers_1 = QtWidgets.QHBoxLayout()
                    hbox_for_answers_2 = QtWidgets.QHBoxLayout()
                    hbox_for_answers_3 = QtWidgets.QHBoxLayout()
                    hbox_for_answers_4 = QtWidgets.QHBoxLayout()
                    
                    vbox_for_cycle_1 = QtWidgets.QVBoxLayout()
                    
                    groupBox = QtWidgets.QGroupBox(widget)
                    groupBox.setFixedSize(350, 300)
                    groupLayout = QtWidgets.QWidget(groupBox)
                    groupVerticalLayout = QtWidgets.QVBoxLayout(groupLayout)
                    
                    quest_text = 'Вопрос № ' + str(num)
                    label_of_quest = QtWidgets.QLabel(quest_text, widget)
                    field_of_quest = QTextEdit(str(list_of_questions[num - 1]), widget)
                    field_of_quest.setFixedSize(300,50)
                    ##### Изменить в будущем, добавить туплейнтекст
                    list_of_all_quest_field.append(field_of_quest)
                    
                    delete_quest_button = QtWidgets.QPushButton('Удалить вопрос', modalWindowEdit)
                    delete_quest_button.clicked.connect(func_for_delete_quest)
                    delete_quest_button.setFixedSize(150, 50)
                    delete_quest_button.setCheckable(True)
                    delete_quest_button.show()
                    list_for_delete_quest_button.append(delete_quest_button)
                    
                    
                   # button_of_subject.setCheckable(True)
                   # button_of_subject.clicked.connect(click_subj_choose_themes)
                   # button_of_subject.move(130, x_coord_for_btn_subj)
                   # button_of_subject.setFixedSize(300, 50)
                   # button_of_subject.setStyleSheet("QPushButton {white-space: pre-line;}")
                   # button_of_subject.show()
                   # list_for_subj_buttons.append(button_of_subject)
                    
                    hbox_for_cycle_1.addWidget(label_of_quest)
                    hbox_for_cycle_1.addWidget(field_of_quest)
                    hbox_for_cycle_1.addWidget(delete_quest_button)
                    vbox.addLayout(hbox_for_cycle_1)
                    
                    label_of_answ_variants = QtWidgets.QLabel('Варианты ответа: ', widget)
                   
                    hbox_for_cycle_2.addWidget(label_of_answ_variants)
                   
                    vbox.addLayout(hbox_for_cycle_2)
                    
                    radio_1 = QtWidgets.QRadioButton(widget)
                    radio_2 = QtWidgets.QRadioButton(widget)
                    radio_3 = QtWidgets.QRadioButton(widget)
                    radio_4 = QtWidgets.QRadioButton(widget)
                    
                    list_of_all_radiobtn.append(radio_1)
                    list_of_all_radiobtn.append(radio_2)
                    list_of_all_radiobtn.append(radio_3)
                    list_of_all_radiobtn.append(radio_4)
                    # на самом деле поля ответов 
                    
                    
                    field_of_answer_1 = QTextEdit(list_for_answers[num - 1][0], widget)
                    field_of_answer_1.setFixedSize(300,50)
                    field_of_answer_2 = QTextEdit(list_for_answers[num - 1][1], widget)
                    field_of_answer_2.setFixedSize(300,50)
                    field_of_answer_3 = QTextEdit(list_for_answers[num - 1][2], widget)
                    field_of_answer_3.setFixedSize(300,50)
                    field_of_answer_4 = QTextEdit(list_for_answers[num - 1][3], widget)
                    field_of_answer_4.setFixedSize(300,50)
                    

                    list_of_answers_text_field.append(field_of_answer_1.toPlainText())
                    list_of_answers_text_field.append(field_of_answer_2.toPlainText())
                    list_of_answers_text_field.append(field_of_answer_3.toPlainText())
                    list_of_answers_text_field.append(field_of_answer_4.toPlainText())
                    
                    list_of_text_field_answers.append(field_of_answer_1)
                    list_of_text_field_answers.append(field_of_answer_2)
                    list_of_text_field_answers.append(field_of_answer_3)
                    list_of_text_field_answers.append(field_of_answer_4)
                    
                    for answ_for_check in list_of_answers_text_field:
                        # Удаляет пробел в конце правильного ответа
                        if answ_for_check[-1] == ' ':
                            index_of_right_answ = list_of_answers_text_field.index(answ_for_check)
                            list_of_all_radiobtn[index_of_right_answ].setChecked(True)
                            text_of_field = list_of_text_field_answers[index_of_right_answ].toPlainText()
                            list_of_text_field_answers[index_of_right_answ].setText(text_of_field.rstrip())
                    hbox_for_answers_1.addWidget(radio_1)
                    hbox_for_answers_1.addWidget(field_of_answer_1)
                    groupVerticalLayout.addLayout(hbox_for_answers_1)
                    
                    hbox_for_answers_2.addWidget(radio_2)
                    hbox_for_answers_2.addWidget(field_of_answer_2)
                    groupVerticalLayout.addLayout(hbox_for_answers_2)
                    
                    hbox_for_answers_3.addWidget(radio_3)
                    hbox_for_answers_3.addWidget(field_of_answer_3)
                    groupVerticalLayout.addLayout(hbox_for_answers_3)
                    
                    hbox_for_answers_4.addWidget(radio_4)
                    hbox_for_answers_4.addWidget(field_of_answer_4)
                    groupVerticalLayout.addLayout(hbox_for_answers_4)
                    
                    #ЕСЛИ НАДО ДОБАВИТЬ ПРОБЕЛЫ МЕЖДУ БАТОНАМИ
                    hbox_for_cycle_3.addWidget(groupBox)
                    vbox.addLayout(hbox_for_cycle_3)
                       
                widget.setLayout(vbox)
                scrollArea.setWidget(widget)
                scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
                mainbox = QtWidgets.QVBoxLayout()
                mainbox.addWidget(scrollArea)
                mainbox.addSpacing(50)
                modalWindowEdit.setLayout(mainbox)
                
        def creator_mod_win_adder_quest():
       
            modalWindowAddQuest = QtWidgets.QWidget(modalWindowEdit, QtCore.Qt.Window)
            modalWindowAddQuest.setWindowTitle('Добавление вопроса')
            modalWindowAddQuest.setFixedSize(512, 450)
            modalWindowAddQuest.setWindowFlags(QtCore.Qt.Dialog)
            modalWindowAddQuest.setWindowModality(QtCore.Qt.WindowModal)
            modalWindowAddQuest.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
            modalWindowAddQuest.move(modalWindowEdit.geometry().center() - modalWindowAddQuest.rect().center() - QtCore.QPoint(4, 30))
            
            
            
            widget_create = QtWidgets.QWidget()
        
            vbox_create = QtWidgets.QVBoxLayout()
                
            hbox_create_1 = QtWidgets.QHBoxLayout()
            hbox_create_2 = QtWidgets.QHBoxLayout()
            
            hbox_for_create_1 = QtWidgets.QHBoxLayout()
            hbox_for_create_2 = QtWidgets.QHBoxLayout()
            hbox_for_create_3 = QtWidgets.QHBoxLayout()
            hbox_for_create_4 = QtWidgets.QHBoxLayout()
            
            hbox_for_create_answ_1 = QtWidgets.QHBoxLayout()
            hbox_for_create_answ_2 = QtWidgets.QHBoxLayout()
            hbox_for_create_answ_3 = QtWidgets.QHBoxLayout()
            hbox_for_create_answ_4 = QtWidgets.QHBoxLayout()
            
            vbox_for_create_1 = QtWidgets.QVBoxLayout()
            
            groupBox_for_create = QtWidgets.QGroupBox(widget_create)
            groupBox_for_create.setFixedSize(350, 300)
            groupLayout_create = QtWidgets.QWidget(groupBox_for_create)
            groupVerticalLayout_create = QtWidgets.QVBoxLayout(groupLayout_create)
            
            label_of_create_quest = QtWidgets.QLabel('Новый вопрос: ', widget_create)
            field_of_create_quest = QtWidgets.QTextEdit(widget_create)
            field_of_create_quest.setFixedSize(300, 50)
            
            hbox_for_create_1.addWidget(label_of_create_quest)
            hbox_for_create_1.addWidget(field_of_create_quest)
            vbox_create.addLayout(hbox_for_create_1)
            
            label_of_answ_choices_for_create = QtWidgets.QLabel('Варианты ответа: ', widget_create)
            hbox_for_create_2.addWidget(label_of_answ_choices_for_create)
            vbox_create.addLayout(hbox_for_create_2)
            
            radio_create_1 = QtWidgets.QRadioButton(widget_create)
            radio_create_2 = QtWidgets.QRadioButton(widget_create)
            radio_create_3 = QtWidgets.QRadioButton(widget_create)
            radio_create_4 = QtWidgets.QRadioButton(widget_create)
            
            field_of_quest_create_1 = QtWidgets.QTextEdit(widget_create)
            field_of_quest_create_1.setFixedSize(300, 50)
            field_of_quest_create_2 = QtWidgets.QTextEdit(widget_create)
            field_of_quest_create_2.setFixedSize(300, 50)
            field_of_quest_create_3 = QtWidgets.QTextEdit(widget_create)
            field_of_quest_create_3.setFixedSize(300, 50)
            field_of_quest_create_4 = QtWidgets.QTextEdit(widget_create)
            field_of_quest_create_4.setFixedSize(300, 50)
            
            hbox_for_create_answ_1.addWidget(radio_create_1)
            hbox_for_create_answ_1.addWidget(field_of_quest_create_1)
            groupVerticalLayout_create.addLayout(hbox_for_create_answ_1)
            
            hbox_for_create_answ_2.addWidget(radio_create_2)
            hbox_for_create_answ_2.addWidget(field_of_quest_create_2)
            groupVerticalLayout_create.addLayout(hbox_for_create_answ_2)
            
            hbox_for_create_answ_3.addWidget(radio_create_3)
            hbox_for_create_answ_3.addWidget(field_of_quest_create_3)
            groupVerticalLayout_create.addLayout(hbox_for_create_answ_3)
            
            hbox_for_create_answ_4.addWidget(radio_create_4)
            hbox_for_create_answ_4.addWidget(field_of_quest_create_4)
            groupVerticalLayout_create.addLayout(hbox_for_create_answ_4)
            
            hbox_for_create_3.addWidget(groupBox_for_create)
            vbox_create.addLayout(hbox_for_create_3)
            
            widget_create.setLayout(vbox_create)
            mainbox_create = QtWidgets.QVBoxLayout()
            mainbox_create.addWidget(widget_create)
            mainbox_create.addSpacing(100)
            modalWindowAddQuest.setLayout(mainbox_create)
            
            
            
            def final_save_new_quest():
                
                list_of_all_text_field = []
                list_of_all_radiobtn = []
                list_of_questions_test_field = []
                
                copy_of_ultra_dict = copy.deepcopy(ultra_dict)
                
                list_of_all_text_field.append(field_of_create_quest)
                list_of_all_text_field.append(field_of_quest_create_1)
                list_of_all_text_field.append(field_of_quest_create_2)
                list_of_all_text_field.append(field_of_quest_create_3)
                list_of_all_text_field.append(field_of_quest_create_4)
                
                list_of_questions_test_field.append(field_of_quest_create_1.toPlainText().strip())
                list_of_questions_test_field.append(field_of_quest_create_2.toPlainText().strip())
                list_of_questions_test_field.append(field_of_quest_create_3.toPlainText().strip())
                list_of_questions_test_field.append(field_of_quest_create_4.toPlainText().strip())
                
                list_of_all_radiobtn.append(radio_create_1)
                list_of_all_radiobtn.append(radio_create_2)
                list_of_all_radiobtn.append(radio_create_3)
                list_of_all_radiobtn.append(radio_create_4)
                
                var_for_pass_1 = True
                var_for_pass_2 = True
                var_for_pass_3 = True
                var_for_pass_4 = True 
                var_for_pass_5 = True
                
                modalWindowError = QtWidgets.QWidget(modalWindowAddQuest, QtCore.Qt.Window)
                modalWindowErrorChoose = QtWidgets.QWidget(modalWindowAddQuest, QtCore.Qt.Window)
                for one in list_of_all_text_field:
                    
                    if bool(one.toPlainText().strip()) != True:
                        #modalWindowError = QtWidgets.QWidget(modalWindowAddQuest, QtCore.Qt.Window)
                        modalWindowError.setWindowTitle('Ошибка')
                        modalWindowError.setFixedSize(300, 250)
                        modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                        modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                        modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                        modalWindowError.move(modalWindowAddQuest.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                        
                        label_of_error = QtWidgets.QLabel('Заполните все ячейки', modalWindowError)
                        label_of_error.move(80, 100)
                        
                    
                        
                        btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                        btn_ok.move(80, 200)
                        btn_ok.clicked.connect(modalWindowError.close)
                        modalWindowError.show()
                        var_for_pass_1 = False
                        break
                    var_for_pass_1 = True
                    
                list_for_radio_btn_check_or_no = []        
                for two in list_of_all_radiobtn:
                    if two.isChecked() == False:
                        list_for_radio_btn_check_or_no.append(False)
                    elif two.isChecked():
                        list_for_radio_btn_check_or_no.append(True)
                if True not in list_for_radio_btn_check_or_no and modalWindowError.isHidden() == True:
                    
                    #modalWindowErrorChoose = QtWidgets.QWidget(modalWindowAddQuest, QtCore.Qt.Window)
                    modalWindowErrorChoose.setWindowTitle('Ошибка')
                    modalWindowErrorChoose.setFixedSize(300, 250)
                    modalWindowErrorChoose.setWindowFlags(QtCore.Qt.Dialog)
                    modalWindowErrorChoose.setWindowModality(QtCore.Qt.WindowModal)
                    modalWindowErrorChoose.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                    modalWindowErrorChoose.move(modalWindowAddQuest.geometry().center() - modalWindowErrorChoose.rect().center() - QtCore.QPoint(4, 30))
                    
                    label_of_error_choose = QtWidgets.QLabel('Выберите правильный ответ', modalWindowErrorChoose)
                    label_of_error_choose.move(80, 100)
                    
                    btn_ok_choose = QtWidgets.QPushButton('Ок', modalWindowErrorChoose)
                    btn_ok_choose.move(80, 200)
                    btn_ok_choose.clicked.connect(modalWindowErrorChoose.close)
                    var_for_pass_2 = False
                    modalWindowErrorChoose.show()
                    #break
                if field_of_create_quest.toPlainText().strip() in ultra_dict[var_for_subj][var_for_theme].keys() and modalWindowError.isHidden() == True and modalWindowErrorChoose.isHidden() == True :
                    modalWindowErrorChoose = QtWidgets.QWidget(modalWindowAddQuest, QtCore.Qt.Window)
                    modalWindowErrorChoose.setWindowTitle('Ошибка')
                    modalWindowErrorChoose.setFixedSize(300, 250)
                    modalWindowErrorChoose.setWindowFlags(QtCore.Qt.Dialog)
                    modalWindowErrorChoose.setWindowModality(QtCore.Qt.WindowModal)
                    modalWindowErrorChoose.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                    modalWindowErrorChoose.move(modalWindowAddQuest.geometry().center() - modalWindowErrorChoose.rect().center() - QtCore.QPoint(4, 30))
                    
                    label_of_error_choose = QtWidgets.QLabel('Такой вопрос уже существует.', modalWindowErrorChoose)
                    label_of_error_choose.move(80, 100)
                    
                    btn_ok_choose = QtWidgets.QPushButton('Ок', modalWindowErrorChoose)
                    btn_ok_choose.move(80, 200)
                    btn_ok_choose.clicked.connect(modalWindowErrorChoose.close)
                    var_for_pass_3 = False
                    modalWindowErrorChoose.show()
                
                setArr = set(list_of_questions_test_field)
                
                if len(list_of_questions_test_field) != len(setArr) and modalWindowError.isHidden() == True and modalWindowErrorChoose.isHidden() == True :
                    
                    modalWindowError.setWindowTitle('Ошибка')
                    modalWindowError.setFixedSize(300, 250)
                    modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                    modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                    modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                    modalWindowError.move(modalWindowAddQuest.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                    
                    label_of_error = QtWidgets.QLabel('Невозможно сохранить одинаковые ответы.', modalWindowError)
                    label_of_error.move(20, 100)
                    
                
                    
                    btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                    btn_ok.move(80, 200)
                    btn_ok.clicked.connect(modalWindowError.close)
                    modalWindowError.show()
                    var_for_pass_4 = False
                
                for subj in ultra_dict:
                    for theme in ultra_dict[subj]:
                        for quest in ultra_dict[subj][theme]:
                            if field_of_create_quest.toPlainText() == quest and modalWindowError.isHidden() == True and modalWindowErrorChoose.isHidden() == True:
                                var_for_pass_5 = False
                                modalWindowError.setWindowTitle('Ошибка')
                                modalWindowError.setFixedSize(300, 250)
                                modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                                modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                                modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                                modalWindowError.move(modalWindowAddQuest.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                                
                                label_of_error = QtWidgets.QLabel('Невозможно сохранить вопрос,\n так как такой же вопрос есть в другом тесте.', modalWindowError)
                                label_of_error.move(20, 100)
                                
                            
                                
                                btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                                btn_ok.move(80, 200)
                                btn_ok.clicked.connect(modalWindowError.close)
                                modalWindowError.show()
                
                if var_for_pass_1 and var_for_pass_2 and var_for_pass_3 and var_for_pass_4 and var_for_pass_5:        
                    
                    var_for_index = 0
                    for index_checked_btn in list_of_all_radiobtn:
                        if index_checked_btn.isChecked():
                            var_for_index = list_of_all_radiobtn.index(index_checked_btn) 
                    new_list_of_clear_elems = []
                    for elem in list_of_questions_test_field:
                        elem_for_new_list = elem.strip()
                        new_list_of_clear_elems.append(elem_for_new_list)
                    list_of_questions_test_field = new_list_of_clear_elems
                    list_of_questions_test_field[var_for_index] += ' '
                    
                    create_quest_answ_dict = {field_of_create_quest.toPlainText() : list_of_answers_text_field}
                    

                    ultra_dict[var_for_subj][var_for_theme][field_of_create_quest.toPlainText()] = list_of_questions_test_field
                    
                    with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                        file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                    modalWindowAddQuest.close()
                    modalWindowEdit.close()
                    list_for_pressed_btn_for_repaint[0].setChecked(True)
                    self.click_theme_start_edit()
                    #break
                        
            save_new_quest = QtWidgets.QPushButton('Сохранить вопрос', modalWindowAddQuest)
            save_new_quest.clicked.connect(final_save_new_quest)
            save_new_quest.resize(150, 50)
            save_new_quest.move(270, 360)
            
            cancel_create_quest = QtWidgets.QPushButton('Отмена', modalWindowAddQuest)
            cancel_create_quest.clicked.connect(modalWindowAddQuest.close)
            cancel_create_quest.resize(150, 50)
            cancel_create_quest.move(80, 360)
            
                    
            modalWindowAddQuest.show()
            
        def saver_all_mod_win():
            with open('database.json', 'r',encoding="utf-8", ) as file_db:
                ultra_dict = json.load(file_db)
            
            list_for_new_clear_list = []
            list_for_quest_to_delete = []
            list_for_true_fields = []
            
            copy_of_ultra_dict = copy.deepcopy(ultra_dict)
            # проверка заполненности всех полей
            for elem in list_of_text_field_answers:
                
                if bool(elem.toPlainText().strip()) == False:
                    
                    list_for_true_fields.append(False)
                    modalWindowError = QtWidgets.QWidget(modalWindowEdit, QtCore.Qt.Window)
                    modalWindowError.setWindowTitle('Ошибка')
                    modalWindowError.setFixedSize(300, 250)
                    modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                    modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                    modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                    modalWindowError.move(modalWindowEdit.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                    
                    label_of_error = QtWidgets.QLabel('Заполните все поля ответов ', modalWindowError)
                    label_of_error.move(80, 100)
                    
                    btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                    btn_ok.move(80, 200)
                    btn_ok.clicked.connect(modalWindowError.close)
                    modalWindowError.show()
                    break
                elif bool(elem.toPlainText().strip()) == True:
                    list_for_true_fields.append(True)
            
            for subj in ultra_dict:
                list_of_subj = [subj for subj in ultra_dict]
                list_of_subj_2 = [subj for subj in ultra_dict]
                list_of_subj_2.remove(text_of_subj_before_edit)
                list_of_subj_2.append(field_of_subj.toPlainText().rstrip())
                set_1 = set(list_of_subj_2)
                if len(list_of_subj) != len(set_1):
                    list_for_true_fields.append(False)
                    modalWindowError = QtWidgets.QWidget(modalWindowEdit, QtCore.Qt.Window)
                    modalWindowError.setWindowTitle('Ошибка')
                    modalWindowError.setFixedSize(300, 250)
                    modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                    modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                    modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                    modalWindowError.move(modalWindowEdit.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                    
                    label_of_error = QtWidgets.QLabel('Невозможно сохранить вопрос,\n так как такой предмет уже существует.', modalWindowError)
                    label_of_error.move(20, 100)

                    btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                    btn_ok.move(80, 200)
                    btn_ok.clicked.connect(modalWindowError.close)
                    modalWindowError.show()
                    break
                list_of_theme_1 = []
                list_of_theme_2 = []
                for theme in ultra_dict[subj]:
                    for subj in list_of_subj:
                        for theme in ultra_dict[subj]:
                            list_of_theme_1.append(theme)
                            list_of_theme_2.append(theme)
                    #list_of_theme = [theme for theme in [subj for subj in ultra_dict]]
                    #print(list_of_theme_1)
                    #print(1)
                    list_of_theme_2.remove(text_of_theme_before_edit)
                    list_of_theme_2.append(field_of_theme.toPlainText().rstrip())
                    #if len(list_of_theme_1) != len(set(list_of_theme_2)):
                       # print('Такая тема уже есть')
                    #list_of_theme_2 = [theme for theme in ultra_dict[subj]]
                    #list_of_theme_2.remove(text_of_theme_before_edit)
                    #list_of_theme_2.append(field_of_theme.toPlainText().rstrip())
                    #set_2 = set(list_of_theme_2)
                    if len(list_of_theme_1) != len(set(list_of_theme_2)):
                         
                    #field_of_theme.toPlainText().rstrip() == theme and theme not in ultra_dict[subj]:
                        #len(list_of_theme) != len(set_2):
                        #field_of_theme.toPlainText().rstrip() == theme and theme not in ultra_dict[subj]:
                        list_for_true_fields.append(False)
                        modalWindowError = QtWidgets.QWidget(modalWindowEdit, QtCore.Qt.Window)
                        modalWindowError.setWindowTitle('Ошибка')
                        modalWindowError.setFixedSize(300, 250)
                        modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                        modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                        modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                        modalWindowError.move(modalWindowEdit.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                        
                        label_of_error = QtWidgets.QLabel('Невозможно сохранить вопрос,\n так как такая же тема есть в другом тесте.', modalWindowError)
                        label_of_error.move(20, 100)

                        btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                        btn_ok.move(80, 200)
                        btn_ok.clicked.connect(modalWindowError.close)
                        modalWindowError.show()
                        break
                    
                    for new_quest in list_of_all_quest_field:
                        try:
                            for quest in ultra_dict[subj][theme]:
                                if new_quest.toPlainText().rstrip() == quest.rstrip() and theme.rstrip() != var_for_theme.rstrip():
                                    list_for_true_fields.append(False)
                                    modalWindowError = QtWidgets.QWidget(modalWindowEdit, QtCore.Qt.Window)
                                    modalWindowError.setWindowTitle('Ошибка')
                                    modalWindowError.setFixedSize(300, 250)
                                    modalWindowError.setWindowFlags(QtCore.Qt.Dialog)
                                    modalWindowError.setWindowModality(QtCore.Qt.WindowModal)
                                    modalWindowError.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
                                    modalWindowError.move(modalWindowEdit.geometry().center() - modalWindowError.rect().center() - QtCore.QPoint(4, 30))
                                    
                                    label_of_error = QtWidgets.QLabel('Невозможно сохранить вопрос,\n так как такой же вопрос есть в другом тесте.', modalWindowError)
                                    label_of_error.move(20, 100)
                                    
                                
                                    
                                    btn_ok = QtWidgets.QPushButton('Ок', modalWindowError)
                                    btn_ok.move(80, 200)
                                    btn_ok.clicked.connect(modalWindowError.close)
                                    modalWindowError.show()
                                    break
                            
                                break
                        except:
                            None
                        break
                    
                    break
                break
            if False not in list_for_true_fields:
                # Вот тут создать новый словарь и записать вместо старого
                new_theme_dict = {}
                list_for_text_of_question = []
                list_for_text_of_answers = []
                
                for button_1 in list_for_subj_buttons:
                    if button_1.isChecked():
                        name_of_theme = field_of_theme.toPlainText()
                        #бесполезно? 
                        for quest in list_of_all_quest_field:
                            list_for_text_of_question.append(quest.toPlainText())
                       
                        
                        new_test_list = copy.copy(list_for_text_of_question)
                        try:
                            new_test_list.pop()
                        except:
                            None
                        ###    
                        list_for_index_radio = []
                      
                        list_for_doing_final_list = copy.copy(list_of_text_field_answers)
                        list_for_index_true_false_radio = copy.copy(list_of_all_radiobtn)

                        for elem in range(len(list_for_text_of_question)):
                            list_for_add = []
                            list_for_radio = []
                            
                            list_for_add.append(list_of_text_field_answers.pop(0).toPlainText())
                            list_for_add.append(list_of_text_field_answers.pop(0).toPlainText())
                            list_for_add.append(list_of_text_field_answers.pop(0).toPlainText())
                            list_for_add.append(list_of_text_field_answers.pop(0).toPlainText())
                            
                            list_for_text_of_answers.append(list_for_add)
                            
                            
                            list_for_radio.append(list_for_index_true_false_radio.pop(0).isChecked())
                            list_for_radio.append(list_for_index_true_false_radio.pop(0).isChecked())
                            list_for_radio.append(list_for_index_true_false_radio.pop(0).isChecked())
                            list_for_radio.append(list_for_index_true_false_radio.pop(0).isChecked())
                            
                            list_for_index_radio.append(list_for_radio)
                            
                        for radio_list in list_for_index_radio:
                            for radio in radio_list:
                                if radio == True:
                                    local_index = radio_list.index(radio)
                                    nonlocal_index = list_for_index_radio.index(radio_list)
                                    list_for_text_of_answers[nonlocal_index][local_index] += ' '
                        dict_quest_answ = {}
                        for quest_field in list_of_all_quest_field:
                            dict_quest_answ[quest_field.toPlainText()] = list_for_text_of_answers[list_of_all_quest_field.index(quest_field)]
                        dict_theme_quests_answ = {}
                        dict_theme_quests_answ[field_of_theme.toPlainText().rstrip()] = dict_quest_answ
                        new_theme_text = field_of_theme.toPlainText().rstrip()
                        list_of_themes = list(ultra_dict[var_for_subj].keys())
                        list_of_values_themes = list(ultra_dict[var_for_subj].values())
                       # print(list_of_values_themes)
                        #print(list_of_themes)
                        theme_index_in_global_dict = list_of_themes.index(list_for_field_of_theme[0])
                        
                        new_final_dict = {}
                        for x in range(len(list_of_themes)):
                            if x == theme_index_in_global_dict:
                                new_final_dict[new_theme_text] = dict_quest_answ
                            else:
                                new_final_dict[list_of_themes[x]] = list_of_values_themes[x]
                        #text_of_subj_before_edit
                        ultra_keys = list(ultra_dict.keys())
                        ultra_values = list(ultra_dict.values())
                        ultra_index = ultra_keys.index(text_of_subj_before_edit)
                        #print(ultra_index)
                        total_new_dict = {}
                        for x in range(len(ultra_keys)):
                            if x == ultra_index:
                                total_new_dict[field_of_subj.toPlainText().rstrip()] = new_final_dict
                            else:
                                total_new_dict[ultra_keys[x]] = ultra_values[x]
                        
                        #ultra_dict[var_for_subj] = new_final_dict
                        ultra_dict = total_new_dict
                        #print(ultra_dict)
                        with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                            file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                        modalWindowEdit.close()
                        
                        #btn_subj_index = 0
                        for btn_subj in list_for_subj_buttons:
                            if btn_subj.isChecked():
                                btn_subj_index = list_for_subj_buttons.index(btn_subj)
                        
                        self.creator_subj_buttons()
                        #list_for_subj_buttons[btn_subj_index].setChecked(True)
                        #click_subj_choose_themes_local_for_add_theme()
                        self.creator_theme_buttons()
                        list_for_subj_buttons[btn_subj_index].click()
                        #click_theme_start_edit()
                # Реализует удаление вопроса по пустому имени? 
                '''
                for quest in list_of_all_quest_field:
                    if bool(quest.toPlainText().strip()) == True:
                        if quest.toPlainText().strip() in copy_of_ultra_dict[var_for_subj][var_for_theme]:
                            None
                            
                        else:
                           
                            break
                    elif bool(quest.toPlainText().strip()) == False:
                       
                        index_for_delete = list_of_all_quest_field.index(quest) 
                        
                        quest_to_delete = list(copy_of_ultra_dict[var_for_subj][var_for_theme].keys())[index_for_delete]
                        list_for_quest_to_delete.append(quest_to_delete)
                        modalWindowEdit.close()
                        
                 '''   
                
           
        def deleter_theme():
            
            modalWindowWarning = QtWidgets.QWidget(modalWindowEdit, QtCore.Qt.Window)
            modalWindowWarning.setWindowTitle('Внимание')
            modalWindowWarning.setFixedSize(300, 250)
            modalWindowWarning.setWindowFlags(QtCore.Qt.Dialog)
            modalWindowWarning.setWindowModality(QtCore.Qt.WindowModal)
            modalWindowWarning.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
            modalWindowWarning.move(modalWindowEdit.geometry().center() - modalWindowWarning.rect().center() - QtCore.QPoint(4, 30))
            
            label_of_warning = QtWidgets.QLabel('Вы уверены, что хотите удалить тему?', modalWindowWarning)
            label_of_warning.move(40, 100)
            
            def final_delete():
                copy_of_ultra_dict = copy.deepcopy(ultra_dict)
               
                copy_of_ultra_dict[var_for_subj].pop(var_for_theme)
                
                with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                    file_1.write(json.dumps(copy_of_ultra_dict, ensure_ascii = False))
                for btn_theme in list_for_theme_buttons:
                    
                    btn_theme.hide()
                
                
                self.creator_theme_buttons()
                
                self.click_subj_choose_themes_local_for_add_theme()
                modalWindowEdit.close()
                
            
            def cancel_delete():
                modalWindowWarning.close()
            
            btn_delete = QtWidgets.QPushButton('Да', modalWindowWarning)
            btn_delete.move(40, 200)
            btn_delete.clicked.connect(final_delete)
            
            btn_cancel = QtWidgets.QPushButton('Нет', modalWindowWarning)
            btn_cancel.move(150, 200)
            btn_cancel.clicked.connect(cancel_delete)
            modalWindowWarning.show()
            
            

            
        add_quest_btn = QtWidgets.QPushButton('Добвить вопрос', modalWindowEdit)
        add_quest_btn.setToolTip('here')
        add_quest_btn.clicked.connect(creator_mod_win_adder_quest)
        add_quest_btn.resize(150, 50)
        add_quest_btn.move(50, 700)
        
        save_all_btn = QtWidgets.QPushButton('Сохранить', modalWindowEdit)
        save_all_btn.clicked.connect(saver_all_mod_win)
        save_all_btn.resize(150, 50)
        save_all_btn.move(400, 700)
        
        
        delete_theme_btn = QtWidgets.QPushButton('Удалить тему', modalWindowEdit)
        delete_theme_btn.clicked.connect(deleter_theme)
        delete_theme_btn.resize(150, 50)
        delete_theme_btn.move(750, 700)
        for btn in list_for_theme_buttons:
            btn.setChecked(False)        
        modalWindowEdit.show()




    def creator_theme_buttons(self):
        
        #list_for_theme_buttons.clear()
        global dict_for_theme_btn_textofbtn_and_label
        dict_for_theme_btn_textofbtn_and_label = {}
        
        for last_btn in list_for_theme_buttons:
            last_btn.hide()
        list_for_theme_buttons.clear()
        with open('database.json', 'r', encoding="utf-8") as file_db:
            ultra_dict = json.load(file_db)
        
        ultra_mainbox_for_theme = QtWidgets.QWidget(self)
        
        scrollArea_for_theme = QtWidgets.QScrollArea()
        widget_for_theme = QtWidgets.QWidget()
        widget_for_theme.resize(460, 1000)
        #widget_for_theme.setFixedSize(400, 250)
       # widget_for_theme.move(522, 557)
        #btn_test = QtWidgets.QPushButton('Добавить предмет', widget_for_theme)
        #widget_for_theme.show()
        vbox_for_theme = QtWidgets.QVBoxLayout()

        for name in ultra_dict.keys():
            #print(name)
            x_coord_for_btn_theme = 150
            #widget_for_theme = QtWidgets.QWidget()
            #widget_for_theme.resize(400, 500)
            for one in ultra_dict[name]:
                
                hbox_for_cycle_theme = QtWidgets.QHBoxLayout()
                
                button_of_theme = QtWidgets.QPushButton(str(one), widget_for_theme)#self
                font_obj_for_btn = QtGui.QFont('Segoe UI', pointSize = 10)
                button_of_theme.setFont(font_obj_for_btn)
                label_of_theme_for_btn = QtWidgets.QLabel(button_of_theme)
                label_of_theme_for_btn.setWordWrap(True)
                hboxlayout = QtWidgets.QHBoxLayout(button_of_theme)
                hboxlayout.addWidget(label_of_theme_for_btn)
                
                button_of_theme.setCheckable(True)
                button_of_theme.clicked.connect(self.click_theme_start_edit)
             #   button_of_theme.move(550, x_coord_for_btn_theme)
                button_of_theme.setFixedSize(418, 101)
                button_of_theme.hide()
                
                #hbox_for_cycle_theme.addWidget(button_of_theme)
                #vbox_for_theme.addLayout(hbox_for_cycle_theme)
                vbox_for_theme.addWidget(button_of_theme,stretch = 10, alignment = QtCore.Qt.AlignTop)
                list_for_theme_buttons.append(button_of_theme)
                
                dict_for_theme_btn_textofbtn_and_label[button_of_theme] = [button_of_theme.text(), label_of_theme_for_btn]

                x_coord_for_btn_theme += 50 
            #vbox_for_theme.addSpacing(100)
        widget_for_theme.setLayout(vbox_for_theme)
        scrollArea_for_theme.setWidget(widget_for_theme)
        scrollArea_for_theme.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        
        
        mainbox_for_theme = QtWidgets.QVBoxLayout()
        
        #mainbox_for_theme.setFixedSize(400, 400)
        mainbox_for_theme.addWidget(scrollArea_for_theme)#, alignment = QtCore.Qt.AlignTop)
        #mainbox_for_theme.addSpacing(500)
        #self.setLayout(mainbox_for_theme)
        ultra_mainbox_for_theme.setLayout(mainbox_for_theme)
        ultra_mainbox_for_theme.move(509, 146)
        ultra_mainbox_for_theme.setFixedSize(513, 614)
        ultra_mainbox_for_theme.show()
        #mainbox.addSpacing(50)
        #modalWindowEdit.setLayout(mainbox)
#class mod_win_append_subj(MainCodeClass):
    #print(1)
   # labels(window)
   # buttons(window)
   # creator_subj_buttons()
   # creator_theme_buttons()
   # window.show()
   # sys.exit(app.exec_())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    smth = MainCodeClass()
    sys.exit(app.exec_())
#MainCodeClass()
