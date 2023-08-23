#TODO finish find_best_sv() and feel_no_paint()

def find_best_sv() -> int:
    '''
        some characters has involneruble saves or similar. 
        This function will pick the best SV to use according to the situation
    '''
    SV = get_sv()
    inv_save = get_inv_save()
    alt_saves = get_alt_save() # E.g. Demon save, etc
    mortal_wounds = ()

    
    best_sv = 0

    return best_sv

def feel_no_paint():
    '''
        after saving throw is made, if defender has feel no pain ability, the defender make a fell_no_pain_roll
        on critical hit: no wound is lost 
    '''
    return None