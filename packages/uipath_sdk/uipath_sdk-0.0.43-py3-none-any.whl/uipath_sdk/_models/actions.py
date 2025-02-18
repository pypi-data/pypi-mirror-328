from datetime import datetime
from typing import Any, Dict, List, Optional, TypedDict


class Action(TypedDict):
    task_definition_properties_id: Optional[int]
    app_tasks_metadata: Optional[Any]
    action_label: Optional[str]
    status: Optional[str]
    data: Optional[Dict[str, Any]]
    action: Optional[str]
    wait_job_state: Optional[str]
    organization_unit_fully_qualified_name: Optional[str]
    tags: Optional[List[Any]]
    assigned_to_user: Optional[Any]
    task_sla_details: Optional[List[Any]]
    completed_by_user: Optional[Any]
    task_assignment_criteria: Optional[str]
    task_assignees: Optional[List[Any]]
    title: Optional[str]
    type: Optional[str]
    priority: Optional[str]
    assigned_to_user_id: Optional[int]
    organization_unit_id: Optional[int]
    external_tag: Optional[str]
    creator_job_key: Optional[str]
    wait_job_key: Optional[str]
    last_assigned_time: Optional[datetime]
    completion_time: Optional[datetime]
    parent_operation_id: Optional[str]
    key: Optional[str]
    is_deleted: Optional[bool]
    deleter_user_id: Optional[int]
    deletion_time: Optional[datetime]
    last_modification_time: Optional[datetime]
    last_modifier_user_id: Optional[int]
    creation_time: Optional[datetime]
    creator_user_id: Optional[int]
    id: Optional[int]
