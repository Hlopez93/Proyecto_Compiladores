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


    # Visit a parse tree produced by ExpresionesParser#assignment.
    def visitAssignment(self, ctx:ExpresionesParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#ifStatement.
    def visitIfStatement(self, ctx:ExpresionesParser.IfStatementContext):
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


    # Visit a parse tree produced by ExpresionesParser#relop.
    def visitRelop(self, ctx:ExpresionesParser.RelopContext):
        return self.visitChildren(ctx)



del ExpresionesParser