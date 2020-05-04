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
    'Added vitamins',
    'Familiar foods',
    'Fresh and tasty',
    'Crunchy',
    'Traditionally prepared',
    'Improved flavor',
    'Frozen',
    'Instant',
    'Fussy eater',
    'Pre-sliced',
    'Enriched'
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
    'Unsliced',
    'Locally produced'
]
INTRO = 'Klik hier om te beginen, klik dan vervolgens je huidige humeur bij elkaar'
PAYOFF = 'Je koos voornamelijk %s dingen!'
WORD_A = 'This jam is produced year round on a large scale, to ensure constant quality.\n' \
         'The production facilities meet the highest hygiene standards and the strawberries were grown in controlled ' \
         'indoor areas, decreasing the environmental impact and amount of spill. Due to this process, '\
         'this strawberry jam is a responsible choice.'
WORD_B = 'For this strawberry jam only the most colorful and juicy strawberries were used. '\
         'Picked by hand from the fields of local strawberry farms. '\
         'Due to production on open fields in the fresh air and no use of chemicals, this jam is 100 percent natural.\n'\
         'Note that the flavor may differ depending on season and harvest.'
TITLE = 'Convenience %s Sustainable %s'
IMAGE = 'background.jpg'
BACK_TEXT = 'Dit product bevat %s dingen, daarnaast bevat het natuurlijk ook ingrediënten en heeft voedingswaarde.\n' \
            'Sommige mensen kunnen hun geluk niet op wanneer ze dit product consumeren.\n' \
            'Andere mensen vinden het maar zo-zo . .\n' \
            'Er is ook een aanbevolen dagelijkse hoeveelheid echter publiceren wij die slechts op onze website.\n' \
            '\n\n' \
            'Ten minste houdbaar tot: ' + (datetime.date.today() + datetime.timedelta(days=7)).strftime('%d-%m-%Y')
