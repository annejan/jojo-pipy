"""
Product config file for Product Label App

© 2019 - 2020 Jolanda Versteeg
Based on a demo application by Anne Jan Brouwer
"""
import datetime

QUESTIONS = 7

LIST_A = [
    'Ik wil wel koken\nmaar wel makkelijk',
    'Comfy food is oké',
    'Wat is er mis\nmet bestellen?',
    'Rummikub is voor mij\nplezier en ontspanning',
    'Die Iglo risotto met\ngroente uit de magnetron\nis ook prima',
    'Grown in controlled\nindoor areas',
    'Always the same\nlook and feel',
    'Assured of constant\nquality and hygiene'
]
LIST_B = [
    'Koken, is voor mij het\nzand van de piepers boenen',
    'Geef mij maar een wortel\nwant gezond',
    'Gezonde afhaalmaaltijden\nbestaan niet',
    'Joggen in het park geeft\nmij plezier en ik ben\ngoed bezig',
    'Mijn risotto kost mij een\nuur maar dan weet ik wat\nerin zit endat is beter',
    'Handpicked products\nfrom local fields',
    'Flavor, color and\nshape may differ',
    'Fresh air and\nno chemicals'
]
INTRO = 'Good morning, almost ready for breakfast. What do you like today?\n\nFind my jam!'
PAYOFF = '%s'
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
