# Generated from LaTeX.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaTeXParser import LaTeXParser
else:
    from LaTeXParser import LaTeXParser

# This class defines a complete listener for a parse tree produced by LaTeXParser.
class LaTeXListener(ParseTreeListener):

    # Enter a parse tree produced by LaTeXParser#math.
    def enterMath(self, ctx:LaTeXParser.MathContext):
        pass

    # Exit a parse tree produced by LaTeXParser#math.
    def exitMath(self, ctx:LaTeXParser.MathContext):
        pass


    # Enter a parse tree produced by LaTeXParser#relation.
    def enterRelation(self, ctx:LaTeXParser.RelationContext):
        pass

    # Exit a parse tree produced by LaTeXParser#relation.
    def exitRelation(self, ctx:LaTeXParser.RelationContext):
        pass


    # Enter a parse tree produced by LaTeXParser#equality.
    def enterEquality(self, ctx:LaTeXParser.EqualityContext):
        pass

    # Exit a parse tree produced by LaTeXParser#equality.
    def exitEquality(self, ctx:LaTeXParser.EqualityContext):
        pass


    # Enter a parse tree produced by LaTeXParser#expr.
    def enterExpr(self, ctx:LaTeXParser.ExprContext):
        pass

    # Exit a parse tree produced by LaTeXParser#expr.
    def exitExpr(self, ctx:LaTeXParser.ExprContext):
        pass


    # Enter a parse tree produced by LaTeXParser#expr_relation.
    def enterExpr_relation(self, ctx:LaTeXParser.Expr_relationContext):
        pass

    # Exit a parse tree produced by LaTeXParser#expr_relation.
    def exitExpr_relation(self, ctx:LaTeXParser.Expr_relationContext):
        pass


    # Enter a parse tree produced by LaTeXParser#additive.
    def enterAdditive(self, ctx:LaTeXParser.AdditiveContext):
        pass

    # Exit a parse tree produced by LaTeXParser#additive.
    def exitAdditive(self, ctx:LaTeXParser.AdditiveContext):
        pass


    # Enter a parse tree produced by LaTeXParser#mp.
    def enterMp(self, ctx:LaTeXParser.MpContext):
        pass

    # Exit a parse tree produced by LaTeXParser#mp.
    def exitMp(self, ctx:LaTeXParser.MpContext):
        pass


    # Enter a parse tree produced by LaTeXParser#mp_nofunc.
    def enterMp_nofunc(self, ctx:LaTeXParser.Mp_nofuncContext):
        pass

    # Exit a parse tree produced by LaTeXParser#mp_nofunc.
    def exitMp_nofunc(self, ctx:LaTeXParser.Mp_nofuncContext):
        pass


    # Enter a parse tree produced by LaTeXParser#unary.
    def enterUnary(self, ctx:LaTeXParser.UnaryContext):
        pass

    # Exit a parse tree produced by LaTeXParser#unary.
    def exitUnary(self, ctx:LaTeXParser.UnaryContext):
        pass


    # Enter a parse tree produced by LaTeXParser#unary_nofunc.
    def enterUnary_nofunc(self, ctx:LaTeXParser.Unary_nofuncContext):
        pass

    # Exit a parse tree produced by LaTeXParser#unary_nofunc.
    def exitUnary_nofunc(self, ctx:LaTeXParser.Unary_nofuncContext):
        pass


    # Enter a parse tree produced by LaTeXParser#postfix.
    def enterPostfix(self, ctx:LaTeXParser.PostfixContext):
        pass

    # Exit a parse tree produced by LaTeXParser#postfix.
    def exitPostfix(self, ctx:LaTeXParser.PostfixContext):
        pass


    # Enter a parse tree produced by LaTeXParser#postfix_nofunc.
    def enterPostfix_nofunc(self, ctx:LaTeXParser.Postfix_nofuncContext):
        pass

    # Exit a parse tree produced by LaTeXParser#postfix_nofunc.
    def exitPostfix_nofunc(self, ctx:LaTeXParser.Postfix_nofuncContext):
        pass


    # Enter a parse tree produced by LaTeXParser#postfix_op.
    def enterPostfix_op(self, ctx:LaTeXParser.Postfix_opContext):
        pass

    # Exit a parse tree produced by LaTeXParser#postfix_op.
    def exitPostfix_op(self, ctx:LaTeXParser.Postfix_opContext):
        pass


    # Enter a parse tree produced by LaTeXParser#eval_at.
    def enterEval_at(self, ctx:LaTeXParser.Eval_atContext):
        pass

    # Exit a parse tree produced by LaTeXParser#eval_at.
    def exitEval_at(self, ctx:LaTeXParser.Eval_atContext):
        pass


    # Enter a parse tree produced by LaTeXParser#eval_at_sub.
    def enterEval_at_sub(self, ctx:LaTeXParser.Eval_at_subContext):
        pass

    # Exit a parse tree produced by LaTeXParser#eval_at_sub.
    def exitEval_at_sub(self, ctx:LaTeXParser.Eval_at_subContext):
        pass


    # Enter a parse tree produced by LaTeXParser#eval_at_sup.
    def enterEval_at_sup(self, ctx:LaTeXParser.Eval_at_supContext):
        pass

    # Exit a parse tree produced by LaTeXParser#eval_at_sup.
    def exitEval_at_sup(self, ctx:LaTeXParser.Eval_at_supContext):
        pass


    # Enter a parse tree produced by LaTeXParser#exp.
    def enterExp(self, ctx:LaTeXParser.ExpContext):
        pass

    # Exit a parse tree produced by LaTeXParser#exp.
    def exitExp(self, ctx:LaTeXParser.ExpContext):
        pass


    # Enter a parse tree produced by LaTeXParser#exp_nofunc.
    def enterExp_nofunc(self, ctx:LaTeXParser.Exp_nofuncContext):
        pass

    # Exit a parse tree produced by LaTeXParser#exp_nofunc.
    def exitExp_nofunc(self, ctx:LaTeXParser.Exp_nofuncContext):
        pass


    # Enter a parse tree produced by LaTeXParser#comp.
    def enterComp(self, ctx:LaTeXParser.CompContext):
        pass

    # Exit a parse tree produced by LaTeXParser#comp.
    def exitComp(self, ctx:LaTeXParser.CompContext):
        pass


    # Enter a parse tree produced by LaTeXParser#comp_nofunc.
    def enterComp_nofunc(self, ctx:LaTeXParser.Comp_nofuncContext):
        pass

    # Exit a parse tree produced by LaTeXParser#comp_nofunc.
    def exitComp_nofunc(self, ctx:LaTeXParser.Comp_nofuncContext):
        pass


    # Enter a parse tree produced by LaTeXParser#group.
    def enterGroup(self, ctx:LaTeXParser.GroupContext):
        pass

    # Exit a parse tree produced by LaTeXParser#group.
    def exitGroup(self, ctx:LaTeXParser.GroupContext):
        pass


    # Enter a parse tree produced by LaTeXParser#abs_group.
    def enterAbs_group(self, ctx:LaTeXParser.Abs_groupContext):
        pass

    # Exit a parse tree produced by LaTeXParser#abs_group.
    def exitAbs_group(self, ctx:LaTeXParser.Abs_groupContext):
        pass


    # Enter a parse tree produced by LaTeXParser#number.
    def enterNumber(self, ctx:LaTeXParser.NumberContext):
        pass

    # Exit a parse tree produced by LaTeXParser#number.
    def exitNumber(self, ctx:LaTeXParser.NumberContext):
        pass


    # Enter a parse tree produced by LaTeXParser#atom.
    def enterAtom(self, ctx:LaTeXParser.AtomContext):
        pass

    # Exit a parse tree produced by LaTeXParser#atom.
    def exitAtom(self, ctx:LaTeXParser.AtomContext):
        pass


    # Enter a parse tree produced by LaTeXParser#bra.
    def enterBra(self, ctx:LaTeXParser.BraContext):
        pass

    # Exit a parse tree produced by LaTeXParser#bra.
    def exitBra(self, ctx:LaTeXParser.BraContext):
        pass


    # Enter a parse tree produced by LaTeXParser#ket.
    def enterKet(self, ctx:LaTeXParser.KetContext):
        pass

    # Exit a parse tree produced by LaTeXParser#ket.
    def exitKet(self, ctx:LaTeXParser.KetContext):
        pass


    # Enter a parse tree produced by LaTeXParser#mathit.
    def enterMathit(self, ctx:LaTeXParser.MathitContext):
        pass

    # Exit a parse tree produced by LaTeXParser#mathit.
    def exitMathit(self, ctx:LaTeXParser.MathitContext):
        pass


    # Enter a parse tree produced by LaTeXParser#mathit_text.
    def enterMathit_text(self, ctx:LaTeXParser.Mathit_textContext):
        pass

    # Exit a parse tree produced by LaTeXParser#mathit_text.
    def exitMathit_text(self, ctx:LaTeXParser.Mathit_textContext):
        pass


    # Enter a parse tree produced by LaTeXParser#frac.
    def enterFrac(self, ctx:LaTeXParser.FracContext):
        pass

    # Exit a parse tree produced by LaTeXParser#frac.
    def exitFrac(self, ctx:LaTeXParser.FracContext):
        pass


    # Enter a parse tree produced by LaTeXParser#binom.
    def enterBinom(self, ctx:LaTeXParser.BinomContext):
        pass

    # Exit a parse tree produced by LaTeXParser#binom.
    def exitBinom(self, ctx:LaTeXParser.BinomContext):
        pass


    # Enter a parse tree produced by LaTeXParser#floor.
    def enterFloor(self, ctx:LaTeXParser.FloorContext):
        pass

    # Exit a parse tree produced by LaTeXParser#floor.
    def exitFloor(self, ctx:LaTeXParser.FloorContext):
        pass


    # Enter a parse tree produced by LaTeXParser#ceil.
    def enterCeil(self, ctx:LaTeXParser.CeilContext):
        pass

    # Exit a parse tree produced by LaTeXParser#ceil.
    def exitCeil(self, ctx:LaTeXParser.CeilContext):
        pass


    # Enter a parse tree produced by LaTeXParser#func_normal.
    def enterFunc_normal(self, ctx:LaTeXParser.Func_normalContext):
        pass

    # Exit a parse tree produced by LaTeXParser#func_normal.
    def exitFunc_normal(self, ctx:LaTeXParser.Func_normalContext):
        pass


    # Enter a parse tree produced by LaTeXParser#func.
    def enterFunc(self, ctx:LaTeXParser.FuncContext):
        pass

    # Exit a parse tree produced by LaTeXParser#func.
    def exitFunc(self, ctx:LaTeXParser.FuncContext):
        pass


    # Enter a parse tree produced by LaTeXParser#args.
    def enterArgs(self, ctx:LaTeXParser.ArgsContext):
        pass

    # Exit a parse tree produced by LaTeXParser#args.
    def exitArgs(self, ctx:LaTeXParser.ArgsContext):
        pass


    # Enter a parse tree produced by LaTeXParser#limit_sub.
    def enterLimit_sub(self, ctx:LaTeXParser.Limit_subContext):
        pass

    # Exit a parse tree produced by LaTeXParser#limit_sub.
    def exitLimit_sub(self, ctx:LaTeXParser.Limit_subContext):
        pass


    # Enter a parse tree produced by LaTeXParser#func_arg.
    def enterFunc_arg(self, ctx:LaTeXParser.Func_argContext):
        pass

    # Exit a parse tree produced by LaTeXParser#func_arg.
    def exitFunc_arg(self, ctx:LaTeXParser.Func_argContext):
        pass


    # Enter a parse tree produced by LaTeXParser#func_arg_noparens.
    def enterFunc_arg_noparens(self, ctx:LaTeXParser.Func_arg_noparensContext):
        pass

    # Exit a parse tree produced by LaTeXParser#func_arg_noparens.
    def exitFunc_arg_noparens(self, ctx:LaTeXParser.Func_arg_noparensContext):
        pass


    # Enter a parse tree produced by LaTeXParser#subexpr.
    def enterSubexpr(self, ctx:LaTeXParser.SubexprContext):
        pass

    # Exit a parse tree produced by LaTeXParser#subexpr.
    def exitSubexpr(self, ctx:LaTeXParser.SubexprContext):
        pass


    # Enter a parse tree produced by LaTeXParser#supexpr.
    def enterSupexpr(self, ctx:LaTeXParser.SupexprContext):
        pass

    # Exit a parse tree produced by LaTeXParser#supexpr.
    def exitSupexpr(self, ctx:LaTeXParser.SupexprContext):
        pass


    # Enter a parse tree produced by LaTeXParser#subeq.
    def enterSubeq(self, ctx:LaTeXParser.SubeqContext):
        pass

    # Exit a parse tree produced by LaTeXParser#subeq.
    def exitSubeq(self, ctx:LaTeXParser.SubeqContext):
        pass


    # Enter a parse tree produced by LaTeXParser#supeq.
    def enterSupeq(self, ctx:LaTeXParser.SupeqContext):
        pass

    # Exit a parse tree produced by LaTeXParser#supeq.
    def exitSupeq(self, ctx:LaTeXParser.SupeqContext):
        pass



del LaTeXParser