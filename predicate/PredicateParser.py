# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 Predicate.g 2012-10-10 19:08:35

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import sys
import traceback

from PredicateLexer import PredicateLexer



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
INTEGER=9
T__16=16
T__15=15
DISJ=5
T__14=14
IDENTIFIER=7
NEG=6
VARSTART=12
WHITESPACE=13
CONJ=4
VAR=8
DIGIT=11
EOF=-1
IDENTSTART=10

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "CONJ", "DISJ", "NEG", "IDENTIFIER", "VAR", "INTEGER", "IDENTSTART", 
    "DIGIT", "VARSTART", "WHITESPACE", "'('", "')'", "','"
]




class PredicateParser(Parser):
    grammarFileName = "Predicate.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(PredicateParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "statement"
    # Predicate.g:27:1: statement returns [sexp] : conj EOF ;
    def statement(self, ):

        sexp = None

        conj1 = None


        try:
            try:
                # Predicate.g:28:2: ( conj EOF )
                # Predicate.g:28:4: conj EOF
                pass 
                self._state.following.append(self.FOLLOW_conj_in_statement39)
                conj1 = self.conj()

                self._state.following.pop()
                self.match(self.input, EOF, self.FOLLOW_EOF_in_statement41)
                #action start
                sexp = conj1
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "statement"


    # $ANTLR start "conj"
    # Predicate.g:31:1: conj returns [sexp] : m1= disj ( CONJ m2= disj )* ;
    def conj(self, ):

        sexp = None

        m1 = None

        m2 = None


        try:
            try:
                # Predicate.g:32:2: (m1= disj ( CONJ m2= disj )* )
                # Predicate.g:32:4: m1= disj ( CONJ m2= disj )*
                pass 
                self._state.following.append(self.FOLLOW_disj_in_conj60)
                m1 = self.disj()

                self._state.following.pop()
                #action start
                sexp = m1
                #action end
                # Predicate.g:33:4: ( CONJ m2= disj )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CONJ) :
                        alt1 = 1


                    if alt1 == 1:
                        # Predicate.g:33:6: CONJ m2= disj
                        pass 
                        self.match(self.input, CONJ, self.FOLLOW_CONJ_in_conj70)
                        self._state.following.append(self.FOLLOW_disj_in_conj74)
                        m2 = self.disj()

                        self._state.following.pop()
                        #action start
                        sexp = ['conj', sexp, m2]
                        #action end


                    else:
                        break #loop1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "conj"


    # $ANTLR start "disj"
    # Predicate.g:37:1: disj returns [sexp] : a1= polarity ( DISJ a2= polarity )* ;
    def disj(self, ):

        sexp = None

        a1 = None

        a2 = None


        try:
            try:
                # Predicate.g:38:2: (a1= polarity ( DISJ a2= polarity )* )
                # Predicate.g:38:4: a1= polarity ( DISJ a2= polarity )*
                pass 
                self._state.following.append(self.FOLLOW_polarity_in_disj100)
                a1 = self.polarity()

                self._state.following.pop()
                #action start
                sexp = a1
                #action end
                # Predicate.g:39:4: ( DISJ a2= polarity )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == DISJ) :
                        alt2 = 1


                    if alt2 == 1:
                        # Predicate.g:39:6: DISJ a2= polarity
                        pass 
                        self.match(self.input, DISJ, self.FOLLOW_DISJ_in_disj110)
                        self._state.following.append(self.FOLLOW_polarity_in_disj114)
                        a2 = self.polarity()

                        self._state.following.pop()
                        #action start
                        sexp = ['disj', sexp, a2]
                        #action end


                    else:
                        break #loop2




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "disj"


    # $ANTLR start "polarity"
    # Predicate.g:43:1: polarity returns [sexp] : ( NEG atom | atom );
    def polarity(self, ):

        sexp = None

        atom2 = None

        atom3 = None


        try:
            try:
                # Predicate.g:44:2: ( NEG atom | atom )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == NEG) :
                    alt3 = 1
                elif (LA3_0 == IDENTIFIER or LA3_0 == 14) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # Predicate.g:44:4: NEG atom
                    pass 
                    self.match(self.input, NEG, self.FOLLOW_NEG_in_polarity138)
                    self._state.following.append(self.FOLLOW_atom_in_polarity140)
                    atom2 = self.atom()

                    self._state.following.pop()
                    #action start
                    sexp = ['neg', atom2]
                    #action end


                elif alt3 == 2:
                    # Predicate.g:45:4: atom
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_polarity148)
                    atom3 = self.atom()

                    self._state.following.pop()
                    #action start
                    sexp = atom3 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "polarity"


    # $ANTLR start "atom"
    # Predicate.g:48:1: atom returns [sexp] : ( IDENTIFIER '(' lst= args ')' | IDENTIFIER | '(' conj ')' );
    def atom(self, ):

        sexp = None

        IDENTIFIER4 = None
        IDENTIFIER5 = None
        lst = None

        conj6 = None


        try:
            try:
                # Predicate.g:49:2: ( IDENTIFIER '(' lst= args ')' | IDENTIFIER | '(' conj ')' )
                alt4 = 3
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENTIFIER) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 14) :
                        alt4 = 1
                    elif (LA4_1 == EOF or (CONJ <= LA4_1 <= DISJ) or LA4_1 == 15) :
                        alt4 = 2
                    else:
                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae

                elif (LA4_0 == 14) :
                    alt4 = 3
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # Predicate.g:49:4: IDENTIFIER '(' lst= args ')'
                    pass 
                    IDENTIFIER4=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_atom167)
                    self.match(self.input, 14, self.FOLLOW_14_in_atom169)
                    self._state.following.append(self.FOLLOW_args_in_atom173)
                    lst = self.args()

                    self._state.following.pop()
                    self.match(self.input, 15, self.FOLLOW_15_in_atom175)
                    #action start
                    sexp = ['predicate', IDENTIFIER4.text] + lst
                    #action end


                elif alt4 == 2:
                    # Predicate.g:50:4: IDENTIFIER
                    pass 
                    IDENTIFIER5=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_atom182)
                    #action start
                    sexp = ['predicate', IDENTIFIER5.text]
                    #action end


                elif alt4 == 3:
                    # Predicate.g:51:4: '(' conj ')'
                    pass 
                    self.match(self.input, 14, self.FOLLOW_14_in_atom190)
                    self._state.following.append(self.FOLLOW_conj_in_atom192)
                    conj6 = self.conj()

                    self._state.following.pop()
                    self.match(self.input, 15, self.FOLLOW_15_in_atom194)
                    #action start
                    sexp = conj6
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "atom"


    # $ANTLR start "args"
    # Predicate.g:54:1: args returns [sexp] : f1= funsym ( ',' f2= funsym )* ;
    def args(self, ):

        sexp = None

        f1 = None

        f2 = None


        try:
            try:
                # Predicate.g:55:2: (f1= funsym ( ',' f2= funsym )* )
                # Predicate.g:55:4: f1= funsym ( ',' f2= funsym )*
                pass 
                self._state.following.append(self.FOLLOW_funsym_in_args214)
                f1 = self.funsym()

                self._state.following.pop()
                #action start
                sexp = [f1]
                #action end
                # Predicate.g:56:4: ( ',' f2= funsym )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 16) :
                        alt5 = 1


                    if alt5 == 1:
                        # Predicate.g:56:6: ',' f2= funsym
                        pass 
                        self.match(self.input, 16, self.FOLLOW_16_in_args224)
                        self._state.following.append(self.FOLLOW_funsym_in_args228)
                        f2 = self.funsym()

                        self._state.following.pop()
                        #action start
                        sexp = sexp + [f2] 
                        #action end


                    else:
                        break #loop5




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "args"


    # $ANTLR start "funsym"
    # Predicate.g:60:1: funsym returns [sexp] : ( IDENTIFIER '(' lst= funargs ')' | IDENTIFIER | VAR | INTEGER );
    def funsym(self, ):

        sexp = None

        IDENTIFIER7 = None
        IDENTIFIER8 = None
        VAR9 = None
        INTEGER10 = None
        lst = None


        try:
            try:
                # Predicate.g:61:2: ( IDENTIFIER '(' lst= funargs ')' | IDENTIFIER | VAR | INTEGER )
                alt6 = 4
                LA6 = self.input.LA(1)
                if LA6 == IDENTIFIER:
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == 14) :
                        alt6 = 1
                    elif ((15 <= LA6_1 <= 16)) :
                        alt6 = 2
                    else:
                        nvae = NoViableAltException("", 6, 1, self.input)

                        raise nvae

                elif LA6 == VAR:
                    alt6 = 3
                elif LA6 == INTEGER:
                    alt6 = 4
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # Predicate.g:61:4: IDENTIFIER '(' lst= funargs ')'
                    pass 
                    IDENTIFIER7=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_funsym253)
                    self.match(self.input, 14, self.FOLLOW_14_in_funsym255)
                    self._state.following.append(self.FOLLOW_funargs_in_funsym259)
                    lst = self.funargs()

                    self._state.following.pop()
                    self.match(self.input, 15, self.FOLLOW_15_in_funsym261)
                    #action start
                    sexp = ['funsym', IDENTIFIER7.text] + lst
                    #action end


                elif alt6 == 2:
                    # Predicate.g:62:4: IDENTIFIER
                    pass 
                    IDENTIFIER8=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_funsym268)
                    #action start
                    sexp = ['funsym', IDENTIFIER8.text]
                    #action end


                elif alt6 == 3:
                    # Predicate.g:63:4: VAR
                    pass 
                    VAR9=self.match(self.input, VAR, self.FOLLOW_VAR_in_funsym277)
                    #action start
                    sexp = ['var', VAR9.text]
                    #action end


                elif alt6 == 4:
                    # Predicate.g:64:4: INTEGER
                    pass 
                    INTEGER10=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_funsym285)
                    #action start
                    sexp = ['int', INTEGER10.text]
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "funsym"


    # $ANTLR start "funargs"
    # Predicate.g:67:1: funargs returns [sexp] : f1= funsym ( ',' f2= funsym )* ;
    def funargs(self, ):

        sexp = None

        f1 = None

        f2 = None


        try:
            try:
                # Predicate.g:68:2: (f1= funsym ( ',' f2= funsym )* )
                # Predicate.g:68:4: f1= funsym ( ',' f2= funsym )*
                pass 
                self._state.following.append(self.FOLLOW_funsym_in_funargs305)
                f1 = self.funsym()

                self._state.following.pop()
                #action start
                sexp = [f1]
                #action end
                # Predicate.g:69:4: ( ',' f2= funsym )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 16) :
                        alt7 = 1


                    if alt7 == 1:
                        # Predicate.g:69:6: ',' f2= funsym
                        pass 
                        self.match(self.input, 16, self.FOLLOW_16_in_funargs315)
                        self._state.following.append(self.FOLLOW_funsym_in_funargs319)
                        f2 = self.funsym()

                        self._state.following.pop()
                        #action start
                        sexp = sexp + [f2] 
                        #action end


                    else:
                        break #loop7




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "funargs"


    # Delegated rules


 

    FOLLOW_conj_in_statement39 = frozenset([])
    FOLLOW_EOF_in_statement41 = frozenset([1])
    FOLLOW_disj_in_conj60 = frozenset([1, 4])
    FOLLOW_CONJ_in_conj70 = frozenset([6, 7, 14])
    FOLLOW_disj_in_conj74 = frozenset([1, 4])
    FOLLOW_polarity_in_disj100 = frozenset([1, 5])
    FOLLOW_DISJ_in_disj110 = frozenset([6, 7, 14])
    FOLLOW_polarity_in_disj114 = frozenset([1, 5])
    FOLLOW_NEG_in_polarity138 = frozenset([6, 7, 14])
    FOLLOW_atom_in_polarity140 = frozenset([1])
    FOLLOW_atom_in_polarity148 = frozenset([1])
    FOLLOW_IDENTIFIER_in_atom167 = frozenset([14])
    FOLLOW_14_in_atom169 = frozenset([7, 8, 9])
    FOLLOW_args_in_atom173 = frozenset([15])
    FOLLOW_15_in_atom175 = frozenset([1])
    FOLLOW_IDENTIFIER_in_atom182 = frozenset([1])
    FOLLOW_14_in_atom190 = frozenset([6, 7, 14])
    FOLLOW_conj_in_atom192 = frozenset([15])
    FOLLOW_15_in_atom194 = frozenset([1])
    FOLLOW_funsym_in_args214 = frozenset([1, 16])
    FOLLOW_16_in_args224 = frozenset([7, 8, 9])
    FOLLOW_funsym_in_args228 = frozenset([1, 16])
    FOLLOW_IDENTIFIER_in_funsym253 = frozenset([14])
    FOLLOW_14_in_funsym255 = frozenset([7, 8, 9])
    FOLLOW_funargs_in_funsym259 = frozenset([15])
    FOLLOW_15_in_funsym261 = frozenset([1])
    FOLLOW_IDENTIFIER_in_funsym268 = frozenset([1])
    FOLLOW_VAR_in_funsym277 = frozenset([1])
    FOLLOW_INTEGER_in_funsym285 = frozenset([1])
    FOLLOW_funsym_in_funargs305 = frozenset([1, 16])
    FOLLOW_16_in_funargs315 = frozenset([7, 8, 9])
    FOLLOW_funsym_in_funargs319 = frozenset([1, 16])



       
def main(argv, otherArg=None):
  char_stream = ANTLRStringStream(sys.argv[1].decode('utf-8'))
  lexer = PredicateLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = PredicateParser(tokens);

  try:
    print parser.statement()
  except RecognitionException:
    traceback.print_stack()


if __name__ == '__main__':
    main(sys.argv)
