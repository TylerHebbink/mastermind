def win(code, guess):
    if code==guess:
        return True

def feetback(code, guess):
    right_couler = 0
    right_place = 0
    for j in range(0,len(code)):
        if guess[j] == code[j]:
            right_place += 1
    for l in range(0,len(guess)):
        if guess[l] != code[l] and guess[l] in code:
            right_couler += 1
    right_pins = (right_place,right_couler)
    return right_pins