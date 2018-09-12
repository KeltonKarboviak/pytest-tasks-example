# -*- coding: utf-8 -*-

"""Minimal Project Task Management."""

from .api import (
    Task,
    TasksException,
    add,
    get,
    list_tasks,
    count,
    update,
    delete,
    delete_all,
    unique_id,
    start_tasks_db,
    stop_tasks_db,
)