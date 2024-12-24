from enum import Enum

class ProjectStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ONHOLD = "ONHOLD"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
    BLOCKED = "BLOCKED"