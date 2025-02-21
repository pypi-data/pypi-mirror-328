import pytest
from pathlib import Path
from pygments import lexers
from pygments.token import Name, String, Token


def _load_local_lexer():
    filename = Path(*Path(__file__).parts[:-2], 'src','mbdyn_lexer', 'mbdynlexer.py')
    lexer = lexers.load_lexer_from_file(filename, lexername="MBDynLexer")
    return lexer


def _mbdtokenize(text):
    return _load_local_lexer().get_tokens(text)


def test_load_local_lexer():
    lexer = _load_local_lexer()
    assert lexer.filenames == ['*.mbd']


@pytest.mark.parametrize(
    "test_input,expected",
    [(r'abcdef',     Token.Name.Label),
     (r'abc_23',     Token.Name.Label),
     
     (r'1.e3',              Token.Literal.Number.Float),
     (r'1.2',               Token.Literal.Number.Float),
     (r'1.e+4',             Token.Literal.Number.Float),
     (r'0.',                Token.Literal.Number.Float),
     (r'0.0',               Token.Literal.Number.Float),
     (r'.0',                Token.Literal.Number.Float),
     pytest.param(r'1e+4' , Token.Literal.Number.Float , marks=pytest.mark.xfail),
     
     (r'12',        Token.Literal.Number.Integer),
     (r'0',         Token.Literal.Number.Integer),
     (r'-12',       Token.Literal.Number.Integer),
        
     (r'"ö\näü\"2"'              , Token.String.Double),
     (r'"...\n ⛈️ \" ..."' , Token.String.Double),
     (r'"...\n ⛈️ \" ..."' , Token.Literal.String.Double), # alias

     # to continue ...
    ]
)
class TestSingleTokens:
    def test_tokentyp(self, test_input,expected):
        '''test first token of expected two'''
        assert list(_mbdtokenize(test_input))[0][0] == expected

    def test_tokenstring(self, test_input,expected):
        '''test completeness of string'''
        assert list(_mbdtokenize(test_input))[0][1] == test_input
