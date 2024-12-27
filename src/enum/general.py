from enum import Enum

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    DEVELOPER = "DEVELOPER"
    TESTER = "TESTER"
    MANAGER = "MANAGER"

class AddressType(str, Enum):
    ADBOR = "ADBOR"
    SBMASTER = "SBMASTER"
    LGAMASTER = "LGAMASTER"
    STATEMASTER = "STATEMASTER"
    POSTCODEMASTER = "POSTCODEMASTER"