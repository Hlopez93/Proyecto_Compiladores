# Generated from gramatica_v3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramatica_v3Parser import gramatica_v3Parser
else:
    from gramatica_v3Parser import gramatica_v3Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v3Parser.

class gramatica_v3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v3Parser#root.
    def visitRoot(self, ctx:gramatica_v3Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#statement.
    def visitStatement(self, ctx:gramatica_v3Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#declaration.
    def visitDeclaration(self, ctx:gramatica_v3Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#declarationStatement.
    def visitDeclarationStatement(self, ctx:gramatica_v3Parser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#tipo.
    def visitTipo(self, ctx:gramatica_v3Parser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#assignment.
    def visitAssignment(self, ctx:gramatica_v3Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:gramatica_v3Parser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#ifStatement.
    def visitIfStatement(self, ctx:gramatica_v3Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#whileStatement.
    def visitWhileStatement(self, ctx:gramatica_v3Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#forStatement.
    def visitForStatement(self, ctx:gramatica_v3Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#forInit.
    def visitForInit(self, ctx:gramatica_v3Parser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#forUpdate.
    def visitForUpdate(self, ctx:gramatica_v3Parser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#functionDecl.
    def visitFunctionDecl(self, ctx:gramatica_v3Parser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#paramList.
    def visitParamList(self, ctx:gramatica_v3Parser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#param.
    def visitParam(self, ctx:gramatica_v3Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#returnStmt.
    def visitReturnStmt(self, ctx:gramatica_v3Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#printStmt.
    def visitPrintStmt(self, ctx:gramatica_v3Parser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#importStmt.
    def visitImportStmt(self, ctx:gramatica_v3Parser.ImportStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#breakStmt.
    def visitBreakStmt(self, ctx:gramatica_v3Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#continueStmt.
    def visitContinueStmt(self, ctx:gramatica_v3Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#block.
    def visitBlock(self, ctx:gramatica_v3Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#condition.
    def visitCondition(self, ctx:gramatica_v3Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#expr.
    def visitExpr(self, ctx:gramatica_v3Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#functionCall.
    def visitFunctionCall(self, ctx:gramatica_v3Parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#argList.
    def visitArgList(self, ctx:gramatica_v3Parser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:gramatica_v3Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#relop.
    def visitRelop(self, ctx:gramatica_v3Parser.RelopContext):
        return self.visitChildren(ctx)



del gramatica_v3Parser