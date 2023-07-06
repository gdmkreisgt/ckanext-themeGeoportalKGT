import click


@click.group(short_help="themegeoportalkgt CLI.")
def themegeoportalkgt():
    """themegeoportalkgt CLI.
    """
    pass


@themegeoportalkgt.command()
@click.argument("name", default="themegeoportalkgt")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [themegeoportalkgt]
