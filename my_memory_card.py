#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint
# 
class Question():
    def __init__(self, question, right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
# 
app = QApplication([])
WINDOW = QWidget()
WINDOW.stat = 0
WINDOW.resize(350,250)
# функции
def show_result():
    option_answer.hide()
    result_box.show()
    to_answer.setText('Следующий вопрос')

def show_question():
    for i in answers:
        i.setAutoExclusive(False)
        i.setChecked(False)
        i.setAutoExclusive(True)
    option_answer.show()
    result_box.hide()
    to_answer.setText('Ответить')

def start_test():
    if to_answer.text() == 'Ответить':
        show_result()
        check_answer()
        if q0 in quest_list:
            quest_list.remove(q0)
    elif to_answer.text() == 'Следующий вопрос':
        if len(quest_list) == 0:
            print('Всего вопросов:', len_quest_list)
            print('Правильных ответов:', WINDOW.stat)
            print('Рейтинг:', round((WINDOW.stat/len_quest_list)*100, 0), "%")
            exit()
        rand_q = randint(0, len(quest_list)-1)
        ask(quest_list[rand_q])
        quest_list.remove(quest_list[rand_q])


def check_answer(): 
    if answers[0].isChecked() == True:
        result_label.setText('Правильно')
        WINDOW.stat +=1
    elif answers[1].isChecked() == True or answers[2].isChecked() == True or answers[3].isChecked() == True:
        result_label.setText('Неверно')
    else:
        show_question()

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quest.setText(q.question) 
    result_answer.setText(q.right_answer)
    result_answer.setText(q.right_answer)
    show_question()
    
#
# 
WINDOW.setWindowTitle("Memory Card")
to_answer = QPushButton('Ответить')
quest = QLabel('Какой национальности не существует?')
#  создание групп
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
h_line1 = QHBoxLayout()
option_answer = QGroupBox('Варианты ответов')
answer1 = QRadioButton('Смурфы')
answer2 = QRadioButton('Энцы')
answer3 = QRadioButton('Чулымцы')
answer4 = QRadioButton('Алеуты')
answers = [answer1, answer2, answer3, answer4]


q0 = Question(quest.text(), answer1.text(), answer2.text(), answer3.text(), answer4.text())
q1 = Question("2+2?", "4", "22", "не 4","2345")
q2 = Question("Правильный ответ: 2", "2", "1", "32", "875")
q3 = Question("Вопрос", "правильный ответ", "неправильный ответ", "неправильный ответ", "неправильный ответ")
q4 = Question("Сколько вариантов ответов в этом опросе?", "4", "0", "100", "ну допустим 2")
quest_list = [q0,q1,q2,q3,q4]
len_quest_list = len(quest_list)

v_line1.addWidget(answer1)
v_line1.addWidget(answer2)
v_line2.addWidget(answer3)
v_line2.addWidget(answer4)
h_line1.addLayout(v_line1)
h_line1.addLayout(v_line2)
option_answer.setLayout(h_line1)
result_box = QGroupBox('Результат теста')
result_line = QVBoxLayout()
result_label = QLabel('Правильно/Неправильно')
result_answer = QLabel(answers[0].text())
result_line.addWidget(result_label)
result_line.addWidget(result_answer)
result_box.setLayout(result_line)
# расположение и выравнивание
to_answer_line = QHBoxLayout()
to_answer_line.addStretch(1)
to_answer_line.addWidget(to_answer,2)
to_answer_line.addStretch(1)

box_line = QHBoxLayout()
box_line.addStretch(1)
box_line.addWidget(result_box, 8)
box_line.addWidget(option_answer, 8)
box_line.addStretch(1)

v_line3 = QVBoxLayout()
v_line3.addWidget(quest,1, alignment = Qt.AlignHCenter)
v_line3.addLayout(box_line,5)
v_line3.addLayout(to_answer_line,1)
WINDOW.setLayout(v_line3)
result_box.hide()
# 
to_answer.clicked.connect(start_test)
# 
WINDOW.show()
app.exec_()
