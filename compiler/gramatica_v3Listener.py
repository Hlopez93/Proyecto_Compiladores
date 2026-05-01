# Generated from gramatica_v3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramatica_v3Parser import gramatica_v3Parser
else:
    from gramatica_v3Parser import gramatica_v3Parser

# This class defines a complete listener for a parse tree produced by gramatica_v3Parser.
class gramatica_v3Listener(ParseTreeListener):

    # Enter a parse tree produced by gramatica_v3Parser#root.
    def enterRoot(self, ctx:gramatica_v3Parser.RootContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#root.
    def exitRoot(self, ctx:gramatica_v3Parser.RootContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#statement.
    def enterStatement(self, ctx:gramatica_v3Parser.StatementContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#statement.
    def exitStatement(self, ctx:gramatica_v3Parser.StatementContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#declaration.
    def enterDeclaration(self, ctx:gramatica_v3Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#declaration.
    def exitDeclaration(self, ctx:gramatica_v3Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#declarationStatement.
    def enterDeclarationStatement(self, ctx:gramatica_v3Parser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#declarationStatement.
    def exitDeclarationStatement(self, ctx:gramatica_v3Parser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#tipo.
    def enterTipo(self, ctx:gramatica_v3Parser.TipoContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#tipo.
    def exitTipo(self, ctx:gramatica_v3Parser.TipoContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#baseTipo.
    def enterBaseTipo(self, ctx:gramatica_v3Parser.BaseTipoContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#baseTipo.
    def exitBaseTipo(self, ctx:gramatica_v3Parser.BaseTipoContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#assignment.
    def enterAssignment(self, ctx:gramatica_v3Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#assignment.
    def exitAssignment(self, ctx:gramatica_v3Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:gramatica_v3Parser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:gramatica_v3Parser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#ifStatement.
    def enterIfStatement(self, ctx:gramatica_v3Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#ifStatement.
    def exitIfStatement(self, ctx:gramatica_v3Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#whileStatement.
    def enterWhileStatement(self, ctx:gramatica_v3Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#whileStatement.
    def exitWhileStatement(self, ctx:gramatica_v3Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#forStatement.
    def enterForStatement(self, ctx:gramatica_v3Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#forStatement.
    def exitForStatement(self, ctx:gramatica_v3Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#forInit.
    def enterForInit(self, ctx:gramatica_v3Parser.ForInitContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#forInit.
    def exitForInit(self, ctx:gramatica_v3Parser.ForInitContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#forUpdate.
    def enterForUpdate(self, ctx:gramatica_v3Parser.ForUpdateContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#forUpdate.
    def exitForUpdate(self, ctx:gramatica_v3Parser.ForUpdateContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#functionDecl.
    def enterFunctionDecl(self, ctx:gramatica_v3Parser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#functionDecl.
    def exitFunctionDecl(self, ctx:gramatica_v3Parser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#paramList.
    def enterParamList(self, ctx:gramatica_v3Parser.ParamListContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#paramList.
    def exitParamList(self, ctx:gramatica_v3Parser.ParamListContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#param.
    def enterParam(self, ctx:gramatica_v3Parser.ParamContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#param.
    def exitParam(self, ctx:gramatica_v3Parser.ParamContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#returnStmt.
    def enterReturnStmt(self, ctx:gramatica_v3Parser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#returnStmt.
    def exitReturnStmt(self, ctx:gramatica_v3Parser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#printStmt.
    def enterPrintStmt(self, ctx:gramatica_v3Parser.PrintStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#printStmt.
    def exitPrintStmt(self, ctx:gramatica_v3Parser.PrintStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#importStmt.
    def enterImportStmt(self, ctx:gramatica_v3Parser.ImportStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#importStmt.
    def exitImportStmt(self, ctx:gramatica_v3Parser.ImportStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#breakStmt.
    def enterBreakStmt(self, ctx:gramatica_v3Parser.BreakStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#breakStmt.
    def exitBreakStmt(self, ctx:gramatica_v3Parser.BreakStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#continueStmt.
    def enterContinueStmt(self, ctx:gramatica_v3Parser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#continueStmt.
    def exitContinueStmt(self, ctx:gramatica_v3Parser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#block.
    def enterBlock(self, ctx:gramatica_v3Parser.BlockContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#block.
    def exitBlock(self, ctx:gramatica_v3Parser.BlockContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#condition.
    def enterCondition(self, ctx:gramatica_v3Parser.ConditionContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#condition.
    def exitCondition(self, ctx:gramatica_v3Parser.ConditionContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#expr.
    def enterExpr(self, ctx:gramatica_v3Parser.ExprContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#expr.
    def exitExpr(self, ctx:gramatica_v3Parser.ExprContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#term.
    def enterTerm(self, ctx:gramatica_v3Parser.TermContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#term.
    def exitTerm(self, ctx:gramatica_v3Parser.TermContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#factor.
    def enterFactor(self, ctx:gramatica_v3Parser.FactorContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#factor.
    def exitFactor(self, ctx:gramatica_v3Parser.FactorContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#functionCall.
    def enterFunctionCall(self, ctx:gramatica_v3Parser.FunctionCallContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#functionCall.
    def exitFunctionCall(self, ctx:gramatica_v3Parser.FunctionCallContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#argList.
    def enterArgList(self, ctx:gramatica_v3Parser.ArgListContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#argList.
    def exitArgList(self, ctx:gramatica_v3Parser.ArgListContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#arrayLiteral.
    def enterArrayLiteral(self, ctx:gramatica_v3Parser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#arrayLiteral.
    def exitArrayLiteral(self, ctx:gramatica_v3Parser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by gramatica_v3Parser#relop.
    def enterRelop(self, ctx:gramatica_v3Parser.RelopContext):
        pass

    # Exit a parse tree produced by gramatica_v3Parser#relop.
    def exitRelop(self, ctx:gramatica_v3Parser.RelopContext):
        pass



del gramatica_v3Parser