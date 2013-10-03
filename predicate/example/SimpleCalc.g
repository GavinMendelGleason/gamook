grammar SimpleCalc;

options {
  language=Python;
}

@header {
import sys
import traceback

from SimpleCalcLexer import SimpleCalcLexer
}

@main {
def main(argv, otherArg=None):
  char_stream = ANTLRStringStream(sys.argv[1])
  lexer = SimpleCalcLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = SimpleCalcParser(tokens);

  try:
    print parser.eval()
  except RecognitionException:
    traceback.print_stack()
}

eval returns [value]
 : add EOF {$value = $add.value}
 ;

add returns [value]
 : m1=mult {$value = $m1.value} ( '+' m2=mult {$value += $m2.value}
                                | '-' m2=mult {$value -= $m2.value}
                                )* 
 ;

mult returns [value]
 : a1=atom {$value = $a1.value} ( '*' a2=atom {$value *= $a2.value}
                                | '/' a2=atom {$value /= $a2.value}
                                )* 
 ;

atom returns [value]
 : NUMBER      {$value = float($NUMBER.text)}
 | '(' add ')' {$value = $add.value}
 ;

NUMBER         : DIGIT+ ('.' DIGIT*)?;
WHITESPACE     : ('\t' | ' ' | '\r' | '\n')+ {$channel = HIDDEN;};
fragment DIGIT : '0'..'9' ;
