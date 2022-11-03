#Cathy Doherty and Amanda Miloserny
rvc= {"flour" : 3, "eggs": 2, "milk": 4, "butter" : 1, "chocolate": 1}
lc= {"flour" : 3, "eggs": 2, "milk": 4, "butter" : 1, "lemon" : 1}
def cakes():
    match = []
    x = rvc
    y = lc
    for ingredient in x:
        if ingredient in y:
            match.append(ingredient)
    print(match)
cakes()
