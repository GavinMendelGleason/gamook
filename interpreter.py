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

import MySQLdb 
from config import * 


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


def parsePredicate(string): 
    char_stream = ANTLRStringStream(string.decode('utf-8'))
    lexer = PredicateLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = PredicateParser(tokens);

    try:
        print parser.statement()
    except RecognitionException:
        traceback.print_stack()

def parseEffects(string): 
    char_stream = ANTLRStringStream(sys.argv[1].decode('utf-8'))
    lexer = EffectsLexer(char_stream)
    tokens = CommonTokenStream(lexer)
    parser = EffectsParser(tokens);

    try:
        print parser.effects()
    except RecognitionException:
        traceback.print_stack()

LIBRARY = []



def lookup(atom, library): 
    for pred in library: 
        com = pred[0]
        if com == atom: 
            return (pred[1],pred[2])
    return None

def evalPredicate(exp,env={}): 
    name = exp[0]
    if name == 'cong': 
        fst = exp[1]
        snd = exp[2]
    elif name == 'disj': 
        fst = exp[1] 
        snd = exp[2]
    elif name == 'neg':
        pass
    elif name == 'predicate': 
        cmd = exp[1]
        args = exp[2:]
        result = lookup(exp[1])
        if result:
            (params,body) = result 
            newenv = unify(args,env)
            substitue(args,params,body,env)
