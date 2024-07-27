# Player from 1-4: Blue Team
# Player from 5-8: Red Team
# Round calculator end when 1 vs x

player_names = []
player_names_start = player_names
d_p = 0
blueDie = 0
redDie = 0
dead_table = []
stack3v3Blue = []
stack3v3Red = []
not_enough_player = False
round_change_rule = 999999

# matchups round table when 0
# Base matchups table
matchups_table = [
    [(1, 6), (2, 7), (3, 8), (4, 5)],
    [(1, 5), (2, 6), (3, 7), (4, 8)],
    [(1, 8), (2, 5), (3, 6), (4, 7)],
    [(1, 7), (2, 8), (3, 5), (4, 6)]
]

def swap(n1, n2):
    tmp = n1
    n1 = n2
    n2 = tmp

# Complete matchups table
for i in range(4, 51):
    matchups_table.append(matchups_table[i % 4])

# Get player's name when start game
def get_player(number_player):
    for i in range(0, number_player):
        name = input(f"Enter player {i+1} name: ")
        player_names.append(name)

def print_player():
    for i in range(player_names.size()):
        print(f"{i} : {player_names[i]}")

def replace4vs3(deadPlayer, ePlayer):
    #              1 - blueTeam -1: 2->1; 3->2; 4->3
    if (ePlayer == 7 and deadPlayer == 1):
        return player_names_start[2] + "copy" #7-2 --> 7-3
    if (ePlayer == 6 and deadPlayer == 1):
        return player_names_start[3] + "copy" #6-3
    if (ePlayer == 5 and deadPlayer == 1):
        return player_names_start[1] + "copy" #5-1
    if (ePlayer == 8 and deadPlayer == 1):
        return player_names_start[2] + "copy" #8-1 testcase 2

    #              2
    if (ePlayer == 7 and deadPlayer == 2):
        return player_names_start[0] + "copy" #7-4 sau 20, 7-2 truoc 20
    if (ePlayer == 6 and deadPlayer == 2):
        return player_names_start[3] + "copy" #6-3 ?
    if (ePlayer == 5 and deadPlayer == 2):
        return player_names_start[2] + "copy" #5-3
    if (ePlayer == 8 and deadPlayer == 2):
        return player_names_start[2] + "copy" #8-3
    
    #               3
    if (ePlayer == 5 and deadPlayer == 3):
        return player_names_start[5] + "copy" #5
    if (ePlayer == 6 and deadPlayer == 3):
        return player_names_start[5] + "copy" #6
    if (ePlayer == 7 and deadPlayer == 3):
        return player_names_start[0] + "copy" #7-1
    if (ePlayer == 8 and deadPlayer == 3):
        return player_names_start[3] + "copy" #8-4
    
    #               4
    if (ePlayer == 7 and deadPlayer == 4):
        return player_names_start[1] + "copy" #7-2
    if (ePlayer == 6 and deadPlayer == 4):
        return player_names_start[2] + "copy" #6-3
    if (ePlayer == 5 and deadPlayer == 4):
        return player_names_start[0] + "copy" #5-1
    if (ePlayer == 8 and deadPlayer == 4):
        return player_names_start[1] + "copy" #8-1 testcase 2 (round > 30). 8-2 testcase 9
    
    #               5
    if (ePlayer == 3 and deadPlayer == 5):
        return player_names_start[5] + "copy" #3-6
    if (ePlayer == 4 and deadPlayer == 5):
        return player_names_start[5] + "copy" #4-6
    if (ePlayer == 1 and deadPlayer == 5):
        return player_names_start[5] + "copy" #1-6  
    if (ePlayer == 2 and deadPlayer == 5):
        return player_names_start[6] + "copy" #2-7  // du doan
    
    #               6
    if (ePlayer == 3 and deadPlayer == 6):
        return player_names_start[5] + "copy" #3-5 ??
    if (ePlayer == 4 and deadPlayer == 6):
        return player_names_start[4] + "copy" #4-5
    if (ePlayer == 1 and deadPlayer == 6):
        return player_names_start[4] + "copy" #1-5  
    if (ePlayer == 2 and deadPlayer == 6):
        return player_names_start[6] + "copy" #2-7  ??
    

    #               8
    if (ePlayer == 3 and deadPlayer == 6):
        return player_names_start[5] + "copy" #3-5 ??
    if (ePlayer == 4 and deadPlayer == 6):
        return player_names_start[4] + "copy" #4-5
    if (ePlayer == 1 and deadPlayer == 6):
        return player_names_start[5] + "copy" #1-5  ??
    if (ePlayer == 2 and deadPlayer == 6):
        return player_names_start[6] + "copy" #2-7  ??
def replace4v2(roundNum, deadPlayer1, deadPlayer2):
    pass

def replace3v3(preRound, roundNum, deadPlayerBlue, deadPlayerRed):
    # Swap deadPlayerRed and deadPlayerBlue if necessary
    if deadPlayerBlue > deadPlayerRed:
        deadPlayerBlue, deadPlayerRed = deadPlayerRed, deadPlayerBlue

    # Increment roundNum by 3
    roundNum += 3

    # Adjust roundNum based on certain conditions
    if preRound in {23, 28, 33, 38}:
        roundNum += 1

    # Reset the stacks
    stack3v3Blue.clear()
    stack3v3Red.clear()

    # Copy to stack player
    for i in range(3):
        if i != deadPlayerBlue:
            stack3v3Blue.append(i)
    
    for i in range(4, 7):
        if i != deadPlayerRed:
            stack3v3Red.append(i)
    
    # Process the matchups for the current round
    for matchup in matchups_table[roundNum]:
        print(f"Round: {roundNum}")
        
        # Check if current matchup should be skipped
        if (deadPlayerBlue == matchup[0] - 1 and deadPlayerRed == matchup[1] - 1):
            continue

        # Print matchups where neither dead player is involved
        if (deadPlayerBlue != matchup[0] - 1 and deadPlayerRed != matchup[1] - 1):
            print(f"{player_names_start[matchup[0] - 1]} - {player_names_start[matchup[1] - 1]}")
            
            # Remove the player from stack3v3Blue if involved in the matchup
            if matchup[0] - 1 in stack3v3Blue:
                stack3v3Blue.remove(matchup[0] - 1)
            
            # Remove the player from stack3v3Red if involved in the matchup
            if matchup[1] - 1 in stack3v3Red:
                stack3v3Red.remove(matchup[1] - 1)

        # Print matchups involving one of the dead players
        if deadPlayerBlue != matchup[0] - 1:
            if stack3v3Red:
                print(f"{player_names_start[matchup[0] - 1]} - {player_names_start[stack3v3Red[-1]]}")
                stack3v3Red.pop()
                stack3v3Blue.remove(matchup[0] - 1)



#                           GAME LOOP
def game(player_names, d_p, round_num):
    global round_change_rule, not_enough_player
    #------------------ Const
    while redDie != 1 or blueDie != 1:
        if round_num == 10 or round_num == 15 or round_num == 20 or round_num == 25 or round_num == 30 or round_num == 35 or round_num == 40:
            print(f"Round {round_num}: Round quai !")
            round_num += 1
            continue
        # Round "Doi mat"
        elif round_num in [9, 14, 19, 24, 29, 34, 39]:
            print(f"Round: {round_num}: Doi mat --------")
            round_num += 1
            command = input("Have any players died? (y/n): ")
            if command.lower() == 'y':
                NOdeadPlayer = int(input("Enter the number dead player: "))
                for i in range(NOdeadPlayer):
                    d_p = input("Enter the index of dead player: ")
                    dead_table.append(d_p)
                    # Change name of dead player
                    player_names[d_p-1] = player_names[d_p - 1] + "XXXXXXXXXXXXXXX"
                    if (d_p > 4):
                        redDie = redDie + 1
                    else:
                        blueDie = blueDie + 1
            else:
                d_p = 0
                round_num += 1
            continue
        if (redDie == 0 and blueDie == 0):
        #--------------------------------4 v 4
        # Print the matchups for the round
            print(f"Round {round_num}:")
            for matchup in matchups_table[round_num]:
                print(f"{player_names[matchup[0]-1]} - {player_names[matchup[1]-1]}")
        #------------------------------------
        else: 
            if((redDie + blueDie) == 1):
                #---------------------4 v 3
                print(f"Round {round_num}:")
                for matchup in matchups_table[round_num + 1]:
                    if (player_names[matchup[0]-1] == dead_table[0]):
                        print(f"{replace4vs3(player_names[matchup[0]-1], player_names[matchup[1]-1])} - {player_names[matchup[1]-1]}")
                    else:
                        if (player_names[matchup[1]-1] == dead_table[0]):
                            print(f"{replace4vs3(player_names[matchup[1]-1], player_names[matchup[0]-1])} - {player_names[matchup[0]-1]}")
                        else:
                            print(f"{player_names[matchup[0]-1]} - {player_names[matchup[1]-1]}") 

        if ((redDie == 2 and blueDie == 0) or (redDie == 0 and blueDie == 2)):
            #----------------------------- 4 v 2
            replace4v2(round_num, dead_table[0], dead_table[1])
            #-----------------------------
        if (redDie == 1 and blueDie == 1):
            #----------------------------- 3 v 3
            replace3v3(round_num, dead_table[0], dead_table[1])
            #------------------------------------

        # Continue or change d_p
        command = input("Have any players died? (y/n): ")
        if command.lower() == 'y':
            NOdeadPlayer = int(input("Enter the number dead player: "))
            for i in range(NOdeadPlayer):
                d_p = input("Enter the index of dead player: ")
                dead_table.append(d_p)
                # Change name of dead player
                player_names_start[d_p-1] = player_names_start[d_p - 1] + "XXXXXXXXXXXXXXX"
                if (d_p > 4):
                    redDie = redDie + 1
                else:
                    blueDie = blueDie + 1
            round_num += 1
        else:
            d_p = 0
            round_num += 1


def main():
    get_player(8)
    game(player_names, d_p, 4)

main()
