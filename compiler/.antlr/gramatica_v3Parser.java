// Generated from c:/Users/Gabriela Aguilar/Proyecto_Compiladores/compiler/gramatica_v3.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class gramatica_v3Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, PROGRAM=3, DECL=4, INT=5, FLOAT_T=6, STRING_T=7, BOOL=8, 
		VOID=9, IF=10, ELSE=11, WHILE=12, FOR=13, SWITCH=14, CASE=15, DEFAULT=16, 
		COLON=17, RETURN=18, PRINT=19, IMPORT=20, BREAK=21, CONTINUE=22, TRUE=23, 
		FALSE=24, ASIG=25, SUM=26, RES=27, MUL=28, DIV=29, MOD=30, AND=31, OR=32, 
		NOT=33, GT=34, LT=35, GTE=36, LTE=37, EQ=38, NEQ=39, PAI=40, PAD=41, LLA=42, 
		LLC=43, SEMI=44, COMMA=45, NUM=46, FLOAT=47, STRING=48, VAR=49, LINE_COMMENT=50, 
		WS=51;
	public static final int
		RULE_root = 0, RULE_statement = 1, RULE_declaration = 2, RULE_declarationStatement = 3, 
		RULE_tipo = 4, RULE_baseTipo = 5, RULE_assignment = 6, RULE_assignmentStatement = 7, 
		RULE_ifStatement = 8, RULE_whileStatement = 9, RULE_forStatement = 10, 
		RULE_forInit = 11, RULE_forUpdate = 12, RULE_switchStatement = 13, RULE_caseClause = 14, 
		RULE_defaultClause = 15, RULE_literal = 16, RULE_functionDecl = 17, RULE_paramList = 18, 
		RULE_param = 19, RULE_returnStmt = 20, RULE_printStmt = 21, RULE_importStmt = 22, 
		RULE_breakStmt = 23, RULE_continueStmt = 24, RULE_block = 25, RULE_condition = 26, 
		RULE_expr = 27, RULE_term = 28, RULE_factor = 29, RULE_functionCall = 30, 
		RULE_argList = 31, RULE_arrayLiteral = 32, RULE_relop = 33;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "statement", "declaration", "declarationStatement", "tipo", "baseTipo", 
			"assignment", "assignmentStatement", "ifStatement", "whileStatement", 
			"forStatement", "forInit", "forUpdate", "switchStatement", "caseClause", 
			"defaultClause", "literal", "functionDecl", "paramList", "param", "returnStmt", 
			"printStmt", "importStmt", "breakStmt", "continueStmt", "block", "condition", 
			"expr", "term", "factor", "functionCall", "argList", "arrayLiteral", 
			"relop"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'['", "']'", "'program'", null, "'int'", "'float'", "'string'", 
			"'bool'", "'void'", "'if'", "'else'", "'while'", "'for'", "'switch'", 
			"'case'", "'default'", "':'", "'return'", "'print'", "'import'", "'break'", 
			"'continue'", "'true'", "'false'", "'='", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "'&&'", "'||'", "'!'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
			"'('", "')'", "'{'", "'}'", "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "PROGRAM", "DECL", "INT", "FLOAT_T", "STRING_T", "BOOL", 
			"VOID", "IF", "ELSE", "WHILE", "FOR", "SWITCH", "CASE", "DEFAULT", "COLON", 
			"RETURN", "PRINT", "IMPORT", "BREAK", "CONTINUE", "TRUE", "FALSE", "ASIG", 
			"SUM", "RES", "MUL", "DIV", "MOD", "AND", "OR", "NOT", "GT", "LT", "GTE", 
			"LTE", "EQ", "NEQ", "PAI", "PAD", "LLA", "LLC", "SEMI", "COMMA", "NUM", 
			"FLOAT", "STRING", "VAR", "LINE_COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gramatica_v3.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gramatica_v3Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public TerminalNode PROGRAM() { return getToken(gramatica_v3Parser.PROGRAM, 0); }
		public TerminalNode LLA() { return getToken(gramatica_v3Parser.LLA, 0); }
		public TerminalNode LLC() { return getToken(gramatica_v3Parser.LLC, 0); }
		public TerminalNode EOF() { return getToken(gramatica_v3Parser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(PROGRAM);
			setState(69);
			match(LLA);
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 562949961578480L) != 0)) {
				{
				{
				setState(70);
				statement();
				}
				}
				setState(75);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(76);
			match(LLC);
			setState(77);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public FunctionDeclContext functionDecl() {
			return getRuleContext(FunctionDeclContext.class,0);
		}
		public ReturnStmtContext returnStmt() {
			return getRuleContext(ReturnStmtContext.class,0);
		}
		public PrintStmtContext printStmt() {
			return getRuleContext(PrintStmtContext.class,0);
		}
		public ImportStmtContext importStmt() {
			return getRuleContext(ImportStmtContext.class,0);
		}
		public BreakStmtContext breakStmt() {
			return getRuleContext(BreakStmtContext.class,0);
		}
		public ContinueStmtContext continueStmt() {
			return getRuleContext(ContinueStmtContext.class,0);
		}
		public SwitchStatementContext switchStatement() {
			return getRuleContext(SwitchStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(91);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECL:
				enterOuterAlt(_localctx, 1);
				{
				setState(79);
				declaration();
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				assignment();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(81);
				ifStatement();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(82);
				whileStatement();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 5);
				{
				setState(83);
				forStatement();
				}
				break;
			case INT:
			case FLOAT_T:
			case STRING_T:
			case BOOL:
			case VOID:
				enterOuterAlt(_localctx, 6);
				{
				setState(84);
				functionDecl();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 7);
				{
				setState(85);
				returnStmt();
				}
				break;
			case PRINT:
				enterOuterAlt(_localctx, 8);
				{
				setState(86);
				printStmt();
				}
				break;
			case IMPORT:
				enterOuterAlt(_localctx, 9);
				{
				setState(87);
				importStmt();
				}
				break;
			case BREAK:
				enterOuterAlt(_localctx, 10);
				{
				setState(88);
				breakStmt();
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 11);
				{
				setState(89);
				continueStmt();
				}
				break;
			case SWITCH:
				enterOuterAlt(_localctx, 12);
				{
				setState(90);
				switchStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public DeclarationStatementContext declarationStatement() {
			return getRuleContext(DeclarationStatementContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(gramatica_v3Parser.SEMI, 0); }
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			declarationStatement();
			setState(94);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationStatementContext extends ParserRuleContext {
		public TerminalNode DECL() { return getToken(gramatica_v3Parser.DECL, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode VAR() { return getToken(gramatica_v3Parser.VAR, 0); }
		public TerminalNode ASIG() { return getToken(gramatica_v3Parser.ASIG, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ArrayLiteralContext arrayLiteral() {
			return getRuleContext(ArrayLiteralContext.class,0);
		}
		public DeclarationStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarationStatement; }
	}

	public final DeclarationStatementContext declarationStatement() throws RecognitionException {
		DeclarationStatementContext _localctx = new DeclarationStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declarationStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(DECL);
			setState(97);
			tipo();
			setState(98);
			match(VAR);
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASIG) {
				{
				setState(99);
				match(ASIG);
				setState(102);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case TRUE:
				case FALSE:
				case PAI:
				case NUM:
				case FLOAT:
				case STRING:
				case VAR:
					{
					setState(100);
					expr(0);
					}
					break;
				case T__0:
					{
					setState(101);
					arrayLiteral();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public BaseTipoContext baseTipo() {
			return getRuleContext(BaseTipoContext.class,0);
		}
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			baseTipo();
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__0) {
				{
				setState(107);
				match(T__0);
				setState(108);
				match(T__1);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BaseTipoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(gramatica_v3Parser.INT, 0); }
		public TerminalNode FLOAT_T() { return getToken(gramatica_v3Parser.FLOAT_T, 0); }
		public TerminalNode STRING_T() { return getToken(gramatica_v3Parser.STRING_T, 0); }
		public TerminalNode BOOL() { return getToken(gramatica_v3Parser.BOOL, 0); }
		public TerminalNode VOID() { return getToken(gramatica_v3Parser.VOID, 0); }
		public BaseTipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_baseTipo; }
	}

	public final BaseTipoContext baseTipo() throws RecognitionException {
		BaseTipoContext _localctx = new BaseTipoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_baseTipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 992L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(gramatica_v3Parser.SEMI, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			assignmentStatement();
			setState(114);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentStatementContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(gramatica_v3Parser.VAR, 0); }
		public TerminalNode ASIG() { return getToken(gramatica_v3Parser.ASIG, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentStatement; }
	}

	public final AssignmentStatementContext assignmentStatement() throws RecognitionException {
		AssignmentStatementContext _localctx = new AssignmentStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assignmentStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(VAR);
			setState(117);
			match(ASIG);
			setState(118);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(gramatica_v3Parser.IF, 0); }
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(gramatica_v3Parser.ELSE, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ifStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(IF);
			setState(121);
			match(PAI);
			setState(122);
			condition(0);
			setState(123);
			match(PAD);
			setState(124);
			block();
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(125);
				match(ELSE);
				setState(126);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(gramatica_v3Parser.WHILE, 0); }
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(WHILE);
			setState(130);
			match(PAI);
			setState(131);
			condition(0);
			setState(132);
			match(PAD);
			setState(133);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(gramatica_v3Parser.FOR, 0); }
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public List<TerminalNode> SEMI() { return getTokens(gramatica_v3Parser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(gramatica_v3Parser.SEMI, i);
		}
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForInitContext forInit() {
			return getRuleContext(ForInitContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public ForUpdateContext forUpdate() {
			return getRuleContext(ForUpdateContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(FOR);
			setState(136);
			match(PAI);
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DECL || _la==VAR) {
				{
				setState(137);
				forInit();
				}
			}

			setState(140);
			match(SEMI);
			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1056639289393152L) != 0)) {
				{
				setState(141);
				condition(0);
				}
			}

			setState(144);
			match(SEMI);
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(145);
				forUpdate();
				}
			}

			setState(148);
			match(PAD);
			setState(149);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForInitContext extends ParserRuleContext {
		public DeclarationStatementContext declarationStatement() {
			return getRuleContext(DeclarationStatementContext.class,0);
		}
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public ForInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forInit; }
	}

	public final ForInitContext forInit() throws RecognitionException {
		ForInitContext _localctx = new ForInitContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_forInit);
		try {
			setState(153);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECL:
				enterOuterAlt(_localctx, 1);
				{
				setState(151);
				declarationStatement();
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				assignmentStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForUpdateContext extends ParserRuleContext {
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public ForUpdateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forUpdate; }
	}

	public final ForUpdateContext forUpdate() throws RecognitionException {
		ForUpdateContext _localctx = new ForUpdateContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_forUpdate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			assignmentStatement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SwitchStatementContext extends ParserRuleContext {
		public TerminalNode SWITCH() { return getToken(gramatica_v3Parser.SWITCH, 0); }
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public TerminalNode LLA() { return getToken(gramatica_v3Parser.LLA, 0); }
		public TerminalNode LLC() { return getToken(gramatica_v3Parser.LLC, 0); }
		public List<CaseClauseContext> caseClause() {
			return getRuleContexts(CaseClauseContext.class);
		}
		public CaseClauseContext caseClause(int i) {
			return getRuleContext(CaseClauseContext.class,i);
		}
		public DefaultClauseContext defaultClause() {
			return getRuleContext(DefaultClauseContext.class,0);
		}
		public SwitchStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStatement; }
	}

	public final SwitchStatementContext switchStatement() throws RecognitionException {
		SwitchStatementContext _localctx = new SwitchStatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_switchStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(SWITCH);
			setState(158);
			match(PAI);
			setState(159);
			expr(0);
			setState(160);
			match(PAD);
			setState(161);
			match(LLA);
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE) {
				{
				{
				setState(162);
				caseClause();
				}
				}
				setState(167);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DEFAULT) {
				{
				setState(168);
				defaultClause();
				}
			}

			setState(171);
			match(LLC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CaseClauseContext extends ParserRuleContext {
		public TerminalNode CASE() { return getToken(gramatica_v3Parser.CASE, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode COLON() { return getToken(gramatica_v3Parser.COLON, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CaseClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseClause; }
	}

	public final CaseClauseContext caseClause() throws RecognitionException {
		CaseClauseContext _localctx = new CaseClauseContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_caseClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(CASE);
			setState(174);
			literal();
			setState(175);
			match(COLON);
			setState(179);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 562949961578480L) != 0)) {
				{
				{
				setState(176);
				statement();
				}
				}
				setState(181);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefaultClauseContext extends ParserRuleContext {
		public TerminalNode DEFAULT() { return getToken(gramatica_v3Parser.DEFAULT, 0); }
		public TerminalNode COLON() { return getToken(gramatica_v3Parser.COLON, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public DefaultClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultClause; }
	}

	public final DefaultClauseContext defaultClause() throws RecognitionException {
		DefaultClauseContext _localctx = new DefaultClauseContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_defaultClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(DEFAULT);
			setState(183);
			match(COLON);
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 562949961578480L) != 0)) {
				{
				{
				setState(184);
				statement();
				}
				}
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode NUM() { return getToken(gramatica_v3Parser.NUM, 0); }
		public TerminalNode FLOAT() { return getToken(gramatica_v3Parser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(gramatica_v3Parser.STRING, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 492581209243648L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode VAR() { return getToken(gramatica_v3Parser.VAR, 0); }
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public FunctionDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDecl; }
	}

	public final FunctionDeclContext functionDecl() throws RecognitionException {
		FunctionDeclContext _localctx = new FunctionDeclContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_functionDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			tipo();
			setState(193);
			match(VAR);
			setState(194);
			match(PAI);
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 992L) != 0)) {
				{
				setState(195);
				paramList();
				}
			}

			setState(198);
			match(PAD);
			setState(199);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamListContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(gramatica_v3Parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(gramatica_v3Parser.COMMA, i);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
	}

	public final ParamListContext paramList() throws RecognitionException {
		ParamListContext _localctx = new ParamListContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			param();
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(202);
				match(COMMA);
				setState(203);
				param();
				}
				}
				setState(208);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode VAR() { return getToken(gramatica_v3Parser.VAR, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			tipo();
			setState(210);
			match(VAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(gramatica_v3Parser.RETURN, 0); }
		public TerminalNode SEMI() { return getToken(gramatica_v3Parser.SEMI, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStmt; }
	}

	public final ReturnStmtContext returnStmt() throws RecognitionException {
		ReturnStmtContext _localctx = new ReturnStmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_returnStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(RETURN);
			setState(214);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1056630699458560L) != 0)) {
				{
				setState(213);
				expr(0);
				}
			}

			setState(216);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStmtContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(gramatica_v3Parser.PRINT, 0); }
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public TerminalNode SEMI() { return getToken(gramatica_v3Parser.SEMI, 0); }
		public PrintStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStmt; }
	}

	public final PrintStmtContext printStmt() throws RecognitionException {
		PrintStmtContext _localctx = new PrintStmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_printStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(PRINT);
			setState(219);
			match(PAI);
			setState(220);
			expr(0);
			setState(221);
			match(PAD);
			setState(222);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImportStmtContext extends ParserRuleContext {
		public TerminalNode IMPORT() { return getToken(gramatica_v3Parser.IMPORT, 0); }
		public TerminalNode VAR() { return getToken(gramatica_v3Parser.VAR, 0); }
		public TerminalNode SEMI() { return getToken(gramatica_v3Parser.SEMI, 0); }
		public ImportStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importStmt; }
	}

	public final ImportStmtContext importStmt() throws RecognitionException {
		ImportStmtContext _localctx = new ImportStmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_importStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(IMPORT);
			setState(225);
			match(VAR);
			setState(226);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BreakStmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(gramatica_v3Parser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(gramatica_v3Parser.SEMI, 0); }
		public BreakStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStmt; }
	}

	public final BreakStmtContext breakStmt() throws RecognitionException {
		BreakStmtContext _localctx = new BreakStmtContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_breakStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(BREAK);
			setState(229);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContinueStmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(gramatica_v3Parser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(gramatica_v3Parser.SEMI, 0); }
		public ContinueStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueStmt; }
	}

	public final ContinueStmtContext continueStmt() throws RecognitionException {
		ContinueStmtContext _localctx = new ContinueStmtContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_continueStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(CONTINUE);
			setState(232);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LLA() { return getToken(gramatica_v3Parser.LLA, 0); }
		public TerminalNode LLC() { return getToken(gramatica_v3Parser.LLC, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(LLA);
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 562949961578480L) != 0)) {
				{
				{
				setState(235);
				statement();
				}
				}
				setState(240);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(241);
			match(LLC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(gramatica_v3Parser.NOT, 0); }
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public RelopContext relop() {
			return getRuleContext(RelopContext.class,0);
		}
		public TerminalNode TRUE() { return getToken(gramatica_v3Parser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(gramatica_v3Parser.FALSE, 0); }
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public TerminalNode AND() { return getToken(gramatica_v3Parser.AND, 0); }
		public TerminalNode OR() { return getToken(gramatica_v3Parser.OR, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		return condition(0);
	}

	private ConditionContext condition(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ConditionContext _localctx = new ConditionContext(_ctx, _parentState);
		ConditionContext _prevctx = _localctx;
		int _startState = 52;
		enterRecursionRule(_localctx, 52, RULE_condition, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(244);
				match(NOT);
				setState(245);
				condition(5);
				}
				break;
			case 2:
				{
				setState(246);
				expr(0);
				setState(247);
				relop();
				setState(248);
				expr(0);
				}
				break;
			case 3:
				{
				setState(250);
				match(TRUE);
				}
				break;
			case 4:
				{
				setState(251);
				match(FALSE);
				}
				break;
			case 5:
				{
				setState(252);
				match(PAI);
				setState(253);
				condition(0);
				setState(254);
				match(PAD);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(266);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(264);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
					case 1:
						{
						_localctx = new ConditionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_condition);
						setState(258);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(259);
						match(AND);
						setState(260);
						condition(8);
						}
						break;
					case 2:
						{
						_localctx = new ConditionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_condition);
						setState(261);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(262);
						match(OR);
						setState(263);
						condition(7);
						}
						break;
					}
					} 
				}
				setState(268);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SUM() { return getToken(gramatica_v3Parser.SUM, 0); }
		public TerminalNode RES() { return getToken(gramatica_v3Parser.RES, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 54;
		enterRecursionRule(_localctx, 54, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(270);
			term(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(280);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(278);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(272);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(273);
						match(SUM);
						setState(274);
						term(0);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(275);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(276);
						match(RES);
						setState(277);
						term(0);
						}
						break;
					}
					} 
				}
				setState(282);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode MUL() { return getToken(gramatica_v3Parser.MUL, 0); }
		public TerminalNode DIV() { return getToken(gramatica_v3Parser.DIV, 0); }
		public TerminalNode MOD() { return getToken(gramatica_v3Parser.MOD, 0); }
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		return term(0);
	}

	private TermContext term(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermContext _localctx = new TermContext(_ctx, _parentState);
		TermContext _prevctx = _localctx;
		int _startState = 56;
		enterRecursionRule(_localctx, 56, RULE_term, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(284);
			factor();
			}
			_ctx.stop = _input.LT(-1);
			setState(297);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(295);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
					case 1:
						{
						_localctx = new TermContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(286);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(287);
						match(MUL);
						setState(288);
						factor();
						}
						break;
					case 2:
						{
						_localctx = new TermContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(289);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(290);
						match(DIV);
						setState(291);
						factor();
						}
						break;
					case 3:
						{
						_localctx = new TermContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(292);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(293);
						match(MOD);
						setState(294);
						factor();
						}
						break;
					}
					} 
				}
				setState(299);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode VAR() { return getToken(gramatica_v3Parser.VAR, 0); }
		public TerminalNode TRUE() { return getToken(gramatica_v3Parser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(gramatica_v3Parser.FALSE, 0); }
		public TerminalNode NUM() { return getToken(gramatica_v3Parser.NUM, 0); }
		public TerminalNode FLOAT() { return getToken(gramatica_v3Parser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(gramatica_v3Parser.STRING, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_factor);
		try {
			setState(316);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(300);
				match(PAI);
				setState(301);
				expr(0);
				setState(302);
				match(PAD);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(304);
				functionCall();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(305);
				match(VAR);
				setState(306);
				match(T__0);
				setState(307);
				expr(0);
				setState(308);
				match(T__1);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(310);
				match(TRUE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(311);
				match(FALSE);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(312);
				match(NUM);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(313);
				match(FLOAT);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(314);
				match(STRING);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(315);
				match(VAR);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(gramatica_v3Parser.VAR, 0); }
		public TerminalNode PAI() { return getToken(gramatica_v3Parser.PAI, 0); }
		public TerminalNode PAD() { return getToken(gramatica_v3Parser.PAD, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			match(VAR);
			setState(319);
			match(PAI);
			setState(321);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1056630699458560L) != 0)) {
				{
				setState(320);
				argList();
				}
			}

			setState(323);
			match(PAD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgListContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(gramatica_v3Parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(gramatica_v3Parser.COMMA, i);
		}
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_argList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(325);
			expr(0);
			setState(330);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(326);
				match(COMMA);
				setState(327);
				expr(0);
				}
				}
				setState(332);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayLiteralContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(gramatica_v3Parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(gramatica_v3Parser.COMMA, i);
		}
		public ArrayLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayLiteral; }
	}

	public final ArrayLiteralContext arrayLiteral() throws RecognitionException {
		ArrayLiteralContext _localctx = new ArrayLiteralContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_arrayLiteral);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(333);
			match(T__0);
			setState(334);
			expr(0);
			setState(339);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(335);
				match(COMMA);
				setState(336);
				expr(0);
				}
				}
				setState(341);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(342);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelopContext extends ParserRuleContext {
		public TerminalNode GT() { return getToken(gramatica_v3Parser.GT, 0); }
		public TerminalNode LT() { return getToken(gramatica_v3Parser.LT, 0); }
		public TerminalNode GTE() { return getToken(gramatica_v3Parser.GTE, 0); }
		public TerminalNode LTE() { return getToken(gramatica_v3Parser.LTE, 0); }
		public TerminalNode EQ() { return getToken(gramatica_v3Parser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(gramatica_v3Parser.NEQ, 0); }
		public RelopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relop; }
	}

	public final RelopContext relop() throws RecognitionException {
		RelopContext _localctx = new RelopContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_relop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(344);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1082331758592L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 26:
			return condition_sempred((ConditionContext)_localctx, predIndex);
		case 27:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 28:
			return term_sempred((TermContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean condition_sempred(ConditionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean term_sempred(TermContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 4);
		case 5:
			return precpred(_ctx, 3);
		case 6:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00013\u015b\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0005\u0000H\b\u0000\n\u0000\f\u0000K\t\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u0001\\\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u0003g\b\u0003\u0003\u0003i\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004n\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003"+
		"\b\u0080\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u008b\b\n\u0001\n\u0001\n\u0003\n\u008f\b\n\u0001\n"+
		"\u0001\n\u0003\n\u0093\b\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0003\u000b\u009a\b\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0005\r\u00a4\b\r\n\r\f\r\u00a7\t\r\u0001\r\u0003\r"+
		"\u00aa\b\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0005\u000e\u00b2\b\u000e\n\u000e\f\u000e\u00b5\t\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0005\u000f\u00ba\b\u000f\n\u000f\f\u000f\u00bd\t\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0003\u0011\u00c5\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0005\u0012\u00cd\b\u0012\n\u0012\f\u0012\u00d0"+
		"\t\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u00d7\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0005\u0019\u00ed\b\u0019\n"+
		"\u0019\f\u0019\u00f0\t\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003"+
		"\u001a\u0101\b\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0005\u001a\u0109\b\u001a\n\u001a\f\u001a\u010c\t\u001a"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0005\u001b\u0117\b\u001b\n\u001b"+
		"\f\u001b\u011a\t\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001c\u0005\u001c\u0128\b\u001c\n\u001c\f\u001c\u012b"+
		"\t\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u013d"+
		"\b\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u0142\b\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0005\u001f"+
		"\u0149\b\u001f\n\u001f\f\u001f\u014c\t\u001f\u0001 \u0001 \u0001 \u0001"+
		" \u0005 \u0152\b \n \f \u0155\t \u0001 \u0001 \u0001!\u0001!\u0001!\u0000"+
		"\u0003468\"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@B\u0000\u0003\u0001\u0000\u0005"+
		"\t\u0001\u0000.0\u0001\u0000\"\'\u016a\u0000D\u0001\u0000\u0000\u0000"+
		"\u0002[\u0001\u0000\u0000\u0000\u0004]\u0001\u0000\u0000\u0000\u0006`"+
		"\u0001\u0000\u0000\u0000\bj\u0001\u0000\u0000\u0000\no\u0001\u0000\u0000"+
		"\u0000\fq\u0001\u0000\u0000\u0000\u000et\u0001\u0000\u0000\u0000\u0010"+
		"x\u0001\u0000\u0000\u0000\u0012\u0081\u0001\u0000\u0000\u0000\u0014\u0087"+
		"\u0001\u0000\u0000\u0000\u0016\u0099\u0001\u0000\u0000\u0000\u0018\u009b"+
		"\u0001\u0000\u0000\u0000\u001a\u009d\u0001\u0000\u0000\u0000\u001c\u00ad"+
		"\u0001\u0000\u0000\u0000\u001e\u00b6\u0001\u0000\u0000\u0000 \u00be\u0001"+
		"\u0000\u0000\u0000\"\u00c0\u0001\u0000\u0000\u0000$\u00c9\u0001\u0000"+
		"\u0000\u0000&\u00d1\u0001\u0000\u0000\u0000(\u00d4\u0001\u0000\u0000\u0000"+
		"*\u00da\u0001\u0000\u0000\u0000,\u00e0\u0001\u0000\u0000\u0000.\u00e4"+
		"\u0001\u0000\u0000\u00000\u00e7\u0001\u0000\u0000\u00002\u00ea\u0001\u0000"+
		"\u0000\u00004\u0100\u0001\u0000\u0000\u00006\u010d\u0001\u0000\u0000\u0000"+
		"8\u011b\u0001\u0000\u0000\u0000:\u013c\u0001\u0000\u0000\u0000<\u013e"+
		"\u0001\u0000\u0000\u0000>\u0145\u0001\u0000\u0000\u0000@\u014d\u0001\u0000"+
		"\u0000\u0000B\u0158\u0001\u0000\u0000\u0000DE\u0005\u0003\u0000\u0000"+
		"EI\u0005*\u0000\u0000FH\u0003\u0002\u0001\u0000GF\u0001\u0000\u0000\u0000"+
		"HK\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000"+
		"\u0000JL\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000LM\u0005+\u0000"+
		"\u0000MN\u0005\u0000\u0000\u0001N\u0001\u0001\u0000\u0000\u0000O\\\u0003"+
		"\u0004\u0002\u0000P\\\u0003\f\u0006\u0000Q\\\u0003\u0010\b\u0000R\\\u0003"+
		"\u0012\t\u0000S\\\u0003\u0014\n\u0000T\\\u0003\"\u0011\u0000U\\\u0003"+
		"(\u0014\u0000V\\\u0003*\u0015\u0000W\\\u0003,\u0016\u0000X\\\u0003.\u0017"+
		"\u0000Y\\\u00030\u0018\u0000Z\\\u0003\u001a\r\u0000[O\u0001\u0000\u0000"+
		"\u0000[P\u0001\u0000\u0000\u0000[Q\u0001\u0000\u0000\u0000[R\u0001\u0000"+
		"\u0000\u0000[S\u0001\u0000\u0000\u0000[T\u0001\u0000\u0000\u0000[U\u0001"+
		"\u0000\u0000\u0000[V\u0001\u0000\u0000\u0000[W\u0001\u0000\u0000\u0000"+
		"[X\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000[Z\u0001\u0000\u0000"+
		"\u0000\\\u0003\u0001\u0000\u0000\u0000]^\u0003\u0006\u0003\u0000^_\u0005"+
		",\u0000\u0000_\u0005\u0001\u0000\u0000\u0000`a\u0005\u0004\u0000\u0000"+
		"ab\u0003\b\u0004\u0000bh\u00051\u0000\u0000cf\u0005\u0019\u0000\u0000"+
		"dg\u00036\u001b\u0000eg\u0003@ \u0000fd\u0001\u0000\u0000\u0000fe\u0001"+
		"\u0000\u0000\u0000gi\u0001\u0000\u0000\u0000hc\u0001\u0000\u0000\u0000"+
		"hi\u0001\u0000\u0000\u0000i\u0007\u0001\u0000\u0000\u0000jm\u0003\n\u0005"+
		"\u0000kl\u0005\u0001\u0000\u0000ln\u0005\u0002\u0000\u0000mk\u0001\u0000"+
		"\u0000\u0000mn\u0001\u0000\u0000\u0000n\t\u0001\u0000\u0000\u0000op\u0007"+
		"\u0000\u0000\u0000p\u000b\u0001\u0000\u0000\u0000qr\u0003\u000e\u0007"+
		"\u0000rs\u0005,\u0000\u0000s\r\u0001\u0000\u0000\u0000tu\u00051\u0000"+
		"\u0000uv\u0005\u0019\u0000\u0000vw\u00036\u001b\u0000w\u000f\u0001\u0000"+
		"\u0000\u0000xy\u0005\n\u0000\u0000yz\u0005(\u0000\u0000z{\u00034\u001a"+
		"\u0000{|\u0005)\u0000\u0000|\u007f\u00032\u0019\u0000}~\u0005\u000b\u0000"+
		"\u0000~\u0080\u00032\u0019\u0000\u007f}\u0001\u0000\u0000\u0000\u007f"+
		"\u0080\u0001\u0000\u0000\u0000\u0080\u0011\u0001\u0000\u0000\u0000\u0081"+
		"\u0082\u0005\f\u0000\u0000\u0082\u0083\u0005(\u0000\u0000\u0083\u0084"+
		"\u00034\u001a\u0000\u0084\u0085\u0005)\u0000\u0000\u0085\u0086\u00032"+
		"\u0019\u0000\u0086\u0013\u0001\u0000\u0000\u0000\u0087\u0088\u0005\r\u0000"+
		"\u0000\u0088\u008a\u0005(\u0000\u0000\u0089\u008b\u0003\u0016\u000b\u0000"+
		"\u008a\u0089\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000"+
		"\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u008e\u0005,\u0000\u0000\u008d"+
		"\u008f\u00034\u001a\u0000\u008e\u008d\u0001\u0000\u0000\u0000\u008e\u008f"+
		"\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0092"+
		"\u0005,\u0000\u0000\u0091\u0093\u0003\u0018\f\u0000\u0092\u0091\u0001"+
		"\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u0094\u0001"+
		"\u0000\u0000\u0000\u0094\u0095\u0005)\u0000\u0000\u0095\u0096\u00032\u0019"+
		"\u0000\u0096\u0015\u0001\u0000\u0000\u0000\u0097\u009a\u0003\u0006\u0003"+
		"\u0000\u0098\u009a\u0003\u000e\u0007\u0000\u0099\u0097\u0001\u0000\u0000"+
		"\u0000\u0099\u0098\u0001\u0000\u0000\u0000\u009a\u0017\u0001\u0000\u0000"+
		"\u0000\u009b\u009c\u0003\u000e\u0007\u0000\u009c\u0019\u0001\u0000\u0000"+
		"\u0000\u009d\u009e\u0005\u000e\u0000\u0000\u009e\u009f\u0005(\u0000\u0000"+
		"\u009f\u00a0\u00036\u001b\u0000\u00a0\u00a1\u0005)\u0000\u0000\u00a1\u00a5"+
		"\u0005*\u0000\u0000\u00a2\u00a4\u0003\u001c\u000e\u0000\u00a3\u00a2\u0001"+
		"\u0000\u0000\u0000\u00a4\u00a7\u0001\u0000\u0000\u0000\u00a5\u00a3\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6\u00a9\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a8\u00aa\u0003"+
		"\u001e\u000f\u0000\u00a9\u00a8\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001"+
		"\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ac\u0005"+
		"+\u0000\u0000\u00ac\u001b\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005\u000f"+
		"\u0000\u0000\u00ae\u00af\u0003 \u0010\u0000\u00af\u00b3\u0005\u0011\u0000"+
		"\u0000\u00b0\u00b2\u0003\u0002\u0001\u0000\u00b1\u00b0\u0001\u0000\u0000"+
		"\u0000\u00b2\u00b5\u0001\u0000\u0000\u0000\u00b3\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b3\u00b4\u0001\u0000\u0000\u0000\u00b4\u001d\u0001\u0000\u0000"+
		"\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005\u0010\u0000"+
		"\u0000\u00b7\u00bb\u0005\u0011\u0000\u0000\u00b8\u00ba\u0003\u0002\u0001"+
		"\u0000\u00b9\u00b8\u0001\u0000\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000"+
		"\u0000\u00bb\u00b9\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000"+
		"\u0000\u00bc\u001f\u0001\u0000\u0000\u0000\u00bd\u00bb\u0001\u0000\u0000"+
		"\u0000\u00be\u00bf\u0007\u0001\u0000\u0000\u00bf!\u0001\u0000\u0000\u0000"+
		"\u00c0\u00c1\u0003\b\u0004\u0000\u00c1\u00c2\u00051\u0000\u0000\u00c2"+
		"\u00c4\u0005(\u0000\u0000\u00c3\u00c5\u0003$\u0012\u0000\u00c4\u00c3\u0001"+
		"\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5\u00c6\u0001"+
		"\u0000\u0000\u0000\u00c6\u00c7\u0005)\u0000\u0000\u00c7\u00c8\u00032\u0019"+
		"\u0000\u00c8#\u0001\u0000\u0000\u0000\u00c9\u00ce\u0003&\u0013\u0000\u00ca"+
		"\u00cb\u0005-\u0000\u0000\u00cb\u00cd\u0003&\u0013\u0000\u00cc\u00ca\u0001"+
		"\u0000\u0000\u0000\u00cd\u00d0\u0001\u0000\u0000\u0000\u00ce\u00cc\u0001"+
		"\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf%\u0001\u0000"+
		"\u0000\u0000\u00d0\u00ce\u0001\u0000\u0000\u0000\u00d1\u00d2\u0003\b\u0004"+
		"\u0000\u00d2\u00d3\u00051\u0000\u0000\u00d3\'\u0001\u0000\u0000\u0000"+
		"\u00d4\u00d6\u0005\u0012\u0000\u0000\u00d5\u00d7\u00036\u001b\u0000\u00d6"+
		"\u00d5\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7"+
		"\u00d8\u0001\u0000\u0000\u0000\u00d8\u00d9\u0005,\u0000\u0000\u00d9)\u0001"+
		"\u0000\u0000\u0000\u00da\u00db\u0005\u0013\u0000\u0000\u00db\u00dc\u0005"+
		"(\u0000\u0000\u00dc\u00dd\u00036\u001b\u0000\u00dd\u00de\u0005)\u0000"+
		"\u0000\u00de\u00df\u0005,\u0000\u0000\u00df+\u0001\u0000\u0000\u0000\u00e0"+
		"\u00e1\u0005\u0014\u0000\u0000\u00e1\u00e2\u00051\u0000\u0000\u00e2\u00e3"+
		"\u0005,\u0000\u0000\u00e3-\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005\u0015"+
		"\u0000\u0000\u00e5\u00e6\u0005,\u0000\u0000\u00e6/\u0001\u0000\u0000\u0000"+
		"\u00e7\u00e8\u0005\u0016\u0000\u0000\u00e8\u00e9\u0005,\u0000\u0000\u00e9"+
		"1\u0001\u0000\u0000\u0000\u00ea\u00ee\u0005*\u0000\u0000\u00eb\u00ed\u0003"+
		"\u0002\u0001\u0000\u00ec\u00eb\u0001\u0000\u0000\u0000\u00ed\u00f0\u0001"+
		"\u0000\u0000\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000\u00ee\u00ef\u0001"+
		"\u0000\u0000\u0000\u00ef\u00f1\u0001\u0000\u0000\u0000\u00f0\u00ee\u0001"+
		"\u0000\u0000\u0000\u00f1\u00f2\u0005+\u0000\u0000\u00f23\u0001\u0000\u0000"+
		"\u0000\u00f3\u00f4\u0006\u001a\uffff\uffff\u0000\u00f4\u00f5\u0005!\u0000"+
		"\u0000\u00f5\u0101\u00034\u001a\u0005\u00f6\u00f7\u00036\u001b\u0000\u00f7"+
		"\u00f8\u0003B!\u0000\u00f8\u00f9\u00036\u001b\u0000\u00f9\u0101\u0001"+
		"\u0000\u0000\u0000\u00fa\u0101\u0005\u0017\u0000\u0000\u00fb\u0101\u0005"+
		"\u0018\u0000\u0000\u00fc\u00fd\u0005(\u0000\u0000\u00fd\u00fe\u00034\u001a"+
		"\u0000\u00fe\u00ff\u0005)\u0000\u0000\u00ff\u0101\u0001\u0000\u0000\u0000"+
		"\u0100\u00f3\u0001\u0000\u0000\u0000\u0100\u00f6\u0001\u0000\u0000\u0000"+
		"\u0100\u00fa\u0001\u0000\u0000\u0000\u0100\u00fb\u0001\u0000\u0000\u0000"+
		"\u0100\u00fc\u0001\u0000\u0000\u0000\u0101\u010a\u0001\u0000\u0000\u0000"+
		"\u0102\u0103\n\u0007\u0000\u0000\u0103\u0104\u0005\u001f\u0000\u0000\u0104"+
		"\u0109\u00034\u001a\b\u0105\u0106\n\u0006\u0000\u0000\u0106\u0107\u0005"+
		" \u0000\u0000\u0107\u0109\u00034\u001a\u0007\u0108\u0102\u0001\u0000\u0000"+
		"\u0000\u0108\u0105\u0001\u0000\u0000\u0000\u0109\u010c\u0001\u0000\u0000"+
		"\u0000\u010a\u0108\u0001\u0000\u0000\u0000\u010a\u010b\u0001\u0000\u0000"+
		"\u0000\u010b5\u0001\u0000\u0000\u0000\u010c\u010a\u0001\u0000\u0000\u0000"+
		"\u010d\u010e\u0006\u001b\uffff\uffff\u0000\u010e\u010f\u00038\u001c\u0000"+
		"\u010f\u0118\u0001\u0000\u0000\u0000\u0110\u0111\n\u0003\u0000\u0000\u0111"+
		"\u0112\u0005\u001a\u0000\u0000\u0112\u0117\u00038\u001c\u0000\u0113\u0114"+
		"\n\u0002\u0000\u0000\u0114\u0115\u0005\u001b\u0000\u0000\u0115\u0117\u0003"+
		"8\u001c\u0000\u0116\u0110\u0001\u0000\u0000\u0000\u0116\u0113\u0001\u0000"+
		"\u0000\u0000\u0117\u011a\u0001\u0000\u0000\u0000\u0118\u0116\u0001\u0000"+
		"\u0000\u0000\u0118\u0119\u0001\u0000\u0000\u0000\u01197\u0001\u0000\u0000"+
		"\u0000\u011a\u0118\u0001\u0000\u0000\u0000\u011b\u011c\u0006\u001c\uffff"+
		"\uffff\u0000\u011c\u011d\u0003:\u001d\u0000\u011d\u0129\u0001\u0000\u0000"+
		"\u0000\u011e\u011f\n\u0004\u0000\u0000\u011f\u0120\u0005\u001c\u0000\u0000"+
		"\u0120\u0128\u0003:\u001d\u0000\u0121\u0122\n\u0003\u0000\u0000\u0122"+
		"\u0123\u0005\u001d\u0000\u0000\u0123\u0128\u0003:\u001d\u0000\u0124\u0125"+
		"\n\u0002\u0000\u0000\u0125\u0126\u0005\u001e\u0000\u0000\u0126\u0128\u0003"+
		":\u001d\u0000\u0127\u011e\u0001\u0000\u0000\u0000\u0127\u0121\u0001\u0000"+
		"\u0000\u0000\u0127\u0124\u0001\u0000\u0000\u0000\u0128\u012b\u0001\u0000"+
		"\u0000\u0000\u0129\u0127\u0001\u0000\u0000\u0000\u0129\u012a\u0001\u0000"+
		"\u0000\u0000\u012a9\u0001\u0000\u0000\u0000\u012b\u0129\u0001\u0000\u0000"+
		"\u0000\u012c\u012d\u0005(\u0000\u0000\u012d\u012e\u00036\u001b\u0000\u012e"+
		"\u012f\u0005)\u0000\u0000\u012f\u013d\u0001\u0000\u0000\u0000\u0130\u013d"+
		"\u0003<\u001e\u0000\u0131\u0132\u00051\u0000\u0000\u0132\u0133\u0005\u0001"+
		"\u0000\u0000\u0133\u0134\u00036\u001b\u0000\u0134\u0135\u0005\u0002\u0000"+
		"\u0000\u0135\u013d\u0001\u0000\u0000\u0000\u0136\u013d\u0005\u0017\u0000"+
		"\u0000\u0137\u013d\u0005\u0018\u0000\u0000\u0138\u013d\u0005.\u0000\u0000"+
		"\u0139\u013d\u0005/\u0000\u0000\u013a\u013d\u00050\u0000\u0000\u013b\u013d"+
		"\u00051\u0000\u0000\u013c\u012c\u0001\u0000\u0000\u0000\u013c\u0130\u0001"+
		"\u0000\u0000\u0000\u013c\u0131\u0001\u0000\u0000\u0000\u013c\u0136\u0001"+
		"\u0000\u0000\u0000\u013c\u0137\u0001\u0000\u0000\u0000\u013c\u0138\u0001"+
		"\u0000\u0000\u0000\u013c\u0139\u0001\u0000\u0000\u0000\u013c\u013a\u0001"+
		"\u0000\u0000\u0000\u013c\u013b\u0001\u0000\u0000\u0000\u013d;\u0001\u0000"+
		"\u0000\u0000\u013e\u013f\u00051\u0000\u0000\u013f\u0141\u0005(\u0000\u0000"+
		"\u0140\u0142\u0003>\u001f\u0000\u0141\u0140\u0001\u0000\u0000\u0000\u0141"+
		"\u0142\u0001\u0000\u0000\u0000\u0142\u0143\u0001\u0000\u0000\u0000\u0143"+
		"\u0144\u0005)\u0000\u0000\u0144=\u0001\u0000\u0000\u0000\u0145\u014a\u0003"+
		"6\u001b\u0000\u0146\u0147\u0005-\u0000\u0000\u0147\u0149\u00036\u001b"+
		"\u0000\u0148\u0146\u0001\u0000\u0000\u0000\u0149\u014c\u0001\u0000\u0000"+
		"\u0000\u014a\u0148\u0001\u0000\u0000\u0000\u014a\u014b\u0001\u0000\u0000"+
		"\u0000\u014b?\u0001\u0000\u0000\u0000\u014c\u014a\u0001\u0000\u0000\u0000"+
		"\u014d\u014e\u0005\u0001\u0000\u0000\u014e\u0153\u00036\u001b\u0000\u014f"+
		"\u0150\u0005-\u0000\u0000\u0150\u0152\u00036\u001b\u0000\u0151\u014f\u0001"+
		"\u0000\u0000\u0000\u0152\u0155\u0001\u0000\u0000\u0000\u0153\u0151\u0001"+
		"\u0000\u0000\u0000\u0153\u0154\u0001\u0000\u0000\u0000\u0154\u0156\u0001"+
		"\u0000\u0000\u0000\u0155\u0153\u0001\u0000\u0000\u0000\u0156\u0157\u0005"+
		"\u0002\u0000\u0000\u0157A\u0001\u0000\u0000\u0000\u0158\u0159\u0007\u0002"+
		"\u0000\u0000\u0159C\u0001\u0000\u0000\u0000\u001dI[fhm\u007f\u008a\u008e"+
		"\u0092\u0099\u00a5\u00a9\u00b3\u00bb\u00c4\u00ce\u00d6\u00ee\u0100\u0108"+
		"\u010a\u0116\u0118\u0127\u0129\u013c\u0141\u014a\u0153";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}