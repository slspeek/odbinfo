""" Interaction with the ANTLR tokenizers """
import antlr4
from antlr4 import CommonTokenStream, InputStream


def convert_token(atoken: antlr4.Token, token_class):
    """ convert antlr4 token to Token subclass"""
    return \
        token_class(
            atoken.text,
            atoken.type,
            atoken.tokenIndex,
            atoken.channel == antlr4.Token.HIDDEN_CHANNEL
        )


def get_token_stream(source_code, lexer) -> CommonTokenStream:
    """ return antlr4.CommonTokenStream on `source_code` with `lexer`"""
    input_stream = InputStream(source_code)
    lexer = lexer(input_stream)
    return CommonTokenStream(lexer)


def get_tokens(stream, token_class):
    """Read `stream` and return the tokens"""
    stream.fill()
    # exclude EOF token, by leaving the last token out
    atokens = stream.tokens[:-1]

    return [convert_token(atoken, token_class) for atoken in atokens]
