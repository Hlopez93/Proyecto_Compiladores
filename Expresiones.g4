grammar Expresiones;

// REGLA INICIAL
root : ID '{' statement* '}' EOF ;

// SENTENCIAS
statement : declaration ';'
    | assignment ';'
    | ifStatement
    ;

// DECLARACIÓN
declaration : VAR type ID ('=' expression)? ;

type : INT ;

// ASIGNACIÓN
assignment : ID '=' expression ;

// IF / ELSE
ifStatement : 'if' '(' expression ')' block ('else' block)? ;

block : '{' statement* '}' ;

// EXPRESIONES (con precedencia)
expression : logicalOrExpression ;

logicalOrExpression : logicalAndExpression ( '||' logicalAndExpression )* ;

logicalAndExpression : equalityExpression ( '&&' equalityExpression )* ;

equalityExpression : relationalExpression ( ('==' | '!=' | '<>') relationalExpression )* ;

relationalExpression : additiveExpression ( ('<' | '>' | '<=' | '>=') additiveExpression )* ;

additiveExpression : multiplicativeExpression ( ('+' | '-') multiplicativeExpression )* ;

multiplicativeExpression : unaryExpression ( ('*' | '/') unaryExpression )* ;

unaryExpression : '!' unaryExpression
    | primary
    ;

primary : NUM
    | ID
    | '(' expression ')'
    ;

// TOKENS
VAR : 'var' ;
NUM : [0-9]+ ;
ID : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : 'int' ;
WS : [ \t\r\n]+ -> skip ;