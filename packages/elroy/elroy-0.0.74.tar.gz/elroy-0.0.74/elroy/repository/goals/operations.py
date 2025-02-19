# Should have param for checking if a similar goal already exists
import logging
from typing import Optional

from sqlmodel import select
from toolz import pipe
from toolz.curried import filter

from ...config.constants import (
    SYSTEM,
    GoalAlreadyExistsError,
    GoalDoesNotExistError,
    tool,
)
from ...config.ctx import ElroyContext
from ...db.db_models import Goal
from ...utils.clock import get_utc_now, string_to_timedelta
from ...utils.utils import first_or_none, is_blank
from ..context_messages.data_models import ContextMessage
from ..context_messages.operations import (
    add_context_messages,
    drop_goal_from_current_context,
)
from ..recall.operations import (
    add_to_context,
    remove_from_context,
    upsert_embedding_if_needed,
)
from ..recall.transforms import to_recalled_memory_metadata
from .queries import get_active_goals, get_db_goal_by_name


@tool
def create_goal(
    ctx: ElroyContext,
    goal_name: str,
    strategy: Optional[str] = None,
    description: Optional[str] = None,
    end_condition: Optional[str] = None,
    time_to_completion: Optional[str] = None,
    priority: Optional[int] = None,
) -> str:
    """Creates a goal. The goal can be for the AI user, or for the assistant in relation to helping the user somehow.
    Goals should be *specific* and *measurable*. They should be based on the user's needs and desires, and should
    be achievable within a reasonable timeframe.

    Args:
        goal_name (str): Name of the goal
        strategy (str): The strategy to achieve the goal. Your strategy should detail either how you (the personal assistant) will achieve the goal, or how you will assist your user to solve the goal. Limit to 100 words.
        description (str): A brief description of the goal. Limit to 100 words.
        end_condition (str): The condition that indicate to you (the personal assistant) that the goal is achieved or terminated. It is critical that this end condition be OBSERVABLE BY YOU (the assistant). For example, the end_condition may be that you've asked the user about the goal status.
        time_to_completion (str): The amount of time from now until the goal can be completed. Should be in the form of NUMBER TIME_UNIT, where TIME_UNIT is one of HOURS, DAYS, WEEKS, MONTHS. For example, "1 DAYS" would be a goal that should be completed within 1 day.
        priority (int, optional): The priority of the goal, from 0-4. Priority 0 is the highest priority, and 4 is the lowest.

    Returns:
        str: A confirmation message that the goal was created.

    Raises:
        ValueError: If goal_name is empty
        GoalAlreadyExistsError: If a goal with the same name already exists
    """
    if is_blank(goal_name):
        raise ValueError("Goal name cannot be empty")

    existing_goal = ctx.db.exec(
        select(Goal).where(
            Goal.user_id == ctx.user_id,
            Goal.name == goal_name,
            Goal.is_active == True,
        )
    ).one_or_none()
    if existing_goal:
        raise GoalAlreadyExistsError(goal_name)
    else:
        goal = Goal(
            user_id=ctx.user_id,
            name=goal_name,
            description=description,
            strategy=strategy,
            end_condition=end_condition,
            priority=priority,
            target_completion_time=get_utc_now() + string_to_timedelta(time_to_completion) if time_to_completion else None,
        )  # type: ignore
        ctx.db.add(goal)
        ctx.db.commit()
        ctx.db.refresh(goal)

        add_context_messages(
            ctx,
            [
                ContextMessage(
                    role=SYSTEM,
                    content=f"New goal created: {goal.to_fact()}",
                    memory_metadata=[to_recalled_memory_metadata(goal)],
                    chat_model=ctx.chat_model.name,
                )
            ],
        )

        upsert_embedding_if_needed(ctx, goal)

        return f"Goal '{goal_name}' has been created."


@tool
def rename_goal(ctx: ElroyContext, old_goal_name: str, new_goal_name: str) -> str:
    """Renames an existing active goal.

    Args:
        old_goal_name (str): The current name of the goal
        new_goal_name (str): The new name for the goal

    Returns:
        str: A confirmation message that the goal was renamed

    Raises:
        GoalDoesNotExistError: If the goal with old_goal_name doesn't exist
        Exception: If a goal with new_goal_name already exists
    """
    # Check if the old goal exists and is active
    active_goals = get_active_goals(ctx)
    old_goal = pipe(
        active_goals,
        filter(lambda g: g.name == old_goal_name),
        first_or_none,
    )

    if not old_goal:
        raise Exception(
            f"Active goal '{old_goal_name}' not found for user {ctx.user_id}. Active goals: " + ", ".join([g.name for g in active_goals])
        )

    existing_goal_with_new_name = pipe(
        active_goals,
        filter(lambda g: g.name == new_goal_name),
        first_or_none,
    )

    assert isinstance(old_goal, Goal)

    if existing_goal_with_new_name:
        raise Exception(f"Active goal '{new_goal_name}' already exists for user {ctx.user_id}")

    # we need to drop the goal from context as the metadata includes the goal name.
    drop_goal_from_current_context(ctx, old_goal.name)

    # Rename the goal
    old_goal.name = new_goal_name
    old_goal.updated_at = get_utc_now()  # noqa F841

    ctx.db.commit()
    ctx.db.refresh(old_goal)

    upsert_embedding_if_needed(ctx, old_goal)

    add_context_messages(
        ctx,
        [
            ContextMessage(
                role=SYSTEM,
                content=f"Goal '{old_goal_name}' has been renamed to '{new_goal_name}': {old_goal.to_fact()}",
                memory_metadata=[to_recalled_memory_metadata(old_goal)],
                chat_model=ctx.chat_model.name,
            )
        ],
    )
    return f"Goal '{old_goal_name}' has been renamed to '{new_goal_name}'."


@tool
def add_goal_status_update(ctx: ElroyContext, goal_name: str, status_update_or_note: str) -> str:
    """Captures either a progress update or note relevant to the goal.

    Args:
        goal_name (str): Name of the goal
        status_update_or_note (str): A brief status update or note about either progress or learnings relevant to the goal. Limit to 100 words.

    Returns:
        str: Confirmation message that the status update was added.
    """
    logging.info(f"Updating goal {goal_name} for user {ctx.user_id}")
    _update_goal_status(ctx, goal_name, False, status_update_or_note)

    return f"Status update added to goal '{goal_name}'."


def create_onboarding_goal(ctx: ElroyContext, preferred_name: str) -> None:

    create_goal(
        ctx=ctx,
        goal_name=f"Introduce myself to {preferred_name}",
        description="Introduce myself - a few things that make me unique are my ability to form long term memories, and the ability to set and track goals.",
        strategy=f"After exchanging some pleasantries, tell {preferred_name} about my ability to form long term memories, including goals. Use function {add_goal_status_update.__name__} with any progress or learnings.",
        end_condition=f"{preferred_name} has been informed about my ability to track goals",
        priority=1,
        time_to_completion="1 HOUR",
    )


@tool
def mark_goal_completed(ctx: ElroyContext, goal_name: str, closing_comments: Optional[str] = None) -> str:
    """Marks a goal as completed, with closing comments.

    Args:
        goal_name (str): The name of the goal
        closing_comments (Optional[str]): Updated status with a short account of how the goal was completed and what was learned

    Returns:
        str: Confirmation message that the goal was marked as completed

    Raises:
        GoalDoesNotExistError: If the goal doesn't exist
    """
    _update_goal_status(
        ctx,
        goal_name,
        True,
        closing_comments,
    )

    return f"Goal '{goal_name}' has been marked as completed."


@tool
def delete_goal_permanently(ctx: ElroyContext, goal_name: str) -> str:
    """Permanently deletes a goal.

    Args:
        goal_name (str): The name of the goal to delete

    Returns:
        str: Confirmation message that the goal was deleted

    Raises:
        GoalDoesNotExistError: If the goal doesn't exist
    """

    _update_goal_status(
        ctx,
        goal_name,
        True,
        "Goal has been deleted",
    )

    return f"Goal '{goal_name}' has been deleted."


def _update_goal_status(ctx: ElroyContext, goal_name: str, is_terminal: bool, status: Optional[str]) -> None:
    from ..memories.operations import do_create_memory

    goal = get_db_goal_by_name(ctx, goal_name)

    if not goal:
        raise GoalDoesNotExistError(goal_name, [g.name for g in get_active_goals(ctx)])
    assert isinstance(goal, Goal)

    logging.info(f"Updating goal {goal_name} for user {ctx.user_id}")
    logging.info(f"Current status updates: {goal.status_updates}")

    # Get current status updates and append new one
    status_updates = goal.get_status_updates()
    if status:
        status_updates.append(status)
        goal.set_status_updates(status_updates)

    if is_terminal:
        goal.is_active = None
        remove_from_context(ctx, goal)
        do_create_memory(ctx, "Completed Goal: " + goal_name, goal.to_fact(), [goal], True)
    else:
        add_to_context(ctx, goal)

    logging.info(f"Updated status updates: {goal.status_updates}")

    ctx.db.commit()
    ctx.db.refresh(goal)

    upsert_embedding_if_needed(ctx, goal)
