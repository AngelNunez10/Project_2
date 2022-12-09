from PyQt5.QtWidgets import *
from view import *
import random


# pyuic5 -x view.ui -o view.py


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


words_list = ['Thing', 'topic', 'wealth', 'poem', 'shirt', 'worker', 'week', 'height', 'hotel', 'love', 'depth', 'tooth', 'studio', 'Mexico', 'Tokyo', 'Japan', 'Canada',
'membership', 'sister', 'coding', 'law', 'computer', 'reaction', 'intention', 'category', 'mud', 'data', 'idea', 'road', 'session', 'employee', 'sample',
'restaurant', 'charity', 'county', 'history', 'management', 'menu', 'hear', 'terror', 'disaster', 'length', 'assistant', 'teaching', 'platform']

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_enter.clicked.connect(lambda: self.enter())
        self.button_reset.clicked.connect(lambda: self.set_up())

        self.set_up()

    def set_up(self):
        self.word = random.choice(words_list).lower()
        print(self.word)
        self.max_attempts = 8
        self.list_check = []

        self.guess_list = ''

        self.word_list = self.word.split()
        self.user_attempts = 0

        under_score = '_     ' * len(self.word)
        self.label_underscore.setText(under_score)
        self.label_right_wrong.setText('')
        print(under_score)

        self.img_bar.setVisible(False)
        self.img_top_bar.setVisible(False)
        self.img_head.setVisible(False)
        self.img_body.setVisible(False)
        self.img_l_arm.setVisible(False)
        self.img_r_arm.setVisible(False)
        self.img_l_leg.setVisible(False)
        self.img_r_leg.setVisible(False)


    def enter(self):

        if self.user_attempts < self.max_attempts:

            self.user_input = self.user_letter.text().lower().strip()
            self.user_letter.setText('')


            if self.user_input in self.word:
                self.guess_list += self.user_input
                self.label_right_wrong.setText('THAT IS CORRECT!')
                print('You are correct')

            else:
                self.label_right_wrong.setText('THAT IS INCORRECT')
                self.user_attempts += 1
                self.show_images()

                print('Wrong Guess')

            space = ''

            for i in self.word:
               if i.lower() in self.guess_list:
                   space = space + i + '    '
                   self.list_check.append(i.lower)
               else:
                   space += '_      '

            space.rstrip()
            self.label_underscore.setText(space)




    def show_images(self):
        if self.user_attempts == 1:
            self.img_bar.setVisible(True)
        elif self.user_attempts == 2:
            self.img_top_bar.setVisible(True)
        elif self.user_attempts == 3:
            self.img_head.setVisible(True)
        elif self.user_attempts == 4:
            self.img_body.setVisible(True)
        elif self.user_attempts == 5:
            self.img_l_arm.setVisible(True)
        elif self.user_attempts == 6:
            self.img_r_arm.setVisible(True)
        elif self.user_attempts == 7:
            self.img_l_leg.setVisible(True)
        elif self.user_attempts == 8:
            self.img_r_leg.setVisible(True)
            self.label_right_wrong.setText('GAME OVER!\nTRY AGAIN')












