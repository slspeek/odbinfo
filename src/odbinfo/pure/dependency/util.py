""" utilities for dependency search """
import logging

from odbinfo.pure.datatype import NamedNode, User

logger = logging.getLogger(__name__)


def link_user_to_usuable(user: User, referand: NamedNode) -> None:
    """link `token` to `referand`"""

    if user.link:

        # pylint:disable=logging-too-many-args
        logger.warning(
            "Replacing link in user: %s:%s (link=%s:%s) with %s:%s",
            user.content_type,
            user.obj_id,
            user.link.content_type,
            user.link.local_id,
            referand.content_type,
            referand.name)
    user.link = referand.identifier
