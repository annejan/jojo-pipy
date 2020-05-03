"""
Product config file for Product Label App

© 2019 - 2020 Jolanda Versteeg
Based on a demo application by Anne Jan Brouwer
"""
import datetime

QUESTIONS = 7

LIST_A = [
    'Have a sweet tooth',
    'Quick & easy',
    'Fried',
    'Home delivery',
    'Meal kits',
    'Ready meals',
    'Takeaways',
    'Addes vitamines',
    'Familiar foods',
    'Fresh and tasty',
    'Crunchy',
    'Traditionally prepared',
    'Improved flavor',
    'Frozen',
    'Instant',
    'Fussy eater',
    'Pre-cutted'
]
LIST_B = [
    'Eat sensibility',
    'Five a day',
    'Try new foods',
    'Experimental',
    'Natural',
    'Organic',
    'Mindful eating',
    'New world foods',
    'Clean label',
    'Sustainable',
    'It may take some effort',
    'A critical view',
    'Health',
    'Fresh is important',
    'Additive free',
    'Slow cooking',
    'Home cutted'
]
INTRO = 'Klik hier om te beginen, klik dan vervolgens je huidige humeur bij elkaar'
PAYOFF = 'Je koos voornamelijk %s dingen!'
WORD_A = 'convenience'
WORD_B = 'sustainable'
TITLE = 'Convenience %s Sustainable %s'
IMAGE = 'background.jpg'
BACK_TEXT = 'Dit product bevat %s dingen, daarnaast bevat het natuurlijk ook ingrediënten en heeft voedingswaarde.\n' \
            'Sommige mensen kunnen hun geluk niet op wanneer ze dit product consumeren.\n' \
            'Andere mensen vinden het maar zo-zo . .\n' \
            'Er is ook een aanbevolen dagelijkse hoeveelheid echter publiceren wij die slechts op onze website.\n' \
            '\n\n' \
            'Ten minste houdbaar tot: ' + (datetime.date.today() + datetime.timedelta(days=7)).strftime('%d-%m-%Y')
