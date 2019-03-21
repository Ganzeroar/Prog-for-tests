import sys
import json
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class MainCode(QWidget):
   
    def __init__(self, parent=None):
        super(MainCode, self).__init__(parent)
        self.initUI()
        #словарь с базой данных
        
        global ultra_dict
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
             
    def initUI(self):
        # запускает функции создания кнопок, задаёт размеры окна
        #print(self)
        self.buttons()
        self.labels()
        self.resize(1024, 768) #geometry(300, 300, 280, 270)
        self.setWindowTitle('Программа для тестов ')
        self.show()
        
    def labels(self):
        # создаёт лейблы в окнах выбора темы и редактирования
        self.label_subject = QtWidgets.QLabel("Выбор предмета", self)
        self.label_subject.move(230, 100)
        self.label_subject.hide()
        self.label_theme = QtWidgets.QLabel("Выбор темы", self)
        self.label_theme.move(650, 100)
        self.label_theme.hide()
        
                
    def buttons(self):
        #######################3
        # УДАЛИТЬ КНОПКИ ПО ВЫЗОВУ, ЧТО БЫ ПРИ ВЫЗОВЕ ВСЁ УДАЛЯЛОСЬ, А ЗАТЕМ СОЗДАВАЛОСЬ ЗАНОВО
        ##########################333
        # создаёт кнопки
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
            ultra_dict = json.load(file_db)
        
        global list_for_subj_buttons
        global list_for_theme_buttons
        global list_of_subj_buttons_for_edit
        global list_of_theme_buttons_for_edit
        global list_for_checked_subj_button
        global list_of_checked_subj_button_for_edit
        list_of_checked_subj_button_for_edit = []
        list_for_checked_subj_button = []
        list_for_subj_buttons = []
        list_for_theme_buttons = []
        list_of_subj_buttons_for_edit = []
        list_of_theme_buttons_for_edit = []
        #метод с созданием всего, а затем с показыванием и скрыванем работает
        #  по крайней мере с кнопками
        
        
      
        # кнопка в редактировании
        self.btn_add_subject = QtWidgets.QPushButton('Добавить предмет', self)
        self.btn_add_subject.move(340, 90)
        self.btn_add_subject.setFixedSize(150, 50)
        self.btn_add_subject.clicked.connect(self.mod_win_append_subj)
        self.btn_add_subject.hide() 
    
         
        self.button_back_to_main_menu = QtWidgets.QPushButton('Назад', self)
        self.button_back_to_main_menu.move(150, 50)
        self.button_back_to_main_menu.clicked.connect(self.click_back_1)
        self.button_back_to_main_menu.hide()
        
        
        
        self.button_choose_test = QtWidgets.QPushButton('Выбор темы ',self)
        #self.button_choose_test.setFont(pointSize = 10)
        #self.button_choose_test.setText('Выбор темы, {font-size:xx_large;}')
        self.button_choose_test.setFixedSize(300, 100)
        self.button_choose_test.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 50px 50px 50px 50px;}"
                           "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_choose_test.clicked.connect(self.click_but_choose)
        
        
        
        ############################
        # Совместить вторую часть программы с этой кнопкой
        ############################
        self.button_edit = QtWidgets.QPushButton('Редактирование', self)
        self.button_edit.setFixedSize(300,100)
        self.button_edit.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 50px 50px 50px 50px;}"
                           "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.button_edit.clicked.connect(self.click_but_edit)
        self.button_edit.hide()
        
        #def click_btn_of_udp_and_rpt(self):
        #    creating_btn_of_theme_for_edit_and_push_in_list(self) 

        #self.button_of_update_and_repaint = QtWidgets.QPushButton('Обновить', self)
        #self.button_of_update_and_repaint.move(600, 50)
        #self.button_of_update_and_repaint.setFixedSize(100,50)
        #self.button_of_update_and_repaint.clicked.connect(click_btn_of_udp_and_rpt)
        
        
        
        
        
        # Создание кнопок предметов и обработчик нажатия на кнопки
        
        def click_subj_choose_themeS(self):
            for btn in list_for_checked_subj_button:
                btn.setChecked(False)
                list_for_checked_subj_button.pop()
            for h in list_for_theme_buttons:
                h.hide()
            for button_1 in list_for_subj_buttons:
                if button_1.isChecked():
                    list_for_checked_subj_button.append(button_1)
                    for y in list_for_theme_buttons:
                        if y.text() in ultra_dict[button_1.text()]:
                            y.show()

        
        x_coord_for_btn_subj = 150
        # Создаёт кнопки предметов 
        for x in ultra_dict.items():
            self.button_of_subject = QtWidgets.QPushButton(str(x[0]), self)
            self.button_of_subject.setCheckable(True)
            # поправить имя функции-обработчика
            self.button_of_subject.clicked.connect(click_subj_choose_themeS)
            self.button_of_subject.move(230, x_coord_for_btn_subj)
            self.button_of_subject.hide()
            list_for_subj_buttons.append(self.button_of_subject)
            x_coord_for_btn_subj += 50   

       
        # Создание кнопок предметов ДЛЯ РЕДАКТИРОВАНИЯ и обработчик нажатия на кнопки
        def click_subj_choose_themes_for_edit(self):
            for btn in list_of_checked_subj_button_for_edit:
                btn.setChecked(False)
                list_of_checked_subj_button_for_edit.pop()
            for button_of_theme in list_of_theme_buttons_for_edit:
                button_of_theme.hide()
            for button_of_theme_mb_checked in list_of_subj_buttons_for_edit:
                if button_of_theme_mb_checked.isChecked():
                    list_of_checked_subj_button_for_edit.append(button_of_theme_mb_checked)
                    for theme_buttons_for_edit in list_of_theme_buttons_for_edit:
                        if theme_buttons_for_edit.text() in ultra_dict[button_of_theme_mb_checked.text()]:
                            theme_buttons_for_edit.show()
            
       
        x_coord_for_btn_subj_for_edit = 150    
        for subj_for_edit in ultra_dict.items():
            self.button_of_subject_for_edit = QtWidgets.QPushButton(str(subj_for_edit[0]), self)
            self.button_of_subject_for_edit.setCheckable(True)
            self.button_of_subject_for_edit.clicked.connect(click_subj_choose_themes_for_edit)
            self.button_of_subject_for_edit.move(230, x_coord_for_btn_subj_for_edit)
            self.button_of_subject_for_edit.hide()
            list_of_subj_buttons_for_edit.append(self.button_of_subject_for_edit)
            x_coord_for_btn_subj_for_edit += 50
        
      
        button_of_theme = ''
        # Создаёт модальное окно где начинается тест
        def click_theme_start_test():
            # МОДАЛЬНОЕ ОКНО В КОТОРОМ ПРОИСХОДИТ ТЕСТИРОВАНИЕ 
            for x in list_for_theme_buttons:
                if x.isChecked():
                    
                    # создаёт модальное окно для теста
                    global modalWindowTest
                    modalWindowTest = QtWidgets.QWidget(self, QtCore.Qt.Window)
                    modalWindowTest.setWindowModality(QtCore.Qt.WindowModal)
                    modalWindowTest.resize(1024, 768)
                    modalWindowTest.setWindowFlags(QtCore.Qt.Dialog)
                    text_name_of_test = 'Тест по теме: '+ str(x.text())
                    modal_label_theme = QtWidgets.QLabel(text_name_of_test, modalWindowTest)
                    modal_label_theme.move(146, 242)
                    
                    final_score_label = QtWidgets.QLabel('', modalWindowTest)
                    final_score_label.move(200, 200)
                    final_score_label.hide()
                    
                    list_for_questions = []
                    list_for_answers = []
                    list_of_quest_labels = []
                    list_of_lists_of_radio_buttons = []
                    counter_for_right_answ = []
                    
                    # Достаточно сложная схема с помещением элементов в списки
                    # а затем используя индексы их показывания\скрывания
                    for subject in ultra_dict.keys():
                        try:
                            for theme in ultra_dict[subject].keys():
                                if x.text() == theme:
                                    dict_of_questions = ultra_dict[subject][theme]
                                    
                                    for quests in dict_of_questions.keys():
                                        #print(quests)
                                        list_for_questions.append(quests)
                                        for answer in dict_of_questions[quests]:
                                            list_for_answers.append(answer)
                        except:
                            None
                           # print(1)
                    x_count_answ = 0
                    
                    if len(list_for_questions) == 0:
                        global modalWindowErrorMissQuestions
                        modalWindowErrorMissQuestions = QtWidgets.QWidget(modalWindowTest, QtCore.Qt.Window)
                        modalWindowErrorMissQuestions.setWindowModality(QtCore.Qt.WindowModal)
                        modalWindowErrorMissQuestions.resize(300, 300)
                        modalWindowErrorMissQuestions.setWindowFlags(QtCore.Qt.Dialog)
                        label_of_error = QtWidgets.QLabel('В теме ещё не созданы вопросы', modalWindowErrorMissQuestions)
                        label_of_error.move(60, 100)
                        
                        btn_ok = QtWidgets.QPushButton('Ок', modalWindowErrorMissQuestions)
                        btn_ok.move(80, 200)
                        btn_ok.clicked.connect(modalWindowErrorMissQuestions.close)
                        
                        x.setChecked(False)
                        modalWindowErrorMissQuestions.show()
                    elif len(list_for_questions) != 0:
                        for quest in list_for_questions:
                    
                            quest_label = QtWidgets.QLabel(str(quest), modalWindowTest)
                            quest_label.move(30,30)
                            quest_label.hide()
                            list_of_quest_labels.append(quest_label)
                            
                            list_of_radio_buttons = []
                            
                            radio1 = QtWidgets.QRadioButton(list_for_answers[x_count_answ], modalWindowTest)
                            radio1.move(50, 50)
                            radio1.hide()
                            radio2 = QtWidgets.QRadioButton(list_for_answers[x_count_answ+1], modalWindowTest)
                            radio2.move(50, 70)
                            radio2.hide()
                            radio3 = QtWidgets.QRadioButton(list_for_answers[x_count_answ+2], modalWindowTest)
                            radio3.move(50, 90)
                            radio3.hide()
                            radio4 = QtWidgets.QRadioButton(list_for_answers[x_count_answ+3], modalWindowTest)
                            radio4.move(50, 110)
                            radio4.hide()
                            list_of_radio_buttons.append(radio1)
                            list_of_radio_buttons.append(radio2)
                            list_of_radio_buttons.append(radio3)
                            list_of_radio_buttons.append(radio4)
                            list_of_lists_of_radio_buttons.append(list_of_radio_buttons)
                            x_count_answ += 4
                       
                            
                            
                            def click_start_test_button():
                               
                                for x in range(len(counter_for_right_answ)):
                                    counter_for_right_answ.pop()
                                
                                next_quest_button.show()
                               # last_quest_button.show()
                                modal_label_theme.hide()
                                repeat_test_button.hide()
                               
                                list_of_quest_labels[0].show()
                         
                                for list_radiobut in list_of_lists_of_radio_buttons[0]:  
                                    list_radiobut.setAutoExclusive(False)
                                    list_radiobut.setChecked(False)
                                    list_radiobut.repaint()
                                    list_radiobut.setAutoExclusive(True)
                                    list_radiobut.show()
                                 
                                start_test_button.hide()
                          
                            
                           
                            
                            def click_next_but():
  
                                start_test_button.hide()   
                                for x_count in range(len(list_of_quest_labels)): 
                                    if list_of_quest_labels[x_count].isVisible():
                                        last_quest_button.show()
                                        list_of_quest_labels[x_count].hide()
                                        #
                                        # Пробел в конце ответа ознчает правильный ответ
                                        #
                                        for one_button in list_of_lists_of_radio_buttons[x_count]:
                                            if one_button.isChecked() and one_button.text()[-1] == ' ':
                                                counter_for_right_answ.append(1)
      
                                        for x in range(4):
                                            list_of_lists_of_radio_buttons[x_count][x].setAutoExclusive(False)
                                            list_of_lists_of_radio_buttons[x_count][x].setChecked(False)
                                            list_of_lists_of_radio_buttons[x_count][x].repaint()
                                            list_of_lists_of_radio_buttons[x_count][x].setAutoExclusive(True)
                                            list_of_lists_of_radio_buttons[x_count][x].hide()

                                        try:
                                            list_of_quest_labels[x_count+1].show() 
                                            for list_radiobtn in list_of_lists_of_radio_buttons[x_count + 1]:
                                                list_radiobtn.show()
                                        except:
                                            None
                                            #print('Конец теста')
                                        break
                                if list_of_quest_labels[-1].isVisible():
                                   
                                    finish_test_button.show()
                            def finish_test_but():
                                
                                next_quest_button.hide()
                                
                                for x_count in range(len(list_of_quest_labels)):
                                    if list_of_quest_labels[x_count].isVisible():
                                        
                                        list_of_quest_labels[x_count].hide()
                                        #
                                        # Пробел в конце ответа ознчает правильный ответ
                                        #
                                        for one_button in list_of_lists_of_radio_buttons[x_count]:
                                            if one_button.isChecked() and one_button.text()[-1] == ' ':
                                                
                                                counter_for_right_answ.append(1)
                                        
                                        for x in range(4):
                                            list_of_lists_of_radio_buttons[x_count][x].setAutoExclusive(False)
                                            list_of_lists_of_radio_buttons[x_count][x].setChecked(False)
                                            list_of_lists_of_radio_buttons[x_count][x].repaint()
                                            list_of_lists_of_radio_buttons[x_count][x].setAutoExclusive(True)
                                            list_of_lists_of_radio_buttons[x_count][x].hide()
                                     
                                last_quest_button.hide()
                                
                                text_for_score_label = 'Правильно ' + str(len(counter_for_right_answ)) + ' из ' + str(len(list_of_quest_labels))
                                final_score_label.setText(text_for_score_label)
                                final_score_label.show()
                                
                                finish_test_button.hide()
                                repeat_test_button.show()
                                
                            def repeat_test_but():

                                start_test_button.show()
                                repeat_test_button.hide()
                                final_score_label.hide()
                                
                                x_count_answ = 0
                                
                                click_theme_start_test()
                                        
                                for list_of_radiobtn in list_of_lists_of_radio_buttons:
                                    for radiobtn in list_of_radiobtn:
                                        radiobtn.show()
                                        radiobtn.setChecked(False)
                                        radiobtn.hide()

                                repeat_test_button.hide()
                                
                                counter_for_right_answ = []
                                start_test_button.show()
                                
                            def click_last_but():
                                try:
                                    counter_for_right_answ.pop()
                                except:
                                    None
                                finish_test_button.hide()
                                
                                
                                for x_count in range(len(list_of_quest_labels)):
                                    
                                    if list_of_quest_labels[x_count].isVisible():
                                        
                                        list_of_quest_labels[x_count].hide()
                                      
                                        list_of_lists_of_radio_buttons[x_count][0].hide()
                                        list_of_lists_of_radio_buttons[x_count][1].hide()
                                        list_of_lists_of_radio_buttons[x_count][2].hide()
                                        list_of_lists_of_radio_buttons[x_count][3].hide()
                                        
                                        try:
                                            list_of_quest_labels[x_count-1].show()
                                            for list_radiobtn in list_of_lists_of_radio_buttons[x_count - 1]:
                                                
                                                if 'правильно' in list_radiobtn.text():
                                
                                                    formatted_answ = list_radiobtn.text().replace('правильно', '')
                                                    list_radiobtn.setText(formatted_answ)
                                                    list_radiobtn.show()
                                                    
                                                else:   
                                                    list_radiobtn.show()
                                            
                                          
                                        except:
                                            print(1)
                                    
                                if list_of_lists_of_radio_buttons[0][0].isVisible():
                                    last_quest_button.hide()
                                 
                            
                            start_test_button = QtWidgets.QPushButton('Начать тест', modalWindowTest)
                            start_test_button.move(300, 400)
                            start_test_button.hide()
                            start_test_button.clicked.connect(click_start_test_button)
                            
                            
                            next_quest_button = QtWidgets.QPushButton('Следующий вопрос', modalWindowTest)
                            next_quest_button.move(300, 300)
                            next_quest_button.hide()
                            next_quest_button.clicked.connect(click_next_but)
                        
                            last_quest_button = QtWidgets.QPushButton('Предыдущий вопрос', modalWindowTest)
                            last_quest_button.move(100, 300)
                            last_quest_button.hide()
                            last_quest_button.clicked.connect(click_last_but)
                            
                            finish_test_button = QtWidgets.QPushButton('Завершить тест', modalWindowTest)
                            finish_test_button.move(300, 300)
                            finish_test_button.setFixedSize(125,28)
                            finish_test_button.clicked.connect(finish_test_but)
                            finish_test_button.hide()
                            
                            repeat_test_button = QtWidgets.QPushButton('Повторить тест', modalWindowTest)
                            repeat_test_button.move(100, 300)
                            repeat_test_button.clicked.connect(repeat_test_but)
                            repeat_test_button.hide()
                        
                        start_test_button.show()
                        modalWindowTest.show()
                        
                        x.setChecked(False)
                    break
     
        # Создание кнопок тем и обработчик нажатия на темы 
        for x in ultra_dict.keys():
            x_coord_for_btn_theme = 150
            for y in ultra_dict[x]:
                self.button_of_theme = QtWidgets.QPushButton(str(y), self)
                self.button_of_theme.setCheckable(True)
                self.button_of_theme.clicked.connect(click_theme_start_test)
                self.button_of_theme.move(650, x_coord_for_btn_theme)
                self.button_of_theme.hide()
                list_for_theme_buttons.append(self.button_of_theme)
                x_coord_for_btn_theme += 50
        
        
        
        
        
        
        # Обработчик кнопок тем для редактирования, ДОЛЖЕН создавать окно редактирования темы 
        # Добавить это из другой части программы, этот код удалить или адаптировать        
        def click_theme_for_edit(self):
            for btn_for_mainwind in list_of_theme_buttons_for_edit:
                if btn_for_mainwind.isChecked():
                    print(ultra_dict)
                    global modalWindowEdit
                    modalWindowEdit = QtWidgets.QWidget()
                    modalWindowEdit.resize(500,500) 
                    modalWindowEdit.show()
                    global x_coord_test
                    x_coord_test = 50
                    def test_func_create_textedit():
                        test_text_edit = QTextEdit('Тема', modalWindowEdit)
                        test_text_edit.setFixedSize(30, 70)
                        test_text_edit.move(30, x_coord_test )
                        test_text_edit.show()
                        x_coord_test += 50
                    btn_for_test = QtWidgets.QPushButton('Тест', modalWindowEdit)
                    btn_for_test.move(400, 400)
                    btn_for_test.clicked.connect(test_func_create_textedit)
                    btn_for_test.show()
                    
                    text_edit_theme = QTextEdit('Theme', modalWindowEdit)
                    text_edit_theme.setFixedSize(250, 40)
                    text_edit_theme.move(10, 10)
                    
                    text_edit_quest = QTextEdit('Quest', modalWindowEdit)
                    text_edit_quest.setFixedSize(250, 40)
                    text_edit_quest.move(30, 55)
                    
                    text_edit_answ = QTextEdit('Answer 1', modalWindowEdit)
                    text_edit_answ.setFixedSize(250, 40)
                    text_edit_answ.move(50, 100)
                    
                    text_edit_answ.show()
                    text_edit_theme.show()
                    text_edit_quest.show()
        # Создание кнопок тем для редактирования
        def creating_btn_of_theme_for_edit_and_push_in_list(self):
            try:
                list_of_theme_buttons_for_edit.clear()
            except:
                None
            for subj_themes in ultra_dict.keys():
                x_coord_for_btn_theme_for_edit = 150
                for theme_for_edit in ultra_dict[subj_themes]:
                    self.button_of_theme_for_edit = QtWidgets.QPushButton(str(theme_for_edit), self)
                    self.button_of_theme_for_edit.setCheckable(True)
                    self.button_of_theme_for_edit.clicked.connect(click_theme_for_edit)
                    self.button_of_theme_for_edit.move(650, x_coord_for_btn_theme_for_edit)
                    self.button_of_theme_for_edit.hide()
                    list_of_theme_buttons_for_edit.append(self.button_of_theme_for_edit)
                    x_coord_for_btn_theme_for_edit += 50
        creating_btn_of_theme_for_edit_and_push_in_list(self)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.button_choose_test, alignment = QtCore.Qt.AlignRight)
        vbox.addStretch(1)
        vbox.addWidget(self.button_edit)
        vbox.addStretch(1)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        self.setLayout(hbox)
        
    
            
            
    # создаёт окно добавления предмета
    def mod_win_append_subj(self):
        
        modalWindow = QtWidgets.QWidget(self, QtCore.Qt.Window)
        modalWindow.setWindowTitle("Добавление предмета")
        modalWindow.resize(400, 400)
        # какие-то  непонятные инструкции, скопированные из примера
        modalWindow.setWindowModality(QtCore.Qt.WindowModal)
        modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modalWindow.move(self.geometry().center() - modalWindow.rect().center() - QtCore.QPoint(4, 30))
        label_name_new_subj = QtWidgets.QLabel("Введите название предмета", modalWindow)
        label_name_new_subj.move(10, 10)
        
        name_subj = QLineEdit(modalWindow)
        name_subj.move(20,40)
        
        btn_exit = QtWidgets.QPushButton('Отмена', modalWindow)
        btn_exit.move(20,350)
        # Кнопка для сохранения предмета в окне создания предмета
        def save_name_subj(self):
            
            string_name_subj = name_subj.text()
            ultra_dict[string_name_subj] = 'place_for_theme'
            with open('database.json', 'w',encoding="utf-8",  ) as file_1:
                file_1.write(json.dumps(ultra_dict, ensure_ascii = False))
            modalWindow.hide()
            
            #self.click_but_edit(self)
            #self.buttons()
            #self.update()
        btn_save_subj = QtWidgets.QPushButton('Сохранить', modalWindow)
        btn_save_subj.move(200, 350)
        btn_save_subj.clicked.connect(save_name_subj)
       # btn_save_subj.clicked.connect(click_but_edit)
     
        modalWindow.show() 
        
    

    
    
    
    
    def click_but_choose(self):
        self.button_choose_test.hide()
        self.button_edit.hide()
        self.label_subject.show()
        self.label_theme.show()
        self.button_back_to_main_menu.show()
        for subject in list_for_subj_buttons:
            subject.show()
         
    def click_but_edit(self):
        self.button_choose_test.hide()
        self.button_edit.hide()
        self.label_subject.show()
        self.label_theme.show()
        self.button_back_to_main_menu.show()
        self.btn_add_subject.show()
        for subject in list_of_subj_buttons_for_edit:
            subject.show()
    
    def click_back_1(self):
      
        self.button_back_to_main_menu.hide()
        self.label_subject.hide()
        self.label_theme.hide()
        self.button_choose_test.show()
        #self.button_edit.show()
        self.btn_add_subject.hide()
        for button_1 in list_for_subj_buttons:
            button_1.setChecked(False)
            button_1.repaint()
            button_1.hide()
        for button_2 in list_for_theme_buttons:
            button_2.hide()
        for button_3 in list_of_subj_buttons_for_edit:
            button_3.setChecked(False)
            button_3.repaint()
            button_3.hide()
        for button_4 in list_of_theme_buttons_for_edit:
            button_4.hide()
        
        



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainCode()
    sys.exit(app.exec_())
