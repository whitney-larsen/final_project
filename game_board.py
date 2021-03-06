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

game_board_key = {0:0,1:90, 2:91, 3:92, 4:93, 5:94, 6:95, 7:96, 8:97, 9:98, 10:99, \
11:89, 12:88, 13:87, 14:86, 15:85, 16:84, 17:83, 18:82, 19:81, 20:80, \
21:70, 22:71, 23:72, 24:73, 25:74, 26:75, 27:76, 28:77, 29:78, 30:79, \
31:69, 32:68, 33:67, 34:66, 35:65, 36:64, 37:63, 38:62, 39:61, 40:60, \
41:50, 42:51, 43:52, 44:53, 45:54, 46:55, 47:56, 48:57, 49:58, 50:59, \
51:49, 52:48, 53:47, 54:46, 55:45, 56:44, 57:43, 58:42, 59:41, 60:40, \
61:30, 62:31, 63:32, 64:33, 65:34, 66:35, 67:36, 68:37, 69:38, 70:39, \
71:29, 72:28, 73:27, 74:26, 75:25, 76:24, 77:23, 78:22, 79:21, 80:20, \
81:10, 82:11, 83:12, 84:13, 85:14, 86:15, 87:16, 88:17, 89:18, 90:19, \
91:9, 92:8, 93:7, 94:6, 95:5, 96:4, 97:3, 98:2, 99:1, 100:0}

ladders = {1:38, 4:14, 9:31, 28:84, 36:44, 21:42, 51:68, 71:91, 80:100}
chutes = {16:6, 47:26, 49:11, 56:53, 62:19, 64:60, 87:24, 93:73, 95:75, 98:78}