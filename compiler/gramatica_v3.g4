grammar gramatica_v3;

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
    | importStmt
    | breakStmt
    | continueStmt
    ;

// DECLARACION
declaration : declarationStatement ';' ;
declarationStatement : TVAR tipo VAR (ASIG (expr | arrayLiteral))? ;

// TIPOS
tipo : INT
     | FLOAT_T
     | STRING_T
     | BOOL
     | VOID
     | tipo '[' ']'
     ;

// ASIGNACION
assignment : assignmentStatement ';' ;
assignmentStatement : VAR ASIG expr ;

// IF
ifStatement : IF PAI condition PAD block (ELSE block)? ;

// WHILE
whileStatement : WHILE PAI condition PAD block ;

// FOR
forStatement : FOR PAI forInit? ';' condition? ';' forUpdate? PAD block ;

forInit : declarationStatement | assignmentStatement ;
forUpdate : assignmentStatement ;

// FUNCIONES
functionDecl : FUNCTION tipo VAR PAI paramList? PAD block ;

paramList : param (',' param)* ;

param : tipo VAR ;

returnStmt : RETURN expr? ';' ;

// PRINT
printStmt : PRINT PAI expr PAD ';' ;

// IMPORT
importStmt : IMPORT VAR ';' ;

// BREAK y CONTINUE
breakStmt : BREAK ';' ;
continueStmt : CONTINUE ';' ;

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
    | expr (MUL | DIV | MOD) expr
    | expr (SUM | RES) expr
    | expr relop expr
    | functionCall
    | arrayAccess
    | TRUE
    | FALSE
    | NUM
    | FLOAT_LITERAL
    | STRING_LITERAL
    | VAR
    ;

// FUNCION CALL
functionCall : VAR PAI argList? PAD ;

argList : expr (',' expr)* ;

// ARRAY
arrayLiteral : '[' expr (',' expr)* ']' ;

// ACCESO A ARRAY
arrayAccess : VAR '[' expr ']' ;

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

IMPORT : 'import' ;

BREAK : 'break' ;
CONTINUE : 'continue' ;

TRUE : 'true' ;
FALSE : 'false' ;

ASIG : '=' ;

SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;
MOD : '%' ;

AND : '&&' ;
OR  : '||' ;
NOT : '!' ;

PAI : '(' ;
PAD : ')' ;

LLA : '{' ;
LLC : '}' ;

NUM : [0-9]+ ;
FLOAT_LITERAL : [0-9]+ '.' [0-9]+ ;
STRING_LITERAL : '"' .*? '"' ;

VAR : [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ;

// ERROR LEXICO
ERROR_CHAR 
    : . 
    {
        raise Exception(f"[Error Léxico] Línea {self.line}, Columna {self.column}: Símbolo no reconocido '{self.text}'")
    }
;
