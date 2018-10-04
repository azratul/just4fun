#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass

PLAYER1 = 'PRINCIPIANTES'
PLAYER2 = 'DA IGUAL'
BOARD   = [26,26] # rows(infinito),cols(máx. 26)
HIT     = '\033[1;32m★\033[0;37m'
MISS    = '\033[1;31m✕\033[0;37m'
EMPTY   = '- '

team         = [[],[]]
team_repeat  = [[],[]]
cols         = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
board_team1  = [[EMPTY for i in range(BOARD[0])] for j in range(BOARD[1])]
board_team2  = [[EMPTY for i in range(BOARD[0])] for j in range(BOARD[1])]

def fill_board(shoot, turn):
	os.system('clear')
	for x in xrange(BOARD[0]):
		for y in range(0, BOARD[1]):
			if shoot == cols[y] + str(x + 1):
				if turn == PLAYER1:
					if shoot in team[1]:
						team[1].remove(shoot)
						board_team2[y][x] = HIT
					else:
						board_team2[y][x] = MISS
					team_repeat[0].append(shoot)

				if turn == PLAYER2:
					if shoot in team[0]:
						team[0].remove(shoot)
						board_team1[y][x] = HIT
					else:
						board_team1[y][x] = MISS
					team_repeat[1].append(shoot)

	draw_board()

def draw_board():
	title1 = (' ' * (BOARD[1] - (len(PLAYER1) / 2))) + '\033[1;37m' + PLAYER1 + '\033[0;37m' + (' ' * (BOARD[1] - (len(PLAYER1) / 2) - (len(PLAYER1) % 2)))
	title2 = (' ' * (BOARD[1] - (len(PLAYER2) / 2))) + '\033[1;37m' + PLAYER2 + '\033[0;37m' + (' ' * (BOARD[1] - (len(PLAYER2) / 2) - (len(PLAYER2) % 2)))
	print '''
┌──────{3}──────┐
│   {0}  ││  {1}   │
├──────{3}──────┤
│    \033[1;37m{2}\033[0;37m  ├┤  \033[1;37m{2}\033[0;37m    │'''.format(title1, title2, ' '.join(cols[:BOARD[1]]), ('────' * BOARD[1]))

	for x in xrange(BOARD[0]):
		if (x+1) < 10:
			print '│\033[1;37m {0} \033[0;37m'.format(x+1),
		else:
			print '│\033[1;37m{0} \033[0;37m'.format(x+1),

		for y in xrange(BOARD[1]):
			print '{0}'.format(board_team1[y][x]),

		print ' ├┤ ',

		for y in xrange(BOARD[1]):
			print '{0}'.format(board_team2[y][x]),

		if (x+1) < 10:
			print '\033[1;37m {0} \033[0;37m│'.format(x+1)
		else:
			print '\033[1;37m {0}\033[0;37m│'.format(x+1)

	print '└──────{0}──────┘'.format('────' * BOARD[1])

def start():
	fill_board('', '')

	ships = int(raw_input("Ingrese números de naves(5 por defecto) > ") or "5")
	limit = (BOARD[0] * BOARD[1]) / 2

	print ''

	if ships > 0 and ships <= limit:
		print 'TEAM: {0} ({1} naves)'.format(PLAYER1, ships)
		for x in xrange(ships):
			while True:
				tmp = getpass.getpass("Ingrese coordenada de nave " + str(x+1) + " > ").upper()
				if tmp in team[0]:
					print "Ya se encuentra en tu selección"
					continue

				team[0].append(tmp)
				break

		print 'TEAM: {0} ({1} naves)'.format(PLAYER2, ships)
		for x in xrange(ships):
			while True:
				tmp = getpass.getpass("Ingrese coordenada de nave " + str(x+1) + " > ").upper()
				if tmp in team[1]:
					print "Ya se encuentra en tu selección"
					continue

				team[1].append(tmp)
				break
		play()
	else:
		print 'El número de naves debe ser mayor a 0 y menor o igual a {0}'.format(limit)

def play():
	fill_board('', '')

	turn = ''

	while True:
		if len(team[0]) == 0 or len(team[1]) == 0:
			print "\033[1;32m¡¡¡ E L  E Q U I P O  '{0}'  H A  G A N A D O !!!\033[0;37m".format(turn)
			break

		if turn == PLAYER1:
			turn = PLAYER2
		else:
			turn = PLAYER1

		shoot = raw_input("[" + turn + "] Ingrese coordenada > ").upper()

		fill_board(shoot, turn)

if __name__ == "__main__":
	start()