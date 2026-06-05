grammar gramatica_v4;

// PROGRAMA
root : PROGRAM LLA statement* LLC EOF ;

// SENTENCIAS
statement
    : declaration
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
    | switchStatement
    ;

// DECLARACION
declaration : declarationStatement SEMI ;
declarationStatement : DECL tipo VAR (ASIG (expr | arrayLiteral))? ;

// TIPOS
tipo : baseTipo ('[' ']')? ;

baseTipo
    : INT
    | FLOAT_T
    | STRING_T
    | BOOL
    | VOID
    ;

// ASIGNACION
assignment : assignmentStatement SEMI ;
assignmentStatement : VAR ASIG expr ;

// IF
ifStatement : IF PAI condition PAD block (ELSE block)? ;

// WHILE
whileStatement : WHILE PAI condition PAD block ;

// FOR
forStatement : FOR PAI forInit? SEMI condition? SEMI forUpdate? PAD block ;

forInit : declarationStatement | assignmentStatement ;
forUpdate : assignmentStatement ;

// SWITCH / CASE
switchStatement : SWITCH PAI expr PAD LLA caseClause* defaultClause? LLC ;
caseClause      : CASE literal COLON statement* ;
defaultClause   : DEFAULT COLON statement* ;
literal         : NUM | FLOAT | STRING ;

// FUNCIONES
functionDecl : tipo VAR PAI paramList? PAD block ;

paramList : param (COMMA param)* ;

param : tipo VAR ;

returnStmt : RETURN expr? SEMI ;

// PRINT
printStmt : PRINT PAI expr PAD SEMI ;

// IMPORT
importStmt : IMPORT VAR SEMI ;

// BREAK / CONTINUE
breakStmt : BREAK SEMI ;
continueStmt : CONTINUE SEMI ;

// BLOQUE
block : LLA statement* LLC ;

// CONDICION
condition
    : condition AND condition
    | condition OR condition
    | NOT condition
    | expr relop expr
    | TRUE
    | FALSE
    | PAI condition PAD
    ;

// EXPRESIONES
expr
    : PAI expr PAD
    | expr (MUL | DIV | MOD) expr
    | expr (SUM | RES) expr
    | expr relop expr
    | functionCall
    | VAR '[' expr ']'
    | TRUE
    | FALSE
    | NUM
    | FLOAT
    | STRING
    | VAR
    ;

// FUNCION CALL
functionCall : VAR PAI argList? PAD ;

argList : expr (COMMA expr)* ;

// ARRAY
arrayLiteral : '[' expr (COMMA expr)* ']' ;

// RELACIONALES
relop
    : GT
    | LT
    | GTE
    | LTE
    | EQ
    | NEQ
    ;

// TOKENS
PROGRAM : 'program' ;

DECL
    : 'var'
    | 'let'
    | 'const'
    ;

INT         : 'int' ;
FLOAT_T     : 'float' ;
STRING_T    : 'string' ;
BOOL        : 'bool' ;
VOID        : 'void' ;

IF      : 'if' ;
ELSE    : 'else' ;
WHILE   : 'while' ;
FOR     : 'for' ;

// IMPLEMENTACIÓN DE TOKENS
SWITCH  : 'switch' ;
CASE    : 'case' ;
DEFAULT : 'default' ;
COLON   : ':' ;

RETURN      : 'return' ;
PRINT       : 'print' ;
IMPORT      : 'import' ;
BREAK       : 'break' ;
CONTINUE    : 'continue' ;

TRUE  : 'true' ;
FALSE : 'false' ;

ASIG : '=' ;
SUM  : '+' ;
RES  : '-' ;
MUL  : '*' ;
DIV  : '/' ;
MOD  : '%' ;

AND : '&&' ;
OR  : '||' ;
NOT : '!' ;

GT  : '>'  ;
LT  : '<'  ;
GTE : '>=' ;
LTE : '<=' ;
EQ  : '==' ;
NEQ : '!=' ;

PAI   : '(' ;
PAD   : ')' ;
LLA   : '{' ;
LLC   : '}' ;
SEMI  : ';' ;
COMMA : ',' ;

// LITERALES
NUM : [0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]+ ;
STRING : '"' .*? '"' ;

VAR : [a-zA-Z_][a-zA-Z0-9_]* ;

// COMENTARIOS
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

// ESPACIOS
WS : [ \t\r\n]+ -> skip ;

// ERROR LEXICO
ERROR_CHAR
    : .
    {
        raise Exception(f"[Error Léxico] Línea {self.line}, Columna {self.column}: Símbolo no reconocido '{self.text}'")
    }
;