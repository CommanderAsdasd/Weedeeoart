#!/usr/bin/env python

import click
import preset as prst
import weedeeoGui as Gui

@click.group()
def cli():
    pass

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)

@click.command()
# @click.option('--count', default=1, help='number of greetings')
# @click.argument('name')
def gui():
    WeedeeoGui = Gui.GUI()


@click.command()
@click.option('--count', default=1, help='number of runs')
@click.argument('path')
def preset(path, count):
    prst.preset_manager(path, count)

cli.add_command(preset)
cli.add_command(gui)


if __name__ == '__main__':
    cli()