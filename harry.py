# import termcolor

from logic import *

# rain = Symbol("rain") #it is raining
# hagrid =Symbol("hagrid")#harry visited Hagrid
# dumbledore= Symbol("dumbledore") #harry visited dumvledore

# knowledge = And(Implication(Not(rain), hagrid),Or(hagrid, dumbledore),Not(And(hagrid,dumbledore)), dumbledore)

# print(model_check(knowledge, hagrid))
# print(knowledge.formula())


mustard = Symbol("mustard")
plum= Symbol("plum")
scarlet= Symbol("scarlet")
characters=[mustard,plum,scarlet]

ballroom = Symbol("ballroom")
kitchen= Symbol("kitchen")
library= Symbol("library")
rooms=[ballroom,kitchen,library]

knife = Symbol("knife")
revolver= Symbol("revolver")
wrench= Symbol("wrench")
weapons=[knife,revolver,wrench]

symbols = characters+rooms+weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: YES")
        elif not model_check(knowledge,Not(symbol)):
            print(f"{symbol}: MAYBE")

knowledge =And(Or(mustard,plum,scarlet),Or(ballroom,kitchen,library), Or(knife,revolver,wrench))

knowledge.add(Not(mustard))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))

knowledge.add(Or(Not(scarlet),Not(library),Not(wrench)))

knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

print(knowledge.formula())

check_knowledge(knowledge)