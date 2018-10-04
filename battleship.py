#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass

PLAYERS = ['PRINCIPIANTES', 'DA IGUAL']
BOARD   = [40,26] # rows(máx. 99),cols(máx. 26)

team        = [[],[]]
team_repeat = [[],[]]
cols        = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
board_team  = [[['⃞ ' for i in range(BOARD[0])] for j in range(BOARD[1])],[['⃞ ' for i in range(BOARD[0])] for j in range(BOARD[1])]]

def fill_board(shoot, turn):
	os.system('clear')
	for x in xrange(BOARD[0]):
		for y in range(0, BOARD[1]):
			if shoot == cols[y] + str(x + 1):
				if shoot in team[1-turn]:
					team[1-turn].remove(shoot)
					board_team[1-turn][y][x] = '\033[1;32m★\033[0;37m'
				else:
					board_team[1-turn][y][x] = '\033[1;31m✕\033[0;37m'
				team_repeat[turn].append(shoot)
	draw_board()

def draw_board():
	title1 = (' ' * (BOARD[1] - (len(PLAYERS[0]) / 2))) + '\033[1;37m' + PLAYERS[0] + '\033[0;37m' + (' ' * (BOARD[1] - (len(PLAYERS[0]) / 2) - (len(PLAYERS[0]) % 2)))
	title2 = (' ' * (BOARD[1] - (len(PLAYERS[1]) / 2))) + '\033[1;37m' + PLAYERS[1] + '\033[0;37m' + (' ' * (BOARD[1] - (len(PLAYERS[1]) / 2) - (len(PLAYERS[1]) % 2)))
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
			print '{0}'.format(board_team[0][y][x]),

		print ' ├┤ ',

		for y in xrange(BOARD[1]):
			print '{0}'.format(board_team[1][y][x]),

		if (x+1) < 10:
			print '\033[1;37m {0} \033[0;37m│'.format(x+1)
		else:
			print '\033[1;37m {0}\033[0;37m│'.format(x+1)

	print '└──────{0}──────┘'.format('────' * BOARD[1])

def is_valid(s):
	try:
		if (0 < int(s[1:]) <= BOARD[0]) and s[:1] in cols:
			return True
		return False
	except ValueError:
		return False

def start():
	fill_board('', '')

	ships = int(raw_input("Ingrese números de naves(5 por defecto) > ") or "5")
	limit = (BOARD[0] * BOARD[1]) / 2

	print ''

	if ships > 0 and ships <= limit:
		print 'TEAM: {0} ({1} naves)'.format(PLAYERS[0], ships)
		for x in xrange(ships):
			while True:
				tmp = getpass.getpass("Ingrese coordenada de nave " + str(x+1) + " > ").upper()
				if tmp in team[0]:
					print "Ya se encuentra en tu selección"
					continue

				if not is_valid(tmp):
					print "Debe ingresar una coordinada válida"
					continue

				team[0].append(tmp)
				break

		print 'TEAM: {0} ({1} naves)'.format(PLAYERS[1], ships)
		for x in xrange(ships):
			while True:
				tmp = getpass.getpass("Ingrese coordenada de nave " + str(x+1) + " > ").upper()
				if tmp in team[1]:
					print "Ya se encuentra en tu selección"
					continue

				if not is_valid(tmp):
					print "Debe ingresar una coordinada válida"
					continue

				team[1].append(tmp)
				break
		play()
	else:
		print 'El número de naves debe ser mayor a 0 y menor o igual a {0}'.format(limit)

def play():
	fill_board('', '')
	turn = 1

	while True:
		if len(team[0]) == 0 or len(team[1]) == 0:
			print "\033[1;32m¡¡¡ E L  E Q U I P O  '{0}'  H A  G A N A D O !!!\033[0;37m".format(PLAYERS[turn])
			break

		turn = 1 - turn

		while True:
			shoot = raw_input("[" + PLAYERS[turn] + "] Ingrese coordenada > ").upper()

			if shoot not in team_repeat[turn]:
				fill_board(shoot, turn)
				break
			else:
				print '[ Ya dijiste esa coordenada ]'
				continue

if __name__ == "__main__":
	start()