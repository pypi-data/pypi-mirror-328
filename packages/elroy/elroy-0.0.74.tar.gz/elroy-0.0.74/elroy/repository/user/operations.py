import logging
from typing import Optional

import typer
from toolz import do, pipe
from toolz.curried import do

from ...config.constants import UNKNOWN, tool
from ...config.ctx import ElroyContext
from ...db.db_models import User, UserPreference
from ...db.db_session import DbSession
from ...utils.utils import is_blank


def create_user_id(db: DbSession, user_token: str) -> int:
    return pipe(
        User(token=user_token),
        do(db.add),
        do(lambda _: db.commit()),
        do(db.refresh),
        lambda user: user.id,
    )  # type: ignore


def get_or_create_user_preference(ctx: ElroyContext) -> UserPreference:
    from sqlmodel import select

    user_preference = ctx.db.exec(
        select(UserPreference).where(
            UserPreference.user_id == ctx.user_id,
            UserPreference.is_active == True,
        )
    ).first()

    if user_preference is None:
        user_preference = UserPreference(user_id=ctx.user_id, is_active=True)
        ctx.db.add(user_preference)
        ctx.db.commit()
        ctx.db.refresh(user_preference)
    return user_preference


def set_assistant_name(ctx: ElroyContext, assistant_name: str) -> str:
    """
    Sets the assistant name for the user
    """
    from ..context_messages.operations import refresh_system_instructions

    user_preference = get_or_create_user_preference(ctx)
    user_preference.assistant_name = assistant_name
    ctx.db.add(user_preference)
    ctx.db.commit()
    refresh_system_instructions(ctx)
    return f"Assistant name updated to {assistant_name}."


@tool
def set_user_full_name(ctx: ElroyContext, full_name: str, override_existing: Optional[bool] = False) -> str:
    """Sets the user's full name.

    Guidance for usage:
    - Should predominantly be used relatively in the user journey. However, ensure to not be pushy in getting personal information early.
    - For existing users, this should be used relatively rarely.

    Args:
        full_name: The full name of the user
        override_existing: Whether to override an existing full name, if it is already set. Override existing should only be used if a known full name has been found to be incorrect.

    Returns:
        str: Result of the attempt to set the user's full name
    """

    user_preference = get_or_create_user_preference(ctx)

    old_full_name = user_preference.full_name or UNKNOWN
    if old_full_name != UNKNOWN and not override_existing:
        return f"Full name already set to {user_preference.full_name}. If this should be changed, set override_existing=True."
    else:
        user_preference.full_name = full_name
        ctx.db.commit()

        return f"Full name set to {full_name}. Previous value was {old_full_name}."


@tool
def set_user_preferred_name(ctx: ElroyContext, preferred_name: str, override_existing: Optional[bool] = False) -> str:
    """
    Set the user's preferred name. Should predominantly be used relatively early in first conversations, and relatively rarely afterward.

    Args:
        preferred_name: The user's preferred name.
        override_existing: Whether to override an existing preferred name, if it is already set. Override existing should only be used if a known preferred name has been found to be incorrect.
    """

    user_preference = get_or_create_user_preference(ctx)

    old_preferred_name = user_preference.preferred_name or UNKNOWN

    if old_preferred_name != UNKNOWN and not override_existing:
        return f"Preferred name already set to {user_preference.preferred_name}. If this should be changed, use override_existing=True."
    else:
        user_preference.preferred_name = preferred_name

        ctx.db.commit()
        return f"Set user preferred name to {preferred_name}. Was {old_preferred_name}."


def reset_system_persona(ctx: ElroyContext) -> str:
    """
    Clears the system instruction for the user
    """
    from ..context_messages.operations import refresh_system_instructions

    user_preference = get_or_create_user_preference(ctx)
    if not user_preference.system_persona:
        # Re-clear the persona even if it was already blank, in case some malformed value has been set
        logging.warning("System persona was already set to default")

    user_preference.system_persona = None

    ctx.db.add(user_preference)
    ctx.db.commit()

    refresh_system_instructions(ctx)
    return "System persona cleared, will now use default persona."


def set_persona(ctx: ElroyContext, system_persona: str) -> str:
    """
    Sets the system instruction for the user
    """
    from ..context_messages.operations import refresh_system_instructions

    system_persona = system_persona.strip()

    if is_blank(system_persona):
        raise typer.BadParameter("System persona cannot be blank.")

    user_preference = get_or_create_user_preference(ctx)

    if user_preference.system_persona == system_persona:
        return do(
            logging.info,
            "New system persona and old system persona are identical",
        )  # type: ignore

    user_preference.system_persona = system_persona

    ctx.db.add(user_preference)
    ctx.db.commit()

    refresh_system_instructions(ctx)
    return "System persona updated."
