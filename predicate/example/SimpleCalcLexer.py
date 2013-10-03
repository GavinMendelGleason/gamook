# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 SimpleCalc.g 2012-10-09 20:58:56

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class SimpleCalcLexer(Lexer):

    grammarFileName = "SimpleCalc.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SimpleCalcLexer, self).__init__(input, state)







    # $ANTLR start "T__7"
    def mT__7(self, ):

        try:
            _type = T__7
            _channel = DEFAULT_CHANNEL

            # SimpleCalc.g:7:6: ( '+' )
            # SimpleCalc.g:7:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__7"



    # $ANTLR start "T__8"
    def mT__8(self, ):

        try:
            _type = T__8
            _channel = DEFAULT_CHANNEL

            # SimpleCalc.g:8:6: ( '-' )
            # SimpleCalc.g:8:8: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__8"



    # $ANTLR start "T__9"
    def mT__9(self, ):

        try:
            _type = T__9
            _channel = DEFAULT_CHANNEL

            # SimpleCalc.g:9:6: ( '*' )
            # SimpleCalc.g:9:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__9"



    # $ANTLR start "T__10"
    def mT__10(self, ):

        try:
            _type = T__10
            _channel = DEFAULT_CHANNEL

            # SimpleCalc.g:10:7: ( '/' )
            # SimpleCalc.g:10:9: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__10"



    # $ANTLR start "T__11"
    def mT__11(self, ):

        try:
            _type = T__11
            _channel = DEFAULT_CHANNEL

            # SimpleCalc.g:11:7: ( '(' )
            # SimpleCalc.g:11:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__11"



    # $ANTLR start "T__12"
    def mT__12(self, ):

        try:
            _type = T__12
            _channel = DEFAULT_CHANNEL

            # SimpleCalc.g:12:7: ( ')' )
            # SimpleCalc.g:12:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__12"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):

        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # SimpleCalc.g:48:16: ( ( DIGIT )+ ( '.' ( DIGIT )* )? )
            # SimpleCalc.g:48:18: ( DIGIT )+ ( '.' ( DIGIT )* )?
            pass 
            # SimpleCalc.g:48:18: ( DIGIT )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # SimpleCalc.g:48:18: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1
            # SimpleCalc.g:48:25: ( '.' ( DIGIT )* )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 46) :
                alt3 = 1
            if alt3 == 1:
                # SimpleCalc.g:48:26: '.' ( DIGIT )*
                pass 
                self.match(46)
                # SimpleCalc.g:48:30: ( DIGIT )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((48 <= LA2_0 <= 57)) :
                        alt2 = 1


                    if alt2 == 1:
                        # SimpleCalc.g:48:30: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        break #loop2






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # SimpleCalc.g:49:16: ( ( '\\t' | ' ' | '\\r' | '\\n' )+ )
            # SimpleCalc.g:49:18: ( '\\t' | ' ' | '\\r' | '\\n' )+
            pass 
            # SimpleCalc.g:49:18: ( '\\t' | ' ' | '\\r' | '\\n' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((9 <= LA4_0 <= 10) or LA4_0 == 13 or LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # SimpleCalc.g:
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



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # SimpleCalc.g:50:16: ( '0' .. '9' )
            # SimpleCalc.g:50:18: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # SimpleCalc.g:1:8: ( T__7 | T__8 | T__9 | T__10 | T__11 | T__12 | NUMBER | WHITESPACE )
        alt5 = 8
        LA5 = self.input.LA(1)
        if LA5 == 43:
            alt5 = 1
        elif LA5 == 45:
            alt5 = 2
        elif LA5 == 42:
            alt5 = 3
        elif LA5 == 47:
            alt5 = 4
        elif LA5 == 40:
            alt5 = 5
        elif LA5 == 41:
            alt5 = 6
        elif LA5 == 48 or LA5 == 49 or LA5 == 50 or LA5 == 51 or LA5 == 52 or LA5 == 53 or LA5 == 54 or LA5 == 55 or LA5 == 56 or LA5 == 57:
            alt5 = 7
        elif LA5 == 9 or LA5 == 10 or LA5 == 13 or LA5 == 32:
            alt5 = 8
        else:
            nvae = NoViableAltException("", 5, 0, self.input)

            raise nvae

        if alt5 == 1:
            # SimpleCalc.g:1:10: T__7
            pass 
            self.mT__7()


        elif alt5 == 2:
            # SimpleCalc.g:1:15: T__8
            pass 
            self.mT__8()


        elif alt5 == 3:
            # SimpleCalc.g:1:20: T__9
            pass 
            self.mT__9()


        elif alt5 == 4:
            # SimpleCalc.g:1:25: T__10
            pass 
            self.mT__10()


        elif alt5 == 5:
            # SimpleCalc.g:1:31: T__11
            pass 
            self.mT__11()


        elif alt5 == 6:
            # SimpleCalc.g:1:37: T__12
            pass 
            self.mT__12()


        elif alt5 == 7:
            # SimpleCalc.g:1:43: NUMBER
            pass 
            self.mNUMBER()


        elif alt5 == 8:
            # SimpleCalc.g:1:50: WHITESPACE
            pass 
            self.mWHITESPACE()







 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SimpleCalcLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
