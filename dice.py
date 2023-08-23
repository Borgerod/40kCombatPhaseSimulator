import random
from subphase import SubPhase

class Dice(SubPhase):
    '''
        Controlls all dice rolls 
    '''
    def __init__(self,):# numdice, sides, ):
        self.numdice = None#numdice
        self.sides = None#sides
        self.valid_dice = [3,6]

    def parse_dice_input(self,a_input:str or int) -> [int, int]:  #NB; do not know the correct annotation for setters (this techinically does not return anything)
        '''
            first check if input uses valid dice 
            Then check if input string does not contain a numdice (common for when only 1 die is used, e.g.: 1d6 = d6 ) 
            Finally removes "d" character, splits string and sets numdice and sides.
        '''
        if int(a_input[-1]) not in [3, 6]:
            raise ValueError("invalid dice type, the die can only be a 3 sided or 6 sided")
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
        return dice_roll

