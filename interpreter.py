# -*- python -*-
#
# Author: Gavin Mendel-Gleason
# Copyright: Peer Production License (see http://p2pfoundation.net/Peer_Production_License)
#
# Interpreter for gamook DB logic. 

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
from effects.EffectsLexer import EffectsLexer
from effects.EffectsParser import EffectsParser
from predicate.PredicateLexer import PredicateLexer
from predicate.PredicateParser import PrediateParser



""" 
The Grammar of predicates is as follows: 

string := "'" [char] "'"
ident := [char]
var := ident
number := [0-10]
literal := string | number
builtin := "defined(" var ")"
op := "and" | "or" | "not" 
args := term | term "," term
term := var | literal | unary | random 
predicate := "ident(" args ")"

"""

def parsePredicate(string): 
    char_stream = ANTLRStringStream(string.decode('utf-8'))
    lexer = PredicateLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = PredicateParser(tokens);

    try:
        print parser.statement()
    except RecognitionException:
        traceback.print_stack()

"""
The Grammar of effects is as follows: 

var := [char]
string := "'" [char] "'"
number := [0-10]
literal := string | number
random := num "D" num
term := var | literal | unary | random 
function := "random"
op := "+" | "-" | "%" | "*" 
statement := function([statement]) | statement op statement 
           | (statment) | term
assign := var " := " statement
clause := assign "\n" clause
"""

def parseEffects(string): 
    char_stream = ANTLRStringStream(sys.argv[1].decode('utf-8'))
    lexer = EffectsLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = EffectsParser(tokens);

    try:
        print parser.effects()
    except RecognitionException:
        traceback.print_stack()

