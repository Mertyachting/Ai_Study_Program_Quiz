buildings = 1
math = 1
science = 1
garedening = 1
biology = 1
nature = 1
planning = 1
culture = 1
politics = 1
social = 1
people = 1
speech = 1
language = 1
engineering = 1
computer = 1
graphics = 1
programming = 1
Systems = 1
development = 1
animation = 1
communication = 1
media = 1
design = 1
aesthetics = 1
art = 1
chemistry = 1
physics = 1
anamoty = 1
photography = 1
history = 1
painting = 1
drawing = 1
psychology = 1





array = [buildings , math, science ,
    garedening ,
    biology ,
    nature ,
    planning ,
    culture ,
    politics ,
    social ,
    people ,
    speech,
    language,
    engineering,
    computer,
    graphics ,
    programming,
    Systems ,
    development ,
    animation ,
    communication ,
    media  ,
    design ,
    aesthetics ,
    art ,
    chemistry ,
    physics ,
    anamoty ,
    photography ,
    history ,
    painting ,
    drawing ,
    psychology ]

print(len(array))



def printZeros(x):
    total = range(33-x)
    for i in total:
        print(0,end=',')

#printZeros(5)

import random

def printRandom():
    total = range(33)
    for i in total:
        print(random.randint(0,5), end=",")

#printRandom()



import json

with open('answers.json') as f:
    data = json.load(f)

keys = list(data[0])

for q in data:
    print(f'{[q["question"]]}:{[q["answer"]]}')
    




