import pygame
from pygame.locals import *
import sys
import numpy as np
from util import *
from search import *
import os
from time import sleep
import time

LEFT = 1
RIGHT = 3
cuadro_size = 20
dimension = 30
maze = np.zeros((30,30))
maze_cost = np.zeros((30,30))
start = [1,0]
goal = [29,28]

#################################################
#                  funciones                    #
#################################################
def pintar_cuadro(x,y,num):
	pygame.draw.rect(ventana, color[num],(cuadro_size*x,cuadro_size*y,cuadro_size,cuadro_size))
	grid()

def grid():
	for x in range(dimension):
		pygame.draw.line(ventana,color[1],(cuadro_size*(x+1),0),(cuadro_size*(x+1),cuadro_size*dimension))
		pygame.draw.line(ventana,color[1],(0,cuadro_size*(x+1)),(cuadro_size*dimension,cuadro_size*(x+1)))
	pygame.display.update()

def load_maze():
	archivo = open("maze.txt","r")
	archivo2 = open("maze_cost.txt","r")
	for linea in range(30):
		Slinea = archivo.readline()
		maze[linea, :] = Slinea.split(",")

		Slinea = archivo2.readline()							#lee la linea completa
		maze_cost[linea, :] = Slinea.split(",")					#separa por , y guarda la fila entera

	for linea in range(30):
		for caracter in range(30):
			if maze[linea,caracter] == 1:
				pintar_cuadro(caracter,linea,1)

	pintar_cuadro(start[0],start[1],4)
	pintar_cuadro(goal[0],goal[1],3)
	archivo.close()
	archivo2.close()

def pintar_camino(acciones):
	x = start[0]
	y = start[1]
	for i in acciones:
		if i == 'W':
			x = x-1
		elif i == 'E':
			x = x+1
		elif i == 'N':
			y = y-1
		elif i == 'S':
			y = y+1
		pintar_cuadro(x,y,19)

#################################################
#                  Programa                     #
#################################################
pygame.init()
os.system("clear")
color = np.zeros((20,3))
color[0]  = (255,255,255)	#blanco
color[1]  = (10,10,10)		#negro
color[2]  = (34,113,179)	#azul
color[3]  = (87,166,57)		#verde
color[4]  = (213,48,50)		#rojo
color[5]  = (99,58,52)		#cafe
color[6]  = (215,45,109)	#magenta
color[7]  = (255,117,20)	#naranja
color[8]  = (127,181,181)	#turquesa
color[9]  = (234,137,154)	#rosa
color[10] = (40,114,51)		#esmeralda
color[11] = (1,93,82)		#opalo
color[12] = (0,247,0)		#verde brillante
color[13] = (244,169,0)		#melon
color[14] = (71,64,46)		#oliva
color[15] = (37,109,123)	#agua
color[16] = (194,176,120)	#beige
color[17] = (110,28,52)		#brudeos
color[18] = (125,132,113)	#gris cemento
color[19] = (255,255,0)		#amarillo

ventana = pygame.display.set_mode((cuadro_size*dimension,cuadro_size*dimension))
pygame.display.set_caption("programa")
ventana.fill(color[0])
load_maze()
start_time = time.time()

problem = start , goal, maze , maze_cost
visitados, acciones , costos = depthFirstSearch(problem)
end_time = time.time()
print("Elapsed time: %s Seg" %(end_time - start_time))
print("\nAmount of explored states: %s States "%(len(visitados)))

for i in visitados:
	pintar_cuadro(i[0],i[1],2)
	sleep(0.005)
pintar_camino(acciones)

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		pygame.quit()
		sys.exit()
