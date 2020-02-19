import random

def random_code():
    amount_of_colours = 6
    a=random.randint(0, amount_of_colours-1)
    b=random.randint(0, amount_of_colours-1)
    c=random.randint(0, amount_of_colours-1)
    d=random.randint(0, amount_of_colours-1)
    code = (a,b,c,d)
    return (code)

def own_code():
    a = input ("Chose you coulers, 0 to 5, one at a time \nColour 1 ")
    b = input("Colour 2 ")
    c = input("Colour 3 ")
    d = input("Colour 4 ")
    code = (int(a), int(b), int(c), int(d))
    return (code)

def create_options():
    amount_of_colours = 6
    optional_codes = []
    for i in range(0, amount_of_colours):
        for j in range(0, amount_of_colours):
            for k in range(0, amount_of_colours):
                for l in range(0, amount_of_colours):
                    option = (i, j, k, l)
                    optional_codes.append(option)
                    l +=1
                k +=1
            j += 1
        i +=1

    return optional_codes

def create_all__feetback ():
    all_feetback = []
    for i in range (0,5):
        for j in range (0,5):
            option = (i,j)
            all_feetback.append(option)
            j+=1
        i+=1
    return all_feetback
