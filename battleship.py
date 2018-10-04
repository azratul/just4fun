#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

cols   = ['A','B','C','D','E','F','G','H','I','J']

azul   = []
rojo   = []

b_azul = [['-' for i in range(10)] for j in range(10)]
b_rojo = [['-' for i in range(10)] for j in range(10)]

def fill_board(shoot, team):
	os.system('clear')
	for x in xrange(10):
		for y in range(0, len(cols)):
			if shoot == cols[y] + str(x + 1):
				if team == 'AZUL':
					if shoot in rojo:
						b_rojo[x][y] = 'O'
					else:
						b_rojo[x][y] = 'X'

				if team == 'ROJO':
					if shoot in azul:
						b_azul[x][y] = 'O'
					else:
						b_azul[x][y] = 'X'

	draw_board()

def draw_board():
	print '''
------------------------------------------------------------------------
|               AZUL               ||               ROJO               |
------------------------------------------------------------------------
|    A  B  C  D  E  F  G  H  I  J  ||  A  B  C  D  E  F  G  H  I  J    |'''

	for x in xrange(10):
		if x < 9:
			print '| {0} '.format(x+1),
		else:
			print '|{0} '.format(x+1),

		for y in xrange(10):
			print '{0} '.format(b_azul[x][y]),

		print '|| ',

		for y in xrange(10):
			print '{0} '.format(b_rojo[x][y]),

		if x < 9:
			print '{0} |'.format(x+1)
		else:
			print '{0}|'.format(x+1)

	print '------------------------------------------------------------------------'

def start():
	fill_board('', '')

	print ''
	print 'TEAM: AZUL'
	for x in xrange(10):
		azul.append(raw_input("Ingrese nave(1 espacio) > ").upper())

	print 'TEAM: ROJO'
	for x in xrange(10):
		rojo.append(raw_input("Ingrese nave(1 espacio) > ").upper())

	play()

def play():
	fill_board('', '')

	team = ''
	print azul
	print rojo

	while True:
		if team == 'AZUL':
			team = 'ROJO'
		else:
			team = 'AZUL'

		print team
		shoot = raw_input("Ingrese coordenada > ").upper()

		fill_board(shoot, team)

if __name__ == "__main__":
	start()
