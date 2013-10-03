# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 Predicate.g 2012-10-10 19:08:35

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class PredicateLexer(Lexer):

    grammarFileName = "Predicate.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(PredicateLexer, self).__init__(input, state)


        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )






    # $ANTLR start "T__14"
    def mT__14(self, ):

        try:
            _type = T__14
            _channel = DEFAULT_CHANNEL

            # Predicate.g:7:7: ( '(' )
            # Predicate.g:7:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__14"



    # $ANTLR start "T__15"
    def mT__15(self, ):

        try:
            _type = T__15
            _channel = DEFAULT_CHANNEL

            # Predicate.g:8:7: ( ')' )
            # Predicate.g:8:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__15"



    # $ANTLR start "T__16"
    def mT__16(self, ):

        try:
            _type = T__16
            _channel = DEFAULT_CHANNEL

            # Predicate.g:9:7: ( ',' )
            # Predicate.g:9:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__16"



    # $ANTLR start "IDENTIFIER"
    def mIDENTIFIER(self, ):

        try:
            _type = IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # Predicate.g:73:16: ( IDENTSTART ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )* )
            # Predicate.g:73:18: IDENTSTART ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )*
            pass 
            self.mIDENTSTART()
            # Predicate.g:73:29: ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # Predicate.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENTIFIER"



    # $ANTLR start "VAR"
    def mVAR(self, ):

        try:
            _type = VAR
            _channel = DEFAULT_CHANNEL

            # Predicate.g:74:16: ( VARSTART ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )* )
            # Predicate.g:74:18: VARSTART ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )*
            pass 
            self.mVARSTART()
            # Predicate.g:74:27: ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57) or (65 <= LA2_0 <= 90) or (97 <= LA2_0 <= 122)) :
                    alt2 = 1


                if alt2 == 1:
                    # Predicate.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop2



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VAR"



    # $ANTLR start "INTEGER"
    def mINTEGER(self, ):

        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # Predicate.g:75:16: ( ( DIGIT )+ )
            # Predicate.g:75:18: ( DIGIT )+
            pass 
            # Predicate.g:75:18: ( DIGIT )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # Predicate.g:75:18: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # Predicate.g:76:16: ( ( '\\t' | ' ' | '\\r' | '\\n' )+ )
            # Predicate.g:76:18: ( '\\t' | ' ' | '\\r' | '\\n' )+
            pass 
            # Predicate.g:76:18: ( '\\t' | ' ' | '\\r' | '\\n' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((9 <= LA4_0 <= 10) or LA4_0 == 13 or LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # Predicate.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1
            #action start
            _channel = HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "CONJ"
    def mCONJ(self, ):

        try:
            _type = CONJ
            _channel = DEFAULT_CHANNEL

            # Predicate.g:77:16: ( ( '&' | '\\u2227' ) )
            # Predicate.g:77:18: ( '&' | '\\u2227' )
            pass 
            if self.input.LA(1) == 38 or self.input.LA(1) == 8743:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONJ"



    # $ANTLR start "DISJ"
    def mDISJ(self, ):

        try:
            _type = DISJ
            _channel = DEFAULT_CHANNEL

            # Predicate.g:78:16: ( ( '|' | '\\u2228' ) )
            # Predicate.g:78:18: ( '|' | '\\u2228' )
            pass 
            if self.input.LA(1) == 124 or self.input.LA(1) == 8744:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DISJ"



    # $ANTLR start "NEG"
    def mNEG(self, ):

        try:
            _type = NEG
            _channel = DEFAULT_CHANNEL

            # Predicate.g:79:16: ( ( 'not' | '\\u00ac' ) )
            # Predicate.g:79:18: ( 'not' | '\\u00ac' )
            pass 
            # Predicate.g:79:18: ( 'not' | '\\u00ac' )
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 110) :
                alt5 = 1
            elif (LA5_0 == 172) :
                alt5 = 2
            else:
                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae

            if alt5 == 1:
                # Predicate.g:79:19: 'not'
                pass 
                self.match("not")


            elif alt5 == 2:
                # Predicate.g:79:27: '\\u00ac'
                pass 
                self.match(172)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEG"



    # $ANTLR start "IDENTSTART"
    def mIDENTSTART(self, ):

        try:
            # Predicate.g:80:21: ( 'a' .. 'z' )
            # Predicate.g:80:23: 'a' .. 'z'
            pass 
            self.matchRange(97, 122)




        finally:

            pass

    # $ANTLR end "IDENTSTART"



    # $ANTLR start "VARSTART"
    def mVARSTART(self, ):

        try:
            # Predicate.g:81:19: ( 'A' .. 'Z' )
            # Predicate.g:81:21: 'A' .. 'Z'
            pass 
            self.matchRange(65, 90)




        finally:

            pass

    # $ANTLR end "VARSTART"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # Predicate.g:82:16: ( '0' .. '9' )
            # Predicate.g:82:18: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # Predicate.g:1:8: ( T__14 | T__15 | T__16 | IDENTIFIER | VAR | INTEGER | WHITESPACE | CONJ | DISJ | NEG )
        alt6 = 10
        alt6 = self.dfa6.predict(self.input)
        if alt6 == 1:
            # Predicate.g:1:10: T__14
            pass 
            self.mT__14()


        elif alt6 == 2:
            # Predicate.g:1:16: T__15
            pass 
            self.mT__15()


        elif alt6 == 3:
            # Predicate.g:1:22: T__16
            pass 
            self.mT__16()


        elif alt6 == 4:
            # Predicate.g:1:28: IDENTIFIER
            pass 
            self.mIDENTIFIER()


        elif alt6 == 5:
            # Predicate.g:1:39: VAR
            pass 
            self.mVAR()


        elif alt6 == 6:
            # Predicate.g:1:43: INTEGER
            pass 
            self.mINTEGER()


        elif alt6 == 7:
            # Predicate.g:1:51: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt6 == 8:
            # Predicate.g:1:62: CONJ
            pass 
            self.mCONJ()


        elif alt6 == 9:
            # Predicate.g:1:67: DISJ
            pass 
            self.mDISJ()


        elif alt6 == 10:
            # Predicate.g:1:72: NEG
            pass 
            self.mNEG()







    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\4\uffff\1\12\7\uffff\1\12\1\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\11\3\uffff\1\157\7\uffff\1\164\1\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\u2228\3\uffff\1\157\7\uffff\1\164\1\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\uffff\1\5\1\6\1\7\1\10\1\11\1\4\1\12\1\uffff"
        u"\1\4"
        )

    DFA6_special = DFA.unpack(
        u"\16\uffff"
        )

            
    DFA6_transition = [
        DFA.unpack(u"\2\7\2\uffff\1\7\22\uffff\1\7\5\uffff\1\10\1\uffff\1"
        u"\1\1\2\2\uffff\1\3\3\uffff\12\6\7\uffff\32\5\6\uffff\15\12\1\4"
        u"\14\12\1\uffff\1\11\57\uffff\1\13\u217a\uffff\1\10\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(PredicateLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
