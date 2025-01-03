from enum import Enum

class ActionType(str, Enum):
    DOWNLOAD = "DOWNLOAD"
    UPLOAD = "UPLOAD"
    CREATE = "CREATE"
    EDIT = "EDIT"
    DELETE = "DELETE"
    SEARCH = "SEARCH"
    ADD = "ADD" # when a record is added to a project