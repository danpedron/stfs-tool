from pathlib import Path

from rich import print

from stfs.package import Package


def human_size(size):

    for unit in ("B", "KiB", "MiB", "GiB"):

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} TiB"


def info(filename: Path):

    pkg = Package(filename)

    print(f"[cyan]File[/cyan]         : {pkg.path}")
    print(f"[cyan]Size[/cyan]         : {human_size(pkg.size)}")

    sig = pkg.signature

    if sig in ("LIVE", "PIRS", "CON "):
        print(f"[green]Package Type[/green] : {sig}")
        print("[green]Signature[/green]    : OK")
    else:
        print(f"[red]Unknown signature[/red] : {sig!r}")
