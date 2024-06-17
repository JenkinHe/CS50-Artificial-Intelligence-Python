from logic import *

rain = Symbol("rain") #it is raining
hagrid =Symbol("hagrid")#harry visited Hagrid
dumbledore= Symbol("dumbledore") #harry visited dumvledore

knowledge = And(Implication(Not(rain), hagrid),Or(hagrid, dumbledore),Not(And(hagrid,dumbledore)), dumbledore)

print(knowledge.formula())