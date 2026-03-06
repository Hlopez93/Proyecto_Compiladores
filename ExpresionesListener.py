# Generated from Expresiones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete listener for a parse tree produced by ExpresionesParser.
class ExpresionesListener(ParseTreeListener):

    # Enter a parse tree produced by ExpresionesParser#root.
    def enterRoot(self, ctx:ExpresionesParser.RootContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#root.
    def exitRoot(self, ctx:ExpresionesParser.RootContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#statement.
    def enterStatement(self, ctx:ExpresionesParser.StatementContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#statement.
    def exitStatement(self, ctx:ExpresionesParser.StatementContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#declaration.
    def enterDeclaration(self, ctx:ExpresionesParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#declaration.
    def exitDeclaration(self, ctx:ExpresionesParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#type.
    def enterType(self, ctx:ExpresionesParser.TypeContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#type.
    def exitType(self, ctx:ExpresionesParser.TypeContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#assignment.
    def enterAssignment(self, ctx:ExpresionesParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#assignment.
    def exitAssignment(self, ctx:ExpresionesParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#ifStatement.
    def enterIfStatement(self, ctx:ExpresionesParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#ifStatement.
    def exitIfStatement(self, ctx:ExpresionesParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#block.
    def enterBlock(self, ctx:ExpresionesParser.BlockContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#block.
    def exitBlock(self, ctx:ExpresionesParser.BlockContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#expression.
    def enterExpression(self, ctx:ExpresionesParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#expression.
    def exitExpression(self, ctx:ExpresionesParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:ExpresionesParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:ExpresionesParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:ExpresionesParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:ExpresionesParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#equalityExpression.
    def enterEqualityExpression(self, ctx:ExpresionesParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#equalityExpression.
    def exitEqualityExpression(self, ctx:ExpresionesParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#relationalExpression.
    def enterRelationalExpression(self, ctx:ExpresionesParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#relationalExpression.
    def exitRelationalExpression(self, ctx:ExpresionesParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:ExpresionesParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:ExpresionesParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:ExpresionesParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:ExpresionesParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#unaryExpression.
    def enterUnaryExpression(self, ctx:ExpresionesParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#unaryExpression.
    def exitUnaryExpression(self, ctx:ExpresionesParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#primary.
    def enterPrimary(self, ctx:ExpresionesParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#primary.
    def exitPrimary(self, ctx:ExpresionesParser.PrimaryContext):
        pass



del ExpresionesParser