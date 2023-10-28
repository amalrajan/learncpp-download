import argparse
import logging

from helper import render


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--weasy", action="store_true")
    parser.add_argument("--pisa", action="store_true")
    parser.add_argument("--sequential", action="store_true")

    return parser.parse_args()


args = argument_parser()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)


if args.weasy:
    instance = render.WeasyRender()
elif args.pisa:
    instance = render.PisaRender()
else:
    instance = render.WkRender(sequential=args.sequential)

if __name__ == "__main__":
    instance.download()
