'''
    mbdynlexer.lexer
    ~~~~~~~~~~~~~~~~

    Lexer for MBDyn input files.

    :copyright: Copyright 2025 by Andre Zettel.
    :license: GPL, see http://www.gnu.org for details.
'''

import re

from pygments.lexers.python import PythonLexer
from pygments.lexer import RegexLexer, bygroups, using, words, default, this
from pygments.token import Text, Comment, String, Name, Keyword, \
    Generic, Whitespace, Operator, Punctuation, Number

__all__ = ['MBDynLexer']


class MBDynLexer(RegexLexer):
    '''
    A MBDyn input file lexer.
    '''

    name = 'MBDyn'
    url = 'http://www.aero.polimi.it/'
    aliases = ['mbdyn']
    filenames = ['*.mbd']
    mimetypes = ['application/mbdyn']

    identifier = r'[$a-zA-Z_]\w*'

    _decpart = r'\d(\'?\d)*'

    flags = re.DOTALL

    tokens = {
        'root': [
            (r'\s+', Whitespace),

            (r'/\*', Comment.Multiline, 'comment'),
            (r'#beginpreprocess', Comment, 'prepro'),
            (r'#.*?\n', Comment.Single),

            (r'[bB]egin.*?:\s*\w*\s*\w*', Generic.Heading),
            (r'[eE]nd.*?:\s*\w*\s*\w*', Generic.Heading),

            (r'(\w*\s*\w*\s*\w*:\s*)', Generic.Strong),

            # FIXME check if this is numbers in mbdyn 2.e2 = 200
            (r'(-+)?(\d(\'?\d)*\.)[eE]\d(\'?\d)*',
             Number.Float),

            # FIXME check if this is numbers in mbdyn 2.e-2 = 0.02
            (r'(-+)?(\d(\'?\d)*\.)[eE][+-]\d(\'?\d)*',
             Number.Float),

            # from c_pp lexer
            (r'(-+)?(\d(\'?\d)*\.\d(\'?\d)*|\.\d(\'?\d)*|\d(\'?\d)*)[eE][+-]?\d(\'?\d)*\d(\'?\d)*',
             Number.Float),

            # from c_pp lexer
            (r'(-+)?(\d(\'?\d)*\.(\d(\'?\d)*)?|\.\d(\'?\d)*)',
             Number.Float),

            (r'(-+)?' + _decpart, Number.Integer),

            (identifier, Name.Label),

            (r'[*+=\/\-\(\)\^\]\[]', Operator),
            (r'[,;]', Punctuation),

            (r'"(\\\\|\\[^\\]|[^"\\])*"', String.Double),
        ],
        # -----------------------------------------------------------------

        'comment': [
            (r'[^*/]+', Comment.Multiline),
            (r'\*/', Comment.Multiline, '#pop'),
        ],
        'prepro': [
            (r'.+?(?=#endpreprocess)', using(PythonLexer), '#pop'),
        ],
    }
