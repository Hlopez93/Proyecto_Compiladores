# Generated from gramatica_v4.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,328,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,5,
        0,68,8,0,10,0,12,0,71,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,88,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,99,8,3,3,3,101,8,3,1,4,1,4,1,4,3,4,106,8,4,1,5,1,5,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,124,8,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,135,8,10,1,10,1,10,3,10,
        139,8,10,1,10,1,10,3,10,143,8,10,1,10,1,10,1,10,1,11,1,11,3,11,150,
        8,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,160,8,13,10,13,
        12,13,163,9,13,1,13,3,13,166,8,13,1,13,1,13,1,14,1,14,1,14,1,14,
        5,14,174,8,14,10,14,12,14,177,9,14,1,15,1,15,1,15,5,15,182,8,15,
        10,15,12,15,185,9,15,1,16,1,16,1,17,1,17,1,17,1,17,3,17,193,8,17,
        1,17,1,17,1,17,1,18,1,18,1,18,5,18,201,8,18,10,18,12,18,204,9,18,
        1,19,1,19,1,19,1,20,1,20,3,20,211,8,20,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,
        1,25,1,25,5,25,233,8,25,10,25,12,25,236,9,25,1,25,1,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,253,
        8,26,1,26,1,26,1,26,1,26,1,26,1,26,5,26,261,8,26,10,26,12,26,264,
        9,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,3,27,283,8,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,5,27,295,8,27,10,27,12,27,298,9,27,1,28,
        1,28,1,28,3,28,303,8,28,1,28,1,28,1,29,1,29,1,29,5,29,310,8,29,10,
        29,12,29,313,9,29,1,30,1,30,1,30,1,30,5,30,319,8,30,10,30,12,30,
        322,9,30,1,30,1,30,1,31,1,31,1,31,0,2,52,54,32,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,0,5,1,0,5,9,1,0,46,48,1,0,28,30,1,0,26,27,1,0,34,39,343,0,
        64,1,0,0,0,2,87,1,0,0,0,4,89,1,0,0,0,6,92,1,0,0,0,8,102,1,0,0,0,
        10,107,1,0,0,0,12,109,1,0,0,0,14,112,1,0,0,0,16,116,1,0,0,0,18,125,
        1,0,0,0,20,131,1,0,0,0,22,149,1,0,0,0,24,151,1,0,0,0,26,153,1,0,
        0,0,28,169,1,0,0,0,30,178,1,0,0,0,32,186,1,0,0,0,34,188,1,0,0,0,
        36,197,1,0,0,0,38,205,1,0,0,0,40,208,1,0,0,0,42,214,1,0,0,0,44,220,
        1,0,0,0,46,224,1,0,0,0,48,227,1,0,0,0,50,230,1,0,0,0,52,252,1,0,
        0,0,54,282,1,0,0,0,56,299,1,0,0,0,58,306,1,0,0,0,60,314,1,0,0,0,
        62,325,1,0,0,0,64,65,5,3,0,0,65,69,5,42,0,0,66,68,3,2,1,0,67,66,
        1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,
        71,69,1,0,0,0,72,73,5,43,0,0,73,74,5,0,0,1,74,1,1,0,0,0,75,88,3,
        4,2,0,76,88,3,12,6,0,77,88,3,16,8,0,78,88,3,18,9,0,79,88,3,20,10,
        0,80,88,3,34,17,0,81,88,3,40,20,0,82,88,3,42,21,0,83,88,3,44,22,
        0,84,88,3,46,23,0,85,88,3,48,24,0,86,88,3,26,13,0,87,75,1,0,0,0,
        87,76,1,0,0,0,87,77,1,0,0,0,87,78,1,0,0,0,87,79,1,0,0,0,87,80,1,
        0,0,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,87,84,1,0,0,0,87,
        85,1,0,0,0,87,86,1,0,0,0,88,3,1,0,0,0,89,90,3,6,3,0,90,91,5,44,0,
        0,91,5,1,0,0,0,92,93,5,4,0,0,93,94,3,8,4,0,94,100,5,49,0,0,95,98,
        5,25,0,0,96,99,3,54,27,0,97,99,3,60,30,0,98,96,1,0,0,0,98,97,1,0,
        0,0,99,101,1,0,0,0,100,95,1,0,0,0,100,101,1,0,0,0,101,7,1,0,0,0,
        102,105,3,10,5,0,103,104,5,1,0,0,104,106,5,2,0,0,105,103,1,0,0,0,
        105,106,1,0,0,0,106,9,1,0,0,0,107,108,7,0,0,0,108,11,1,0,0,0,109,
        110,3,14,7,0,110,111,5,44,0,0,111,13,1,0,0,0,112,113,5,49,0,0,113,
        114,5,25,0,0,114,115,3,54,27,0,115,15,1,0,0,0,116,117,5,10,0,0,117,
        118,5,40,0,0,118,119,3,52,26,0,119,120,5,41,0,0,120,123,3,50,25,
        0,121,122,5,11,0,0,122,124,3,50,25,0,123,121,1,0,0,0,123,124,1,0,
        0,0,124,17,1,0,0,0,125,126,5,12,0,0,126,127,5,40,0,0,127,128,3,52,
        26,0,128,129,5,41,0,0,129,130,3,50,25,0,130,19,1,0,0,0,131,132,5,
        13,0,0,132,134,5,40,0,0,133,135,3,22,11,0,134,133,1,0,0,0,134,135,
        1,0,0,0,135,136,1,0,0,0,136,138,5,44,0,0,137,139,3,52,26,0,138,137,
        1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,142,5,44,0,0,141,143,
        3,24,12,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,
        5,41,0,0,145,146,3,50,25,0,146,21,1,0,0,0,147,150,3,6,3,0,148,150,
        3,14,7,0,149,147,1,0,0,0,149,148,1,0,0,0,150,23,1,0,0,0,151,152,
        3,14,7,0,152,25,1,0,0,0,153,154,5,14,0,0,154,155,5,40,0,0,155,156,
        3,54,27,0,156,157,5,41,0,0,157,161,5,42,0,0,158,160,3,28,14,0,159,
        158,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,
        165,1,0,0,0,163,161,1,0,0,0,164,166,3,30,15,0,165,164,1,0,0,0,165,
        166,1,0,0,0,166,167,1,0,0,0,167,168,5,43,0,0,168,27,1,0,0,0,169,
        170,5,15,0,0,170,171,3,32,16,0,171,175,5,17,0,0,172,174,3,2,1,0,
        173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,
        176,29,1,0,0,0,177,175,1,0,0,0,178,179,5,16,0,0,179,183,5,17,0,0,
        180,182,3,2,1,0,181,180,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,
        183,184,1,0,0,0,184,31,1,0,0,0,185,183,1,0,0,0,186,187,7,1,0,0,187,
        33,1,0,0,0,188,189,3,8,4,0,189,190,5,49,0,0,190,192,5,40,0,0,191,
        193,3,36,18,0,192,191,1,0,0,0,192,193,1,0,0,0,193,194,1,0,0,0,194,
        195,5,41,0,0,195,196,3,50,25,0,196,35,1,0,0,0,197,202,3,38,19,0,
        198,199,5,45,0,0,199,201,3,38,19,0,200,198,1,0,0,0,201,204,1,0,0,
        0,202,200,1,0,0,0,202,203,1,0,0,0,203,37,1,0,0,0,204,202,1,0,0,0,
        205,206,3,8,4,0,206,207,5,49,0,0,207,39,1,0,0,0,208,210,5,18,0,0,
        209,211,3,54,27,0,210,209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,
        0,212,213,5,44,0,0,213,41,1,0,0,0,214,215,5,19,0,0,215,216,5,40,
        0,0,216,217,3,54,27,0,217,218,5,41,0,0,218,219,5,44,0,0,219,43,1,
        0,0,0,220,221,5,20,0,0,221,222,5,49,0,0,222,223,5,44,0,0,223,45,
        1,0,0,0,224,225,5,21,0,0,225,226,5,44,0,0,226,47,1,0,0,0,227,228,
        5,22,0,0,228,229,5,44,0,0,229,49,1,0,0,0,230,234,5,42,0,0,231,233,
        3,2,1,0,232,231,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,
        1,0,0,0,235,237,1,0,0,0,236,234,1,0,0,0,237,238,5,43,0,0,238,51,
        1,0,0,0,239,240,6,26,-1,0,240,241,5,33,0,0,241,253,3,52,26,5,242,
        243,3,54,27,0,243,244,3,62,31,0,244,245,3,54,27,0,245,253,1,0,0,
        0,246,253,5,23,0,0,247,253,5,24,0,0,248,249,5,40,0,0,249,250,3,52,
        26,0,250,251,5,41,0,0,251,253,1,0,0,0,252,239,1,0,0,0,252,242,1,
        0,0,0,252,246,1,0,0,0,252,247,1,0,0,0,252,248,1,0,0,0,253,262,1,
        0,0,0,254,255,10,7,0,0,255,256,5,31,0,0,256,261,3,52,26,8,257,258,
        10,6,0,0,258,259,5,32,0,0,259,261,3,52,26,7,260,254,1,0,0,0,260,
        257,1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,
        53,1,0,0,0,264,262,1,0,0,0,265,266,6,27,-1,0,266,267,5,40,0,0,267,
        268,3,54,27,0,268,269,5,41,0,0,269,283,1,0,0,0,270,283,3,56,28,0,
        271,272,5,49,0,0,272,273,5,1,0,0,273,274,3,54,27,0,274,275,5,2,0,
        0,275,283,1,0,0,0,276,283,5,23,0,0,277,283,5,24,0,0,278,283,5,46,
        0,0,279,283,5,47,0,0,280,283,5,48,0,0,281,283,5,49,0,0,282,265,1,
        0,0,0,282,270,1,0,0,0,282,271,1,0,0,0,282,276,1,0,0,0,282,277,1,
        0,0,0,282,278,1,0,0,0,282,279,1,0,0,0,282,280,1,0,0,0,282,281,1,
        0,0,0,283,296,1,0,0,0,284,285,10,11,0,0,285,286,7,2,0,0,286,295,
        3,54,27,12,287,288,10,10,0,0,288,289,7,3,0,0,289,295,3,54,27,11,
        290,291,10,9,0,0,291,292,3,62,31,0,292,293,3,54,27,10,293,295,1,
        0,0,0,294,284,1,0,0,0,294,287,1,0,0,0,294,290,1,0,0,0,295,298,1,
        0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,55,1,0,0,0,298,296,1,0,
        0,0,299,300,5,49,0,0,300,302,5,40,0,0,301,303,3,58,29,0,302,301,
        1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,305,5,41,0,0,305,57,
        1,0,0,0,306,311,3,54,27,0,307,308,5,45,0,0,308,310,3,54,27,0,309,
        307,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,
        59,1,0,0,0,313,311,1,0,0,0,314,315,5,1,0,0,315,320,3,54,27,0,316,
        317,5,45,0,0,317,319,3,54,27,0,318,316,1,0,0,0,319,322,1,0,0,0,320,
        318,1,0,0,0,320,321,1,0,0,0,321,323,1,0,0,0,322,320,1,0,0,0,323,
        324,5,2,0,0,324,61,1,0,0,0,325,326,7,4,0,0,326,63,1,0,0,0,27,69,
        87,98,100,105,123,134,138,142,149,161,165,175,183,192,202,210,234,
        252,260,262,282,294,296,302,311,320
    ]

class gramatica_v4Parser ( Parser ):

    grammarFileName = "gramatica_v4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'program'", "<INVALID>", 
                     "'int'", "'float'", "'string'", "'bool'", "'void'", 
                     "'if'", "'else'", "'while'", "'for'", "'switch'", "'case'", 
                     "'default'", "':'", "'return'", "'print'", "'import'", 
                     "'break'", "'continue'", "'true'", "'false'", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", 
                     "'!'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PROGRAM", 
                      "DECL", "INT", "FLOAT_T", "STRING_T", "BOOL", "VOID", 
                      "IF", "ELSE", "WHILE", "FOR", "SWITCH", "CASE", "DEFAULT", 
                      "COLON", "RETURN", "PRINT", "IMPORT", "BREAK", "CONTINUE", 
                      "TRUE", "FALSE", "ASIG", "SUM", "RES", "MUL", "DIV", 
                      "MOD", "AND", "OR", "NOT", "GT", "LT", "GTE", "LTE", 
                      "EQ", "NEQ", "PAI", "PAD", "LLA", "LLC", "SEMI", "COMMA", 
                      "NUM", "FLOAT", "STRING", "VAR", "LINE_COMMENT", "WS", 
                      "ERROR_CHAR" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_declarationStatement = 3
    RULE_tipo = 4
    RULE_baseTipo = 5
    RULE_assignment = 6
    RULE_assignmentStatement = 7
    RULE_ifStatement = 8
    RULE_whileStatement = 9
    RULE_forStatement = 10
    RULE_forInit = 11
    RULE_forUpdate = 12
    RULE_switchStatement = 13
    RULE_caseClause = 14
    RULE_defaultClause = 15
    RULE_literal = 16
    RULE_functionDecl = 17
    RULE_paramList = 18
    RULE_param = 19
    RULE_returnStmt = 20
    RULE_printStmt = 21
    RULE_importStmt = 22
    RULE_breakStmt = 23
    RULE_continueStmt = 24
    RULE_block = 25
    RULE_condition = 26
    RULE_expr = 27
    RULE_functionCall = 28
    RULE_argList = 29
    RULE_arrayLiteral = 30
    RULE_relop = 31

    ruleNames =  [ "root", "statement", "declaration", "declarationStatement", 
                   "tipo", "baseTipo", "assignment", "assignmentStatement", 
                   "ifStatement", "whileStatement", "forStatement", "forInit", 
                   "forUpdate", "switchStatement", "caseClause", "defaultClause", 
                   "literal", "functionDecl", "paramList", "param", "returnStmt", 
                   "printStmt", "importStmt", "breakStmt", "continueStmt", 
                   "block", "condition", "expr", "functionCall", "argList", 
                   "arrayLiteral", "relop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    PROGRAM=3
    DECL=4
    INT=5
    FLOAT_T=6
    STRING_T=7
    BOOL=8
    VOID=9
    IF=10
    ELSE=11
    WHILE=12
    FOR=13
    SWITCH=14
    CASE=15
    DEFAULT=16
    COLON=17
    RETURN=18
    PRINT=19
    IMPORT=20
    BREAK=21
    CONTINUE=22
    TRUE=23
    FALSE=24
    ASIG=25
    SUM=26
    RES=27
    MUL=28
    DIV=29
    MOD=30
    AND=31
    OR=32
    NOT=33
    GT=34
    LT=35
    GTE=36
    LTE=37
    EQ=38
    NEQ=39
    PAI=40
    PAD=41
    LLA=42
    LLC=43
    SEMI=44
    COMMA=45
    NUM=46
    FLOAT=47
    STRING=48
    VAR=49
    LINE_COMMENT=50
    WS=51
    ERROR_CHAR=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(gramatica_v4Parser.PROGRAM, 0)

        def LLA(self):
            return self.getToken(gramatica_v4Parser.LLA, 0)

        def LLC(self):
            return self.getToken(gramatica_v4Parser.LLC, 0)

        def EOF(self):
            return self.getToken(gramatica_v4Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.StatementContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = gramatica_v4Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(gramatica_v4Parser.PROGRAM)
            self.state = 65
            self.match(gramatica_v4Parser.LLA)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949961578480) != 0):
                self.state = 66
                self.statement()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(gramatica_v4Parser.LLC)
            self.state = 73
            self.match(gramatica_v4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(gramatica_v4Parser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(gramatica_v4Parser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ForStatementContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(gramatica_v4Parser.FunctionDeclContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ReturnStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(gramatica_v4Parser.PrintStmtContext,0)


        def importStmt(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ImportStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ContinueStmtContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.SwitchStatementContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramatica_v4Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.declaration()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.assignment()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.ifStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.whileStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.forStatement()
                pass
            elif token in [5, 6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.functionDecl()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.returnStmt()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 8)
                self.state = 82
                self.printStmt()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 9)
                self.state = 83
                self.importStmt()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 10)
                self.state = 84
                self.breakStmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 11)
                self.state = 85
                self.continueStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 12)
                self.state = 86
                self.switchStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.DeclarationStatementContext,0)


        def SEMI(self):
            return self.getToken(gramatica_v4Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = gramatica_v4Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.declarationStatement()
            self.state = 90
            self.match(gramatica_v4Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECL(self):
            return self.getToken(gramatica_v4Parser.DECL, 0)

        def tipo(self):
            return self.getTypedRuleContext(gramatica_v4Parser.TipoContext,0)


        def VAR(self):
            return self.getToken(gramatica_v4Parser.VAR, 0)

        def ASIG(self):
            return self.getToken(gramatica_v4Parser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_declarationStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationStatement(self):

        localctx = gramatica_v4Parser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declarationStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(gramatica_v4Parser.DECL)
            self.state = 93
            self.tipo()
            self.state = 94
            self.match(gramatica_v4Parser.VAR)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 95
                self.match(gramatica_v4Parser.ASIG)
                self.state = 98
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23, 24, 40, 46, 47, 48, 49]:
                    self.state = 96
                    self.expr(0)
                    pass
                elif token in [1]:
                    self.state = 97
                    self.arrayLiteral()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseTipo(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BaseTipoContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_tipo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = gramatica_v4Parser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.baseTipo()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 103
                self.match(gramatica_v4Parser.T__0)
                self.state = 104
                self.match(gramatica_v4Parser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(gramatica_v4Parser.INT, 0)

        def FLOAT_T(self):
            return self.getToken(gramatica_v4Parser.FLOAT_T, 0)

        def STRING_T(self):
            return self.getToken(gramatica_v4Parser.STRING_T, 0)

        def BOOL(self):
            return self.getToken(gramatica_v4Parser.BOOL, 0)

        def VOID(self):
            return self.getToken(gramatica_v4Parser.VOID, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_baseTipo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseTipo" ):
                return visitor.visitBaseTipo(self)
            else:
                return visitor.visitChildren(self)




    def baseTipo(self):

        localctx = gramatica_v4Parser.BaseTipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_baseTipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.AssignmentStatementContext,0)


        def SEMI(self):
            return self.getToken(gramatica_v4Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramatica_v4Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.assignmentStatement()
            self.state = 110
            self.match(gramatica_v4Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(gramatica_v4Parser.VAR, 0)

        def ASIG(self):
            return self.getToken(gramatica_v4Parser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_assignmentStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = gramatica_v4Parser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(gramatica_v4Parser.VAR)
            self.state = 113
            self.match(gramatica_v4Parser.ASIG)
            self.state = 114
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(gramatica_v4Parser.IF, 0)

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def condition(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ConditionContext,0)


        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.BlockContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,i)


        def ELSE(self):
            return self.getToken(gramatica_v4Parser.ELSE, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = gramatica_v4Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(gramatica_v4Parser.IF)
            self.state = 117
            self.match(gramatica_v4Parser.PAI)
            self.state = 118
            self.condition(0)
            self.state = 119
            self.match(gramatica_v4Parser.PAD)
            self.state = 120
            self.block()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 121
                self.match(gramatica_v4Parser.ELSE)
                self.state = 122
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramatica_v4Parser.WHILE, 0)

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def condition(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ConditionContext,0)


        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = gramatica_v4Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(gramatica_v4Parser.WHILE)
            self.state = 126
            self.match(gramatica_v4Parser.PAI)
            self.state = 127
            self.condition(0)
            self.state = 128
            self.match(gramatica_v4Parser.PAD)
            self.state = 129
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(gramatica_v4Parser.FOR, 0)

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.SEMI)
            else:
                return self.getToken(gramatica_v4Parser.SEMI, i)

        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,0)


        def forInit(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ForInitContext,0)


        def condition(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ConditionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ForUpdateContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = gramatica_v4Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(gramatica_v4Parser.FOR)
            self.state = 132
            self.match(gramatica_v4Parser.PAI)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==49:
                self.state = 133
                self.forInit()


            self.state = 136
            self.match(gramatica_v4Parser.SEMI)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056639289393152) != 0):
                self.state = 137
                self.condition(0)


            self.state = 140
            self.match(gramatica_v4Parser.SEMI)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 141
                self.forUpdate()


            self.state = 144
            self.match(gramatica_v4Parser.PAD)
            self.state = 145
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.DeclarationStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_forInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = gramatica_v4Parser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forInit)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.declarationStatement()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.assignmentStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_forUpdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = gramatica_v4Parser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.assignmentStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(gramatica_v4Parser.SWITCH, 0)

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def LLA(self):
            return self.getToken(gramatica_v4Parser.LLA, 0)

        def LLC(self):
            return self.getToken(gramatica_v4Parser.LLC, 0)

        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.CaseClauseContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(gramatica_v4Parser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_switchStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = gramatica_v4Parser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(gramatica_v4Parser.SWITCH)
            self.state = 154
            self.match(gramatica_v4Parser.PAI)
            self.state = 155
            self.expr(0)
            self.state = 156
            self.match(gramatica_v4Parser.PAD)
            self.state = 157
            self.match(gramatica_v4Parser.LLA)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 158
                self.caseClause()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 164
                self.defaultClause()


            self.state = 167
            self.match(gramatica_v4Parser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(gramatica_v4Parser.CASE, 0)

        def literal(self):
            return self.getTypedRuleContext(gramatica_v4Parser.LiteralContext,0)


        def COLON(self):
            return self.getToken(gramatica_v4Parser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.StatementContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_caseClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseClause" ):
                return visitor.visitCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def caseClause(self):

        localctx = gramatica_v4Parser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(gramatica_v4Parser.CASE)
            self.state = 170
            self.literal()
            self.state = 171
            self.match(gramatica_v4Parser.COLON)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949961578480) != 0):
                self.state = 172
                self.statement()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(gramatica_v4Parser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(gramatica_v4Parser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.StatementContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_defaultClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultClause" ):
                return visitor.visitDefaultClause(self)
            else:
                return visitor.visitChildren(self)




    def defaultClause(self):

        localctx = gramatica_v4Parser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(gramatica_v4Parser.DEFAULT)
            self.state = 179
            self.match(gramatica_v4Parser.COLON)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949961578480) != 0):
                self.state = 180
                self.statement()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(gramatica_v4Parser.NUM, 0)

        def FLOAT(self):
            return self.getToken(gramatica_v4Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(gramatica_v4Parser.STRING, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = gramatica_v4Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 492581209243648) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(gramatica_v4Parser.TipoContext,0)


        def VAR(self):
            return self.getToken(gramatica_v4Parser.VAR, 0)

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ParamListContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = gramatica_v4Parser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.tipo()
            self.state = 189
            self.match(gramatica_v4Parser.VAR)
            self.state = 190
            self.match(gramatica_v4Parser.PAI)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0):
                self.state = 191
                self.paramList()


            self.state = 194
            self.match(gramatica_v4Parser.PAD)
            self.state = 195
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ParamContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.COMMA)
            else:
                return self.getToken(gramatica_v4Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = gramatica_v4Parser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.param()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 198
                self.match(gramatica_v4Parser.COMMA)
                self.state = 199
                self.param()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(gramatica_v4Parser.TipoContext,0)


        def VAR(self):
            return self.getToken(gramatica_v4Parser.VAR, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = gramatica_v4Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.tipo()
            self.state = 206
            self.match(gramatica_v4Parser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(gramatica_v4Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(gramatica_v4Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = gramatica_v4Parser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(gramatica_v4Parser.RETURN)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056630699458560) != 0):
                self.state = 209
                self.expr(0)


            self.state = 212
            self.match(gramatica_v4Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(gramatica_v4Parser.PRINT, 0)

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def SEMI(self):
            return self.getToken(gramatica_v4Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_printStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = gramatica_v4Parser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(gramatica_v4Parser.PRINT)
            self.state = 215
            self.match(gramatica_v4Parser.PAI)
            self.state = 216
            self.expr(0)
            self.state = 217
            self.match(gramatica_v4Parser.PAD)
            self.state = 218
            self.match(gramatica_v4Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(gramatica_v4Parser.IMPORT, 0)

        def VAR(self):
            return self.getToken(gramatica_v4Parser.VAR, 0)

        def SEMI(self):
            return self.getToken(gramatica_v4Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_importStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStmt" ):
                return visitor.visitImportStmt(self)
            else:
                return visitor.visitChildren(self)




    def importStmt(self):

        localctx = gramatica_v4Parser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(gramatica_v4Parser.IMPORT)
            self.state = 221
            self.match(gramatica_v4Parser.VAR)
            self.state = 222
            self.match(gramatica_v4Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(gramatica_v4Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(gramatica_v4Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = gramatica_v4Parser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(gramatica_v4Parser.BREAK)
            self.state = 225
            self.match(gramatica_v4Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(gramatica_v4Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(gramatica_v4Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = gramatica_v4Parser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(gramatica_v4Parser.CONTINUE)
            self.state = 228
            self.match(gramatica_v4Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(gramatica_v4Parser.LLA, 0)

        def LLC(self):
            return self.getToken(gramatica_v4Parser.LLC, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.StatementContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = gramatica_v4Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(gramatica_v4Parser.LLA)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562949961578480) != 0):
                self.state = 231
                self.statement()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
            self.match(gramatica_v4Parser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(gramatica_v4Parser.NOT, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ConditionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ConditionContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)


        def relop(self):
            return self.getTypedRuleContext(gramatica_v4Parser.RelopContext,0)


        def TRUE(self):
            return self.getToken(gramatica_v4Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(gramatica_v4Parser.FALSE, 0)

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def AND(self):
            return self.getToken(gramatica_v4Parser.AND, 0)

        def OR(self):
            return self.getToken(gramatica_v4Parser.OR, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatica_v4Parser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 240
                self.match(gramatica_v4Parser.NOT)
                self.state = 241
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 242
                self.expr(0)
                self.state = 243
                self.relop()
                self.state = 244
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 246
                self.match(gramatica_v4Parser.TRUE)
                pass

            elif la_ == 4:
                self.state = 247
                self.match(gramatica_v4Parser.FALSE)
                pass

            elif la_ == 5:
                self.state = 248
                self.match(gramatica_v4Parser.PAI)
                self.state = 249
                self.condition(0)
                self.state = 250
                self.match(gramatica_v4Parser.PAD)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 260
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v4Parser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 254
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 255
                        self.match(gramatica_v4Parser.AND)
                        self.state = 256
                        self.condition(8)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v4Parser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 257
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 258
                        self.match(gramatica_v4Parser.OR)
                        self.state = 259
                        self.condition(7)
                        pass

             
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)


        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def functionCall(self):
            return self.getTypedRuleContext(gramatica_v4Parser.FunctionCallContext,0)


        def VAR(self):
            return self.getToken(gramatica_v4Parser.VAR, 0)

        def TRUE(self):
            return self.getToken(gramatica_v4Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(gramatica_v4Parser.FALSE, 0)

        def NUM(self):
            return self.getToken(gramatica_v4Parser.NUM, 0)

        def FLOAT(self):
            return self.getToken(gramatica_v4Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(gramatica_v4Parser.STRING, 0)

        def MUL(self):
            return self.getToken(gramatica_v4Parser.MUL, 0)

        def DIV(self):
            return self.getToken(gramatica_v4Parser.DIV, 0)

        def MOD(self):
            return self.getToken(gramatica_v4Parser.MOD, 0)

        def SUM(self):
            return self.getToken(gramatica_v4Parser.SUM, 0)

        def RES(self):
            return self.getToken(gramatica_v4Parser.RES, 0)

        def relop(self):
            return self.getTypedRuleContext(gramatica_v4Parser.RelopContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatica_v4Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 266
                self.match(gramatica_v4Parser.PAI)
                self.state = 267
                self.expr(0)
                self.state = 268
                self.match(gramatica_v4Parser.PAD)
                pass

            elif la_ == 2:
                self.state = 270
                self.functionCall()
                pass

            elif la_ == 3:
                self.state = 271
                self.match(gramatica_v4Parser.VAR)
                self.state = 272
                self.match(gramatica_v4Parser.T__0)
                self.state = 273
                self.expr(0)
                self.state = 274
                self.match(gramatica_v4Parser.T__1)
                pass

            elif la_ == 4:
                self.state = 276
                self.match(gramatica_v4Parser.TRUE)
                pass

            elif la_ == 5:
                self.state = 277
                self.match(gramatica_v4Parser.FALSE)
                pass

            elif la_ == 6:
                self.state = 278
                self.match(gramatica_v4Parser.NUM)
                pass

            elif la_ == 7:
                self.state = 279
                self.match(gramatica_v4Parser.FLOAT)
                pass

            elif la_ == 8:
                self.state = 280
                self.match(gramatica_v4Parser.STRING)
                pass

            elif la_ == 9:
                self.state = 281
                self.match(gramatica_v4Parser.VAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 294
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v4Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 284
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 285
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 286
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v4Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 287
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 288
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 289
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = gramatica_v4Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 290
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 291
                        self.relop()
                        self.state = 292
                        self.expr(10)
                        pass

             
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(gramatica_v4Parser.VAR, 0)

        def PAI(self):
            return self.getToken(gramatica_v4Parser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_v4Parser.PAD, 0)

        def argList(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ArgListContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = gramatica_v4Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(gramatica_v4Parser.VAR)
            self.state = 300
            self.match(gramatica_v4Parser.PAI)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056630699458560) != 0):
                self.state = 301
                self.argList()


            self.state = 304
            self.match(gramatica_v4Parser.PAD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.COMMA)
            else:
                return self.getToken(gramatica_v4Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = gramatica_v4Parser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expr(0)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 307
                self.match(gramatica_v4Parser.COMMA)
                self.state = 308
                self.expr(0)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.COMMA)
            else:
                return self.getToken(gramatica_v4Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_arrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = gramatica_v4Parser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(gramatica_v4Parser.T__0)
            self.state = 315
            self.expr(0)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 316
                self.match(gramatica_v4Parser.COMMA)
                self.state = 317
                self.expr(0)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 323
            self.match(gramatica_v4Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(gramatica_v4Parser.GT, 0)

        def LT(self):
            return self.getToken(gramatica_v4Parser.LT, 0)

        def GTE(self):
            return self.getToken(gramatica_v4Parser.GTE, 0)

        def LTE(self):
            return self.getToken(gramatica_v4Parser.LTE, 0)

        def EQ(self):
            return self.getToken(gramatica_v4Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(gramatica_v4Parser.NEQ, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_relop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = gramatica_v4Parser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.condition_sempred
        self._predicates[27] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         




