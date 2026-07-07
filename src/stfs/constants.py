from enum import Enum


class PackageType(str, Enum):
    CON = "CON "
    LIVE = "LIVE"
    PIRS = "PIRS"
