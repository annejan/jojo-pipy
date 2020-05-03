"""
Product config file for Product Label App

© 2019 - 2020 Jolanda Versteeg
Based on a demo application by Anne Jan Brouwer
"""
import datetime

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
IMAGE = 'background.jpg'
BACK_TEXT = 'Dit product bevat %s dingen, daarnaast bevat het natuurlijk ook ingrediënten en heeft voedingswaarde.\n' \
            'Sommige mensen kunnen hun geluk niet op wanneer ze dit product consumeren.\n' \
            'Andere mensen vinden het maar zo-zo . .\n' \
            'Er is ook een aanbevolen dagelijkse hoeveelheid echter publiceren wij die slechts op onze website.\n' \
            '\n\n' \
            'Ten minste houdbaar tot: ' + (datetime.date.today() + datetime.timedelta(days=7)).strftime('%d-%m-%Y')
