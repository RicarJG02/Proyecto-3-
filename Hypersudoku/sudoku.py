class Celda:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.valor = 0 #celda comienza vacía [0-9]

class Sudoku:
    #Crea un sudoku vacio
    def __init__(self):
        self.tablero = []
        for i in range(9):
            filaActual = []
            for j in range(9):
                filaActual.append(Celda(i,j))
            self.tablero.append(filaActual)
    
    #Valida que el tablero sea correcto
    def validarTablero(self):
        identificador_de_bloques = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6],[1,1],[5,5],[1,5],[5,1]]
        validacion = self.validarFilas() and self.validarColumnas()
        for bloque in identificador_de_bloques:
            validacion = validacion and self.validarBloque(bloque) 
        return validacion

    def partida_ganada(self):
        Valores = []
        for i in range(9):
            for j in range(9):
                Valores.append(self.tablero[i][j].valor)
        return self.validarTablero() and Valores.count(0)==0

    def validarBloque(self,id):
        i=id[0]
        j=id[1]
        valores_en_bloque = [
            self.tablero[i][j].valor,
            self.tablero[i][j+1].valor,
            self.tablero[i][j+2].valor,
            self.tablero[i+1][j].valor,
            self.tablero[i+1][j+1].valor,
            self.tablero[i+1][j+2].valor,
            self.tablero[i+2][j].valor,
            self.tablero[i+2][j+1].valor,
            self.tablero[i+2][j+2].valor
        ]
        return self.chequearRepetidos(valores_en_bloque)


    def validarFilas(self):
        for fila in self.tablero:
            valores_en_fila = [celda.valor for celda in fila]
            if(not self.chequearRepetidos(valores_en_fila)):
                return False
        return True
            
    def validarColumnas(self):
        for j in range(9):
            valores_en_columna = [self.tablero[i][j].valor for i in range(9)]
            if(not self.chequearRepetidos(valores_en_columna)):
                return False
        return True
    

    def chequearRepetidos(self,lista):
        for x in lista:
            if(lista.count(x)>1 and x!=0):
                return False
        return True

    def estaVacio(self):
        Valores = []
        for i in range(9):
            for j in range(9):
                Valores.append(self.tablero[i][j].valor)
        return Valores.count(0)==81
    
    def cargar(self, ruta):
        archivo = open(ruta,'r')
        matriz = []
        for linea in archivo.readlines():
            matriz.append( [ int (x) for x in linea.split(',') ] )
        
        for i in range(9):
            for j in range(9):
                self.tablero[i][j].valor = matriz[i][j]

    def guardar(self, ruta):
        archivo = open(ruta,'w')
        for i in range(9):
            fila = []
            for j in range(9):
                fila.append(str(self.tablero[i][j].valor))
            archivo.write(','.join(fila)+"\n")
        archivo.close()
    
    def reiniciar(self):
        for fila in self.tablero:
            for celda in fila:
                celda.valor = 0


