import Mastermind_feetback as fb
import Mastermind_newgame as ng
import Mastermind_guess as gs




def run_x_times(x):
    list=[]
    for i in range (0,x):
        code = ng.random_code()
        print(code)
        all_options = ng.create_options()
        all_feetback = ng.create_all__feetback()
        counter = 0
        while True:
#            guess = gs.take_random_guess(all_options)
            guess= gs.worstcase_strat(all_options,all_feetback)
            print(guess)
            counter +=1
            if fb.win(code, guess):
                break
            feetback_guess = fb.feetback(code,guess)
            gs.remove_options(all_options,feetback_guess ,guess)
        print("you've done well {} try's".format(counter))
        list.append(counter)
    print(sum(list) / len(list))

def own_code():
    code = ng.own_code()
    all_options = ng.create_options()
    all_feetback = ng.create_all__feetback()
    counter = 0
    while True:
#        guess = gs.take_random_guess(all_options)
        guess = gs.worstcase_strat(all_options, all_feetback)
        print(guess)
        counter += 1
        if fb.win(code, guess):
            break
        feetback_guess = fb.feetback(code, guess)
        print(feetback_guess)
        gs.remove_options(all_options, feetback_guess, guess)
    print("you're code has been discovered in {} try's".format(counter))

own_code()