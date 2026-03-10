grammar Expresiones;

programa: PROGRAM bloque EOF;

bloque: LCORCH instruccion* RCORCH;

instruccion: declaracion
           | asignacion;

declaracion: INT EXP ASSIGN INT CVAR;

asignacion: EXP ASSIGN expresion CVAR;

expresion: expresion SUM termino
         | expresion RES termino
         | termino;

termino: termino MUL factor
       | termino DIV factor
       | factor;

factor: LPAREN expresion RPAREN
      | EXP
      | INT;

/* TOKENS */

PROGRAM : 'program';

EXP : [a-zA-Z_][a-zA-Z0-9_]*;
INT : [0-9]+;
SUM : '+';
RES : '-';
MUL : '*';
DIV : '/';

ASSIGN : '=';
LPAREN : '(';
RPAREN : ')';
LCORCH : '{';
RCORCH : '}';

CVAR : ';';
WS : [ \t\r\n]+ -> skip;
