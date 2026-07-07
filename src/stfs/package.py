from pathlib import Path

from .constants import PackageType
from .exceptions import InvalidPackageError
from .header import Header


class Package:

    def __init__(self, path: Path, header: Header):
        self.path = path
        self.header = header

    @classmethod
    def open(cls, filename: str | Path):

        path = Path(filename)

        with path.open("rb") as fp:

            magic = fp.read(4).decode("ascii", errors="ignore")

            try:
                package_type = PackageType(magic)
            except ValueError:
                raise InvalidPackageError(
                    f"{path} não é um pacote STFS válido."
                )

            #
            # Title ID
            # Offset 0x360
            #

            fp.seek(0x360)
            title_id = int.from_bytes(fp.read(4), "big")

            #
            # Display Name
            #
            # Primeiro slot em UTF-16BE
            # Offset 0x411
            # Tamanho 0x80 bytes
            #

            fp.seek(0x411)

            raw = fp.read(0x80)

            display_name = (
                raw.decode("utf-16-be", errors="ignore")
                .split("\x00")[0]
                .strip()
            )

        header = Header(
            package_type=package_type,
            title_id=title_id,
            display_name=display_name,
        )

        return cls(path, header)
