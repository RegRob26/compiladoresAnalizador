import sys
import ply.lex as lex
import copy
from collections import defaultdict
tablaSimbolos = defaultdict(list)

tokens = (
    # Palabras reservadas
    'PRINTF','SCANF','IF','ELSE','FOR','DO','WHILE','SWITCH',
    'CASE','BREAK','CONTINUE','TYPEDEF','STRUCT','CONST','RETURN','INT','FLOAT','CHAR',
    
    #OTROS
    'ID','NUMERO','CADENA','COMENTARIO',
    'COMMENTS','COMMENTS_C99',
    # SIMBOLOS
    'SUMA','RESTA','MULTI','DIV',
    #'MOD',
    'PUNTOCOMA','COMA','APAREN','CPAREN','ACORCHETE','CCORCHETE','ALLAVE','CLLAVE',
    'DOSPUNTOS','AMPERSANT','HASHTAG','PUNTO','COMILLAS','APOSTROFE','DPUNTOS_DPUNTOS',
    'AND','OR','NOT','XOR',
    'MENOR','MENORIGUAL','MAYOR','MAYORIGUAL','IGUAL','ASIGNAR','DISTINTO',
    'FUNCT_FLECHA','INCREMENTO','MASMAS','MENOSMENOS',
)

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
#Palabras reservadas
def t_PRINTF(t):
    r'printf'
    return t

def t_SCANF(t):
    r'scanf'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_DO(t):
    r'do'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_TYPEDEF(t):
    r'typedef'
    return t

def t_STRUCT(t):
    r'struct'
    return t

def t_CONST(t):
    r'const'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_CHAR(t):
    r'char'
    return t
#Simbolos
    
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIV = r'/'
#t_MOD = r'\%'
t_AND = r'\&'
t_OR = r'\|'
t_NOT = r'\!'
t_XOR = r'\^'
t_MENOR = r'<'
t_MAYOR = r'>'
t_ASIGNAR = r'='

t_PUNTOCOMA = r';'
t_COMA     = r','
t_APAREN    = r'\('
t_CPAREN    = r'\)'
t_ACORCHETE  = r'\['
t_CCORCHETE  = r'\]'
t_ALLAVE   = r'{'
t_CLLAVE    = r'}'
t_DOSPUNTOS    = r':'
t_HASHTAG   = r'\#'
#t_PUNTO = r'\.'
t_COMILLAS    = r'\"'
t_APOSTROFE = r'\''

def FUNCT_FLECHA(t):
    r'=>'
    return t
def INCREMENTO(t):
    r'\+='
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_MENOSMENOS(t):
    r'--'
    return t

def t_MASMAS(t):
    r'\+\+'
    return t

def t_DPUNTOS_DPUNTOS(t):
    r'::'
    return t

#OTROS
def t_ID(t):
    r'(_?[A-Za-z0-9])*[A-Za-z](_?[A-Za-z0-9])*'
    try:
        tablaSimbolos[t.value].append(copy.deepcopy(t.lineno))
        return t
    except:
        print("Except")
        pass

def t_CADENA(t):
    r'"?(\w+ \ *\w*\d* \ *)"'
    return t

def t_COMENTARIO(t):
    r'//(.)*'
    return t

def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENTS_C99(t):
    r'(\/\/|\#)(.)*?\n'
    t.lexer.lineno += 1

def t_NUMERO(t):
    r'[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
    return t
error = 0

def t_error(t):
    global error
    error = 1
    print (chr(27)+"[1;31m"+"\t ERROR: Caracter Ilegal"+chr(27)+"[0m")
    print ("\t\tLinea: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)
    with open('errores.txt', 'a+') as estado:
        estado.write(str("\t\tLinea: "+str(t.lexer.lineno)+"\t=> " + t.value[0] + "\n"))

def tablaSimbolosFunc(entrada, dato, tablaSimbolos):
    if entrada == 0:
        tablaSimbolos.append(dato[:])
        return 1
    if entrada == 1:
        tablaSimbolos.pop()
        return 1

lexer = lex.lex()

def main(script):
    simbolo = []
    if (len(sys.argv) > 0):
        #script = sys.argv[1]
        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)
        lexer.input(scriptdata)
        print (chr(27)+"[0;36m"+"INICIA ANALISIS LEXICO"+chr(27)+"[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break

            #print ("\t"+str(i)+" - "+"Linea: "+str(tok.lineno)+"\t"+str(tok.type)+"\t-->  "+str(tok.value))
            if tok.type == "ID":
                with open('validos.txt', 'a+') as estado:
                    estado.write("\t"+str(i)+" - "+"Linea: "+str(tok.lineno)+"\t"+str(tok.type)+"\t-->  "+str(tok.value) + "\n")
                simbolo.append(tok.lineno)
                simbolo.append(tok.type)
                simbolo.append(tok.value)

                #print(simbolo)
                tablaSimbolos[simbolo[2]].append(copy.deepcopy(simbolo[0]))
                #tablaSimbolosFunc(0, simbolo, tablaSimbolos)

            del simbolo[:]
            i += 1
        print (chr(27)+"[0;36m"+"TERMINA ANALISIS LEXICO"+chr(27)+"[0m")
        print(error)
        if(error):
            return 1
        return tablaSimbolos

    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de PRUEBA como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python AnalizadorLexico.py"+chr(27)+"[1;31m"+" <filename>.js"+chr(27)+"[0m")
