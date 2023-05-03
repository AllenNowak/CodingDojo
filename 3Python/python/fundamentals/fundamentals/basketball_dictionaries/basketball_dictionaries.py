# python/fundamentals/fundamentals/basketball_dictionaries

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

'''
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

Challenge 1: Update the constructor
    to accept a dictionary with a single player's information instead of individual arguments for the attributes.
'''
class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
    def __repr__(self):
        return f'Player: name - {self.name}, age - {self.age}, position - {self.position}, team - {self.team}'
    '''Ninja Bonus: 
        Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates 
        and returns a new list of Player objects.
    '''
    @classmethod
    def get_team(cls, team_list):
        cls.player_list = []
        for dictionary in team_list:
            cls.player_list.append(Player(dictionary))
        return cls.player_list

'''
Challenge 2: Create instances using individual player dictionaries.
Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.'''
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


'''
Challenge 3: Make a list of Player instances from a list of dictionaries
Finally, given the example list of players at the top of this module 
(the one with many players) write a for loop that will populate an empty list 
with Player objects from the original list of dictionaries.'''

# ... (class definition and large list of players here)
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
for p in players:
    new_team.append(Player(p))

print('Provided team is now:')
for player in new_team:
    print (player)

'''
NINJA BONUS: Add a get_team(cls, team_list) @class method
Add an @class method called get_team(cls, team_list) that, given a list of dictionaries 
populates and returns a new list of Player objects. Be sure to test your method!'''



bulls_1990 = [
    {
    	"name": "Michael Jordan", 
    	"age": 27, 
    	"position": "Shooting Guard", 
    	"team": "Chicago Bulls"
    },
    {
    	"name": "Scottie Pippen", 
    	"age":24, 
    	"position": "Small Forward", 
    	"team": "Chicago Bulls"
    },
    {
    	"name": "Horace Grant", 
    	"age": 25,
        "position": "Power Forward", 
    	"team": "Chicago Bulls"
    },
    {
    	"name": "Bill Cartwright", 
    	"age": 33,
        "position": "Center", 
    	"team": "Chicago Bulls"
    },
    {
    	"name": "John Paxson", 
    	"age": 30,
        "position": "Point Guard", 
    	"team": "Chicago Bulls"
    },
    {
        "name": "BJ Armstrong",
        "age": 23,
        "position": "Point Guard",
    	"team": "Chicago Bulls"
    }
]

nba_champs = Player.get_team(bulls_1990)

print('\nThe 1991 NBA Champions:')
for player in nba_champs:
    print(player)



dream_team_1992 = [
    {
    	"name": "Michael Jordan", 
    	"age": 29, 
    	"position": "Shooting Guard", 
    	"team": "Chicago Bulls"
    },
    {
    	"name": "Scottie Pippen", 
    	"age":26, 
    	"position": "Small Forward", 
    	"team": "Chicago Bulls"
    },
    {
    	"name": "Charles Barkley", 
    	"age": 29, 
    	"position": "Power Forward", 
    	"team": "Phoenix Suns"
    },
    {
    	"name": "Karl Malone", 
    	"age":28, 
    	"position": "Power Forward", 
    	"team": "Utah Jazz"
    },
    {
    	"name": "John Stockton", 
    	"age":30, 
    	"position": "Point Guard", 
    	"team": "Utah Jazz"
    },
    {
    	"name": "Clyde Drexler", 
    	"age": 30, 
    	"position": "Shooting Guard", 
    	"team": "Portland Trail Blazers"
    },
    {
    	"name": "Magic Johnson", 
    	"age":32, 
    	"position": "Point Guard", 
    	"team": "LA Lakers"
    },
    {
    	"name": "Patrick Ewing", 
    	"age": 29, 
    	"position": "Center", 
    	"team": "New York Knicks"
    },
    {
    	"name": "Larry Bird", 
    	"age":35, 
    	"position": "Small Forward", 
    	"team": "Boston Celtics"
    },
]

print('\nThe 1992 Olympic Dream Team:')
world_champs = Player.get_team(dream_team_1992)
for player in world_champs:
    print(player)






