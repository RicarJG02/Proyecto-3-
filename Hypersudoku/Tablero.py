import pygame
import random
from sudoku import Sudoku
import copy

#PARAMETROS
ANCHO = 500
ALTO = 500
PANTALLA_TAM = (600,600)
BLANCO = (255,255,255) #0
NEGRO = (0,0,0)
AMARILLO = (252, 238, 111) #1
ROJO = (242, 80, 78)#2
AZUL = (111, 196, 252)#3
VERDE =(111, 252, 144)#4
NARANJA = (255, 134, 64)#5
VIOLETA = (227, 128, 255)#6
CYAN = (151, 231, 252)#7
ROSA = (255, 120, 158)#8
AQUA = (120, 255, 203)#9
GRIS = (176, 198, 245)
COLORES = {0:BLANCO,1:AMARILLO,2:ROJO,3:AZUL,4:VERDE,5:NARANJA,6:VIOLETA,7:CYAN,8:ROSA,9:AQUA}
#Posicion inicial del grid
pos_x = 50
pos_y = 60
ancho_celda = ANCHO/9
pygame.font.init()
font = pygame.font.SysFont('Arial', 16)
BLOQUES = [
    pygame.Rect(pos_x+1*ancho_celda,pos_y+1*ancho_celda,3*ancho_celda,3*ancho_celda),
    pygame.Rect(pos_x+5*ancho_celda,pos_y+1*ancho_celda,3*ancho_celda,3*ancho_celda),
    pygame.Rect(pos_x+1*ancho_celda,pos_y+5*ancho_celda,3*ancho_celda,3*ancho_celda),
    pygame.Rect(pos_x+5*ancho_celda,pos_y+5*ancho_celda,3*ancho_celda,3*ancho_celda)
]
TABLERO_COLLIDER = pygame.Rect(pos_x,pos_y,ANCHO,ALTO)
RESET_COLLIDER = pygame.Rect(493,10,60,40)
CLEAR_COLLIDER = pygame.Rect(425,10,60,40)
LOAD_COLLIDER = pygame.Rect(357,10,60,40)
SAVE_COLLIDER = pygame.Rect(289,10,60,40)
sudoku_inicial = Sudoku()

#dibuja valores del sudoku no nulos con su respectivo color
def dibujar_seleccionados(pantalla,sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku.tablero[x][y].valor != 0:
                pygame.draw.rect(pantalla,COLORES[sudoku.tablero[x][y].valor],(pos_x+x*ancho_celda,pos_y+y*ancho_celda, ancho_celda, ancho_celda))

def pos_en_bloque(x,y):
    flag = False
    for bloque in BLOQUES:
        flag = flag or bloque.collidepoint(pos_x+x*ancho_celda,pos_y+y*ancho_celda)
    return flag

def seleccionar_celda(pantalla, sudoku, x,y, direccion):
    indice = sudoku.tablero[x][y].valor
    sudoku.tablero[x][y].valor=(indice+direccion)%10
    dibujar_pantalla(pantalla,sudoku)

#Dibuja los 4 bloques extra del hyper sudoku
def dibujar_bloques(pantalla):
    for x in [1,5]:
        for y in [1,5]:
            for cel_x in range(3):
                for cel_y in range(3):
                    pygame.draw.rect(pantalla,GRIS,(pos_x+(x+cel_x)*ancho_celda,pos_y+(y+cel_y)*ancho_celda, ancho_celda, ancho_celda))

def dibujar_lineas_celdas(pantalla):
    ancho_linea = 1
    for i in range(10):
        if i%3==0:
            ancho_linea = 4
        else:
            ancho_linea = 1
        pygame.draw.line(pantalla,NEGRO,(pos_x,i*ancho_celda+pos_y),(ANCHO+pos_x,i*ancho_celda+pos_y),ancho_linea)
        pygame.draw.line(pantalla,NEGRO,(i*ancho_celda+pos_x,pos_y),(i*ancho_celda+pos_x,ALTO+pos_y),ancho_linea)
        
def get_posicion_click(pantalla, pos_mouse):  
    pos_celda = int((pos_mouse[0]-pos_x)//ancho_celda), int((pos_mouse[1]-pos_y)//ancho_celda)
    return pos_celda

#Dibuja un marcador verde o rojo si el tablero es valido o no resp.
def dibujar_estado(pantalla,estado):
    if estado:
        pygame.draw.circle(pantalla,(0,255,0),(pos_x,30),15)
    else:
        pygame.draw.circle(pantalla,(255,0,0),(pos_x,30),15)

def reset(pantalla, sudoku):
    sudoku = copy.deepcopy(sudoku_inicial)
    dibujar_pantalla(pantalla,sudoku)
    return sudoku
    

def clear(pantalla,sudoku):
    sudoku = Sudoku()
    dibujar_pantalla(pantalla,sudoku)
    return sudoku

def cargar(pantalla,sudoku):
    global sudoku_inicial
    sudoku.cargar("tablero_prueba_2.txt")
    sudoku_inicial = copy.deepcopy(sudoku)
    dibujar_pantalla(pantalla,sudoku)

def guardar(sudoku):
    sudoku.guardar("nuevo_tablero.txt")

#Crea un nuevo tablero con valores aleatorios
def inicializar_tablero(sudoku):
    cantidad = random.randint(8,20)
    for i in range(cantidad):
        x = random.randint(0,8)
        y = random.randint(0,8)
        valor = random.randint(1,9)
        sudoku_inicial.tablero[x][y].valor = valor
        sudoku.tablero[x][y].valor = valor
        while(not sudoku.validarTablero()):
            sudoku_inicial.tablero[x][y].valor =0
            sudoku.tablero[x][y].valor = 0
            x = random.randint(0,8)
            y = random.randint(0,8)
            valor = random.randint(1,9)
            sudoku_inicial.tablero[x][y].valor = valor
            sudoku.tablero[x][y].valor = valor
    
def dibujar_boton_reset(pantalla):
    pygame.draw.rect(pantalla,CYAN,(493,10,60,40))
    pantalla.blit(font.render("RESET",True,NEGRO),(496,19))

def dibujar_boton_clear(pantalla):
    pygame.draw.rect(pantalla,ROSA,(425,10,60,40))
    pantalla.blit(font.render("CLEAR",True,NEGRO),(428,19))

def dibujar_boton_load(pantalla):
    pygame.draw.rect(pantalla,AMARILLO,(357,10,60,40))
    pantalla.blit(font.render("LOAD",True,NEGRO),(365,19))

def dibujar_boton_save(pantalla):
    pygame.draw.rect(pantalla,VERDE,(289,10,60,40))
    pantalla.blit(font.render("SAVE",True,NEGRO),(294,19))

def dibujar_pantalla(pantalla, sudoku):
    pantalla.fill(BLANCO)
    dibujar_bloques(pantalla)
    dibujar_seleccionados(pantalla,sudoku)
    dibujar_lineas_celdas(pantalla)
    dibujar_estado(pantalla,sudoku.validarTablero())
    dibujar_boton_reset(pantalla)
    dibujar_boton_clear(pantalla)
    dibujar_boton_load(pantalla)
    dibujar_boton_save(pantalla)
    pygame.display.update()

def main():
    jugando = True
    sudoku = Sudoku()
    inicializar_tablero(sudoku)
    pantalla = pygame.display.set_mode(PANTALLA_TAM)
    pygame.display.set_caption("Sudoku")    
    dibujar_pantalla(pantalla,sudoku)
    while jugando:
        if(sudoku.partida_ganada()):
            jugando = False
            print("Has ganado. Tu solucion ha quedado guardada [solucion.txt]")
            sudoku.guardar("solucion.txt")
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                jugando = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if RESET_COLLIDER.collidepoint(pos[0],pos[1]):
                    sudoku = reset(pantalla, sudoku)
                if CLEAR_COLLIDER.collidepoint(pos[0],pos[1]):
                    sudoku = clear(pantalla, sudoku)
                if LOAD_COLLIDER.collidepoint(pos[0],pos[1]):
                    cargar(pantalla, sudoku)
                if SAVE_COLLIDER.collidepoint(pos[0],pos[1]):
                    guardar(sudoku)
                if TABLERO_COLLIDER.collidepoint(pos[0],pos[1]):
                    if ev.button == 1:
                        direccion = 1
                    else:
                        direccion = -1
                    pos_mouse = get_posicion_click(pantalla, pos)
                    seleccionar_celda(pantalla,sudoku,pos_mouse[0],pos_mouse[1],direccion)                
main()

