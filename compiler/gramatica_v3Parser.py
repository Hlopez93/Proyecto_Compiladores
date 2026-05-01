# Generated from gramatica_v3.g4 by ANTLR 4.13.2
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
        4,1,47,303,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,5,0,64,8,0,10,0,12,0,67,
        9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        83,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,94,8,3,3,3,96,8,3,
        1,4,1,4,1,4,3,4,101,8,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,119,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,3,10,130,8,10,1,10,1,10,3,10,134,8,10,1,10,1,10,3,10,138,
        8,10,1,10,1,10,1,10,1,11,1,11,3,11,145,8,11,1,12,1,12,1,13,1,13,
        1,13,1,13,3,13,153,8,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,161,8,
        14,10,14,12,14,164,9,14,1,15,1,15,1,15,1,16,1,16,3,16,171,8,16,1,
        16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,
        19,1,19,1,20,1,20,1,20,1,21,1,21,5,21,193,8,21,10,21,12,21,196,9,
        21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,3,22,213,8,22,1,22,1,22,1,22,1,22,1,22,1,22,5,22,221,
        8,22,10,22,12,22,224,9,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,5,23,235,8,23,10,23,12,23,238,9,23,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,5,24,252,8,24,10,24,12,24,255,
        9,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,3,25,273,8,25,1,26,1,26,1,26,3,26,278,8,26,1,
        26,1,26,1,27,1,27,1,27,5,27,285,8,27,10,27,12,27,288,9,27,1,28,1,
        28,1,28,1,28,5,28,294,8,28,10,28,12,28,297,9,28,1,28,1,28,1,29,1,
        29,1,29,0,3,44,46,48,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,2,1,0,5,9,1,0,30,
        35,317,0,60,1,0,0,0,2,82,1,0,0,0,4,84,1,0,0,0,6,87,1,0,0,0,8,97,
        1,0,0,0,10,102,1,0,0,0,12,104,1,0,0,0,14,107,1,0,0,0,16,111,1,0,
        0,0,18,120,1,0,0,0,20,126,1,0,0,0,22,144,1,0,0,0,24,146,1,0,0,0,
        26,148,1,0,0,0,28,157,1,0,0,0,30,165,1,0,0,0,32,168,1,0,0,0,34,174,
        1,0,0,0,36,180,1,0,0,0,38,184,1,0,0,0,40,187,1,0,0,0,42,190,1,0,
        0,0,44,212,1,0,0,0,46,225,1,0,0,0,48,239,1,0,0,0,50,272,1,0,0,0,
        52,274,1,0,0,0,54,281,1,0,0,0,56,289,1,0,0,0,58,300,1,0,0,0,60,61,
        5,3,0,0,61,65,5,38,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,1,0,0,0,
        65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,
        39,0,0,69,70,5,0,0,1,70,1,1,0,0,0,71,83,3,4,2,0,72,83,3,12,6,0,73,
        83,3,16,8,0,74,83,3,18,9,0,75,83,3,20,10,0,76,83,3,26,13,0,77,83,
        3,32,16,0,78,83,3,34,17,0,79,83,3,36,18,0,80,83,3,38,19,0,81,83,
        3,40,20,0,82,71,1,0,0,0,82,72,1,0,0,0,82,73,1,0,0,0,82,74,1,0,0,
        0,82,75,1,0,0,0,82,76,1,0,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,
        1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,3,1,0,0,0,84,85,3,6,3,0,85,
        86,5,40,0,0,86,5,1,0,0,0,87,88,5,4,0,0,88,89,3,8,4,0,89,95,5,45,
        0,0,90,93,5,21,0,0,91,94,3,46,23,0,92,94,3,56,28,0,93,91,1,0,0,0,
        93,92,1,0,0,0,94,96,1,0,0,0,95,90,1,0,0,0,95,96,1,0,0,0,96,7,1,0,
        0,0,97,100,3,10,5,0,98,99,5,1,0,0,99,101,5,2,0,0,100,98,1,0,0,0,
        100,101,1,0,0,0,101,9,1,0,0,0,102,103,7,0,0,0,103,11,1,0,0,0,104,
        105,3,14,7,0,105,106,5,40,0,0,106,13,1,0,0,0,107,108,5,45,0,0,108,
        109,5,21,0,0,109,110,3,46,23,0,110,15,1,0,0,0,111,112,5,10,0,0,112,
        113,5,36,0,0,113,114,3,44,22,0,114,115,5,37,0,0,115,118,3,42,21,
        0,116,117,5,11,0,0,117,119,3,42,21,0,118,116,1,0,0,0,118,119,1,0,
        0,0,119,17,1,0,0,0,120,121,5,12,0,0,121,122,5,36,0,0,122,123,3,44,
        22,0,123,124,5,37,0,0,124,125,3,42,21,0,125,19,1,0,0,0,126,127,5,
        13,0,0,127,129,5,36,0,0,128,130,3,22,11,0,129,128,1,0,0,0,129,130,
        1,0,0,0,130,131,1,0,0,0,131,133,5,40,0,0,132,134,3,44,22,0,133,132,
        1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,137,5,40,0,0,136,138,
        3,24,12,0,137,136,1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,140,
        5,37,0,0,140,141,3,42,21,0,141,21,1,0,0,0,142,145,3,6,3,0,143,145,
        3,14,7,0,144,142,1,0,0,0,144,143,1,0,0,0,145,23,1,0,0,0,146,147,
        3,14,7,0,147,25,1,0,0,0,148,149,3,8,4,0,149,150,5,45,0,0,150,152,
        5,36,0,0,151,153,3,28,14,0,152,151,1,0,0,0,152,153,1,0,0,0,153,154,
        1,0,0,0,154,155,5,37,0,0,155,156,3,42,21,0,156,27,1,0,0,0,157,162,
        3,30,15,0,158,159,5,41,0,0,159,161,3,30,15,0,160,158,1,0,0,0,161,
        164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,29,1,0,0,0,164,162,
        1,0,0,0,165,166,3,8,4,0,166,167,5,45,0,0,167,31,1,0,0,0,168,170,
        5,14,0,0,169,171,3,46,23,0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,
        1,0,0,0,172,173,5,40,0,0,173,33,1,0,0,0,174,175,5,15,0,0,175,176,
        5,36,0,0,176,177,3,46,23,0,177,178,5,37,0,0,178,179,5,40,0,0,179,
        35,1,0,0,0,180,181,5,16,0,0,181,182,5,45,0,0,182,183,5,40,0,0,183,
        37,1,0,0,0,184,185,5,17,0,0,185,186,5,40,0,0,186,39,1,0,0,0,187,
        188,5,18,0,0,188,189,5,40,0,0,189,41,1,0,0,0,190,194,5,38,0,0,191,
        193,3,2,1,0,192,191,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,
        195,1,0,0,0,195,197,1,0,0,0,196,194,1,0,0,0,197,198,5,39,0,0,198,
        43,1,0,0,0,199,200,6,22,-1,0,200,201,5,29,0,0,201,213,3,44,22,5,
        202,203,3,46,23,0,203,204,3,58,29,0,204,205,3,46,23,0,205,213,1,
        0,0,0,206,213,5,19,0,0,207,213,5,20,0,0,208,209,5,36,0,0,209,210,
        3,44,22,0,210,211,5,37,0,0,211,213,1,0,0,0,212,199,1,0,0,0,212,202,
        1,0,0,0,212,206,1,0,0,0,212,207,1,0,0,0,212,208,1,0,0,0,213,222,
        1,0,0,0,214,215,10,7,0,0,215,216,5,27,0,0,216,221,3,44,22,8,217,
        218,10,6,0,0,218,219,5,28,0,0,219,221,3,44,22,7,220,214,1,0,0,0,
        220,217,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,
        223,45,1,0,0,0,224,222,1,0,0,0,225,226,6,23,-1,0,226,227,3,48,24,
        0,227,236,1,0,0,0,228,229,10,3,0,0,229,230,5,22,0,0,230,235,3,48,
        24,0,231,232,10,2,0,0,232,233,5,23,0,0,233,235,3,48,24,0,234,228,
        1,0,0,0,234,231,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,
        1,0,0,0,237,47,1,0,0,0,238,236,1,0,0,0,239,240,6,24,-1,0,240,241,
        3,50,25,0,241,253,1,0,0,0,242,243,10,4,0,0,243,244,5,24,0,0,244,
        252,3,50,25,0,245,246,10,3,0,0,246,247,5,25,0,0,247,252,3,50,25,
        0,248,249,10,2,0,0,249,250,5,26,0,0,250,252,3,50,25,0,251,242,1,
        0,0,0,251,245,1,0,0,0,251,248,1,0,0,0,252,255,1,0,0,0,253,251,1,
        0,0,0,253,254,1,0,0,0,254,49,1,0,0,0,255,253,1,0,0,0,256,257,5,36,
        0,0,257,258,3,46,23,0,258,259,5,37,0,0,259,273,1,0,0,0,260,273,3,
        52,26,0,261,262,5,45,0,0,262,263,5,1,0,0,263,264,3,46,23,0,264,265,
        5,2,0,0,265,273,1,0,0,0,266,273,5,19,0,0,267,273,5,20,0,0,268,273,
        5,42,0,0,269,273,5,43,0,0,270,273,5,44,0,0,271,273,5,45,0,0,272,
        256,1,0,0,0,272,260,1,0,0,0,272,261,1,0,0,0,272,266,1,0,0,0,272,
        267,1,0,0,0,272,268,1,0,0,0,272,269,1,0,0,0,272,270,1,0,0,0,272,
        271,1,0,0,0,273,51,1,0,0,0,274,275,5,45,0,0,275,277,5,36,0,0,276,
        278,3,54,27,0,277,276,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,
        280,5,37,0,0,280,53,1,0,0,0,281,286,3,46,23,0,282,283,5,41,0,0,283,
        285,3,46,23,0,284,282,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,
        287,1,0,0,0,287,55,1,0,0,0,288,286,1,0,0,0,289,290,5,1,0,0,290,295,
        3,46,23,0,291,292,5,41,0,0,292,294,3,46,23,0,293,291,1,0,0,0,294,
        297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,298,1,0,0,0,297,
        295,1,0,0,0,298,299,5,2,0,0,299,57,1,0,0,0,300,301,7,1,0,0,301,59,
        1,0,0,0,25,65,82,93,95,100,118,129,133,137,144,152,162,170,194,212,
        220,222,234,236,251,253,272,277,286,295
    ]

class gramatica_v3Parser ( Parser ):

    grammarFileName = "gramatica_v3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'program'", "<INVALID>", 
                     "'int'", "'float'", "'string'", "'bool'", "'void'", 
                     "'if'", "'else'", "'while'", "'for'", "'return'", "'print'", 
                     "'import'", "'break'", "'continue'", "'true'", "'false'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", 
                     "'!'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PROGRAM", 
                      "DECL", "INT", "FLOAT_T", "STRING_T", "BOOL", "VOID", 
                      "IF", "ELSE", "WHILE", "FOR", "RETURN", "PRINT", "IMPORT", 
                      "BREAK", "CONTINUE", "TRUE", "FALSE", "ASIG", "SUM", 
                      "RES", "MUL", "DIV", "MOD", "AND", "OR", "NOT", "GT", 
                      "LT", "GTE", "LTE", "EQ", "NEQ", "PAI", "PAD", "LLA", 
                      "LLC", "SEMI", "COMMA", "NUM", "FLOAT", "STRING", 
                      "VAR", "LINE_COMMENT", "WS" ]

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
    RULE_functionDecl = 13
    RULE_paramList = 14
    RULE_param = 15
    RULE_returnStmt = 16
    RULE_printStmt = 17
    RULE_importStmt = 18
    RULE_breakStmt = 19
    RULE_continueStmt = 20
    RULE_block = 21
    RULE_condition = 22
    RULE_expr = 23
    RULE_term = 24
    RULE_factor = 25
    RULE_functionCall = 26
    RULE_argList = 27
    RULE_arrayLiteral = 28
    RULE_relop = 29

    ruleNames =  [ "root", "statement", "declaration", "declarationStatement", 
                   "tipo", "baseTipo", "assignment", "assignmentStatement", 
                   "ifStatement", "whileStatement", "forStatement", "forInit", 
                   "forUpdate", "functionDecl", "paramList", "param", "returnStmt", 
                   "printStmt", "importStmt", "breakStmt", "continueStmt", 
                   "block", "condition", "expr", "term", "factor", "functionCall", 
                   "argList", "arrayLiteral", "relop" ]

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
    RETURN=14
    PRINT=15
    IMPORT=16
    BREAK=17
    CONTINUE=18
    TRUE=19
    FALSE=20
    ASIG=21
    SUM=22
    RES=23
    MUL=24
    DIV=25
    MOD=26
    AND=27
    OR=28
    NOT=29
    GT=30
    LT=31
    GTE=32
    LTE=33
    EQ=34
    NEQ=35
    PAI=36
    PAD=37
    LLA=38
    LLC=39
    SEMI=40
    COMMA=41
    NUM=42
    FLOAT=43
    STRING=44
    VAR=45
    LINE_COMMENT=46
    WS=47

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
            return self.getToken(gramatica_v3Parser.PROGRAM, 0)

        def LLA(self):
            return self.getToken(gramatica_v3Parser.LLA, 0)

        def LLC(self):
            return self.getToken(gramatica_v3Parser.LLC, 0)

        def EOF(self):
            return self.getToken(gramatica_v3Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.StatementContext,i)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = gramatica_v3Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(gramatica_v3Parser.PROGRAM)
            self.state = 61
            self.match(gramatica_v3Parser.LLA)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372611056) != 0):
                self.state = 62
                self.statement()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(gramatica_v3Parser.LLC)
            self.state = 69
            self.match(gramatica_v3Parser.EOF)
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
            return self.getTypedRuleContext(gramatica_v3Parser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(gramatica_v3Parser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ForStatementContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(gramatica_v3Parser.FunctionDeclContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ReturnStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(gramatica_v3Parser.PrintStmtContext,0)


        def importStmt(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ImportStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ContinueStmtContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramatica_v3Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.declaration()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.assignment()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.ifStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.whileStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.forStatement()
                pass
            elif token in [5, 6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.functionDecl()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.returnStmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 8)
                self.state = 78
                self.printStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 9)
                self.state = 79
                self.importStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 10)
                self.state = 80
                self.breakStmt()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 11)
                self.state = 81
                self.continueStmt()
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
            return self.getTypedRuleContext(gramatica_v3Parser.DeclarationStatementContext,0)


        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = gramatica_v3Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.declarationStatement()
            self.state = 85
            self.match(gramatica_v3Parser.SEMI)
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
            return self.getToken(gramatica_v3Parser.DECL, 0)

        def tipo(self):
            return self.getTypedRuleContext(gramatica_v3Parser.TipoContext,0)


        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def ASIG(self):
            return self.getToken(gramatica_v3Parser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_declarationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationStatement(self):

        localctx = gramatica_v3Parser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declarationStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(gramatica_v3Parser.DECL)
            self.state = 88
            self.tipo()
            self.state = 89
            self.match(gramatica_v3Parser.VAR)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 90
                self.match(gramatica_v3Parser.ASIG)
                self.state = 93
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [19, 20, 36, 42, 43, 44, 45]:
                    self.state = 91
                    self.expr(0)
                    pass
                elif token in [1]:
                    self.state = 92
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
            return self.getTypedRuleContext(gramatica_v3Parser.BaseTipoContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = gramatica_v3Parser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.baseTipo()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 98
                self.match(gramatica_v3Parser.T__0)
                self.state = 99
                self.match(gramatica_v3Parser.T__1)


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
            return self.getToken(gramatica_v3Parser.INT, 0)

        def FLOAT_T(self):
            return self.getToken(gramatica_v3Parser.FLOAT_T, 0)

        def STRING_T(self):
            return self.getToken(gramatica_v3Parser.STRING_T, 0)

        def BOOL(self):
            return self.getToken(gramatica_v3Parser.BOOL, 0)

        def VOID(self):
            return self.getToken(gramatica_v3Parser.VOID, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_baseTipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseTipo" ):
                listener.enterBaseTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseTipo" ):
                listener.exitBaseTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseTipo" ):
                return visitor.visitBaseTipo(self)
            else:
                return visitor.visitChildren(self)




    def baseTipo(self):

        localctx = gramatica_v3Parser.BaseTipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_baseTipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
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
            return self.getTypedRuleContext(gramatica_v3Parser.AssignmentStatementContext,0)


        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramatica_v3Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.assignmentStatement()
            self.state = 105
            self.match(gramatica_v3Parser.SEMI)
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
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def ASIG(self):
            return self.getToken(gramatica_v3Parser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = gramatica_v3Parser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(gramatica_v3Parser.VAR)
            self.state = 108
            self.match(gramatica_v3Parser.ASIG)
            self.state = 109
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
            return self.getToken(gramatica_v3Parser.IF, 0)

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def condition(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ConditionContext,0)


        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.BlockContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.BlockContext,i)


        def ELSE(self):
            return self.getToken(gramatica_v3Parser.ELSE, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = gramatica_v3Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(gramatica_v3Parser.IF)
            self.state = 112
            self.match(gramatica_v3Parser.PAI)
            self.state = 113
            self.condition(0)
            self.state = 114
            self.match(gramatica_v3Parser.PAD)
            self.state = 115
            self.block()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 116
                self.match(gramatica_v3Parser.ELSE)
                self.state = 117
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
            return self.getToken(gramatica_v3Parser.WHILE, 0)

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def condition(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ConditionContext,0)


        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BlockContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = gramatica_v3Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(gramatica_v3Parser.WHILE)
            self.state = 121
            self.match(gramatica_v3Parser.PAI)
            self.state = 122
            self.condition(0)
            self.state = 123
            self.match(gramatica_v3Parser.PAD)
            self.state = 124
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
            return self.getToken(gramatica_v3Parser.FOR, 0)

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.SEMI)
            else:
                return self.getToken(gramatica_v3Parser.SEMI, i)

        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BlockContext,0)


        def forInit(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ForInitContext,0)


        def condition(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ConditionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ForUpdateContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = gramatica_v3Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(gramatica_v3Parser.FOR)
            self.state = 127
            self.match(gramatica_v3Parser.PAI)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==45:
                self.state = 128
                self.forInit()


            self.state = 131
            self.match(gramatica_v3Parser.SEMI)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66039955587072) != 0):
                self.state = 132
                self.condition(0)


            self.state = 135
            self.match(gramatica_v3Parser.SEMI)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 136
                self.forUpdate()


            self.state = 139
            self.match(gramatica_v3Parser.PAD)
            self.state = 140
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
            return self.getTypedRuleContext(gramatica_v3Parser.DeclarationStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = gramatica_v3Parser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forInit)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.declarationStatement()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
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
            return self.getTypedRuleContext(gramatica_v3Parser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = gramatica_v3Parser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.assignmentStatement()
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
            return self.getTypedRuleContext(gramatica_v3Parser.TipoContext,0)


        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ParamListContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = gramatica_v3Parser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.tipo()
            self.state = 149
            self.match(gramatica_v3Parser.VAR)
            self.state = 150
            self.match(gramatica_v3Parser.PAI)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0):
                self.state = 151
                self.paramList()


            self.state = 154
            self.match(gramatica_v3Parser.PAD)
            self.state = 155
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
                return self.getTypedRuleContexts(gramatica_v3Parser.ParamContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = gramatica_v3Parser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.param()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 158
                self.match(gramatica_v3Parser.COMMA)
                self.state = 159
                self.param()
                self.state = 164
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
            return self.getTypedRuleContext(gramatica_v3Parser.TipoContext,0)


        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = gramatica_v3Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.tipo()
            self.state = 166
            self.match(gramatica_v3Parser.VAR)
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
            return self.getToken(gramatica_v3Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = gramatica_v3Parser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(gramatica_v3Parser.RETURN)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66039418716160) != 0):
                self.state = 169
                self.expr(0)


            self.state = 172
            self.match(gramatica_v3Parser.SEMI)
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
            return self.getToken(gramatica_v3Parser.PRINT, 0)

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = gramatica_v3Parser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(gramatica_v3Parser.PRINT)
            self.state = 175
            self.match(gramatica_v3Parser.PAI)
            self.state = 176
            self.expr(0)
            self.state = 177
            self.match(gramatica_v3Parser.PAD)
            self.state = 178
            self.match(gramatica_v3Parser.SEMI)
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
            return self.getToken(gramatica_v3Parser.IMPORT, 0)

        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_importStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStmt" ):
                listener.enterImportStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStmt" ):
                listener.exitImportStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStmt" ):
                return visitor.visitImportStmt(self)
            else:
                return visitor.visitChildren(self)




    def importStmt(self):

        localctx = gramatica_v3Parser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(gramatica_v3Parser.IMPORT)
            self.state = 181
            self.match(gramatica_v3Parser.VAR)
            self.state = 182
            self.match(gramatica_v3Parser.SEMI)
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
            return self.getToken(gramatica_v3Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = gramatica_v3Parser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(gramatica_v3Parser.BREAK)
            self.state = 185
            self.match(gramatica_v3Parser.SEMI)
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
            return self.getToken(gramatica_v3Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = gramatica_v3Parser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(gramatica_v3Parser.CONTINUE)
            self.state = 188
            self.match(gramatica_v3Parser.SEMI)
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
            return self.getToken(gramatica_v3Parser.LLA, 0)

        def LLC(self):
            return self.getToken(gramatica_v3Parser.LLC, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.StatementContext,i)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = gramatica_v3Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(gramatica_v3Parser.LLA)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372611056) != 0):
                self.state = 191
                self.statement()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self.match(gramatica_v3Parser.LLC)
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
            return self.getToken(gramatica_v3Parser.NOT, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ConditionContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ConditionContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def relop(self):
            return self.getTypedRuleContext(gramatica_v3Parser.RelopContext,0)


        def TRUE(self):
            return self.getToken(gramatica_v3Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(gramatica_v3Parser.FALSE, 0)

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def AND(self):
            return self.getToken(gramatica_v3Parser.AND, 0)

        def OR(self):
            return self.getToken(gramatica_v3Parser.OR, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatica_v3Parser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 200
                self.match(gramatica_v3Parser.NOT)
                self.state = 201
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 202
                self.expr(0)
                self.state = 203
                self.relop()
                self.state = 204
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 206
                self.match(gramatica_v3Parser.TRUE)
                pass

            elif la_ == 4:
                self.state = 207
                self.match(gramatica_v3Parser.FALSE)
                pass

            elif la_ == 5:
                self.state = 208
                self.match(gramatica_v3Parser.PAI)
                self.state = 209
                self.condition(0)
                self.state = 210
                self.match(gramatica_v3Parser.PAD)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 220
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v3Parser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 214
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 215
                        self.match(gramatica_v3Parser.AND)
                        self.state = 216
                        self.condition(8)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v3Parser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 217
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 218
                        self.match(gramatica_v3Parser.OR)
                        self.state = 219
                        self.condition(7)
                        pass

             
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def term(self):
            return self.getTypedRuleContext(gramatica_v3Parser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def SUM(self):
            return self.getToken(gramatica_v3Parser.SUM, 0)

        def RES(self):
            return self.getToken(gramatica_v3Parser.RES, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatica_v3Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 234
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v3Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 228
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 229
                        self.match(gramatica_v3Parser.SUM)
                        self.state = 230
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v3Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 231
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 232
                        self.match(gramatica_v3Parser.RES)
                        self.state = 233
                        self.term(0)
                        pass

             
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(gramatica_v3Parser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(gramatica_v3Parser.TermContext,0)


        def MUL(self):
            return self.getToken(gramatica_v3Parser.MUL, 0)

        def DIV(self):
            return self.getToken(gramatica_v3Parser.DIV, 0)

        def MOD(self):
            return self.getToken(gramatica_v3Parser.MOD, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatica_v3Parser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 251
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v3Parser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 242
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 243
                        self.match(gramatica_v3Parser.MUL)
                        self.state = 244
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v3Parser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 245
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 246
                        self.match(gramatica_v3Parser.DIV)
                        self.state = 247
                        self.factor()
                        pass

                    elif la_ == 3:
                        localctx = gramatica_v3Parser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 248
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 249
                        self.match(gramatica_v3Parser.MOD)
                        self.state = 250
                        self.factor()
                        pass

             
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def functionCall(self):
            return self.getTypedRuleContext(gramatica_v3Parser.FunctionCallContext,0)


        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def TRUE(self):
            return self.getToken(gramatica_v3Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(gramatica_v3Parser.FALSE, 0)

        def NUM(self):
            return self.getToken(gramatica_v3Parser.NUM, 0)

        def FLOAT(self):
            return self.getToken(gramatica_v3Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(gramatica_v3Parser.STRING, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = gramatica_v3Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(gramatica_v3Parser.PAI)
                self.state = 257
                self.expr(0)
                self.state = 258
                self.match(gramatica_v3Parser.PAD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                self.match(gramatica_v3Parser.VAR)
                self.state = 262
                self.match(gramatica_v3Parser.T__0)
                self.state = 263
                self.expr(0)
                self.state = 264
                self.match(gramatica_v3Parser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.match(gramatica_v3Parser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(gramatica_v3Parser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.match(gramatica_v3Parser.NUM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.match(gramatica_v3Parser.FLOAT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 270
                self.match(gramatica_v3Parser.STRING)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 271
                self.match(gramatica_v3Parser.VAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def argList(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArgListContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = gramatica_v3Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(gramatica_v3Parser.VAR)
            self.state = 275
            self.match(gramatica_v3Parser.PAI)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66039418716160) != 0):
                self.state = 276
                self.argList()


            self.state = 279
            self.match(gramatica_v3Parser.PAD)
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
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = gramatica_v3Parser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.expr(0)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 282
                self.match(gramatica_v3Parser.COMMA)
                self.state = 283
                self.expr(0)
                self.state = 288
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
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = gramatica_v3Parser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(gramatica_v3Parser.T__0)
            self.state = 290
            self.expr(0)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 291
                self.match(gramatica_v3Parser.COMMA)
                self.state = 292
                self.expr(0)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 298
            self.match(gramatica_v3Parser.T__1)
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
            return self.getToken(gramatica_v3Parser.GT, 0)

        def LT(self):
            return self.getToken(gramatica_v3Parser.LT, 0)

        def GTE(self):
            return self.getToken(gramatica_v3Parser.GTE, 0)

        def LTE(self):
            return self.getToken(gramatica_v3Parser.LTE, 0)

        def EQ(self):
            return self.getToken(gramatica_v3Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(gramatica_v3Parser.NEQ, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = gramatica_v3Parser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
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
        self._predicates[22] = self.condition_sempred
        self._predicates[23] = self.expr_sempred
        self._predicates[24] = self.term_sempred
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




