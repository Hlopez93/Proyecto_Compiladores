grammar gramatica_v3;

// ================= PROGRAMA =================
root : PROGRAM LLA statement* LLC EOF ;

// ================= SENTENCIAS =================
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
    | switchStatement          // ★ IMPLEMENTACIÓN
    ;

// ================= DECLARACION =================
declaration : declarationStatement SEMI ;
declarationStatement : DECL tipo VAR (ASIG (expr | arrayLiteral))? ;

// ================= TIPOS =================
tipo : baseTipo ('[' ']')? ;

baseTipo
    : INT
    | FLOAT_T
    | STRING_T
    | BOOL
    | VOID
    ;

// ================= ASIGNACION =================
assignment : assignmentStatement SEMI ;
assignmentStatement : VAR ASIG expr ;

// ================= IF =================
ifStatement : IF PAI condition PAD block (ELSE block)? ;

// ================= WHILE =================
whileStatement : WHILE PAI condition PAD block ;

// ================= FOR =================
forStatement : FOR PAI forInit? SEMI condition? SEMI forUpdate? PAD block ;
forInit : declarationStatement | assignmentStatement ;
forUpdate : assignmentStatement ;

// ★ ================= SWITCH / CASE =================
switchStatement : SWITCH PAI expr PAD LLA caseClause* defaultClause? LLC ;
caseClause      : CASE literal COLON statement* ;
defaultClause   : DEFAULT COLON statement* ;
literal         : NUM | FLOAT | STRING ;

// ================= FUNCIONES =================
functionDecl : tipo VAR PAI paramList? PAD block ;
paramList : param (COMMA param)* ;
param : tipo VAR ;
returnStmt : RETURN expr? SEMI ;

// ================= PRINT =================
printStmt : PRINT PAI expr PAD SEMI ;

// ================= IMPORT =================
importStmt : IMPORT VAR SEMI ;

// ================= BREAK =================
breakStmt : BREAK SEMI ;
continueStmt : CONTINUE SEMI ;

// ================= BLOQUE =================
block : LLA statement* LLC ;

// ================= CONDICIONES =================
condition
    : condition AND condition
    | condition OR condition
    | NOT condition
    | expr relop expr
    | TRUE
    | FALSE
    | PAI condition PAD
    ;

// ================= EXPRESIONES =================
expr
    : expr SUM term
    | expr RES term
    | term
    ;

term
    : term MUL factor
    | term DIV factor
    | term MOD factor
    | factor
    ;

factor
    : PAI expr PAD
    | functionCall
    | VAR '[' expr ']'
    | TRUE
    | FALSE
    | NUM
    | FLOAT
    | STRING
    | VAR
    ;

// ================= FUNCION CALL =================
functionCall : VAR PAI argList? PAD ;
argList : expr (COMMA expr)* ;

// ================= ARRAY =================
arrayLiteral : '[' expr (COMMA expr)* ']' ;

// ================= RELACIONALES =================
relop : GT | LT | GTE | LTE | EQ | NEQ ;

// ================= TOKENS =================
PROGRAM : 'program' ;
DECL    : 'var' | 'let' | 'const' ;

INT      : 'int' ;
FLOAT_T  : 'float' ;
STRING_T : 'string' ;
BOOL     : 'bool' ;
VOID     : 'void' ;

IF       : 'if' ;
ELSE     : 'else' ;
WHILE    : 'while' ;
FOR      : 'for' ;

// ★ IMPLEMENTACIÓN DE TOKENS
SWITCH  : 'switch' ;
CASE    : 'case' ;
DEFAULT : 'default' ;
COLON   : ':' ;

RETURN   : 'return' ;
PRINT    : 'print' ;
IMPORT   : 'import' ;
BREAK    : 'break' ;
CONTINUE : 'continue' ;

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

NUM    : [0-9]+ ;
FLOAT  : [0-9]+ '.' [0-9]+ ;
STRING : '"' .*? '"' ;
VAR    : [a-zA-Z_][a-zA-Z0-9_]* ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
WS           : [ \t\r\n]+    -> skip ;