#HW 4 problem 1
#sean maroongroge

from enum import Enum
import numpy as np

#define variables
COST_TO_PLAY = 250
GAIN_PER_WIN = 100

#enumerate heads and tails
class Flip_Result(Enum):
    HEADS = 1
    TAILS = 0

#flip a single coin
class single_flip:
    def __init__(self, flip_id):
        self._flip_id = flip_id
        self._rnd = np.random
        self._rnd.seed(flip_id)
        self._flip_result = Flip_Result.HEADS

    def simulate(self):
        if self._rnd.sample() < 0.5:
            self._flip_result = Flip_Result.TAILS
        else:
            self._flip_result = Flip_Result.HEADS

    def get_single_flip_result(self):
        return self._flip_result  #note: if I use this function and try to print the object, I get the memory pointer and not the actual result variable, so just ignore this function for now


#create a cohort (list) of coins within 1 game
class cohort_of_flips:
    def __init__(self, cohort_id, number_of_flips):
        self._cohort_id = cohort_id
        self._number_of_flips = number_of_flips
        self._list_of_flips = [] #just populate a list with flip objects (with unique IDs)
        self._list_of_flip_results = [] #populate another list with flip results
        self._cohort_reward_amount = 0


        #populate the list with the single flip objects (no results)
        for flip_number in range(number_of_flips):
            flip = single_flip(cohort_id*number_of_flips + flip_number)
            self._list_of_flips.append(flip)

    def simulate(self):

        #populate the list of flip results
        for flip in self._list_of_flips:
            flip.simulate()                  #remember you actually need to run the simulation..
            self._list_of_flip_results.append(flip._flip_result) #append the result
            #print (flip._flip_result)

        #calculate the total reward amount for this list
        self._cohort_reward_amount = -COST_TO_PLAY #start at -250

        #for each "win", add 100 to reward
        self._list_of_flip_results_length = len(self._list_of_flip_results)
        for index, obj in enumerate(self._list_of_flip_results):
            if index > 1:
                self._super_previous_item = self._list_of_flip_results[index - 2]
                self._previous_item = self._list_of_flip_results[index - 1]
                if obj.value == 1 and self._super_previous_item.value ==0 and self._previous_item.value ==0:
                #    print("trial number", index, obj.value, self._super_previous_item.value, self._previous_item.value, "this is a win")
                    self._cohort_reward_amount += 100

                #remember with enumerate to call object values as opposed to objects themselves, using obj.value==1, not obj==1
                #if obj.value ==1:
                #    print('obj is equal to 1')
                #if obj.value ==0:
                #    print('obj is equal to 0')

    #return the reward amount for this single game (single cohort of flips)
    def get_cohort_reward_amount(self):
        return self._cohort_reward_amount


#simulate 1000 games

class cohort_of_games:
    #create the list of games that happened
    def __init__(self, number_of_games, number_of_flips):
        self._number_of_flips = number_of_flips #maybe not needed
        self._number_of_games = number_of_games
        self._list_of_games = []
        self._list_of_game_rewards = []

        for game_id in range(self._number_of_games):
            ThisCohortofFlips = cohort_of_flips(cohort_id = game_id, number_of_flips = self._number_of_flips)
            ThisCohortofFlips.simulate()
            self._list_of_games.append(ThisCohortofFlips)

    #simulate the games to generate the list of rewards for all 1000 games in a list
    def simulate(self):
        for game in self._list_of_games:
            self._list_of_game_rewards.append(game.get_cohort_reward_amount())

    #calculate and return the average of this list of rewards over the entire simulation
    def get_average_reward_amount(self):
        average_reward_amount = sum(self._list_of_game_rewards)/len(self._list_of_game_rewards)
        return average_reward_amount


myCohortofGames = cohort_of_games(number_of_games=1000, number_of_flips=20)
myCohortofGames.simulate()
print(myCohortofGames.get_average_reward_amount())


#test code to make sure single cohorts work
#MyCohort = cohort_of_flips(cohort_id=1, number_of_flips=20)
#MyCohort.simulate()
#print(MyCohort.get_cohort_reward_amount())
#for some reason I can use the get function here but not with the individual flips..#print(MyCohort._cohort_reward_amount)


#other tests:
#MyCoinFlip = single_flip(flip_id=1)
#print(MyCoinFlip.get_single_flip_result())
#print(MyCoinFlip._flip_result)

#testcoin = single_flip(flip_id=1)
#testcoin.simulate()
#print(testcoin._flip_result)
#if testcoin._flip_result==1:
#    print("enum works and heads")
#if testcoin._flip_result==0:
#    print("enum works and tails")
#else:
#    print("enum not working")

#class Color(Enum):
#    RED = 1
#    GREEN = 2
#    BLUE = 3
#print(Color.RED)
#print(repr(Color.RED))
#print(repr(Flip_Result.HEADS))

#if Flip_Result.HEADS.value == 1:
#    print("enum works")
#else:
#    print ("not working")
