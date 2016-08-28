import random

# player_info = {1:{player_name:"Whitney",player_pos:0,player_symb:"###"}, {2:{player_name:"Philip",player_pos:5,player_symb:"@@@"},{3:{player_name:"Gaspard",player_pos:10,player_symb:"+++"},{4:{player_name:"Brani",player_pos:15,player_symb:"$$$"}}

player1_pos = 0
player2_pos = 0
player1_symb = "###"
player2_symb = "@@@"
player1_name = ""
player2_name = ""

player = 1

game_board = [ \
"100", "99 ", "98v", "97 ", "96 ", "95v", "94 ", "93v", "92 ", "91 \n",
"81 ", "82 ", "83 ", "84 ", "85 ", "86 ", "87v", "88 ", "89 ", "90 \n", \
"80v", "79 ", "78 ", "77 ", "76 ", "75 ", "74 ", "73 ", "72 ", "71^\n", \
"61 ", "62v", "63 ", "64v", "65 ", "66 ", "67 ", "68 ", "69 ", "70 \n", \
"60 ", "59 ", "58 ", "57 ", "56v", "55 ", "54 ", "53 ", "52 ", "51^\n", \
"41 ", "42 ", "43 ", "44 ", "45 ", "46 ", "47 ", "48v", "49v", "50 \n", \
"40 ", "39 ", "38 ", "37 ", "36^", "35 ", "34 ", "33 ", "32 ", "31 \n", \
"21^", "22 ", "23 ", "24 ", "25 ", "26 ", "27 ", "28^", "29 ", "30 \n", \
"20 ", "19 ", "18 ", "17 ", "16v", "15 ", "14 ", "13 ", "12 ", "11 \n", \
"1^ ", "2  ", "3  ", "4^ ", "5  ", "6  ", "7  ", "8  ", "9^ ", "10 \n",]

game_board_key = {0:101,1:90, 2:91, 3:92, 4:93, 5:94, 6:95, 7:96, 8:97, 9:98, 10:99, \
11:89, 12:88, 13:87, 14:86, 15:85, 16:84, 17:83, 18:82, 19:81, 20:80, \
21:70, 22:71, 23:72, 24:73, 25:74, 26:75, 27:76, 28:77, 29:78, 30:79, \
31:69, 32:68, 33:67, 34:66, 35:65, 36:64, 37:63, 38:62, 39:61, 40:60, \
41:50, 42:51, 43:52, 44:53, 45:54, 46:55, 47:56, 48:57, 49:58, 50:59, \
51:49, 52:48, 53:47, 54:46, 55:45, 56:44, 57:43, 58:42, 59:41, 60:40, \
61:30, 62:31, 63:32, 64:33, 65:34, 66:35, 67:36, 68:37, 69:38, 70:39, \
71:29, 72:28, 73:27, 74:26, 75:25, 76:24, 77:23, 78:22, 79:21, 80:20, \
81:10, 82:11, 83:12, 84:13, 85:14, 86:15, 87:16, 88:17, 89:18, 90:19, \
91:9, 92:8, 93:7, 94:6, 95:5, 96:4, 97:3, 98:2, 99:1, 100:0}

def roll_die():
	roll = random.randint(1,6)
	print "You rolled a " + str(roll)
	return roll


def main_menu():
	choice = raw_input("1 - Return to Game\n2 - Start new game\n3 - See high scores\n4 - Exit\n")
	if choice.isdigit() == True:
		choice = int(choice)
		return choice
	else:
		print "That is not a valid choice."


def play(roll):
	global player
	if player == 1:
		global player1_pos			
		if player1_pos + roll <= 100:
			player1_pos = player1_pos + roll
			print "You move to " + str(player1_pos) + "\n"
		else:
			print "You stay at " + str(player1_pos) + "\n"
	elif player == 2:
		global player2_pos
		if player2_pos + roll <= 100:
			player2_pos = player2_pos + roll
			print "You move to " + str(player2_pos) + "\n"
		else: 
			print "You stay at " + str(player2_pos) + "\n"
	
	if player == 2:
		player = 1
	else:
		player = 2


def print_board():
	global game_board_key
	global game_board
	global player1_symb
	global player2_symb
	
	player1_key=game_board_key[player1_pos]
	player2_key=game_board_key[player2_pos]
	
	if (player1_key + 1)%10 == 0:
		temp_player1_symb = player1_symb + "\n"
	else:
		temp_player1_symb = player1_symb
	if (player2_key + 1)%10 == 0:
		temp_player2_symb = player2_symb + "\n"
	else:
		temp_player2_symb = player2_symb

	temp_board = game_board[:]
	if player1_key != 101:
		temp_board[player1_key] = temp_player1_symb
	if player2_key != 101:
		temp_board[player2_key] = temp_player2_symb
	
	for i in range(len(temp_board)):
		print temp_board[i],
	print "\n"

def start_new_game():
	global player1_name
	global player1_symb
	global player2_name
	global player2_symb
	global player1_pos
	global player2_pos
	print "Welcome to Chutes and Ladders!"
	player1_name = raw_input("What is Player1's name?")
	print "%s's symbol will be " % player1_name + player1_symb
	player2_name = raw_input("What is Player2's name?")
	print "%s's symbol will be " % player2_name + player2_symb + "\n"
	player1_pos = 0
	player2_pos = 0

def see_high_scores():
	pass

def main():
	while(True):
		choice = main_menu()
		global player_info
		if choice == 1:
			while(player1_pos < 100 and player2_pos < 100):
				roll_choice = raw_input("It's Player%s's turn!\nPress 'R' to roll the die.\n" \
					"Press 'M' to return to the main menu\n" % player).lower()
				if roll_choice == "r":
					play(roll_die())
					print_board()
				else:
					break
		elif choice == 2:
			start_new_game()
		elif choice == 3:
			see_high_scores()
		elif choice == 4:
			# write_to_file("shopping_list.txt", shopping_list)
			break



if __name__ == "__main__":
	main()



