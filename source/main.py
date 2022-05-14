import argparse

import ray

from helper import render


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--weasy', action='store_true'
    )
    parser.add_argument(
        '--pisa', action='store_true'
    )
    parser.add_argument(
        '--sequential', action='store_true'
    )

    return parser.parse_args()


ray.init(log_to_driver=False)
args = argument_parser()

if args.weasy:
    instance = render.WeasyRender()
elif args.pisa:
    instance = render.PisaRender()
else:
    instance = render.WkRender(sequential=args.sequential)

if __name__ == '__main__':
    instance.download()
