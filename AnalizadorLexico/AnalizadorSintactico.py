import sys
import ply.yacc as yacc
from prettytable import PrettyTable
import AnalizadorLexico
from AnalizadorLexico import tokens
from AnalizadorLexico import tablaSimbolos
from tabulate import tabulate

VERBOSE=1

def p_programa(p):
    'programa : funciones'
    print(chr(27) + "[0;36m" + "Lineas analizadas: " + chr(27) + "[0m" + str(p.lexer.lineno))
    pass

def p_funciones(p):
    '''funciones : funcion
                 | funciones funcion
    '''
    pass

def p_funcion(p):
    'funcion : tipo_dato ID APAREN parametros CPAREN ALLAVE declaraciones return CLLAVE'
    pass
def p_return(p):
     '''return : RETURN ID PUNTOCOMA
                | RETURN expresion PUNTOCOMA
                | empty
                '''

def p_parametros(p):
    '''parametros : parametro
                  | parametro COMA parametros
                  | empty
    '''
    pass
def p_empty(p):
    'empty : '
    pass
def p_parametro(p):
    'parametro : tipo_dato ID'
    pass

def p_tipo_dato(p):
    '''tipo_dato : INT
                 | CHAR
                 | FLOAT
    '''
    pass

def p_declaraciones(p):
    '''declaraciones : declaracion
                     | declaraciones declaracion
    '''
    pass
def p_declaracion(p):
    '''declaracion : asignacion
                   | declara
                   | condicional
                   | iteracion
                   | impresion
                   | entrada
    '''
    pass

def p_asignacion(p):
    '''asignacion : ID ASIGNAR expresion PUNTOCOMA'''
    pass
def p_declara(p):
    '''declara : tipo_dato ID PUNTOCOMA
                | tipo_dato ID ASIGNAR expresion PUNTOCOMA'''
    pass

def p_expresion(p):
    '''expresion : expresion_aritmetica
                 | expresion_logica
                 | expresion_comparacion
                 | ID
                 | constante
    '''
    pass

def p_expresion_aritmetica(p):
    '''expresion_aritmetica : expresion SUMA expresion
                            | expresion RESTA expresion
                            | expresion MULTI expresion
                            | expresion DIV expresion
    '''
    pass

def p_expresion_logica(p):
    '''expresion_logica : expresion AND expresion
                        | expresion OR expresion
    '''
    pass

def p_expresion_comparacion(p):
    '''expresion_comparacion : expresion IGUAL expresion
                              | expresion DISTINTO expresion
                              | expresion MAYOR expresion
                              | expresion MAYORIGUAL expresion
                              | expresion MENOR expresion
                              | expresion MENORIGUAL expresion
    '''
    pass

def p_condicional(p):
    '''condicional : IF APAREN expresion CPAREN ALLAVE declaraciones CLLAVE
                   | IF APAREN expresion CPAREN ALLAVE declaraciones CLLAVE ELSE ALLAVE declaraciones CLLAVE
    '''
    pass
def p_asignacion_for(p):
    'asignacion_for : ID ASIGNAR expresion'
    pass

def p_iteracion(p):
    '''iteracion : WHILE APAREN expresion CPAREN ALLAVE declaraciones CLLAVE
                 | DO ALLAVE declaraciones CLLAVE WHILE APAREN expresion CPAREN PUNTOCOMA
                 | FOR APAREN asignacion_for PUNTOCOMA expresion PUNTOCOMA asignacion_for CPAREN ALLAVE declaraciones CLLAVE
    '''
    pass

def p_impresion(p):
    '''impresion : PRINTF APAREN CADENA CPAREN PUNTOCOMA
                 | PRINTF APAREN ID CPAREN PUNTOCOMA
    '''
    pass

def p_entrada(p):
    'entrada : SCANF APAREN ID CPAREN PUNTOCOMA'
    pass

def p_constante(p):
    '''constante : NUMERO
                 | CADENA
    '''
    pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print(chr(27)+"[1;31m"+"\t ERROR: Error de sintaxis - Token inesperado" + chr(27)+"[0m")
            print("\t\tLinea: "+str(p.lineno)+"\t=> "+str(p.value))
        else:
            print(chr(27)+"[1;31m"+"\t ERROR: Error de sintaxis"+chr(27)+"[0m")
            print("\t\tLinea:  "+str(AnalizadorLexico.lexer.lineno))

    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()
lexer = AnalizadorLexico.lexer
def main():
    if (len(sys.argv) > 0):
        #script = sys.argv[1]
        script = 'prueba.c'
        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        # print (scriptdata)

        print(chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        #analisis = AnalizadorLexico.main(script)
        result = parser.parse(scriptdata)
        tablaan = AnalizadorLexico.tablaSimbolos
        #print(tablaan)
        # Obtener el número máximo de elementos en las listas del diccionario
        # Crear una tabla

        if AnalizadorLexico.error != 1:
            tabla = PrettyTable()

            # Establecer el encabezado de la tabla
            tabla.field_names = ["Token", "Linea"]

            # Iterar sobre el diccionario y agregar cada par clave-valor a la tabla
            for token, linea in tablaan.items():
                tabla.add_row([token, linea])

            # Imprimir la tabla
            print(tabla)
            print(chr(27) + "[0;32m" + "Sin errores detectados" + chr(27) + "[0m")

        print(chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")

    else:
        print(chr(27)+"[0;31m" +
              "Pase el archivo de script C como parametro:")
        print(chr(27)+"[0;36m"+"\t$ python AnalizadorSintactico.py" +
              chr(27)+"[1;31m"+" <filename>.c"+chr(27)+"[0m")

main()




