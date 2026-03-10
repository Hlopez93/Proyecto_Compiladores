grammar Expresiones;

// PROGRAMA
root : PROGRAM LLA statement* LLC EOF ;

// SENTENCIAS
statement : declaration
    | assignment
    | ifStatement
    ;

// DECLARACION
declaration : TVAR INT VAR ';' ;

// ASIGNACION
assignment : VAR ASIG expr ';' ;

// IF
ifStatement : IF PAI condition PAD block (ELSE block)? ;

// ESTRUCTURA DE BLOQUE
block : LLA statement* LLC ;

// CONDICION
condition : condition AND condition
    | condition OR condition
    | NOT condition
    | expr relop expr
    | PAI condition PAD
    ;

// EXPRESIONES
expr : PAI expr PAD
    | expr (MUL | DIV) expr
    | expr (SUM | RES) expr
    | NUM
    | VAR
    ;

// OPERADORES RELACIONALES
relop : '>'
    | '<'
    | '>='
    | '<='
    | '=='
    | '!='
    ;

// TOKENS
PROGRAM : 'program' ;
TVAR : 'var' ;
INT : 'int' ;
IF : 'if' ;
ELSE : 'else' ;

ASIG : '=' ;

SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;

AND : '&&' ;
OR  : '||' ;
NOT : '!' ;

PAI : '(' ;
PAD : ')' ;

LLA : '{' ;
LLC : '}' ;

NUM : [0-9]+ ;
VAR : [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ;