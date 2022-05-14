import argparse
import ray
from helper import render


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--wkhtmltopdf', action='store_true'
    )

    return parser.parse_args()


if argument_parser().wkhtmltopdf:
    ray.init()
    wk_render = render.WkRender()
    wk_render.download()
