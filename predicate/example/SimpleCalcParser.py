# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 SimpleCalc.g 2012-10-09 20:58:55

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import sys
import traceback

from SimpleCalcLexer import SimpleCalcLexer



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__12=12
T__11=11
T__10=10
NUMBER=4
WHITESPACE=6
DIGIT=5
EOF=-1
T__9=9
T__8=8
T__7=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "NUMBER", "DIGIT", "WHITESPACE", "'+'", "'-'", "'*'", "'/'", "'('", 
    "')'"
]




class SimpleCalcParser(Parser):
    grammarFileName = "SimpleCalc.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SimpleCalcParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "eval"
    # SimpleCalc.g:27:1: eval returns [value] : add EOF ;
    def eval(self, ):

        value = None

        add1 = None


        try:
            try:
                # SimpleCalc.g:28:2: ( add EOF )
                # SimpleCalc.g:28:4: add EOF
                pass 
                self._state.following.append(self.FOLLOW_add_in_eval39)
                add1 = self.add()

                self._state.following.pop()
                self.match(self.input, EOF, self.FOLLOW_EOF_in_eval41)
                #action start
                value = add1
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "eval"


    # $ANTLR start "add"
    # SimpleCalc.g:31:1: add returns [value] : m1= mult ( '+' m2= mult | '-' m2= mult )* ;
    def add(self, ):

        value = None

        m1 = None

        m2 = None


        try:
            try:
                # SimpleCalc.g:32:2: (m1= mult ( '+' m2= mult | '-' m2= mult )* )
                # SimpleCalc.g:32:4: m1= mult ( '+' m2= mult | '-' m2= mult )*
                pass 
                self._state.following.append(self.FOLLOW_mult_in_add60)
                m1 = self.mult()

                self._state.following.pop()
                #action start
                value = m1
                #action end
                # SimpleCalc.g:32:33: ( '+' m2= mult | '-' m2= mult )*
                while True: #loop1
                    alt1 = 3
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 7) :
                        alt1 = 1
                    elif (LA1_0 == 8) :
                        alt1 = 2


                    if alt1 == 1:
                        # SimpleCalc.g:32:35: '+' m2= mult
                        pass 
                        self.match(self.input, 7, self.FOLLOW_7_in_add66)
                        self._state.following.append(self.FOLLOW_mult_in_add70)
                        m2 = self.mult()

                        self._state.following.pop()
                        #action start
                        value += m2
                        #action end


                    elif alt1 == 2:
                        # SimpleCalc.g:33:35: '-' m2= mult
                        pass 
                        self.match(self.input, 8, self.FOLLOW_8_in_add108)
                        self._state.following.append(self.FOLLOW_mult_in_add112)
                        m2 = self.mult()

                        self._state.following.pop()
                        #action start
                        value -= m2
                        #action end


                    else:
                        break #loop1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "add"


    # $ANTLR start "mult"
    # SimpleCalc.g:37:1: mult returns [value] : a1= atom ( '*' a2= atom | '/' a2= atom )* ;
    def mult(self, ):

        value = None

        a1 = None

        a2 = None


        try:
            try:
                # SimpleCalc.g:38:2: (a1= atom ( '*' a2= atom | '/' a2= atom )* )
                # SimpleCalc.g:38:4: a1= atom ( '*' a2= atom | '/' a2= atom )*
                pass 
                self._state.following.append(self.FOLLOW_atom_in_mult167)
                a1 = self.atom()

                self._state.following.pop()
                #action start
                value = a1
                #action end
                # SimpleCalc.g:38:33: ( '*' a2= atom | '/' a2= atom )*
                while True: #loop2
                    alt2 = 3
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 9) :
                        alt2 = 1
                    elif (LA2_0 == 10) :
                        alt2 = 2


                    if alt2 == 1:
                        # SimpleCalc.g:38:35: '*' a2= atom
                        pass 
                        self.match(self.input, 9, self.FOLLOW_9_in_mult173)
                        self._state.following.append(self.FOLLOW_atom_in_mult177)
                        a2 = self.atom()

                        self._state.following.pop()
                        #action start
                        value *= a2
                        #action end


                    elif alt2 == 2:
                        # SimpleCalc.g:39:35: '/' a2= atom
                        pass 
                        self.match(self.input, 10, self.FOLLOW_10_in_mult215)
                        self._state.following.append(self.FOLLOW_atom_in_mult219)
                        a2 = self.atom()

                        self._state.following.pop()
                        #action start
                        value /= a2
                        #action end


                    else:
                        break #loop2




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "mult"


    # $ANTLR start "atom"
    # SimpleCalc.g:43:1: atom returns [value] : ( NUMBER | '(' add ')' );
    def atom(self, ):

        value = None

        NUMBER2 = None
        add3 = None


        try:
            try:
                # SimpleCalc.g:44:2: ( NUMBER | '(' add ')' )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == NUMBER) :
                    alt3 = 1
                elif (LA3_0 == 11) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # SimpleCalc.g:44:4: NUMBER
                    pass 
                    NUMBER2=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_atom272)
                    #action start
                    value = float(NUMBER2.text)
                    #action end


                elif alt3 == 2:
                    # SimpleCalc.g:45:4: '(' add ')'
                    pass 
                    self.match(self.input, 11, self.FOLLOW_11_in_atom284)
                    self._state.following.append(self.FOLLOW_add_in_atom286)
                    add3 = self.add()

                    self._state.following.pop()
                    self.match(self.input, 12, self.FOLLOW_12_in_atom288)
                    #action start
                    value = add3
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "atom"


    # Delegated rules


 

    FOLLOW_add_in_eval39 = frozenset([])
    FOLLOW_EOF_in_eval41 = frozenset([1])
    FOLLOW_mult_in_add60 = frozenset([1, 7, 8])
    FOLLOW_7_in_add66 = frozenset([4, 11])
    FOLLOW_mult_in_add70 = frozenset([1, 7, 8])
    FOLLOW_8_in_add108 = frozenset([4, 11])
    FOLLOW_mult_in_add112 = frozenset([1, 7, 8])
    FOLLOW_atom_in_mult167 = frozenset([1, 9, 10])
    FOLLOW_9_in_mult173 = frozenset([4, 11])
    FOLLOW_atom_in_mult177 = frozenset([1, 9, 10])
    FOLLOW_10_in_mult215 = frozenset([4, 11])
    FOLLOW_atom_in_mult219 = frozenset([1, 9, 10])
    FOLLOW_NUMBER_in_atom272 = frozenset([1])
    FOLLOW_11_in_atom284 = frozenset([4, 11])
    FOLLOW_add_in_atom286 = frozenset([12])
    FOLLOW_12_in_atom288 = frozenset([1])



       
def main(argv, otherArg=None):
  char_stream = ANTLRStringStream(sys.argv[1])
  lexer = SimpleCalcLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = SimpleCalcParser(tokens);

  try:
    print parser.eval()
  except RecognitionException:
    traceback.print_stack()


if __name__ == '__main__':
    main(sys.argv)
