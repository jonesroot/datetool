#!/usr/bin/env python3

from typing import Optional
from datetime import datetime, timedelta
from pytz import timezone
from jsonargparse import ArgumentParser


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"


clr = Colors()


def usage_display():
    print(f"""{clr.CYAN}Example:

{clr.CYAN}Command: {clr.BOLD}{clr.GREEN}datetools apply -d 01.01.2024 -t 01.03.2024{clr.RESET}
{clr.CYAN}Description: {clr.BOLD}{clr.YELLOW}Gap between those dates will be shown.{clr.RESET}
""")


def date_tools(
    date: Optional[str] = None,
    target: Optional[str] = None,
    week: Optional[int] = None,
    add: Optional[int] = None,
):
    if date:
        base_date = datetime.strptime(date, "%d.%m.%Y")
        if target:
            target_date = datetime.strptime(target, "%d.%m.%Y")
            delta = target_date - base_date
            print(f"Gap: {delta.days // 7} weeks, {delta.days % 7} days.")
        if week or add:
            result_date = base_date + timedelta(weeks=week or 0, days=add or 0)
            print(f"New date: {result_date.strftime('%d.%m.%Y')}")


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="datetools", description="DateTools CLI Utility.")
    sub = parser.add_subcommands()
    sub.add_function("apply", date_tools, help="Date calculation tools")
    return parser


def main():
    parser = get_parser()
    parser.cli()


if __name__ == "__main__":
    main()
