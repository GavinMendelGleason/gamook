# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 Effects.g 2013-10-02 17:53:28

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import sys
import traceback

from EffectsLexer import EffectsLexer



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
OP2=12
INTEGER=5
OP1=11
T__16=16
T__15=15
T__17=17
T__14=14
IDENTIFIER=6
T__13=13
VARSTART=9
WHITESPACE=10
VAR=4
DIGIT=8
EOF=-1
IDENTSTART=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "VAR", "INTEGER", "IDENTIFIER", "IDENTSTART", "DIGIT", "VARSTART", "WHITESPACE", 
    "OP1", "OP2", "';'", "':='", "'('", "')'", "','"
]




class EffectsParser(Parser):
    grammarFileName = "Effects.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(EffectsParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "effects"
    # Effects.g:27:1: effects returns [sexp] : (c1= clause ';' )* ;
    def effects(self, ):

        sexp = None

        c1 = None


        try:
            try:
                # Effects.g:28:2: ( (c1= clause ';' )* )
                # Effects.g:28:4: (c1= clause ';' )*
                pass 
                #action start
                sexp = []
                #action end
                # Effects.g:28:17: (c1= clause ';' )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == VAR) :
                        alt1 = 1


                    if alt1 == 1:
                        # Effects.g:28:18: c1= clause ';'
                        pass 
                        self._state.following.append(self.FOLLOW_clause_in_effects45)
                        c1 = self.clause()

                        self._state.following.pop()
                        self.match(self.input, 13, self.FOLLOW_13_in_effects47)
                        #action start
                        sexp = [c1] + sexp
                        #action end


                    else:
                        break #loop1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "effects"


    # $ANTLR start "clause"
    # Effects.g:31:1: clause returns [sexp] : VAR ':=' atom ;
    def clause(self, ):

        sexp = None

        VAR1 = None
        atom2 = None


        try:
            try:
                # Effects.g:32:2: ( VAR ':=' atom )
                # Effects.g:32:4: VAR ':=' atom
                pass 
                VAR1=self.match(self.input, VAR, self.FOLLOW_VAR_in_clause67)
                self.match(self.input, 14, self.FOLLOW_14_in_clause69)
                self._state.following.append(self.FOLLOW_atom_in_clause71)
                atom2 = self.atom()

                self._state.following.pop()
                #action start
                sexp = ['assign', VAR1.text, atom2]
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "clause"


    # $ANTLR start "atom"
    # Effects.g:41:1: atom returns [sexp] : ( INTEGER | funsym | '(' a2= atom ')' );
    def atom(self, ):

        sexp = None

        INTEGER3 = None
        a2 = None

        funsym4 = None


        try:
            try:
                # Effects.g:42:2: ( INTEGER | funsym | '(' a2= atom ')' )
                alt2 = 3
                LA2 = self.input.LA(1)
                if LA2 == INTEGER:
                    alt2 = 1
                elif LA2 == VAR or LA2 == IDENTIFIER:
                    alt2 = 2
                elif LA2 == 15:
                    alt2 = 3
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # Effects.g:42:4: INTEGER
                    pass 
                    INTEGER3=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_atom91)
                    #action start
                    sexp = ['number', float(INTEGER3.text)]
                    #action end


                elif alt2 == 2:
                    # Effects.g:43:4: funsym
                    pass 
                    self._state.following.append(self.FOLLOW_funsym_in_atom98)
                    funsym4 = self.funsym()

                    self._state.following.pop()
                    #action start
                    sexp = funsym4
                    #action end


                elif alt2 == 3:
                    # Effects.g:44:4: '(' a2= atom ')'
                    pass 
                    self.match(self.input, 15, self.FOLLOW_15_in_atom105)
                    self._state.following.append(self.FOLLOW_atom_in_atom109)
                    a2 = self.atom()

                    self._state.following.pop()
                    self.match(self.input, 16, self.FOLLOW_16_in_atom111)
                    #action start
                    sexp = a2
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "atom"


    # $ANTLR start "funsym"
    # Effects.g:47:1: funsym returns [sexp] : ( IDENTIFIER '(' lst= funargs ')' | IDENTIFIER | VAR | INTEGER );
    def funsym(self, ):

        sexp = None

        IDENTIFIER5 = None
        IDENTIFIER6 = None
        VAR7 = None
        INTEGER8 = None
        lst = None


        try:
            try:
                # Effects.g:48:2: ( IDENTIFIER '(' lst= funargs ')' | IDENTIFIER | VAR | INTEGER )
                alt3 = 4
                LA3 = self.input.LA(1)
                if LA3 == IDENTIFIER:
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == 15) :
                        alt3 = 1
                    elif (LA3_1 == 13 or (16 <= LA3_1 <= 17)) :
                        alt3 = 2
                    else:
                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae

                elif LA3 == VAR:
                    alt3 = 3
                elif LA3 == INTEGER:
                    alt3 = 4
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # Effects.g:48:4: IDENTIFIER '(' lst= funargs ')'
                    pass 
                    IDENTIFIER5=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_funsym131)
                    self.match(self.input, 15, self.FOLLOW_15_in_funsym133)
                    self._state.following.append(self.FOLLOW_funargs_in_funsym137)
                    lst = self.funargs()

                    self._state.following.pop()
                    self.match(self.input, 16, self.FOLLOW_16_in_funsym139)
                    #action start
                    sexp = ['funsym', IDENTIFIER5.text] + lst
                    #action end


                elif alt3 == 2:
                    # Effects.g:49:4: IDENTIFIER
                    pass 
                    IDENTIFIER6=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_funsym146)
                    #action start
                    sexp = ['funsym', IDENTIFIER6.text]
                    #action end


                elif alt3 == 3:
                    # Effects.g:50:4: VAR
                    pass 
                    VAR7=self.match(self.input, VAR, self.FOLLOW_VAR_in_funsym155)
                    #action start
                    sexp = ['var', VAR7.text]
                    #action end


                elif alt3 == 4:
                    # Effects.g:51:4: INTEGER
                    pass 
                    INTEGER8=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_funsym163)
                    #action start
                    sexp = ['int', INTEGER8.text]
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "funsym"


    # $ANTLR start "funargs"
    # Effects.g:54:1: funargs returns [sexp] : f1= funsym ( ',' f2= funsym )* ;
    def funargs(self, ):

        sexp = None

        f1 = None

        f2 = None


        try:
            try:
                # Effects.g:55:2: (f1= funsym ( ',' f2= funsym )* )
                # Effects.g:55:4: f1= funsym ( ',' f2= funsym )*
                pass 
                self._state.following.append(self.FOLLOW_funsym_in_funargs183)
                f1 = self.funsym()

                self._state.following.pop()
                #action start
                sexp = [f1]
                #action end
                # Effects.g:56:4: ( ',' f2= funsym )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 17) :
                        alt4 = 1


                    if alt4 == 1:
                        # Effects.g:56:6: ',' f2= funsym
                        pass 
                        self.match(self.input, 17, self.FOLLOW_17_in_funargs193)
                        self._state.following.append(self.FOLLOW_funsym_in_funargs197)
                        f2 = self.funsym()

                        self._state.following.pop()
                        #action start
                        sexp = sexp + [f2] 
                        #action end


                    else:
                        break #loop4




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return sexp

    # $ANTLR end "funargs"


    # Delegated rules


 

    FOLLOW_clause_in_effects45 = frozenset([13])
    FOLLOW_13_in_effects47 = frozenset([1, 4])
    FOLLOW_VAR_in_clause67 = frozenset([14])
    FOLLOW_14_in_clause69 = frozenset([4, 5, 6, 15])
    FOLLOW_atom_in_clause71 = frozenset([1])
    FOLLOW_INTEGER_in_atom91 = frozenset([1])
    FOLLOW_funsym_in_atom98 = frozenset([1])
    FOLLOW_15_in_atom105 = frozenset([4, 5, 6, 15])
    FOLLOW_atom_in_atom109 = frozenset([16])
    FOLLOW_16_in_atom111 = frozenset([1])
    FOLLOW_IDENTIFIER_in_funsym131 = frozenset([15])
    FOLLOW_15_in_funsym133 = frozenset([4, 5, 6])
    FOLLOW_funargs_in_funsym137 = frozenset([16])
    FOLLOW_16_in_funsym139 = frozenset([1])
    FOLLOW_IDENTIFIER_in_funsym146 = frozenset([1])
    FOLLOW_VAR_in_funsym155 = frozenset([1])
    FOLLOW_INTEGER_in_funsym163 = frozenset([1])
    FOLLOW_funsym_in_funargs183 = frozenset([1, 17])
    FOLLOW_17_in_funargs193 = frozenset([4, 5, 6])
    FOLLOW_funsym_in_funargs197 = frozenset([1, 17])



       
def main(argv, otherArg=None):
  char_stream = ANTLRStringStream(sys.argv[1].decode('utf-8'))
  lexer = EffectsLexer(char_stream)
  tokens = CommonTokenStream(lexer)
  parser = EffectsParser(tokens);

  try:
    print parser.effects()
  except RecognitionException:
    traceback.print_stack()


if __name__ == '__main__':
    main(sys.argv)
