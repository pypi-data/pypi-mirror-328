import sys
from quickmlops.build import build
from quickmlops.config_help import conf


def main(args: list) -> None:
    if len(args) < 2:
        print("Welcome to quickMLOPS")
        print(
            """Use one of the following commands to get started:\n\t- build\n\t- list (alias ls)"""
        )
        return

    if args[1] == "build":
        build(args)
        return

    if args[1] == "config":
        conf(args)
        return

    print(f"Arg: {args[1]} not valid.")


if __name__ == "__main__":
    args = sys.argv
    main(args)
