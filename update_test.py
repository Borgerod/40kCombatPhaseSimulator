import random
#from dice import Dice

class SubPhase:
    '''
        Manages manages the dice-roll-process of each subphase, will run a propriate mini-script based on what statemant used. 
        Child: Dice
    '''

    def __init__(self, sub_phase, a_input, ):
        match sub_phase:
            case "attacks" | "attack":
                res = self.attack_roll(a_input)
            case "hit":
                res = self.hit_roll(a_input)
            case "wound":
                res = self.wound_roll(a_input)
            case "damage":
                res = self.damage_roll(a_input)
            case "savingthrow":
                res = self.savingthrow_roll(a_input)
            case "invulnerable":
                res = self.invulnerable_save_roll(a_input)
            case _:
                print(f"TODO: make {sub_phase} statement")
        self.roll_res = res 
            
    # def get_roll(self) -> int:
    #     '''umbrella function that will simply get which ever statement that was requested'''
    #     return res
    

    def attack_roll(self, a_input) -> int:
        ''' some descr.. '''
        #return Dice(self.numdice, self.sides).parse_dice_input(a_input) ##OLD VERSION
        if type(a_input) == int:    #checks if a input is int which means; 
            '''
                a_input = num attacks (e.g. 6, 1, 3,) and not string("2d3, 1d3") 
                which means; no need to roll for amount of attacks 
                --> pass straight to hit_roll
            '''
            return 1
        return sum(Dice().roll(a_input))

    def hit_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

    def wound_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

    def damage_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

    def savingthrow_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

    def invulnerable_save_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

def shooting_phase_timeline(self):
    # 1. make rolls for or get number of attacks being made

    
    # 2. make hit rolls 
    
    # 3. make wound rolls 
    
    # 4. make damage roll
    
    # 5. make saving throws
    pass


def main():
    '''
        some
    '''
    a_input = "2d6"
    num_attacks = SubPhase("attack", a_input).roll_res
    print(f"num_attacks: {num_attacks}")


if __name__ == '__main__':
    main()



