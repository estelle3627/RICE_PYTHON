# Rock-paper-scissors-lizard-Spock

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# import the random library at the beginning
import random

# helper functions

def number_to_name(number):
    '''
    This helper function translates number into name.
    Number has to be 0, 1, 2, 3 or 4
    '''
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        name = ''
        print 'Please provide correct number'
    
    return name


def name_to_number(name):
    '''
    This helper function translates name to number.
    The input name has to be valid for the game.
    '''
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1        
    elif name == 'paper':
        number = 2        
    elif name == 'lizard':
        number = 3        
    elif name == 'scissors':
        number = 4        
    else:
        number = -1
        print 'Please provide correct name'
    
    return number
    
    
def rpsls(name): 
    '''
    The main function that runs the game.
    '''
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # compute difference of player_number and comp_number modulo five
    diff_mod_5 = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if diff_mod_5 == 1 or diff_mod_5 == 2:
        player_wins = 1
    elif diff_mod_5 == 3 or diff_mod_5 == 4:
        player_wins = -1
    else:
        player_wins = 0
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    # print results
    print "Player chooses " + name
    print "Computer chooses " + comp_name
    if player_wins == 1:
        print "Player wins!"
    elif player_wins == -1:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    # print a new line, in order to match the sample output.    
    print ""
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
