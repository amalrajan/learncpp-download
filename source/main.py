import argparse

import ray

from helper import render


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--weasy', action='store_true'
    )

    return parser.parse_args()


ray.init()
if not argument_parser().weasy:
    instance = render.WkRender()
else:
    instance = render.WeasyRender()

if __name__ == '__main__':
    instance.download()
