grammar Expresiones;

// PROGRAMA
root : PROGRAM LLA statement* LLC EOF ;

// SENTENCIAS
statement 
    : declaration
    | assignment
    | ifStatement
    ;

// DECLARACIÓN
declaration 
    : TVAR tipo VAR ('=' expr)? ';'
    ;

// NUEVA REGLA DE TIPOS
tipo 
    : INT 
    | FLOAT 
    | STRING 
    | BOOL 
    ;

// ASIGNACIÓN
assignment : VAR ASIG expr ';' ;

// IF
ifStatement : IF PAI condition PAD block (ELSE block)? ;

// ESTRUCTURA DE BLOQUE
block : LLA statement* LLC ;

// CONDICIÓN
condition 
    : condition AND condition
    | condition OR condition
    | NOT condition
    | expr relop expr
    | PAI condition PAD
    ;

// EXPRESIONES
expr 
    : PAI expr PAD
    | expr (MUL | DIV) expr
    | expr (SUM | RES) expr
    | NUM
    | FLOAT_NUM
    | STRING_LITERAL
    | BOOL_LITERAL
    | VAR
    ;

// OPERADORES RELACIONALES
relop 
    : '>'
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
FLOAT : 'float' ;
STRING : 'string' ;
BOOL : 'bool' ;

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

FLOAT_NUM : [0-9]+ '.' [0-9]+ ;
STRING_LITERAL : '"' .*? '"' ;
BOOL_LITERAL : 'true' | 'false' ;

NUM : [0-9]+ ;

VAR : [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ;
