grammar Predicate;

options {
  language=Python;
}

@header {
import sys
import traceback

from PredicateLexer import PredicateLexer
}

@main {
def main(argv, otherArg=None):
  char_stream = ANTLRStringStream(sys.argv[1].decode('utf-8'))
  lexer = PredicateLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = PredicateParser(tokens);

  try:
    print parser.statement()
  except RecognitionException:
    traceback.print_stack()
}

statement returns [sexp]
 : conj EOF {$sexp = $conj.sexp}
 ;

conj returns [sexp]
 : m1=disj {$sexp = $m1.sexp} 
   ( CONJ m2=disj {$sexp = ['conj', $sexp, $m2.sexp]}
   )* 
 ;

disj returns [sexp]
 : a1=polarity {$sexp = $a1.sexp} 
   ( DISJ a2=polarity {$sexp = ['disj', $sexp, $a2.sexp]}
   )* 
 ;

polarity returns [sexp]
 : NEG atom {$sexp = ['neg', $atom.sexp]} 
 | atom { $sexp = $atom.sexp }
 ; 
 
atom returns [sexp]
 : IDENTIFIER '(' lst=args ')' {$sexp = ['predicate', $IDENTIFIER.text] + $lst.sexp}
 | IDENTIFIER  {$sexp = ['predicate', $IDENTIFIER.text]}
 | '(' conj ')' {$sexp = $conj.sexp}
 ;

args returns [sexp] 
 : f1=funsym {$sexp = [$f1.sexp]} 
   ( ',' f2=funsym { $sexp = $sexp + [$f2.sexp] }
   )*
 ; 

funsym returns [sexp] 
 : IDENTIFIER '(' lst=funargs ')' {$sexp = ['funsym', $IDENTIFIER.text] + $lst.sexp}
 | IDENTIFIER  {$sexp = ['funsym', $IDENTIFIER.text]} 
 | VAR  {$sexp = ['var', $VAR.text]}
 | INTEGER {$sexp = ['int', $INTEGER.text]}
 ;

funargs returns [sexp] 
 : f1=funsym {$sexp = [$f1.sexp]} 
   ( ',' f2=funsym { $sexp = $sexp + [$f2.sexp] }
   )*
 ; 

IDENTIFIER     : IDENTSTART ('A'..'Z' | 'a'..'z' | DIGIT )* ;
VAR            : VARSTART ('A'..'Z' | 'a'..'z' | DIGIT )* ;
INTEGER        : DIGIT+ ;
WHITESPACE     : ('\t' | ' ' | '\r' | '\n')+ {$channel = HIDDEN;};
CONJ           : ('&' | '\u2227') ; /* \wedge */
DISJ           : ('|' | '\u2228') ; /* \vee */
NEG            : ('not' | '\u00ac') ; /* \neg */
fragment IDENTSTART : 'a'..'z';
fragment VARSTART : 'A'..'Z';
fragment DIGIT : '0'..'9' ;
