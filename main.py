#!/usr/bin/env python3
"""
        RaspberryPi Python app FeedMe

© 2019 Jolanda Versteeg
Based on a demo application by Anne Jan Brouwer

Choose some words, get a nice fitting product label.
Double click the label to reset the app.
"""

import random
import sys
# pylint: disable=import-error
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

QUESTIONS = 7

LIST_A = [
    'mooi', 'fijn', 'gaaf', 'geweldig', 'goed', 'jofel', 'keurig', 'kostelijk', 'netjes',
    'prima', 'reuze', 'uitstekend', 'perfect', 'fantastisch'
]
LIST_B = [
    'lelijk', 'afgrijselijk', 'afschuwelijk', 'afstotelijk', 'afzichtelijk', 'gruwelijk',
    'mismaakt', 'misvormd', 'onesthetisch', 'onfraai', 'onknap', 'onooglijk', 'wanstaltig',
    'weerzinwekkend', 'mottig'
]

INTRO = 'Klik hier om te beginen, klik dan vervolgens je huidige humeur bij elkaar'
PAYOFF = 'Je koos voornamelijk %s dingen!'
WORD_A = 'mooie'
WORD_B = 'lelijke'
TITLE = 'Mooi %s Lelijk %s'


# pylint: disable=too-many-instance-attributes
class FeedMe(QWidget):
    """Feed me some data and I'll show you a nice label"""
    def __init__(self):
        """Window initialisation"""
        super().__init__()
        self.question = 0
        self.a_chosen = 0
        self.b_chosen = 0
        self.which_list = False
        self.label_intro = QLabel(self)
        self.label_intro.move(20, 20)
        self.label_intro.setFont(QFont('SansSerif', 32))
        self.label_intro.setMaximumWidth(440)
        self.label_intro.setMinimumWidth(440)
        self.label_intro.setWordWrap(True)
        self.label_intro.setText(INTRO)
        self.label_intro.setAlignment(Qt.AlignCenter)
        self.label_intro.hide()
        self.label_intro.mousePressEvent = self.start_question

        self.button1 = QPushButton("Button 1 text", self)
        self.button1.move(20, 80)
        self.button1.resize(220, 80)
        self.button1.hide()
        self.button1.clicked.connect(lambda: self.button_clicked(1))

        self.button2 = QPushButton("Button 2 text", self)
        self.button2.move(240, 80)
        self.button2.resize(220, 80)
        self.button2.hide()
        self.button2.clicked.connect(lambda: self.button_clicked(2))

        self.label_image = QLabel(self)
        self.label_image.setPixmap(QPixmap("background.jpg"))
        self.label_image.hide()
        self.label_text = QLabel(self)
        self.label_text.move(20, 20)
        self.label_text.setFont(QFont('SansSerif', 32))
        self.label_text.setStyleSheet('color: darkblue')
        self.label_text.setMaximumWidth(460)
        self.label_text.setMinimumWidth(460)
        self.label_text.setWordWrap(True)
        self.label_text.hide()
        self.label_text.mouseDoubleClickEvent = self.reset_app

        self.setGeometry(0, 0, 480, 300)
        self.setWindowTitle('Mooie demo app')
        self.show()
        # self.showFullScreen()     # enable to run full screen on Pi 😄
        self.reset_app(True)

    def reset_app(self, press):
        """Start from scratch (new customer)"""
        if press:
            self.question = 0
            self.a_chosen = 0
            self.b_chosen = 0
            self.label_image.hide()
            self.label_text.hide()
            self.button1.hide()
            self.button2.hide()
            self.label_intro.show()
            self.update_question()

    def start_question(self, press):
        """Start asking questions"""
        if press:
            self.label_intro.hide()
            self.button1.show()
            self.button2.show()

    def button_clicked(self, button):
        """You have clicked a button, let's add some points to A of B"""
        if (not self.which_list and button == 1) or (self.which_list and button == 2):
            self.a_chosen += 1
        else:
            self.b_chosen += 1
        self.setWindowTitle(TITLE % (self.a_chosen, self.b_chosen))
        self.question += 1
        if self.question < QUESTIONS:
            self.update_question()
        else:
            self.show_label()

    def update_question(self):
        """Choose two new words"""
        self.which_list = bool(random.getrandbits(1))
        self.button1.setText(random.choice((LIST_A, LIST_B)[self.which_list]).title())  # .title() capitalised word
        self.button2.setText(random.choice((LIST_B, LIST_A)[self.which_list]).title())

    def show_label(self):
        """Show payoff label"""
        text = PAYOFF % (WORD_A, WORD_B)[self.a_chosen < self.b_chosen]
        self.button1.hide()
        self.button2.hide()
        self.label_image.show()
        self.label_text.setText(text)
        self.label_text.show()
        self.setWindowTitle(text)


# Start the FeedMe app and quit nicely when Ctrl+Q pressed
if __name__ == '__main__':
    APP = QApplication(sys.argv)
    FeedMe()
    sys.exit(APP.exec_())
