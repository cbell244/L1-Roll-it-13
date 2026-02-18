#initialise list to hold have history
game_history = []

# get data (base component does this already, code below for testing purposes,)
user_score = 0
comp_score = 0

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("User points? "))
    comp_points = int(input("Computer points? "))
    winner = input("Who won? ")
    user_score = int(input("User score? "))
    comp_score = int(input("Computer score? "))

    game_results = (f"Round {rounds_played}: User points {user_points} | "
                    f"Computer points {comp_points}, {winner} wins "
                    f"({user_score} | {comp_score}) ")

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)

rounds_played = input("Round? ")
user_points = int(input("User points? "))
comp_points = int(input("Computer points? "))