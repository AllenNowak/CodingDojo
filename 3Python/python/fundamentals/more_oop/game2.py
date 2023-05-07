from game_classes.pirate import Pirate
from game_classes.wookie import Wookie

pirate = Pirate('Ahab', 45, 30, 30, 2.0, 4, '', '', True, True, True)
wookie = Wookie('Chewie', 80, 5, 50, 1, 1, '', '')

def get_user():
    combatants = {'user': None, 'opponent': None }
    user = ''
    while user.upper() != 'W' and user.upper() != 'P':
        user = input('Are you a [W]ookie? Or a [P]irate?')
    choice = user.upper()
    if choice == 'W':
        combatants = {'user': wookie, 'opponent': pirate }
    else:
        combatants = {'user': pirate, 'opponent': wookie }

    return combatants

def fight(user, opponent):
    while user.health > 0 and opponent.health > 0:
        response = ''
        while not response.isnumeric():
            response = input('Next Move: 1)Attack\n 2)Defend 3) Heal 4)Use Special\n 5)Use Buff\n 6)Heal\n 7)Trash Talk')
            
        if response < 0 and response > 7:
            continue

        handle_move(response, user, opponent)

def handle_move(move_num, user, opponent):
    match move_num:
        case 1:
            user.attack(opponent)
        case 2:
            user.defend()
        case 3:
        case 4:
        case 5:
        case 6:
        case 7:

def game_loop():
    response = ''
    while not response.upper() != 'Y' and response.upper() != 'N':
        response = input('Play again? [Y | N]')

    # get user
    players = get_user()
    # fight
    fight(players['user'], players['opponent'])

        
print ('This is Wookie vs Pirate!')
game_loop()



        
