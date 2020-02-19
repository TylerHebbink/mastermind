import random
import Mastermind_feetback as fb

def take_random_guess(all_options):
    guess_num= random.randint(0,len(all_options)-1)
    guess = all_options[guess_num]
    return guess

def remove_options(all_options,feetback_guess,guess):
    for i in all_options:
        option_fb = fb.feetback(i,guess)
        if option_fb != feetback_guess:
            all_options.remove(i)


def worstcase_strat(all_options,all_feetback):
    worstcase = 10000
    worstcase_code = []
    for i in all_options:
        code = i
        highest = 0
        feetback_wc = []
        for j in all_feetback:
            counter = 0
            for k in all_options:
                option = fb.feetback(k, code)
                if option == j:
                    counter += 1
            if counter > highest:
                highest = counter
                feetback_wc.clear()
                feetback_wc.append(j)
        if highest < worstcase:
            worstcase = highest
            worstcase_code.clear()
            worstcase_code.append(i)
    return worstcase_code[0]




