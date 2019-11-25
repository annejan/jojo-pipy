from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import random
import sys

listA = [
    'mooi', 'fijn', 'gaaf', 'geweldig', 'goed', 'jofel', 'keurig', 'kostelijk', 'netjes', 'prima', 'reuze',
    'uitstekend', 'perfect', 'fantastisch'
]

listB = [
    'lelijk', 'afgrijselijk', 'afschuwelijk', 'afstotelijk', 'afzichtelijk', 'gruwelijk', 'mismaakt', 'misvormd',
    'onesthetisch', 'onfraai', 'onknap', 'onooglijk', 'wanstaltig', 'weerzinwekkend', 'mottig'
]

questions = 7

question = 0
aChosen = 0
bChosen = 0
whichList = False


class FeedMe(QWidget):

    def __init__(self):
        super().__init__()
        self.label_intro = QLabel(self)
        self.label_intro.move(20, 20)
        self.label_intro.setFont(QFont('SansSerif', 32))
        self.label_intro.setMaximumWidth(460)
        self.label_intro.setMinimumWidth(460)
        self.label_intro.setWordWrap(True)
        self.label_intro.setText('Klik hier om te beginen, klik dan wat woorden bij elkaar')
        self.label_intro.mousePressEvent = self.start_question
        self.label_intro.setAlignment(Qt.AlignCenter)
        self.label_intro.hide()

        self.button1 = QPushButton("Button 1 text", self)
        self.button1.move(20, 80)
        self.button1.resize(220, 80)
        self.button1.hide()
        self.button1.clicked.connect(lambda:self.button_clicked(1))

        self.button2 = QPushButton("Button 2 text", self)
        self.button2.move(240, 80)
        self.button2.resize(220, 80)
        self.button2.hide()
        self.button2.clicked.connect(lambda:self.button_clicked(2))

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

        self.setGeometry(300, 300, 480, 300)
        self.setWindowTitle('Mooie demo app')
        self.show()
        self.reset_app()

    def reset_app(self):
        global question, aChosen, bChosen
        question = 0
        aChosen = 0
        bChosen = 0
        self.label_image.hide()
        self.label_text.hide()
        self.button1.hide()
        self.button2.hide()
        self.label_intro.show()
        self.update_question()

    def start_question(self, press):
        if press:
            self.label_intro.hide()
            self.button1.show()
            self.button2.show()

    def button_clicked(self, button):
        global aChosen, bChosen, question, questions, whichList
        if (not whichList and button == 1) or (whichList and button == 2):
            aChosen += 1
        else:
            bChosen += 1
        self.setWindowTitle("Mooi %s Lelijk %s" % (aChosen, bChosen))
        question += 1
        if question < questions:
            self.update_question()
        else:
            self.show_label()

    def update_question(self):
        global whichList
        whichList = bool(random.getrandbits(1))
        self.button1.setText(random.choice((listA, listB)[whichList]))
        self.button2.setText(random.choice((listB, listA)[whichList]))

    def show_label(self):
        global aChosen, bChosen
        self.button1.hide()
        self.button2.hide()
        self.label_image.show()
        self.label_text.setText('Je koos voornamelijk %s dingen!' % ('mooie', 'lelijke')[aChosen < bChosen])
        self.label_text.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FeedMe()
    sys.exit(app.exec_())
