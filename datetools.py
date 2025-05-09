import sys
import os
import time
import subprocess
from typing import Optional
from datetime import datetime, timedelta
from jsonargparse import ArgumentParser


VERSION = "0.1.1"
REPO_URL = "https://raw.githubusercontent.com/jonesroot/datetool/refs/heads/main/datetools.py"


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"


clr = Colors()


def usage_display() -> str:
    return f"""{clr.CYAN}Example:

{clr.CYAN}Command: {clr.BOLD}{clr.GREEN}datetools apply -d 01.01.2024 -t 01.03.2024{clr.RESET}
{clr.CYAN}Description: {clr.BOLD}{clr.YELLOW}Gap between those dates will be shown.{clr.RESET}
"""


def check_update() -> None:
    print(f"{clr.CYAN}Checking for updates...{clr.RESET}")
    time.sleep(1)
    tmp_file = "/tmp/datetools_new"

    try:
        subprocess.run(
            [
                "curl",
                "-s",
                "-o",
                tmp_file,
                REPO_URL
            ],
            check=True
        )
        
        with open(tmp_file, "rb") as new_file, open(sys.argv[0], "rb") as old_file:
            if new_file.read() == old_file.read():
                print(f"{clr.GREEN}You're already using the latest version.{clr.RESET}")
                return

        os.replace(tmp_file, sys.argv[0])
        print(f"{clr.GREEN}Updated to latest version! Restarting in 3 seconds...{clr.RESET}")
        time.sleep(3)
        os.execv(sys.executable, [sys.executable] + sys.argv)

    except Exception as e:
        print(f"{clr.YELLOW}Failed to update: {e}{clr.RESET}")
        if os.path.exists(tmp_file):
            os.remove(tmp_file)


def date_tools(
    date: Optional[str] = None,
    target: Optional[str] = None,
    week: Optional[int] = 0,
    add: Optional[int] = 0,
) -> None:
    if date:
        base_date = datetime.strptime(date, "%d.%m.%Y")
        if target:
            target_date = datetime.strptime(target, "%d.%m.%Y")
            delta = target_date - base_date
            print(f"Gap: {delta.days // 7} weeks, {delta.days % 7} days.")
            return
        if week or add:
            result_date = base_date + timedelta(weeks=week or 0, days=add or 0)
            print(f"New date: {result_date.strftime('%d.%m.%Y')}")
            return


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="datetools", description="DateTools CLI Utility.")

    apply_parser = ArgumentParser(description="Date calculation tools")
    apply_parser.add_argument("-d", "--date", type=str, help="Base date")
    apply_parser.add_argument("-t", "--target", type=str, help="Target date")
    apply_parser.add_argument("-w", "--week", type=int, default=0, help="Weeks to add")
    apply_parser.add_argument("-a", "--add", type=int, default=0, help="Days to add")

    subcommands = parser.add_subcommands()
    subcommands.add_subcommand("apply", apply_parser, func=date_tools)

    return parser


def main() -> None:
    parser = get_parser()
    parser.parse_args()


if __name__ == "__main__":
    main()
