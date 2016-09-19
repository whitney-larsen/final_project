import random
from game_board import game_board
from game_board import game_board_key
from game_board import chutes
from game_board import ladders

player_num = 2
player_list = [["Whitney",0,"###",0],["Philip",0,"@@@",0],["Gaspard",0,"+++",0],["Mehul",0,"$$$",0]]
player = 1

def roll_die():
	roll = random.randint(1,6)
	print "%s rolled a " % player_list[player-1][0] + str(roll)
	return roll

def main_menu():
	print "Main Menu"
	choice = raw_input("1 - Play Game\n2 - Change Players\n3 - See Scores\n4 - Save and Exit\n")
	if choice.isdigit() == True:
		choice = int(choice)
		return choice
	else:
		return

def play(roll):
	global player
	if player_list[player-1][1] + roll <=100:
		player_list[player-1][1] = player_list[player-1][1] + roll
		print "%s moved to " % player_list[player-1][0] + str(player_list[player-1][1]) + "\n"
	else:
		print "%s stayed at " % player_list[player-1][0] + str(player_list[player-1][1]) + "\n"
	
	chutes_and_ladders()

	if player_list[player-1][1] == 100:
		print "%s won!" % player_list[player-1][0] + "\n"
		player_list[player-1][3] = player_list[player-1][3]+1

	if player <player_num:
		player = player +1
	else:
		player = 1

def chutes_and_ladders():
	if player_list[player-1][1] in ladders:
		player_list[player-1][1] = ladders[player_list[player-1][1]]
		print "%s went up a ladder to " % player_list[player-1][0] + str(player_list[player-1][1]) + "\n"

	if player_list[player-1][1] in chutes:
		player_list[player-1][1] = chutes[player_list[player-1][1]]
		print "%s went down a chute to " % player_list[player-1][0] + str(player_list[player-1][1]) + "\n"

def print_board():
	temp_board = game_board[:]

	for i in range(player_num):
		player_key=game_board_key[player_list[i][1]]
		if (player_key + 1)%10 == 0:
			temp_player_symb = player_list[i][2] + "\n"
		else:
			temp_player_symb = player_list[i][2]
		if player_list[i][1] != 0:
			temp_board[player_key] = temp_player_symb
	
	for i in range(len(temp_board)):
		print temp_board[i],
	print "\n"

def change_players():
	global player_list
	global player_num
	player_num_string = raw_input("You can play with up to 4 players.  How many players are there?\n")
	if player_num_string.isdigit() == True:
		player_num = int(player_num_string)
	for i in range(player_num):
		player_list[i][0] = raw_input("What is Player%s's name? " % str(i+1))
		print "%s's symbol will be " % player_list[i][0] + player_list[i][2] + "\n"
		player_list[i][1] = 0
		player_list[i][3] = 0

def see_scores():
	for i in range(player_num):
		print player_list[i][0] + ": " + str(player_list[i][3])
	print "\n"

def write_file():
	with open("player_info.txt",mode = 'w') as my_file:
		for i in range(player_num):
			string = ""
			for j in range(len(player_list)):
				string = string + str(player_list[i][j])+ "," 
			my_file.write(string+"\n")	

def read_file():	
	global player_list
	global player_num
	with open ("player_info.txt", mode = "r") as my_file:
		raw_player_list = my_file.readlines()
		player_num = len(raw_player_list)
		for i in range(len(raw_player_list)):
			split_string = raw_player_list[i].split(",")
			split_string[1] = int(split_string[1])
			split_string[3] = int(split_string[3])
			split_string.pop()
			player_list[i] = split_string

def choose_players_menu():
	print "How would you like to choose players?"
	choice_string = raw_input("1 - Open Players from File\n2 - Use Default Players\n3 - Choose New Players\n")
	if choice_string.isdigit() == True:
		choice = int(choice_string)
	else:
		return
	if choice == 1:
		read_file()
		for i in range(player_num):
			print "%s's symbol will be " % player_list[i][0] + player_list[i][2]
		print "\n"
	if choice ==2:
		for i in range(player_num):
			print "%s's symbol will be " % player_list[i][0] + player_list[i][2]
		print "\n"
	elif choice == 3:
		change_players()
	else:
		return

def main():
	print "\nWelcome to Chutes and Ladders!\n"
	choose_players_menu()

	while(True):
		choice = main_menu()
		if choice == 1:
			while(player_list[0][1]<100 and player_list[1][1]<100 and player_list[2][1]<100 and player_list[3][1]<100):
				roll_choice = raw_input("It's %s's turn!\nPress 'R' to roll the die.\n" \
					"Press 'M' to return to the main menu\n" % player_list[player-1][0]).lower()
				if roll_choice == "r":
					play(roll_die())
					print_board()
				else:
					break
		elif choice == 2:
			choose_players_menu()
		elif choice == 3:
			see_scores()
		elif choice == 4:
			write_file()
			break

if __name__ == "__main__":
	main()



