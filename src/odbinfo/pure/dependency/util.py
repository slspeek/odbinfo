""" utilities for dependency search """
import logging
from typing import Sequence

from odbinfo.pure.datatype import Dependent, NamedNode, Usable, User

logger = logging.getLogger(__name__)


def link_user_to_usuable(user: User, referand: NamedNode) -> None:
    """link `user` to `referand`"""

    if user.link:
        logger.warning(
            "Replacing link in user: %s:%s (link was %s) with %s",
            user.content_type,
            user.obj_id,
            user.link,
            referand.identifier
        )
    user.link = referand.identifier


def product_search(sources: Sequence[Dependent], targets: Sequence[Usable]) -> None:
    """ search for uses of `targets` in `sources`"""
    for source in sources:
        for target in targets:
            source.link_uses(target)
