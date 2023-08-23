import random

class SubPhase:
    '''
        Manages manages the dice-roll-process of each subphase, will run a propriate mini-script based on what statemant used. 
        Child: Dice
    '''

    # def __init__(self, sub_phase, a_input, ):
    #     match sub_phase:
    #         case "attacks" | "attack":
    #             res = self.attack_roll(a_input)
    #         case "hit":
    #             res = self.hit_roll(a_input)
    #         case "wound":
    #             res = self.wound_roll(a_input)
    #         case "damage":
    #             res = self.damage_roll(a_input)
    #         case "savingthrow":
    #             res = self.savingthrow_roll(a_input)
    #         case "invulnerable":
    #             res = self.invulnerable_save_roll(a_input)
    #         case _:
    #             print(f"TODO: make {sub_phase} statement")
    #     self.roll_res = res 


    def attack_roll(self, a_input) -> int:
        ''' some descr.. '''
        #return Dice(self.numdice, self.sides).parse_dice_input(a_input) ##OLD VERSION
        try: 
            if int(a_input):
                '''
                    a_input = num attacks (e.g. 6, 1, 3,) and not string("2d3, 1d3") 
                    which means; no need to roll for amount of attacks 
                    --> pass straight to hit_roll
                '''
                return int(a_input)
        except ValueError:
            return sum(Dice().roll(a_input))
        # if type(a_input) == int:    #checks if a input is int which means; 
        #     print(type(a_input))
        #     '''
        #         a_input = num attacks (e.g. 6, 1, 3,) and not string("2d3, 1d3") 
        #         which means; no need to roll for amount of attacks 
        #         --> pass straight to hit_roll
        #     '''
        #     return a_input
        # else:
        #     print(type(a_input))
        #     #return sum(Dice().roll(a_input))

    def hit_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

    def wound_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

    def damage_roll(self, D, num_not_saved) -> int:
        ''' some descr.. '''
        try: 
            if int(D):
                damage_delt = int(D)*num_not_saved
                print(damage_delt)
        except ValueError:
            damage_delt = sum(Dice().roll(D)) * num_not_saved
            print(damage_delt)
        return damage_delt
    
        #return Dice().parse_dice_input(a_input)

    def savingthrow_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

    def invulnerable_save_roll(self, a_input) -> int:
        ''' some descr.. '''
        return Dice().parse_dice_input(a_input)

class Dice(SubPhase):
    '''
        Controlls all dice rolls 
    '''
    def __init__(self,):
        self.numdice = None 
        self.sides = None 
        self.constant = 0
        self.valid_dice = [3,6]


    def parse_dice_input(self,a_input:str or int) -> [int, int]:  #NB; do not know the correct annotation for setters (this techinically does not return anything)
        ''' 
            first check if input uses valid dice 
            then check if input contains a mix between dice rolls and constant attacks, e.g.: 2d6+3
            Then check if input string does not contain a numdice (common for when only 1 die is used, e.g.: 1d6 = d6 ) 
            Finally removes "d" character, splits string and sets numdice and sides.
        '''
        print(a_input)
        if int(a_input.lower().split("d")[1].split("+")[0]) not in self.valid_dice :
            raise ValueError("invalid dice type, the die can only be a 3 sided or 6 sided")        
        if "+" in a_input:
            a_input, self.constant = a_input.split("+")
        if a_input[0].lower() == "d":
            self.numdice = 1
            self.sides = int(a_input[1:])
        else:
            self.numdice, self.sides = [int(i) for i in a_input.lower().split("d")]
        


    def roll(self, a_input) -> [int]:
        '''
            first calls parse_dice_input to convert string input to numdice & sides
            then makes the rolls and returns list of results 
        '''

        self.parse_dice_input(a_input)
        dice_roll = []
        for _ in range(int(self.numdice)):
            dice_roll.append(random.randint(1, self.sides))
        print(dice_roll+[int(self.constant)])
        return dice_roll+[int(self.constant)]


def shooting_phase_timeline(self):
    # 1. make rolls for or get number of attacks being made

    
    # 2. make hit rolls 
    
    # 3. make wound rolls 
    
    # 4. make damage roll
    
    # 5. make saving throws
    pass
''' OLD VERSION 
# This function returns the amount of integers in the list that is above the hit number
def check_hits(hit_number, rolled_dice):
    total_hit_number = 0
    length = len(rolled_dice)
    # print(length)
    for hits in rolled_dice:
        if hits >= int(hit_number):
            total_hit_number += 1
    return total_hit_number
'''

def main():
    '''
        some
    '''
    a_input = "2d6+3"
    num_attacks = SubPhase().attack_roll(a_input)
    print(f"num_attacks: {num_attacks}")


if __name__ == '__main__':
    main()



