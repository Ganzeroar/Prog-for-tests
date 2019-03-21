import sys
import json
import time
import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


app = QtWidgets.QApplication(sys.argv)   
window = QtWidgets.QWidget()
window.setWindowTitle('Редактирование')
window.setFixedSize(1024, 758)

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
list_of_checked_subj_button_for_edit = []
list_for_checked_subj_button = []
list_for_subj_buttons = []
list_for_theme_buttons = []
list_of_subj_buttons_for_edit = []
list_of_theme_buttons_for_edit = []


dict_for_theme_btn_textofbtn_and_label = {}



def labels(window):
    label_subject = QtWidgets.QLabel("Выбор предмета", window)
    label_subject.move(230, 100)
    label_subject.show()
    label_theme = QtWidgets.QLabel("Выбор темы", window)
    label_theme.move(650, 100)
    label_theme.show()

def buttons(window):
    try:
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
    except:
        None    
    
    btn_add_subject = QtWidgets.QPushButton('Добавить предмет', window)
    font_obj_for_btn_add_subject = QtGui.QFont('times new roman',pointSize = 10)
    btn_add_subject.setFont(font_obj_for_btn_add_subject)
    btn_add_subject.move(340, 90)
    btn_add_subject.setFixedSize(150, 50)
    btn_add_subject.clicked.connect(mod_win_append_subj)
    btn_add_subject.show() 

    global btn_add_theme
    btn_add_theme = QtWidgets.QPushButton('Добавить тему', window)
    btn_add_theme.move(760, 90)
    btn_add_theme.setFixedSize(150, 50)
    btn_add_theme.clicked.connect(mod_win_append_theme)
    btn_add_theme.hide()

    global btn_for_delete_subj
    btn_for_delete_subj = QtWidgets.QPushButton('Удалить выбранный предмет', window)
    btn_for_delete_subj.setFixedSize(200, 50)
    btn_for_delete_subj.move(50,50)
    btn_for_delete_subj.clicked.connect(final_deleter_subj)
    btn_for_delete_subj.hide()
    
 

def final_deleter_subj():
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
                

def mod_win_append_theme():
    with open('database.json', 'r',encoding="utf-8", ) as file_db:
        ultra_dict = json.load(file_db)
    modalWindowAppTheme = QtWidgets.QWidget(window, QtCore.Qt.Window)
    modalWindowAppTheme.setWindowTitle("Добавление темы")
    modalWindowAppTheme.setFixedSize(400, 400)
    modalWindowAppTheme.setWindowFlags(QtCore.Qt.Dialog)
    
    modalWindowAppTheme.setWindowModality(QtCore.Qt.WindowModal)
    modalWindowAppTheme.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindowAppTheme.move(window.geometry().center() - modalWindowAppTheme.rect().center() - QtCore.QPoint(4, 30))
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
        if bool(name_theme.toPlainText().strip()) != True:
            
            modalWindowError = QtWidgets.QWidget(modalWindowAppTheme, QtCore.Qt.Window)
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
            
        elif string_name_theme in ultra_dict[name_of_subj].keys():
            
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
            creator_theme_buttons()
           
            click_subj_choose_themes_local_for_add_theme()
            modalWindowAppTheme.close()
        
    btn_exit.clicked.connect(cancel_add_theme)
        
    btn_save_subj = QtWidgets.QPushButton('Сохранить', modalWindowAppTheme)
    btn_save_subj.move(200, 350)
    btn_save_subj.clicked.connect(save_name_theme)
    
    
    modalWindowAppTheme.show()

def mod_win_append_subj():
    with open('database.json', 'r',encoding="utf-8", ) as file_db:
        ultra_dict = json.load(file_db)
    modalWindowAppSubj = QtWidgets.QWidget(window, QtCore.Qt.Window)
    modalWindowAppSubj.setWindowTitle("Добавление предмета")
    modalWindowAppSubj.setFixedSize(400, 400)
    modalWindowAppSubj.setWindowFlags(QtCore.Qt.Dialog)
    
    modalWindowAppSubj.setWindowModality(QtCore.Qt.WindowModal)
    modalWindowAppSubj.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindowAppSubj.move(window.geometry().center() - modalWindowAppSubj.rect().center() - QtCore.QPoint(4, 30))
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

var_for_number_index_of_checked_button = 0

def click_subj_choose_themes_local_for_add_theme():
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




list_for_text_of_btn_for_wrap = []
list_for_changed_btn_for_text_wrap = []
dict_of_btn_label_for_text_wrap = {}



def click_subj_choose_themes():
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


def creator_subj_buttons():
    for btn in list_for_subj_buttons:
        btn.hide()
    try:
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
    except:
        None
    for btn in list_for_subj_buttons:
        btn.destroy()
        
    list_for_subj_buttons.clear()
    x_coord_for_btn_subj = 150
    # Создаёт кнопки предметов 
    
    for subj in ultra_dict.items():
        
        button_of_subject = QtWidgets.QPushButton(str(subj[0]), window)
        button_of_subject.setCheckable(True)
        button_of_subject.clicked.connect(click_subj_choose_themes)
        button_of_subject.move(130, x_coord_for_btn_subj)
        button_of_subject.setFixedSize(300, 50)
        button_of_subject.setStyleSheet("QPushButton {white-space: pre-line;}")
        button_of_subject.show()
        list_for_subj_buttons.append(button_of_subject)
        x_coord_for_btn_subj += 50   


list_for_text_of_dict_of_btn = []
def click_theme_start_edit():
    
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
    
    modalWindowEdit = QtWidgets.QWidget(window, QtCore.Qt.Window)
    modalWindowEdit.setWindowTitle('Редактирование')
    modalWindowEdit.setFixedSize(1024, 758)
    modalWindowEdit.setWindowFlags(QtCore.Qt.Dialog)
    modalWindowEdit.setWindowModality(QtCore.Qt.WindowModal)
    modalWindowEdit.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindowEdit.move(window.geometry().center() - modalWindowEdit.rect().center() - QtCore.QPoint(4, 30))
    
    scrollArea = QtWidgets.QScrollArea()
    widget = QtWidgets.QWidget()
    
    
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
            hbox_1.addWidget(field_of_subj)
            vbox.addLayout(hbox_1)
            
            label_theme = QtWidgets.QLabel('Название темы: ', widget)
            hbox_2.addWidget(label_theme)
            
            field_of_theme = QTextEdit(str(dict_for_theme_btn_textofbtn_and_label[button][0]), widget)
            field_of_theme.setFixedSize(300, 50)
            list_for_field_of_theme.append(field_of_theme.toPlainText())
            hbox_2.addWidget(field_of_theme)
            vbox.addLayout(hbox_2)
            
            
            list_of_questions = []
            list_for_answers = []
            
            
            
            for subject in ultra_dict.keys():
                try:
                    for theme_2 in dict_for_theme_btn_textofbtn_and_label:

                        if dict_for_theme_btn_textofbtn_and_label[button][0] == dict_for_theme_btn_textofbtn_and_label[theme_2][0]:

                            var_for_subj = subject
                            var_for_theme = dict_for_theme_btn_textofbtn_and_label[theme_2][0]

                            dict_of_questions = ultra_dict[subject][dict_for_theme_btn_textofbtn_and_label[theme_2][0]]
                            
                            for quests in dict_of_questions.keys():
                                list_of_questions.append(quests)
                                local_answ_list = []
                                for answer in dict_of_questions[quests]:
                                    local_answ_list.append(answer)
                                list_for_answers.append(local_answ_list)

                    break
                        
                except:
                    None
                
           # hbox_for_add_1 = QtWidgets.QHBoxLayout()
           # hbox_for_add_2 = QtWidgets.QHBoxLayout()
           # hbox_for_add_3 = QtWidgets.QHBoxLayout()
           # hbox_for_add_4 = QtWidgets.QHBoxLayout()
           # hbox_for_add_5 = QtWidgets.QHBoxLayout()
            
           # hbox_for_empty_answ_1 = QtWidgets.QHBoxLayout()
           # hbox_for_empty_answ_2 = QtWidgets.QHBoxLayout()
           # hbox_for_empty_answ_3 = QtWidgets.QHBoxLayout()
           # hbox_for_empty_answ_4 = QtWidgets.QHBoxLayout()
            
            for num in range(1,len(list_of_questions)+1):
                print(1)

                #Убрать ненужные боксы
                hbox_for_cycle_1 = QtWidgets.QHBoxLayout()
                hbox_for_cycle_2 = QtWidgets.QHBoxLayout()
                hbox_for_cycle_3 = QtWidgets.QHBoxLayout()
              #  hbox_for_cycle_4 = QtWidgets.QHBoxLayout()
              #  hbox_for_cycle_5 = QtWidgets.QHBoxLayout()
              #  hbox_for_cycle_6 = QtWidgets.QHBoxLayout()
                
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
                
                hbox_for_cycle_1.addWidget(label_of_quest)
                hbox_for_cycle_1.addWidget(field_of_quest)
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
                # на самом деле поля ответов? 
                
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
                    if answ_for_check[-1] == ' ':
                        list_of_all_radiobtn[list_of_answers_text_field.index(answ_for_check)].setChecked(True)
                
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
            
            modalWindowError = QtWidgets.QWidget(modalWindowAddQuest, QtCore.Qt.Window)
            modalWindowErrorChoose = QtWidgets.QWidget(modalWindowAddQuest, QtCore.Qt.Window)
            for one in list_of_all_text_field:
                
                if bool(one.toPlainText().strip()) != True:
                    #modalWindowError = QtWidgets.QWidget(modalWindowAddQuest, QtCore.Qt.Window)
                    modalWindowError.setWindowTitle('Ошибка')
                    modalWindowError.setFixedSize(300, 250)
                    
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
            
            if var_for_pass_1 and var_for_pass_2 and var_for_pass_3 and var_for_pass_4:        
                
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
                

                ultra_dict[var_for_subj][var_for_theme][field_of_create_quest.toPlainText()] = list_of_answers_text_field
                with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                    file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
                modalWindowAddQuest.close()
                modalWindowEdit.close()
                list_for_pressed_btn_for_repaint[0].setChecked(True)
                click_theme_start_edit()
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
                        
            # Реализует удаление вопроса по пустому имени? 
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
            
            
            creator_theme_buttons()
            
            click_subj_choose_themes_local_for_add_theme()
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




def creator_theme_buttons():
    list_for_theme_buttons.clear()
    global dict_for_theme_btn_textofbtn_and_label
    dict_for_theme_btn_textofbtn_and_label = {}
    
    for last_btn in list_for_theme_buttons:
        last_btn.hide()
    
    with open('database.json', 'r', encoding="utf-8") as file_db:
        ultra_dict = json.load(file_db)
    
    for name in ultra_dict.keys():
        x_coord_for_btn_theme = 150
        
        for one in ultra_dict[name]:
            

            button_of_theme = QtWidgets.QPushButton(str(one), window)

            label_of_theme_for_btn = QtWidgets.QLabel(button_of_theme)
            label_of_theme_for_btn.setWordWrap(True)
            hboxlayout = QtWidgets.QHBoxLayout(button_of_theme)
            hboxlayout.addWidget(label_of_theme_for_btn)
            
            button_of_theme.setCheckable(True)
            button_of_theme.clicked.connect(click_theme_start_edit)
            button_of_theme.move(550, x_coord_for_btn_theme)
            button_of_theme.setFixedSize(300, 50)
            button_of_theme.hide()

            list_for_theme_buttons.append(button_of_theme)
            
            dict_for_theme_btn_textofbtn_and_label[button_of_theme] = [button_of_theme.text(), label_of_theme_for_btn]

            x_coord_for_btn_theme += 50 
    


labels(window)
buttons(window)
creator_subj_buttons()
creator_theme_buttons()
window.show()
sys.exit(app.exec_())

