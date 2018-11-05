#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PYTHON VERSION: 2.7
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

class Color:
	white   = '\033[0;37m'
	redb    = '\033[1;31m'
	greenb  = '\033[1;32m'
	yellowb = '\033[1;33m'
	whiteb  = '\033[1;37m'

def fill_board(shoot, turn):
	os.system('clear')
	for x in xrange(BOARD[0]):
		for y in range(0, BOARD[1]):
			if shoot == COLS[y] + str(x + 1):
				if shoot in team[1-turn]:
					team[1-turn].remove(shoot)
					board_team[1-turn][y][x] = Color.greenb + '★' + Color.white
				else:
					board_team[1-turn][y][x] = Color.redb + '✕' + Color.white
				team_repeat[turn].append(shoot)
	draw_board()

def draw_board():
	title1 = (' ' * (BOARD[1] - (len(PLAYERS[0]) / 2))) + Color.whiteb + PLAYERS[0] + Color.white + (' ' * (BOARD[1] - (len(PLAYERS[0]) / 2) - (len(PLAYERS[0]) % 2)))
	title2 = (' ' * (BOARD[1] - (len(PLAYERS[1]) / 2))) + Color.whiteb + PLAYERS[1] + Color.white + (' ' * (BOARD[1] - (len(PLAYERS[1]) / 2) - (len(PLAYERS[1]) % 2)))
	print('''
┌─────{3}┬┬{3}─────┐
│   {0}  ││  {1}   │
├─────{3}┼┼{3}─────┤
│    {5}{2}{4}  ├┤  {5}{2}{4}    │'''.format(title1, title2, ' '.join(COLS[:BOARD[1]]), ('──' * BOARD[1]), Color.white, Color.yellowb))

	for x in xrange(BOARD[0]):
		if (x+1) < 10:
			print('│{2} {0} {1}'.format(x+1, Color.white, Color.yellowb)),
		else:
			print('│{2}{0} {1}'.format(x+1, Color.white, Color.yellowb)),

		for y in xrange(BOARD[1]):
			print('{0}'.format(board_team[0][y][x])),

		print(' ├┤ '),

		for y in xrange(BOARD[1]):
			print('{0}'.format(board_team[1][y][x])),

		if (x+1) < 10:
			print('{2} {0} {1}│'.format(x+1, Color.white, Color.yellowb))
		else:
			print('{2} {0}{1}│'.format(x+1, Color.white, Color.yellowb))

	print('└─────{0}┴┴{0}─────┘'.format('──' * BOARD[1]))

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
				print('El número de naves debe ser mayor a 0 y menor o igual a {0}'.format(limit))
				continue
		except ValueError:
			print('Debes ingresar un número')
			continue

	for key, value in enumerate(PLAYERS):
		print('TEAM: {0} ({1} naves)'.format(value, ships))
		for x in xrange(ships):
			while True:
				tmp = getpass.getpass("Ingrese coordenada de nave " + str(x+1) + " " + ARROW + " ").upper()
				if tmp in team[key]:
					print("Ya se encuentra en tu selección")
					continue

				if not is_valid(tmp):
					print("Debe ingresar una coordinada válida")
					continue

				team[key].append(tmp)
				break
	play()

def play():
	fill_board('', '')
	turn = 1

	while True:
		if len(team[0]) == 0 or len(team[1]) == 0:
			print("{2}¡¡¡ E L  E Q U I P O  '{0}'  H A  G A N A D O !!!{1}".format(PLAYERS[turn], Color.white, Color.greenb))
			time.sleep(4)
			break

		turn = 1 - turn

		while True:
			shoot = raw_input(Color.whiteb + "❮" + PLAYERS[turn] + "❯" + Color.white + " Ingrese coordenada " + ARROW + " ").upper()

			if shoot not in team_repeat[turn]:
				fill_board(shoot, turn)
				break
			else:
				print('[ Ya dijiste esa coordenada ]')
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
		print('''{0}
 ╔═══════════════════════════════╗
 ║ ★ ★  B A T T L E S H I P  ★ ★ ║
 ╚═══════════════════════════════╝

 {1}❶{2}  J U G A R
 {1}❷{2}  C O N F I G U R A R
 {1}❸{2}  S A L I R
'''.format(Color.redb, Color.whiteb, Color.white))

		opt = raw_input(" Ingrese Opción " + ARROW + " ")

		if opt == "1":
			start()
		elif opt == "2":
			settings()
		elif opt == "3":
			print('{0}¡ H A S T A  L U E G O !{1}'.format(Color.greenb, Color.white))
			break

if __name__ == "__main__":
	menu()