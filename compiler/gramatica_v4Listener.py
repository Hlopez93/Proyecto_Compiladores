# Generated from compiler/gramatica_v4.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete listener for a parse tree produced by gramatica_v4Parser.
class gramatica_v4Listener(ParseTreeListener):

    # Enter a parse tree produced by gramatica_v4Parser#root.
    def enterRoot(self, ctx:gramatica_v4Parser.RootContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#root.
    def exitRoot(self, ctx:gramatica_v4Parser.RootContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#statement.
    def enterStatement(self, ctx:gramatica_v4Parser.StatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#statement.
    def exitStatement(self, ctx:gramatica_v4Parser.StatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#declaration.
    def enterDeclaration(self, ctx:gramatica_v4Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#declaration.
    def exitDeclaration(self, ctx:gramatica_v4Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#declarationStatement.
    def enterDeclarationStatement(self, ctx:gramatica_v4Parser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#declarationStatement.
    def exitDeclarationStatement(self, ctx:gramatica_v4Parser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#tipo.
    def enterTipo(self, ctx:gramatica_v4Parser.TipoContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#tipo.
    def exitTipo(self, ctx:gramatica_v4Parser.TipoContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#baseTipo.
    def enterBaseTipo(self, ctx:gramatica_v4Parser.BaseTipoContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#baseTipo.
    def exitBaseTipo(self, ctx:gramatica_v4Parser.BaseTipoContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#assignment.
    def enterAssignment(self, ctx:gramatica_v4Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#assignment.
    def exitAssignment(self, ctx:gramatica_v4Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:gramatica_v4Parser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:gramatica_v4Parser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#ifStatement.
    def enterIfStatement(self, ctx:gramatica_v4Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#ifStatement.
    def exitIfStatement(self, ctx:gramatica_v4Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#whileStatement.
    def enterWhileStatement(self, ctx:gramatica_v4Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#whileStatement.
    def exitWhileStatement(self, ctx:gramatica_v4Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#forStatement.
    def enterForStatement(self, ctx:gramatica_v4Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#forStatement.
    def exitForStatement(self, ctx:gramatica_v4Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#forInit.
    def enterForInit(self, ctx:gramatica_v4Parser.ForInitContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#forInit.
    def exitForInit(self, ctx:gramatica_v4Parser.ForInitContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#forUpdate.
    def enterForUpdate(self, ctx:gramatica_v4Parser.ForUpdateContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#forUpdate.
    def exitForUpdate(self, ctx:gramatica_v4Parser.ForUpdateContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#switchStatement.
    def enterSwitchStatement(self, ctx:gramatica_v4Parser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#switchStatement.
    def exitSwitchStatement(self, ctx:gramatica_v4Parser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#caseClause.
    def enterCaseClause(self, ctx:gramatica_v4Parser.CaseClauseContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#caseClause.
    def exitCaseClause(self, ctx:gramatica_v4Parser.CaseClauseContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#defaultClause.
    def enterDefaultClause(self, ctx:gramatica_v4Parser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#defaultClause.
    def exitDefaultClause(self, ctx:gramatica_v4Parser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#literal.
    def enterLiteral(self, ctx:gramatica_v4Parser.LiteralContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#literal.
    def exitLiteral(self, ctx:gramatica_v4Parser.LiteralContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#functionDecl.
    def enterFunctionDecl(self, ctx:gramatica_v4Parser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#functionDecl.
    def exitFunctionDecl(self, ctx:gramatica_v4Parser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#paramList.
    def enterParamList(self, ctx:gramatica_v4Parser.ParamListContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#paramList.
    def exitParamList(self, ctx:gramatica_v4Parser.ParamListContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#param.
    def enterParam(self, ctx:gramatica_v4Parser.ParamContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#param.
    def exitParam(self, ctx:gramatica_v4Parser.ParamContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#returnStmt.
    def enterReturnStmt(self, ctx:gramatica_v4Parser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#returnStmt.
    def exitReturnStmt(self, ctx:gramatica_v4Parser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#printStmt.
    def enterPrintStmt(self, ctx:gramatica_v4Parser.PrintStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#printStmt.
    def exitPrintStmt(self, ctx:gramatica_v4Parser.PrintStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#importStmt.
    def enterImportStmt(self, ctx:gramatica_v4Parser.ImportStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#importStmt.
    def exitImportStmt(self, ctx:gramatica_v4Parser.ImportStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#breakStmt.
    def enterBreakStmt(self, ctx:gramatica_v4Parser.BreakStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#breakStmt.
    def exitBreakStmt(self, ctx:gramatica_v4Parser.BreakStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#continueStmt.
    def enterContinueStmt(self, ctx:gramatica_v4Parser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#continueStmt.
    def exitContinueStmt(self, ctx:gramatica_v4Parser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#block.
    def enterBlock(self, ctx:gramatica_v4Parser.BlockContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#block.
    def exitBlock(self, ctx:gramatica_v4Parser.BlockContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#condition.
    def enterCondition(self, ctx:gramatica_v4Parser.ConditionContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#condition.
    def exitCondition(self, ctx:gramatica_v4Parser.ConditionContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#expr.
    def enterExpr(self, ctx:gramatica_v4Parser.ExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#expr.
    def exitExpr(self, ctx:gramatica_v4Parser.ExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#functionCall.
    def enterFunctionCall(self, ctx:gramatica_v4Parser.FunctionCallContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#functionCall.
    def exitFunctionCall(self, ctx:gramatica_v4Parser.FunctionCallContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#argList.
    def enterArgList(self, ctx:gramatica_v4Parser.ArgListContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#argList.
    def exitArgList(self, ctx:gramatica_v4Parser.ArgListContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#arrayLiteral.
    def enterArrayLiteral(self, ctx:gramatica_v4Parser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#arrayLiteral.
    def exitArrayLiteral(self, ctx:gramatica_v4Parser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#relop.
    def enterRelop(self, ctx:gramatica_v4Parser.RelopContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#relop.
    def exitRelop(self, ctx:gramatica_v4Parser.RelopContext):
        pass



del gramatica_v4Parser