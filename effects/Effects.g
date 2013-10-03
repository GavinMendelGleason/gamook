grammar Effects;

options {
  language=Python;
}

@header {
import sys
import traceback

from EffectsLexer import EffectsLexer
}

@main {
def main(argv, otherArg=None):
  char_stream = ANTLRStringStream(sys.argv[1].decode('utf-8'))
  lexer = EffectsLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = EffectsParser(tokens);

  try:
    print parser.effects()
  except RecognitionException:
    traceback.print_stack()
}

effects returns [sexp] 
 : {$sexp = []} (c1=clause ';' {$sexp = [$c1.sexp] + $sexp}) *
 ;

clause returns [sexp]
 : VAR ':=' atom {$sexp = ['assign', $VAR.text, $atom.sexp]}
 ;

/* ordred by prec 
statement returns [sexp]
 : a1=atom {$sexp = $a1.sexp} ( OP2 a2=atom {$value = [$OP2.text, $value.sexp, $a2.value]}
                                )* 
 ; */

atom returns [sexp]
 : INTEGER {$sexp = ['number', float($INTEGER.text)]}
 | funsym {$sexp = $funsym.sexp}
 | '(' a2=atom ')' {$sexp = $a2.sexp}
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
INTEGER        : DIGIT + ; // ('.' DIGIT*) ? ;
WHITESPACE     : ('\t' | ' ' | '\r' | '\n')+ {$channel = HIDDEN;};
OP1 : '+' | '-';
OP2 : '*' | '/';
fragment IDENTSTART : 'a'..'z';
fragment VARSTART : 'A'..'Z';
fragment DIGIT : '0'..'9' ;
