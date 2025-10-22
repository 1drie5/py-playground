"""

Write a program to input player's name (string) and runs (integer) scored for n number of players where n should be input from the keyboard. Store the player's details in a dictionary called 'cricket'. After preparing the dictionary, input the player's name and print the runs scored by the player otherwise returns'-1' if the player's name is not found.

"""

num_players = int(input("Enter the number of players: "))

cricket = {}

for i in range(num_players):
    player_name = input("Enter Player's Name: ")
    runs = int(input("Enter Runs Scored: "))
    cricket[player_name] = runs

num_queries = int(input("Enter the number of players to search: "))

for i in range(num_queries):
    query_name = input("Enter Player's Name to search: ")
    if query_name in cricket:
        print("Score:", cricket[query_name])
    else:
        print(-1)
