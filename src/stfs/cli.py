import argparse

from .package import Package


def cmd_info(args):

    pkg = Package.open(args.file)

    print(f"Arquivo      : {pkg.path}")
    print(f"Tipo         : {pkg.header.package_type.value}")
    print(f"Title ID     : {pkg.header.title_id:08X}")
    print(f"Display Name : {pkg.header.display_name}")


def main():

    parser = argparse.ArgumentParser("stfs")

    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("info")

    p.add_argument("file")

    p.set_defaults(func=cmd_info)

    args = parser.parse_args()

    args.func(args)
