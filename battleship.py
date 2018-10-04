#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass
import time

PLAYERS = ['JUGADOR 1', 'JUGADOR 2']
BOARD   = [10,10] # rows(máx. 99),cols(máx. 26)
COLS    = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
GRID    = '⃞ '
ARROW   = '➔'

team        = [[],[]]
team_repeat = [[],[]]
board_team  = [[[GRID for i in range(BOARD[0])] for j in range(BOARD[1])],[[GRID for i in range(BOARD[0])] for j in range(BOARD[1])]]

def fill_board(shoot, turn):
	os.system('clear')
	for x in xrange(BOARD[0]):
		for y in range(0, BOARD[1]):
			if shoot == COLS[y] + str(x + 1):
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
┌─────{3}┬┬{3}─────┐
│   {0}  ││  {1}   │
├─────{3}┼┼{3}─────┤
│    \033[1;33m{2}\033[0;37m  ├┤  \033[1;33m{2}\033[0;37m    │'''.format(title1, title2, ' '.join(COLS[:BOARD[1]]), ('──' * BOARD[1]))

	for x in xrange(BOARD[0]):
		if (x+1) < 10:
			print '│\033[1;33m {0} \033[0;37m'.format(x+1),
		else:
			print '│\033[1;33m{0} \033[0;37m'.format(x+1),

		for y in xrange(BOARD[1]):
			print '{0}'.format(board_team[0][y][x]),

		print ' ├┤ ',

		for y in xrange(BOARD[1]):
			print '{0}'.format(board_team[1][y][x]),

		if (x+1) < 10:
			print '\033[1;33m {0} \033[0;37m│'.format(x+1)
		else:
			print '\033[1;33m {0}\033[0;37m│'.format(x+1)

	print '└─────{0}┴┴{0}─────┘'.format('──' * BOARD[1])

def is_valid(s):
	try:
		if (0 < int(s[1:]) <= BOARD[0]) and s[:1] in COLS:
			return True
		return False
	except ValueError:
		return False

def start():
	global team, team_repeat, board_team
	team        = [[],[]]
	team_repeat = [[],[]]
	board_team  = [[[GRID for i in range(BOARD[0])] for j in range(BOARD[1])],[[GRID for i in range(BOARD[0])] for j in range(BOARD[1])]]
	limit       = (BOARD[0] * BOARD[1]) / 2

	fill_board('', '')

	while True:
		try:
			ships = int(raw_input("Ingrese números de naves(5 por defecto) " + ARROW + " ") or "5")
			if 0 < ships <= limit:
				break
			else:
				print 'El número de naves debe ser mayor a 0 y menor o igual a {0}'.format(limit)
				continue
		except ValueError:
			print 'Debes ingresar un número'
			continue

	for key, value in enumerate(PLAYERS):
		print 'TEAM: {0} ({1} naves)'.format(value, ships)
		for x in xrange(ships):
			while True:
				tmp = getpass.getpass("Ingrese coordenada de nave " + str(x+1) + " " + ARROW + " ").upper()
				if tmp in team[key]:
					print "Ya se encuentra en tu selección"
					continue

				if not is_valid(tmp):
					print "Debe ingresar una coordinada válida"
					continue

				team[key].append(tmp)
				break
	play()

def play():
	fill_board('', '')
	turn = 1

	while True:
		if len(team[0]) == 0 or len(team[1]) == 0:
			print "\033[1;32m¡¡¡ E L  E Q U I P O  '{0}'  H A  G A N A D O !!!\033[0;37m".format(PLAYERS[turn])
			time.sleep(4)
			break

		turn = 1 - turn

		while True:
			shoot = raw_input("\033[1;37m❮" + PLAYERS[turn] + "❯\033[0;37m Ingrese coordenada " + ARROW + " ").upper()

			if shoot not in team_repeat[turn]:
				fill_board(shoot, turn)
				break
			else:
				print '[ Ya dijiste esa coordenada ]'
				continue

def settings():
	global PLAYERS, BOARD

	for key, value in enumerate(PLAYERS):
		PLAYERS[key] = raw_input(" Ingrese nombre de equipo " + str(key+1) + " " + ARROW + " ")

	for key, value in enumerate(BOARD):
		if key == 0:
			grid = 'filas'
		else:
			grid = 'columnas'

		while True:
			try:
				BOARD[key] = int(raw_input(" Ingrese grilla[" + grid + "] " + ARROW + " "))
				break
			except ValueError:
				continue

def menu():
	while True:
		os.system('clear')
		print '''\033[1;31m
 ╔═══════════════════════════════╗
 ║ ★ ★  B A T T L E S H I P  ★ ★ ║
 ╚═══════════════════════════════╝
 \033[0;37m
 \033[1;37m❶\033[0;37m  J U G A R\033[0;37m
 \033[1;37m❷\033[0;37m  C O N F I G U R A R\033[0;37m
 \033[1;37m❸\033[0;37m  S A L I R\033[0;37m
'''

		opt = raw_input(" Ingrese Opción " + ARROW + " ")

		if opt == "1":
			start()
		elif opt == "2":
			settings()
		elif opt == "3":
			print '\033[1;32m¡ H A S T A  L U E G O !\033[0;37m'
			break

if __name__ == "__main__":
	menu()