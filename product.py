"""
Product config file for Product Label App

© 2019 - 2020 Jolanda Versteeg
Based on a demo application by Anne Jan Brouwer
"""
import datetime

QUESTIONS = 7

LIST_A = [
    'Ik wil wel koken maar wel makkelijk',
    'Comfy food is oké',
    'Wat is er mis met bestellen?',
    'Rummikub is voor mij plezier en ontspanning',
    'Die Iglo risotto met groente uit de magnetron is ook prima',
    'Grown in controlled indoor areas',
    'Always the same look and feel',
    'Assured of constant quality and hygiene'
]
LIST_B = [
    'Koken, is voor mij het zand van de piepers boenen',
    'Geef mij maar een wortel want gezond',
    'Gezonde afhaalmaaltijden bestaan niet',
    'Joggen in het park geeft mij plezier en ik ben goed bezig',
    'Mijn risotto kost mij een uur maar dan weet ik wat erin zit en dat is beter',
    'Handpicked products from local fields',
    'Flavor, color and shape may differ',
    'Fresh air and no chemicals'
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
