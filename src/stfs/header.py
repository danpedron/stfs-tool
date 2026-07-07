from dataclasses import dataclass

from .constants import PackageType


@dataclass(slots=True)
class Header:
    package_type: PackageType
    title_id: int
    display_name: str
