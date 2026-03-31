grammar Expresiones;

// PROGRAMA
root : PROGRAM LLA statement* LLC EOF ;

// SENTENCIAS
statement : declaration
    | assignment
    | ifStatement
    | whileStatement
    | forStatement
    | functionDecl
    | returnStmt
    | printStmt
    ;

// DECLARACION
declaration : TVAR tipo VAR (ASIG expr)? ';' ;

// TIPOS
tipo : INT 
     | FLOAT_T 
     | STRING_T 
     | BOOL 
     | VOID 
     ;

// ASIGNACION
assignment : VAR ASIG expr ';' ;

// IF
ifStatement : IF PAI condition PAD block (ELSE block)? ;

// WHILE
whileStatement : WHILE PAI condition PAD block ;

// FOR
forStatement : FOR PAI (declaration | assignment)? condition? ';' assignment? PAD block ;

// FUNCIONES
functionDecl : FUNCTION tipo VAR PAI paramList? PAD block ;

paramList : param (',' param)* ;

param : tipo VAR ;

returnStmt : RETURN expr? ';' ;

// PRINT
printStmt : PRINT PAI expr PAD ';' ;

// ESTRUCTURA DE BLOQUE
block : LLA statement* LLC ;

// CONDICION
condition : condition AND condition
    | condition OR condition
    | NOT condition
    | expr relop expr
    | TRUE
    | FALSE
    | PAI condition PAD
    ;

// EXPRESIONES
expr : PAI expr PAD
    | expr (MUL | DIV) expr
    | expr (SUM | RES) expr
    | expr relop expr
    | functionCall
    | TRUE
    | FALSE
    | NUM
    | FLOAT
    | STRING
    | VAR
    ;

// FUNCION CALL
functionCall : VAR PAI argList? PAD ;

argList : expr (',' expr)* ;

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
TVAR : 'var'
    | 'let'
    | 'const'
    ;

INT : 'int' ;
FLOAT_T : 'float' ;
STRING_T : 'string' ;
BOOL : 'bool' ;
VOID : 'void' ;

IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;

FUNCTION : 'function' ;
RETURN : 'return' ;

PRINT : 'print' ;

TRUE : 'true' ;
FALSE : 'false' ;

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
FLOAT : [0-9]+ '.' [0-9]+ ;
STRING : '"' .*? '"' ;

VAR : [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ;

// ERROR LEXICO
ERROR_CHAR : . ;