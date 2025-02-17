from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    TESTER = "tester"

# class PermissionType(str, Enum):
#     READ = "read"
#     CREATE = "create"   
#     DELETE = "delete"

class AddressType(str, Enum):
    ADBOR = "ADBOR"
    SBMASTER = "SBMASTER"
    LGAMASTER = "LGAMASTER"
    STATEMASTER = "STATEMASTER"
    POSTCODEMASTER = "POSTCODEMASTER"