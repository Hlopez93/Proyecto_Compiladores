// Generated from c:/Users/Gabriela Aguilar/Proyecto_Compiladores/compiler/gramatica_v3.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramatica_v3Parser}.
 */
public interface gramatica_v3Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(gramatica_v3Parser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(gramatica_v3Parser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(gramatica_v3Parser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(gramatica_v3Parser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(gramatica_v3Parser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(gramatica_v3Parser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#declarationStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationStatement(gramatica_v3Parser.DeclarationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#declarationStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationStatement(gramatica_v3Parser.DeclarationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(gramatica_v3Parser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(gramatica_v3Parser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#baseTipo}.
	 * @param ctx the parse tree
	 */
	void enterBaseTipo(gramatica_v3Parser.BaseTipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#baseTipo}.
	 * @param ctx the parse tree
	 */
	void exitBaseTipo(gramatica_v3Parser.BaseTipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(gramatica_v3Parser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(gramatica_v3Parser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(gramatica_v3Parser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(gramatica_v3Parser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(gramatica_v3Parser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(gramatica_v3Parser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(gramatica_v3Parser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(gramatica_v3Parser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(gramatica_v3Parser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(gramatica_v3Parser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(gramatica_v3Parser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(gramatica_v3Parser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void enterForUpdate(gramatica_v3Parser.ForUpdateContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void exitForUpdate(gramatica_v3Parser.ForUpdateContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(gramatica_v3Parser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(gramatica_v3Parser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(gramatica_v3Parser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(gramatica_v3Parser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(gramatica_v3Parser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(gramatica_v3Parser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(gramatica_v3Parser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(gramatica_v3Parser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(gramatica_v3Parser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(gramatica_v3Parser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#importStmt}.
	 * @param ctx the parse tree
	 */
	void enterImportStmt(gramatica_v3Parser.ImportStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#importStmt}.
	 * @param ctx the parse tree
	 */
	void exitImportStmt(gramatica_v3Parser.ImportStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakStmt(gramatica_v3Parser.BreakStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakStmt(gramatica_v3Parser.BreakStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void enterContinueStmt(gramatica_v3Parser.ContinueStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void exitContinueStmt(gramatica_v3Parser.ContinueStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(gramatica_v3Parser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(gramatica_v3Parser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(gramatica_v3Parser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(gramatica_v3Parser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(gramatica_v3Parser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(gramatica_v3Parser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(gramatica_v3Parser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(gramatica_v3Parser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(gramatica_v3Parser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(gramatica_v3Parser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(gramatica_v3Parser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(gramatica_v3Parser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#argList}.
	 * @param ctx the parse tree
	 */
	void enterArgList(gramatica_v3Parser.ArgListContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#argList}.
	 * @param ctx the parse tree
	 */
	void exitArgList(gramatica_v3Parser.ArgListContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void enterArrayLiteral(gramatica_v3Parser.ArrayLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void exitArrayLiteral(gramatica_v3Parser.ArrayLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramatica_v3Parser#relop}.
	 * @param ctx the parse tree
	 */
	void enterRelop(gramatica_v3Parser.RelopContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramatica_v3Parser#relop}.
	 * @param ctx the parse tree
	 */
	void exitRelop(gramatica_v3Parser.RelopContext ctx);
}