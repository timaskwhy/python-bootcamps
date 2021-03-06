import random
from arts import rock, paper, scissors

# TODO: add more game modes
# types_of_match = ['singles', 'tournament', 'battle-royale', 'win-streak', 'team']

'''
Assumption #1
There are 3 weapons.
The weapons are ordered.
Each weapon beats the previous one.
'''
arts = [rock, paper, scissors]
weapons = ['rock', 'paper', 'scissors']

num_of_computers = int(input("How many computers you want in a game?\n"))
choices = []

'''
Meaning of values
None: the condition is chaos, neither player wins nor loses, and we cannot find a winner.
<Int>: represent player who choose with this number win the game, where the number represents a weapon.
'''
winning_weapon = 0
winners = []

# Set players and choices
me = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices.append(me)
for i in range(num_of_computers):
    choices.append(random.randint(0, 2))

# Show the choices
for i, v in enumerate(choices):
    name = 'You' if i == 0 else 'Computer ' + str(i)
    print(f"{name} chose: {weapons[v]}")
    print(arts[v])

unique_choices = []
for v in choices:
    if not v in unique_choices:
        unique_choices.append(v)

# We can find the winner only when we are able to compare the choices
if len(unique_choices) != 2:
    winning_weapon = None

if winning_weapon is None:
    print('Draw')
else:
    # Check if the choices are consecutive
    abs_diff = abs(unique_choices[0] - unique_choices[1])
    if (abs_diff == 1):
        is_consecutive = True
    else:
        is_consecutive = False

    '''
    Pattern
    If both numbers are the same, no one wins
    If both numbers are consecutive, the bigger one wins
    If both numbers aren't consecutive, the smaller one wins

    Detailed explaination here:
    https://dev.to/eduherminio/rock-paper-scissors-a-mathematical-approach-33dj
    '''

    # Find winning weapon
    if is_consecutive:  # 連續數
        '''
        if me == 1 (paper) and opponent == 0 (rock), then winning_weapon = 1, you win
        if me == 2 (scissors) and opponent == 1 (paper), then winning_weapon = 2, you win
        if me == 0 (rock) and opponent == 1 (paper), then winning_weapon = 1, you lose
        if me == 1 (paper) and opponent == 2 (scissors), then winning_weapon = 2, you lose
        '''

        winning_weapon = max(unique_choices)

        '''
        Equivalent to the following

        if a > b:
            print('win')
        else:
            print('lose')
        '''

    elif not is_consecutive:  # 非連續數
        '''
        if me == 2 and opponent == 0, then winning_weapon = 0, you lose
        if me == 0 and opponent == 2: then winning_weapon = 0, you win
        '''

        winning_weapon = min(unique_choices)

        '''
        Equivalent to the following
        
        if a < b:
            print('win')
        else:
            print('lose')
        '''

    # Find winners
    for i, v in enumerate(choices):
        if v == winning_weapon:
            if i == 0:
                name = 'You'
            else:
                name = 'Computer ' + str(i)
            winners.append(name)

    # Judge my win-lose
    if 'You' in winners:
        print('You win')
    else:
        print('You lose...')
