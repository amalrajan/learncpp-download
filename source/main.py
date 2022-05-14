import argparse
import logging

import ray

from helper import render


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--weasy', action='store_true'
    )

    return parser.parse_args()


if not argument_parser().weasy:
    ray.init()
    instance = render.WkRender()
else:
    logging.info('Downloading with weasyprint')
    instance = render.WeasyRender()

if __name__ == '__main__':
    instance.download()
