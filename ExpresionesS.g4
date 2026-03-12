grammar Expresiones;

root : expr+ EOF ;

expr : PAI expr PAD
     | expr (MUL | DIV) expr
     | expr (SUM | RES) expr
     | NUM
     ;

//Operadores
SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;
PAI : '(' ;
PAD : ')' ;
NUM : [0-9]+ ;
WS : [ \n\t\r]+ -> skip ;