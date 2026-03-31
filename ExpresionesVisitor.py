# Generated from Expresiones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete generic visitor for a parse tree produced by ExpresionesParser.

class ExpresionesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpresionesParser#root.
    def visitRoot(self, ctx:ExpresionesParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#statement.
    def visitStatement(self, ctx:ExpresionesParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#declaration.
    def visitDeclaration(self, ctx:ExpresionesParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#tipo.
    def visitTipo(self, ctx:ExpresionesParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#assignment.
    def visitAssignment(self, ctx:ExpresionesParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#ifStatement.
    def visitIfStatement(self, ctx:ExpresionesParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#whileStatement.
    def visitWhileStatement(self, ctx:ExpresionesParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#forStatement.
    def visitForStatement(self, ctx:ExpresionesParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#functionDecl.
    def visitFunctionDecl(self, ctx:ExpresionesParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#paramList.
    def visitParamList(self, ctx:ExpresionesParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#param.
    def visitParam(self, ctx:ExpresionesParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#returnStmt.
    def visitReturnStmt(self, ctx:ExpresionesParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#printStmt.
    def visitPrintStmt(self, ctx:ExpresionesParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#block.
    def visitBlock(self, ctx:ExpresionesParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#condition.
    def visitCondition(self, ctx:ExpresionesParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#expr.
    def visitExpr(self, ctx:ExpresionesParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#functionCall.
    def visitFunctionCall(self, ctx:ExpresionesParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#argList.
    def visitArgList(self, ctx:ExpresionesParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#relop.
    def visitRelop(self, ctx:ExpresionesParser.RelopContext):
        return self.visitChildren(ctx)



del ExpresionesParser