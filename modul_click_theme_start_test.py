import sys
import json
import time
import copy
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class click_theme_start_test(QWidget):
    def __init__(self, self_2, list_for_theme_buttons, parent = None):
        super(click_theme_start_test, self).__init__(parent)
        #self.initUI()
        
        self.self_2 = self_2
        
        self.list_for_theme_buttons = list_for_theme_buttons
        self.initUI()
    
    def initUI(self):
        self.setFixedSize(1024, 768)
        self.setWindowTitle('Тест')
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        
        self.labels_and_text()
        #print(self_2)
        #self.show()
        #time.sleep(5)
        
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
        painter_1.drawRect(0, 0, 1024, 80)
        #painter_1.setPen(new_pen)
        #painter_1.drawRect(66, 121, 892, 413)
        painter_1.drawLine(66, 121, 958, 121)
        painter_1.drawLine(66, 224, 958, 224)
        painter_1.drawLine(66, 534, 958, 534)
        painter_1.drawLine(66, 121, 66, 534)
        painter_1.drawLine(958, 121, 958, 534)
        
        
    def labels_and_text(self):
        with open('database.json', 'r',encoding="utf-8", ) as file_db:
                ultra_dict = json.load(file_db)
       # print(2)
      #  print(self_2)       
        list_for_questions = []
        list_for_answers = []
        list_of_quest_labels = []
        list_of_lists_of_radio_buttons = []
        counter_for_right_answ = []        
        
      
        for btn in self.list_for_theme_buttons:
            #print(btn.text())
            if btn.isChecked():
                #print(btn.text())
                var_for_checked_btn = btn
                # Достаточно сложная схема с помещением элементов в списки
                # а затем используя индексы их показывания\скрывания
                for subject in ultra_dict.keys():
                    try:
                        for theme in ultra_dict[subject].keys():
                            if btn.text() == theme:
                                dict_of_questions = ultra_dict[subject][theme]
                                
                                for quests in dict_of_questions.keys():
                                    
                                    list_for_questions.append(quests)
                                    
                                    for answer in dict_of_questions[quests]:
                                        list_for_answers.append(answer)
                                #print(222)
                                #break
                    except:
                        None
                           # print(1)
                    x_count_answ = 0
        text_name_of_test = 'Тест по теме: '+ str(var_for_checked_btn.text())
        modal_label_theme = QtWidgets.QLabel(text_name_of_test, self)
        modal_label_theme.setFixedSize(726, 99)
        font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 15)
        modal_label_theme.setFont(font_obj_for_label)
        modal_label_theme.move(146, 242)
        modal_label_theme.setWordWrap(True) 
            
        
        final_score_label = QtWidgets.QLabel('', self)
        final_score_label.move(400, 180)
        final_score_label.setFont(font_obj_for_label)
        final_score_label.hide()
    
                    
        if len(list_for_questions) == 0:
            
            global modalWindowErrorMissQuestions
            modalWindowErrorMissQuestions = QtWidgets.QWidget()#(self, QtCore.Qt.Window)
            modalWindowErrorMissQuestions.setWindowModality(QtCore.Qt.WindowModal)
            modalWindowErrorMissQuestions.resize(300, 300)
            modalWindowErrorMissQuestions.setWindowFlags(QtCore.Qt.Dialog)
            label_of_error = QtWidgets.QLabel('В теме ещё не созданы вопросы', modalWindowErrorMissQuestions)
            label_of_error.move(60, 100)
            
            btn_ok = QtWidgets.QPushButton('Ок', modalWindowErrorMissQuestions)
            btn_ok.move(80, 200)
            btn_ok.clicked.connect(modalWindowErrorMissQuestions.close)
            
            var_for_checked_btn.setChecked(False)
            modalWindowErrorMissQuestions.show()
            #print(1)
        elif len(list_for_questions) != 0:
            #self.show()
            for quest in list_for_questions:
        
                quest_label = QtWidgets.QLabel(str(quest), self)
                quest_label.setWordWrap(True)
                quest_label.setFixedSize(780, 65)
                font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 28)
                quest_label.setFont(font_obj_for_label)
                quest_label.move(121,152)
                quest_label.hide()
                list_of_quest_labels.append(quest_label)
                
                list_of_radio_buttons = []
                
                font_obj_for_label = QtGui.QFont('Segoe UI', pointSize = 25)
                
                radio1 = QtWidgets.QRadioButton(list_for_answers[x_count_answ], self)
                radio1.move(187, 257)
                radio1.setFont(font_obj_for_label)
                radio1.hide()
                radio2 = QtWidgets.QRadioButton(list_for_answers[x_count_answ+1], self)
                radio2.move(187, 324)
                radio2.setFont(font_obj_for_label)
                radio2.hide()
                radio3 = QtWidgets.QRadioButton(list_for_answers[x_count_answ+2], self)
                radio3.move(187, 391)
                radio3.setFont(font_obj_for_label)
                radio3.hide()
                radio4 = QtWidgets.QRadioButton(list_for_answers[x_count_answ+3], self)
                radio4.move(187, 458)
                radio4.setFont(font_obj_for_label)
                radio4.hide()
                list_of_radio_buttons.append(radio1)
                list_of_radio_buttons.append(radio2)
                list_of_radio_buttons.append(radio3)
                list_of_radio_buttons.append(radio4)
                list_of_lists_of_radio_buttons.append(list_of_radio_buttons)
                x_count_answ += 4
            self.show()
                #print(1)
        global click_start_test_button  
          
        def click_start_test_button():
            print(1)
            print(self) 
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
            #print(1)
            #print(self)
            #print(self_2) 
            start_test_button.show()
            repeat_test_button.hide()
            final_score_label.hide()
            
            x_count_answ = 0
            #print(self)
           # self.self_2.click_theme_start_test()
                    
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
             
        
        start_test_button = QtWidgets.QPushButton('Начать тест', self)
        start_test_button.move(358, 417)
        start_test_button.setFixedSize(390, 106)
        start_test_button.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 50px 50px 50px 50px;}"
       "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        #start_test_button.hide()
        start_test_button.clicked.connect(click_start_test_button)
        start_test_button.show()
            
        next_quest_button = QtWidgets.QPushButton('Следующий вопрос', self)
        next_quest_button.setFixedSize(298, 68)
        next_quest_button.move(564, 629)
        next_quest_button.hide()
        next_quest_button.clicked.connect(click_next_but)
    
        last_quest_button = QtWidgets.QPushButton('Предыдущий вопрос', self)
        last_quest_button.move(156, 629)
        last_quest_button.setFixedSize(298, 68)
        last_quest_button.hide()
        last_quest_button.clicked.connect(click_last_but)
        
        finish_test_button = QtWidgets.QPushButton('Завершить тест', self)
        finish_test_button.move(564, 629)
        finish_test_button.setFixedSize(298,68)
        finish_test_button.clicked.connect(finish_test_but)
        finish_test_button.hide()
        
        repeat_test_button = QtWidgets.QPushButton('Повторить тест', self)
        repeat_test_button.setFixedSize(298,68)
        repeat_test_button.move(564, 629)
        repeat_test_button.clicked.connect(repeat_test_but)
        repeat_test_button.hide()
        def close_func():
            self.close()
        final_end_testing = QtWidgets.QPushButton('Завершить тестирование', self)
        final_end_testing.move(564, 629)
        
        final_end_testing.clicked.connect(close_func)
        #final_end_testing.show()
        final_end_testing.hide()
            
            #start_test_button.show()
            #self.show()
            #modalWindowTest.show()
            
        var_for_checked_btn.setChecked(False)
        #break
        #print(1)

