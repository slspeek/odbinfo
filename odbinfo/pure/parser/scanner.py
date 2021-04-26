""" Generic token scanner """
from odbinfo.pure.datatype import Token


class Scanner:
    " Holds position "

    def __init__(self, tokens: [Token]):
        self.tokens = tokens
        self.tokens_length = len(tokens)
        self.cursor = 0
        self.cur_token = None
        self.set_cursor(0)

    def eat(self, token_type):
        " consume token"
        if self.cur_token is not None and self.cur_token.type == token_type:
            token = self.cur_token
            self.step()
            return token
        return None

    def set_cursor(self, position: int):
        " set cur_node "
        if position < self.tokens_length:
            self.cursor = position
            self.cur_token = self.tokens[self.cursor]

    def step(self):
        " Go one token further"
        if self.cur_token is not None:
            self.cursor += 1
            self.set_cursor(self.cursor)

    def maybe_seq(self, seq: [int]) -> [Token]:
        " Read whole `seq` maybe"
        rtokens = []
        mark = self.cursor
        for token in seq:
            rtoken = self.eat(token)
            if rtoken:
                rtokens.append(rtoken)
            else:
                self.set_cursor(mark)
        return rtokens

    def oneof(self, ptokens: [int]) -> [Token]:
        " Read one of `ptokens`"
        rtokens = []
        for token in ptokens:
            rtoken = self.eat(token)
            if rtoken:
                rtokens.append(rtoken)
        return rtokens

    def find_oneof(self, types: [int]) -> [Token]:
        " seek until one of `types` token is seen"
        rtokens = []
        mark = self.cursor
        for i in range(self.cursor, len(self.tokens)):
            self.set_cursor(i)
            rtokens.append(self.cur_token)
            if self.cur_token.type in types:
                self.step()
                return rtokens

        self.set_cursor(mark)
        return []
