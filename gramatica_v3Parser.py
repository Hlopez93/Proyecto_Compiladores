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
        4,1,48,292,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,88,8,3,3,3,90,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        98,8,4,1,4,1,4,1,4,5,4,103,8,4,10,4,12,4,106,9,4,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,122,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,3,9,133,8,9,1,9,1,9,3,9,137,8,9,1,9,1,9,
        3,9,141,8,9,1,9,1,9,1,9,1,10,1,10,3,10,148,8,10,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,3,12,157,8,12,1,12,1,12,1,12,1,13,1,13,1,13,5,
        13,165,8,13,10,13,12,13,168,9,13,1,14,1,14,1,14,1,15,1,15,3,15,175,
        8,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,5,20,197,8,20,10,20,12,20,
        200,9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,3,21,217,8,21,1,21,1,21,1,21,1,21,1,21,1,21,
        5,21,225,8,21,10,21,12,21,228,9,21,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,247,
        8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,5,22,259,
        8,22,10,22,12,22,262,9,22,1,23,1,23,1,23,3,23,267,8,23,1,23,1,23,
        1,24,1,24,1,24,5,24,274,8,24,10,24,12,24,277,9,24,1,25,1,25,1,25,
        1,25,5,25,283,8,25,10,25,12,25,286,9,25,1,25,1,25,1,26,1,26,1,26,
        0,3,8,42,44,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,0,3,1,0,33,35,1,0,31,32,1,0,5,10,311,
        0,54,1,0,0,0,2,76,1,0,0,0,4,78,1,0,0,0,6,81,1,0,0,0,8,97,1,0,0,0,
        10,107,1,0,0,0,12,110,1,0,0,0,14,114,1,0,0,0,16,123,1,0,0,0,18,129,
        1,0,0,0,20,147,1,0,0,0,22,149,1,0,0,0,24,151,1,0,0,0,26,161,1,0,
        0,0,28,169,1,0,0,0,30,172,1,0,0,0,32,178,1,0,0,0,34,184,1,0,0,0,
        36,188,1,0,0,0,38,191,1,0,0,0,40,194,1,0,0,0,42,216,1,0,0,0,44,246,
        1,0,0,0,46,263,1,0,0,0,48,270,1,0,0,0,50,278,1,0,0,0,52,289,1,0,
        0,0,54,55,5,11,0,0,55,59,5,41,0,0,56,58,3,2,1,0,57,56,1,0,0,0,58,
        61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,
        0,62,63,5,42,0,0,63,64,5,0,0,1,64,1,1,0,0,0,65,77,3,4,2,0,66,77,
        3,10,5,0,67,77,3,14,7,0,68,77,3,16,8,0,69,77,3,18,9,0,70,77,3,24,
        12,0,71,77,3,30,15,0,72,77,3,32,16,0,73,77,3,34,17,0,74,77,3,36,
        18,0,75,77,3,38,19,0,76,65,1,0,0,0,76,66,1,0,0,0,76,67,1,0,0,0,76,
        68,1,0,0,0,76,69,1,0,0,0,76,70,1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,
        0,76,73,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,0,77,3,1,0,0,0,78,79,3,
        6,3,0,79,80,5,1,0,0,80,5,1,0,0,0,81,82,5,12,0,0,82,83,3,8,4,0,83,
        89,5,46,0,0,84,87,5,30,0,0,85,88,3,44,22,0,86,88,3,50,25,0,87,85,
        1,0,0,0,87,86,1,0,0,0,88,90,1,0,0,0,89,84,1,0,0,0,89,90,1,0,0,0,
        90,7,1,0,0,0,91,92,6,4,-1,0,92,98,5,13,0,0,93,98,5,14,0,0,94,98,
        5,15,0,0,95,98,5,16,0,0,96,98,5,17,0,0,97,91,1,0,0,0,97,93,1,0,0,
        0,97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,104,1,0,0,0,99,100,
        10,1,0,0,100,101,5,2,0,0,101,103,5,3,0,0,102,99,1,0,0,0,103,106,
        1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,9,1,0,0,0,106,104,1,
        0,0,0,107,108,3,12,6,0,108,109,5,1,0,0,109,11,1,0,0,0,110,111,5,
        46,0,0,111,112,5,30,0,0,112,113,3,44,22,0,113,13,1,0,0,0,114,115,
        5,18,0,0,115,116,5,39,0,0,116,117,3,42,21,0,117,118,5,40,0,0,118,
        121,3,40,20,0,119,120,5,19,0,0,120,122,3,40,20,0,121,119,1,0,0,0,
        121,122,1,0,0,0,122,15,1,0,0,0,123,124,5,20,0,0,124,125,5,39,0,0,
        125,126,3,42,21,0,126,127,5,40,0,0,127,128,3,40,20,0,128,17,1,0,
        0,0,129,130,5,21,0,0,130,132,5,39,0,0,131,133,3,20,10,0,132,131,
        1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,136,5,1,0,0,135,137,
        3,42,21,0,136,135,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,140,
        5,1,0,0,139,141,3,22,11,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,
        1,0,0,0,142,143,5,40,0,0,143,144,3,40,20,0,144,19,1,0,0,0,145,148,
        3,6,3,0,146,148,3,12,6,0,147,145,1,0,0,0,147,146,1,0,0,0,148,21,
        1,0,0,0,149,150,3,12,6,0,150,23,1,0,0,0,151,152,5,22,0,0,152,153,
        3,8,4,0,153,154,5,46,0,0,154,156,5,39,0,0,155,157,3,26,13,0,156,
        155,1,0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,159,5,40,0,0,159,
        160,3,40,20,0,160,25,1,0,0,0,161,166,3,28,14,0,162,163,5,4,0,0,163,
        165,3,28,14,0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,27,1,0,0,0,168,166,1,0,0,0,169,170,3,8,4,0,170,171,
        5,46,0,0,171,29,1,0,0,0,172,174,5,23,0,0,173,175,3,44,22,0,174,173,
        1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,5,1,0,0,177,31,1,
        0,0,0,178,179,5,24,0,0,179,180,5,39,0,0,180,181,3,44,22,0,181,182,
        5,40,0,0,182,183,5,1,0,0,183,33,1,0,0,0,184,185,5,25,0,0,185,186,
        5,46,0,0,186,187,5,1,0,0,187,35,1,0,0,0,188,189,5,26,0,0,189,190,
        5,1,0,0,190,37,1,0,0,0,191,192,5,27,0,0,192,193,5,1,0,0,193,39,1,
        0,0,0,194,198,5,41,0,0,195,197,3,2,1,0,196,195,1,0,0,0,197,200,1,
        0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,198,1,
        0,0,0,201,202,5,42,0,0,202,41,1,0,0,0,203,204,6,21,-1,0,204,205,
        5,38,0,0,205,217,3,42,21,5,206,207,3,44,22,0,207,208,3,52,26,0,208,
        209,3,44,22,0,209,217,1,0,0,0,210,217,5,28,0,0,211,217,5,29,0,0,
        212,213,5,39,0,0,213,214,3,42,21,0,214,215,5,40,0,0,215,217,1,0,
        0,0,216,203,1,0,0,0,216,206,1,0,0,0,216,210,1,0,0,0,216,211,1,0,
        0,0,216,212,1,0,0,0,217,226,1,0,0,0,218,219,10,7,0,0,219,220,5,36,
        0,0,220,225,3,42,21,8,221,222,10,6,0,0,222,223,5,37,0,0,223,225,
        3,42,21,7,224,218,1,0,0,0,224,221,1,0,0,0,225,228,1,0,0,0,226,224,
        1,0,0,0,226,227,1,0,0,0,227,43,1,0,0,0,228,226,1,0,0,0,229,230,6,
        22,-1,0,230,231,5,39,0,0,231,232,3,44,22,0,232,233,5,40,0,0,233,
        247,1,0,0,0,234,247,3,46,23,0,235,236,5,46,0,0,236,237,5,2,0,0,237,
        238,3,44,22,0,238,239,5,3,0,0,239,247,1,0,0,0,240,247,5,28,0,0,241,
        247,5,29,0,0,242,247,5,43,0,0,243,247,5,44,0,0,244,247,5,45,0,0,
        245,247,5,46,0,0,246,229,1,0,0,0,246,234,1,0,0,0,246,235,1,0,0,0,
        246,240,1,0,0,0,246,241,1,0,0,0,246,242,1,0,0,0,246,243,1,0,0,0,
        246,244,1,0,0,0,246,245,1,0,0,0,247,260,1,0,0,0,248,249,10,11,0,
        0,249,250,7,0,0,0,250,259,3,44,22,12,251,252,10,10,0,0,252,253,7,
        1,0,0,253,259,3,44,22,11,254,255,10,9,0,0,255,256,3,52,26,0,256,
        257,3,44,22,10,257,259,1,0,0,0,258,248,1,0,0,0,258,251,1,0,0,0,258,
        254,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,
        45,1,0,0,0,262,260,1,0,0,0,263,264,5,46,0,0,264,266,5,39,0,0,265,
        267,3,48,24,0,266,265,1,0,0,0,266,267,1,0,0,0,267,268,1,0,0,0,268,
        269,5,40,0,0,269,47,1,0,0,0,270,275,3,44,22,0,271,272,5,4,0,0,272,
        274,3,44,22,0,273,271,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,
        276,1,0,0,0,276,49,1,0,0,0,277,275,1,0,0,0,278,279,5,2,0,0,279,284,
        3,44,22,0,280,281,5,4,0,0,281,283,3,44,22,0,282,280,1,0,0,0,283,
        286,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,
        284,1,0,0,0,287,288,5,3,0,0,288,51,1,0,0,0,289,290,7,2,0,0,290,53,
        1,0,0,0,24,59,76,87,89,97,104,121,132,136,140,147,156,166,174,198,
        216,224,226,246,258,260,266,275,284
    ]

class gramatica_v3Parser ( Parser ):

    grammarFileName = "gramatica_v3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'['", "']'", "','", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='", "'program'", "<INVALID>", 
                     "'int'", "'float'", "'string'", "'bool'", "'void'", 
                     "'if'", "'else'", "'while'", "'for'", "'function'", 
                     "'return'", "'print'", "'import'", "'break'", "'continue'", 
                     "'true'", "'false'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'&&'", "'||'", "'!'", "'('", "')'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PROGRAM", 
                      "TVAR", "INT", "FLOAT_T", "STRING_T", "BOOL", "VOID", 
                      "IF", "ELSE", "WHILE", "FOR", "FUNCTION", "RETURN", 
                      "PRINT", "IMPORT", "BREAK", "CONTINUE", "TRUE", "FALSE", 
                      "ASIG", "SUM", "RES", "MUL", "DIV", "MOD", "AND", 
                      "OR", "NOT", "PAI", "PAD", "LLA", "LLC", "NUM", "FLOAT", 
                      "STRING", "VAR", "WS", "ERROR_CHAR" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_declarationStatement = 3
    RULE_tipo = 4
    RULE_assignment = 5
    RULE_assignmentStatement = 6
    RULE_ifStatement = 7
    RULE_whileStatement = 8
    RULE_forStatement = 9
    RULE_forInit = 10
    RULE_forUpdate = 11
    RULE_functionDecl = 12
    RULE_paramList = 13
    RULE_param = 14
    RULE_returnStmt = 15
    RULE_printStmt = 16
    RULE_importStmt = 17
    RULE_breakStmt = 18
    RULE_continueStmt = 19
    RULE_block = 20
    RULE_condition = 21
    RULE_expr = 22
    RULE_functionCall = 23
    RULE_argList = 24
    RULE_arrayLiteral = 25
    RULE_relop = 26

    ruleNames =  [ "root", "statement", "declaration", "declarationStatement", 
                   "tipo", "assignment", "assignmentStatement", "ifStatement", 
                   "whileStatement", "forStatement", "forInit", "forUpdate", 
                   "functionDecl", "paramList", "param", "returnStmt", "printStmt", 
                   "importStmt", "breakStmt", "continueStmt", "block", "condition", 
                   "expr", "functionCall", "argList", "arrayLiteral", "relop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    PROGRAM=11
    TVAR=12
    INT=13
    FLOAT_T=14
    STRING_T=15
    BOOL=16
    VOID=17
    IF=18
    ELSE=19
    WHILE=20
    FOR=21
    FUNCTION=22
    RETURN=23
    PRINT=24
    IMPORT=25
    BREAK=26
    CONTINUE=27
    TRUE=28
    FALSE=29
    ASIG=30
    SUM=31
    RES=32
    MUL=33
    DIV=34
    MOD=35
    AND=36
    OR=37
    NOT=38
    PAI=39
    PAD=40
    LLA=41
    LLC=42
    NUM=43
    FLOAT=44
    STRING=45
    VAR=46
    WS=47
    ERROR_CHAR=48

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
            self.state = 54
            self.match(gramatica_v3Parser.PROGRAM)
            self.state = 55
            self.match(gramatica_v3Parser.LLA)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70369011830784) != 0):
                self.state = 56
                self.statement()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(gramatica_v3Parser.LLC)
            self.state = 63
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramatica_v3Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.declaration()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.assignment()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.ifStatement()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.whileStatement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.forStatement()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.functionDecl()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 7)
                self.state = 71
                self.returnStmt()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 8)
                self.state = 72
                self.printStmt()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 9)
                self.state = 73
                self.importStmt()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 10)
                self.state = 74
                self.breakStmt()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 11)
                self.state = 75
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


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_declaration

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
            self.state = 78
            self.declarationStatement()
            self.state = 79
            self.match(gramatica_v3Parser.T__0)
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

        def TVAR(self):
            return self.getToken(gramatica_v3Parser.TVAR, 0)

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
            self.state = 81
            self.match(gramatica_v3Parser.TVAR)
            self.state = 82
            self.tipo(0)
            self.state = 83
            self.match(gramatica_v3Parser.VAR)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 84
                self.match(gramatica_v3Parser.ASIG)
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [28, 29, 39, 43, 44, 45, 46]:
                    self.state = 85
                    self.expr(0)
                    pass
                elif token in [2]:
                    self.state = 86
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

        def tipo(self):
            return self.getTypedRuleContext(gramatica_v3Parser.TipoContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_tipo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)



    def tipo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatica_v3Parser.TipoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_tipo, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 92
                self.match(gramatica_v3Parser.INT)
                pass
            elif token in [14]:
                self.state = 93
                self.match(gramatica_v3Parser.FLOAT_T)
                pass
            elif token in [15]:
                self.state = 94
                self.match(gramatica_v3Parser.STRING_T)
                pass
            elif token in [16]:
                self.state = 95
                self.match(gramatica_v3Parser.BOOL)
                pass
            elif token in [17]:
                self.state = 96
                self.match(gramatica_v3Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramatica_v3Parser.TipoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_tipo)
                    self.state = 99
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 100
                    self.match(gramatica_v3Parser.T__1)
                    self.state = 101
                    self.match(gramatica_v3Parser.T__2) 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramatica_v3Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.assignmentStatement()
            self.state = 108
            self.match(gramatica_v3Parser.T__0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = gramatica_v3Parser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(gramatica_v3Parser.VAR)
            self.state = 111
            self.match(gramatica_v3Parser.ASIG)
            self.state = 112
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = gramatica_v3Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(gramatica_v3Parser.IF)
            self.state = 115
            self.match(gramatica_v3Parser.PAI)
            self.state = 116
            self.condition(0)
            self.state = 117
            self.match(gramatica_v3Parser.PAD)
            self.state = 118
            self.block()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 119
                self.match(gramatica_v3Parser.ELSE)
                self.state = 120
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = gramatica_v3Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(gramatica_v3Parser.WHILE)
            self.state = 124
            self.match(gramatica_v3Parser.PAI)
            self.state = 125
            self.condition(0)
            self.state = 126
            self.match(gramatica_v3Parser.PAD)
            self.state = 127
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = gramatica_v3Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(gramatica_v3Parser.FOR)
            self.state = 130
            self.match(gramatica_v3Parser.PAI)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==46:
                self.state = 131
                self.forInit()


            self.state = 134
            self.match(gramatica_v3Parser.T__0)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132766834360320) != 0):
                self.state = 135
                self.condition(0)


            self.state = 138
            self.match(gramatica_v3Parser.T__0)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 139
                self.forUpdate()


            self.state = 142
            self.match(gramatica_v3Parser.PAD)
            self.state = 143
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = gramatica_v3Parser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forInit)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.declarationStatement()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = gramatica_v3Parser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
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

        def FUNCTION(self):
            return self.getToken(gramatica_v3Parser.FUNCTION, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = gramatica_v3Parser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(gramatica_v3Parser.FUNCTION)
            self.state = 152
            self.tipo(0)
            self.state = 153
            self.match(gramatica_v3Parser.VAR)
            self.state = 154
            self.match(gramatica_v3Parser.PAI)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 253952) != 0):
                self.state = 155
                self.paramList()


            self.state = 158
            self.match(gramatica_v3Parser.PAD)
            self.state = 159
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


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = gramatica_v3Parser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.param()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 162
                self.match(gramatica_v3Parser.T__3)
                self.state = 163
                self.param()
                self.state = 168
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = gramatica_v3Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.tipo(0)
            self.state = 170
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

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = gramatica_v3Parser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(gramatica_v3Parser.RETURN)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132491956453376) != 0):
                self.state = 173
                self.expr(0)


            self.state = 176
            self.match(gramatica_v3Parser.T__0)
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

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_printStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = gramatica_v3Parser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(gramatica_v3Parser.PRINT)
            self.state = 179
            self.match(gramatica_v3Parser.PAI)
            self.state = 180
            self.expr(0)
            self.state = 181
            self.match(gramatica_v3Parser.PAD)
            self.state = 182
            self.match(gramatica_v3Parser.T__0)
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

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_importStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStmt" ):
                return visitor.visitImportStmt(self)
            else:
                return visitor.visitChildren(self)




    def importStmt(self):

        localctx = gramatica_v3Parser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(gramatica_v3Parser.IMPORT)
            self.state = 185
            self.match(gramatica_v3Parser.VAR)
            self.state = 186
            self.match(gramatica_v3Parser.T__0)
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

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = gramatica_v3Parser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(gramatica_v3Parser.BREAK)
            self.state = 189
            self.match(gramatica_v3Parser.T__0)
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

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = gramatica_v3Parser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(gramatica_v3Parser.CONTINUE)
            self.state = 192
            self.match(gramatica_v3Parser.T__0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = gramatica_v3Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(gramatica_v3Parser.LLA)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70369011830784) != 0):
                self.state = 195
                self.statement()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 204
                self.match(gramatica_v3Parser.NOT)
                self.state = 205
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 206
                self.expr(0)
                self.state = 207
                self.relop()
                self.state = 208
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 210
                self.match(gramatica_v3Parser.TRUE)
                pass

            elif la_ == 4:
                self.state = 211
                self.match(gramatica_v3Parser.FALSE)
                pass

            elif la_ == 5:
                self.state = 212
                self.match(gramatica_v3Parser.PAI)
                self.state = 213
                self.condition(0)
                self.state = 214
                self.match(gramatica_v3Parser.PAD)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 224
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v3Parser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 218
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 219
                        self.match(gramatica_v3Parser.AND)
                        self.state = 220
                        self.condition(8)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v3Parser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 221
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 222
                        self.match(gramatica_v3Parser.OR)
                        self.state = 223
                        self.condition(7)
                        pass

             
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


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

        def MUL(self):
            return self.getToken(gramatica_v3Parser.MUL, 0)

        def DIV(self):
            return self.getToken(gramatica_v3Parser.DIV, 0)

        def MOD(self):
            return self.getToken(gramatica_v3Parser.MOD, 0)

        def SUM(self):
            return self.getToken(gramatica_v3Parser.SUM, 0)

        def RES(self):
            return self.getToken(gramatica_v3Parser.RES, 0)

        def relop(self):
            return self.getTypedRuleContext(gramatica_v3Parser.RelopContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_expr

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 230
                self.match(gramatica_v3Parser.PAI)
                self.state = 231
                self.expr(0)
                self.state = 232
                self.match(gramatica_v3Parser.PAD)
                pass

            elif la_ == 2:
                self.state = 234
                self.functionCall()
                pass

            elif la_ == 3:
                self.state = 235
                self.match(gramatica_v3Parser.VAR)
                self.state = 236
                self.match(gramatica_v3Parser.T__1)
                self.state = 237
                self.expr(0)
                self.state = 238
                self.match(gramatica_v3Parser.T__2)
                pass

            elif la_ == 4:
                self.state = 240
                self.match(gramatica_v3Parser.TRUE)
                pass

            elif la_ == 5:
                self.state = 241
                self.match(gramatica_v3Parser.FALSE)
                pass

            elif la_ == 6:
                self.state = 242
                self.match(gramatica_v3Parser.NUM)
                pass

            elif la_ == 7:
                self.state = 243
                self.match(gramatica_v3Parser.FLOAT)
                pass

            elif la_ == 8:
                self.state = 244
                self.match(gramatica_v3Parser.STRING)
                pass

            elif la_ == 9:
                self.state = 245
                self.match(gramatica_v3Parser.VAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 258
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v3Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 249
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v3Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 252
                        _la = self._input.LA(1)
                        if not(_la==31 or _la==32):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 253
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = gramatica_v3Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 254
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 255
                        self.relop()
                        self.state = 256
                        self.expr(10)
                        pass

             
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def PAI(self):
            return self.getToken(gramatica_v3Parser.PAI, 0)

        def PAD(self):
            return self.getToken(gramatica_v3Parser.PAD, 0)

        def argList(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArgListContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = gramatica_v3Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(gramatica_v3Parser.VAR)
            self.state = 264
            self.match(gramatica_v3Parser.PAI)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132491956453376) != 0):
                self.state = 265
                self.argList()


            self.state = 268
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


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = gramatica_v3Parser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.expr(0)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 271
                self.match(gramatica_v3Parser.T__3)
                self.state = 272
                self.expr(0)
                self.state = 277
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


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_arrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = gramatica_v3Parser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(gramatica_v3Parser.T__1)
            self.state = 279
            self.expr(0)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 280
                self.match(gramatica_v3Parser.T__3)
                self.state = 281
                self.expr(0)
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
            self.match(gramatica_v3Parser.T__2)
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


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_relop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = gramatica_v3Parser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
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
        self._predicates[4] = self.tipo_sempred
        self._predicates[21] = self.condition_sempred
        self._predicates[22] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def tipo_sempred(self, localctx:TipoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         




