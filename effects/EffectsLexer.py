# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 Effects.g 2013-10-02 17:53:28

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
T__13=13
IDENTIFIER=6
VARSTART=9
WHITESPACE=10
VAR=4
DIGIT=8
EOF=-1
IDENTSTART=7


class EffectsLexer(Lexer):

    grammarFileName = "Effects.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(EffectsLexer, self).__init__(input, state)







    # $ANTLR start "T__13"
    def mT__13(self, ):

        try:
            _type = T__13
            _channel = DEFAULT_CHANNEL

            # Effects.g:7:7: ( ';' )
            # Effects.g:7:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__13"



    # $ANTLR start "T__14"
    def mT__14(self, ):

        try:
            _type = T__14
            _channel = DEFAULT_CHANNEL

            # Effects.g:8:7: ( ':=' )
            # Effects.g:8:9: ':='
            pass 
            self.match(":=")



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

            # Effects.g:9:7: ( '(' )
            # Effects.g:9:9: '('
            pass 
            self.match(40)



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

            # Effects.g:10:7: ( ')' )
            # Effects.g:10:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__16"



    # $ANTLR start "T__17"
    def mT__17(self, ):

        try:
            _type = T__17
            _channel = DEFAULT_CHANNEL

            # Effects.g:11:7: ( ',' )
            # Effects.g:11:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__17"



    # $ANTLR start "IDENTIFIER"
    def mIDENTIFIER(self, ):

        try:
            _type = IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # Effects.g:60:16: ( IDENTSTART ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )* )
            # Effects.g:60:18: IDENTSTART ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )*
            pass 
            self.mIDENTSTART()
            # Effects.g:60:29: ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # Effects.g:
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

            # Effects.g:61:16: ( VARSTART ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )* )
            # Effects.g:61:18: VARSTART ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )*
            pass 
            self.mVARSTART()
            # Effects.g:61:27: ( 'A' .. 'Z' | 'a' .. 'z' | DIGIT )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57) or (65 <= LA2_0 <= 90) or (97 <= LA2_0 <= 122)) :
                    alt2 = 1


                if alt2 == 1:
                    # Effects.g:
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

            # Effects.g:62:16: ( ( DIGIT )+ )
            # Effects.g:62:18: ( DIGIT )+
            pass 
            # Effects.g:62:18: ( DIGIT )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # Effects.g:62:18: DIGIT
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

            # Effects.g:63:16: ( ( '\\t' | ' ' | '\\r' | '\\n' )+ )
            # Effects.g:63:18: ( '\\t' | ' ' | '\\r' | '\\n' )+
            pass 
            # Effects.g:63:18: ( '\\t' | ' ' | '\\r' | '\\n' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((9 <= LA4_0 <= 10) or LA4_0 == 13 or LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # Effects.g:
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



    # $ANTLR start "OP1"
    def mOP1(self, ):

        try:
            _type = OP1
            _channel = DEFAULT_CHANNEL

            # Effects.g:64:5: ( '+' | '-' )
            # Effects.g:
            pass 
            if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OP1"



    # $ANTLR start "OP2"
    def mOP2(self, ):

        try:
            _type = OP2
            _channel = DEFAULT_CHANNEL

            # Effects.g:65:5: ( '*' | '/' )
            # Effects.g:
            pass 
            if self.input.LA(1) == 42 or self.input.LA(1) == 47:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OP2"



    # $ANTLR start "IDENTSTART"
    def mIDENTSTART(self, ):

        try:
            # Effects.g:66:21: ( 'a' .. 'z' )
            # Effects.g:66:23: 'a' .. 'z'
            pass 
            self.matchRange(97, 122)




        finally:

            pass

    # $ANTLR end "IDENTSTART"



    # $ANTLR start "VARSTART"
    def mVARSTART(self, ):

        try:
            # Effects.g:67:19: ( 'A' .. 'Z' )
            # Effects.g:67:21: 'A' .. 'Z'
            pass 
            self.matchRange(65, 90)




        finally:

            pass

    # $ANTLR end "VARSTART"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # Effects.g:68:16: ( '0' .. '9' )
            # Effects.g:68:18: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # Effects.g:1:8: ( T__13 | T__14 | T__15 | T__16 | T__17 | IDENTIFIER | VAR | INTEGER | WHITESPACE | OP1 | OP2 )
        alt5 = 11
        LA5 = self.input.LA(1)
        if LA5 == 59:
            alt5 = 1
        elif LA5 == 58:
            alt5 = 2
        elif LA5 == 40:
            alt5 = 3
        elif LA5 == 41:
            alt5 = 4
        elif LA5 == 44:
            alt5 = 5
        elif LA5 == 97 or LA5 == 98 or LA5 == 99 or LA5 == 100 or LA5 == 101 or LA5 == 102 or LA5 == 103 or LA5 == 104 or LA5 == 105 or LA5 == 106 or LA5 == 107 or LA5 == 108 or LA5 == 109 or LA5 == 110 or LA5 == 111 or LA5 == 112 or LA5 == 113 or LA5 == 114 or LA5 == 115 or LA5 == 116 or LA5 == 117 or LA5 == 118 or LA5 == 119 or LA5 == 120 or LA5 == 121 or LA5 == 122:
            alt5 = 6
        elif LA5 == 65 or LA5 == 66 or LA5 == 67 or LA5 == 68 or LA5 == 69 or LA5 == 70 or LA5 == 71 or LA5 == 72 or LA5 == 73 or LA5 == 74 or LA5 == 75 or LA5 == 76 or LA5 == 77 or LA5 == 78 or LA5 == 79 or LA5 == 80 or LA5 == 81 or LA5 == 82 or LA5 == 83 or LA5 == 84 or LA5 == 85 or LA5 == 86 or LA5 == 87 or LA5 == 88 or LA5 == 89 or LA5 == 90:
            alt5 = 7
        elif LA5 == 48 or LA5 == 49 or LA5 == 50 or LA5 == 51 or LA5 == 52 or LA5 == 53 or LA5 == 54 or LA5 == 55 or LA5 == 56 or LA5 == 57:
            alt5 = 8
        elif LA5 == 9 or LA5 == 10 or LA5 == 13 or LA5 == 32:
            alt5 = 9
        elif LA5 == 43 or LA5 == 45:
            alt5 = 10
        elif LA5 == 42 or LA5 == 47:
            alt5 = 11
        else:
            nvae = NoViableAltException("", 5, 0, self.input)

            raise nvae

        if alt5 == 1:
            # Effects.g:1:10: T__13
            pass 
            self.mT__13()


        elif alt5 == 2:
            # Effects.g:1:16: T__14
            pass 
            self.mT__14()


        elif alt5 == 3:
            # Effects.g:1:22: T__15
            pass 
            self.mT__15()


        elif alt5 == 4:
            # Effects.g:1:28: T__16
            pass 
            self.mT__16()


        elif alt5 == 5:
            # Effects.g:1:34: T__17
            pass 
            self.mT__17()


        elif alt5 == 6:
            # Effects.g:1:40: IDENTIFIER
            pass 
            self.mIDENTIFIER()


        elif alt5 == 7:
            # Effects.g:1:51: VAR
            pass 
            self.mVAR()


        elif alt5 == 8:
            # Effects.g:1:55: INTEGER
            pass 
            self.mINTEGER()


        elif alt5 == 9:
            # Effects.g:1:63: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt5 == 10:
            # Effects.g:1:74: OP1
            pass 
            self.mOP1()


        elif alt5 == 11:
            # Effects.g:1:78: OP2
            pass 
            self.mOP2()







 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(EffectsLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
