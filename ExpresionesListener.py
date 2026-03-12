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


    # Enter a parse tree produced by ExpresionesParser#condition.
    def enterCondition(self, ctx:ExpresionesParser.ConditionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#condition.
    def exitCondition(self, ctx:ExpresionesParser.ConditionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#expr.
    def enterExpr(self, ctx:ExpresionesParser.ExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#expr.
    def exitExpr(self, ctx:ExpresionesParser.ExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#relop.
    def enterRelop(self, ctx:ExpresionesParser.RelopContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#relop.
    def exitRelop(self, ctx:ExpresionesParser.RelopContext):
        pass



del ExpresionesParser