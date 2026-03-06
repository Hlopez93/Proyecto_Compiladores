# Generated from Expresiones.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
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


    # Visit a parse tree produced by ExpresionesParser#type.
    def visitType(self, ctx:ExpresionesParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#assignment.
    def visitAssignment(self, ctx:ExpresionesParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#ifStatement.
    def visitIfStatement(self, ctx:ExpresionesParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#block.
    def visitBlock(self, ctx:ExpresionesParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#expression.
    def visitExpression(self, ctx:ExpresionesParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:ExpresionesParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:ExpresionesParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#equalityExpression.
    def visitEqualityExpression(self, ctx:ExpresionesParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#relationalExpression.
    def visitRelationalExpression(self, ctx:ExpresionesParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:ExpresionesParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:ExpresionesParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#unaryExpression.
    def visitUnaryExpression(self, ctx:ExpresionesParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#primary.
    def visitPrimary(self, ctx:ExpresionesParser.PrimaryContext):
        return self.visitChildren(ctx)



del ExpresionesParser