class User:
    def __init__(self, first_name, last_name, email, age, is_rewards=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards = is_rewards
        self.gold_card_points = gold_card_points
    # from StackOverflow: https://stackoverflow.com/questions/1251692/how-to-enumerate-an-objects-properties-in-python

    def display_info(self):
        print('Displaying User Info')
        for property, value in vars(self).items():
            print(property, ":", value)
        print()

    def enroll(self):
        if (self.is_rewards):
            print(f'User already a member.')
            return False
        self.is_rewards = True
        self.gold_card_points = 200
        return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f'{amount} exceeds balance: {self.gold_card_points}')
            return
        self.gold_card_points -= amount


# In the outer scope, create a user instance and call the display_info method to test.
print('Instantiating a User')
john_doe = User('john', 'doe', 'jdoe@aol.com', 66)
john_doe.display_info()

# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
print('Enrolling the user')
john_doe.enroll()
john_doe.display_info()

# Make 2 more instances of the User class.
jane_doe = User('jane', 'doe', 'invalid@email.com', 61)
junior_doe = User('jimmy', 'doe', 'another@compuserve.com', 43)

# Implement the spend_points(self, amount) method
# Have the first user spend 50 points
print('First user spends 50 points')
john_doe.spend_points(50)

# Have the second user enroll.
print('Have the second user enroll.')
jane_doe.enroll()
# Have the second user spend 80 points
print('Have the second user spend 80 points')
jane_doe.spend_points(80)

print()
# Call the display method on all the users.
print('Call the display method on all the users.')
for j in [john_doe, jane_doe, junior_doe]:
    j.display_info()


# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
print('Trying to re-enroll user 1')
john_doe.enroll()
john_doe.display_info()

# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
print('Trying to overspend user 3')
junior_doe.spend_points(40)
junior_doe.display_info()
