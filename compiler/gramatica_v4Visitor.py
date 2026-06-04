# Generated from gramatica_v4.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v4Parser.

class gramatica_v4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v4Parser#root.
    def visitRoot(self, ctx:gramatica_v4Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#statement.
    def visitStatement(self, ctx:gramatica_v4Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#declaration.
    def visitDeclaration(self, ctx:gramatica_v4Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#declarationStatement.
    def visitDeclarationStatement(self, ctx:gramatica_v4Parser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#tipo.
    def visitTipo(self, ctx:gramatica_v4Parser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#baseTipo.
    def visitBaseTipo(self, ctx:gramatica_v4Parser.BaseTipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#assignment.
    def visitAssignment(self, ctx:gramatica_v4Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:gramatica_v4Parser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ifStatement.
    def visitIfStatement(self, ctx:gramatica_v4Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#whileStatement.
    def visitWhileStatement(self, ctx:gramatica_v4Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forStatement.
    def visitForStatement(self, ctx:gramatica_v4Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forInit.
    def visitForInit(self, ctx:gramatica_v4Parser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forUpdate.
    def visitForUpdate(self, ctx:gramatica_v4Parser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#switchStatement.
    def visitSwitchStatement(self, ctx:gramatica_v4Parser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#caseClause.
    def visitCaseClause(self, ctx:gramatica_v4Parser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#defaultClause.
    def visitDefaultClause(self, ctx:gramatica_v4Parser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#literal.
    def visitLiteral(self, ctx:gramatica_v4Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#functionDecl.
    def visitFunctionDecl(self, ctx:gramatica_v4Parser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#paramList.
    def visitParamList(self, ctx:gramatica_v4Parser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#param.
    def visitParam(self, ctx:gramatica_v4Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#returnStmt.
    def visitReturnStmt(self, ctx:gramatica_v4Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#printStmt.
    def visitPrintStmt(self, ctx:gramatica_v4Parser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#importStmt.
    def visitImportStmt(self, ctx:gramatica_v4Parser.ImportStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#breakStmt.
    def visitBreakStmt(self, ctx:gramatica_v4Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#continueStmt.
    def visitContinueStmt(self, ctx:gramatica_v4Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#block.
    def visitBlock(self, ctx:gramatica_v4Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#condition.
    def visitCondition(self, ctx:gramatica_v4Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#expr.
    def visitExpr(self, ctx:gramatica_v4Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#functionCall.
    def visitFunctionCall(self, ctx:gramatica_v4Parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#argList.
    def visitArgList(self, ctx:gramatica_v4Parser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:gramatica_v4Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#relop.
    def visitRelop(self, ctx:gramatica_v4Parser.RelopContext):
        return self.visitChildren(ctx)



del gramatica_v4Parser