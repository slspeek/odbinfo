" utilities for dependency search "
import logging

from odbinfo.pure.datatype import Token

logger = logging.getLogger(__name__)


def link_token(token: Token, referand):
    "link `token` to `referand`"

    if token.link:
        # pylint:disable=logging-too-many-args
        logger.warning(
            "Replacing link in token: %s (link=%s:%s) with %s:%s",
            str(token.index),
            token.link.content_type,
            token.link.local_id,
            referand.content_type(),
            referand.name)
    token.link = referand.identifier
