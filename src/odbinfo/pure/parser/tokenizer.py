""" Interaction with the ANTLR tokenizers """
import antlr4


def convert_token(atoken: antlr4.Token, token_class):
    """ convert antlr4 token to Token subclass"""
    return \
        token_class(
            text=atoken.text,
            type=atoken.type,
            index=atoken.tokenIndex,
            hidden=(atoken.channel == antlr4.Token.HIDDEN_CHANNEL)
        )


def get_token_stream(source_code: str,
                     lexer: antlr4.Lexer) -> antlr4.CommonTokenStream:
    """ return antlr4.CommonTokenStream on `source_code` with `lexer`"""
    input_stream = antlr4.InputStream(source_code)
    return antlr4.CommonTokenStream(lexer(input_stream))


def get_tokens(stream: antlr4.CommonTokenStream, token_class):
    """Read `stream` and return the tokens"""
    stream.fill()
    # exclude EOF token, by leaving the last token out
    atokens = stream.tokens[:-1]

    return [convert_token(atoken, token_class) for atoken in atokens]
