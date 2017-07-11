import click
import kv


@click.group()
def completion():
    pass


@completion.command()
def list_commands():
    for cmd in kv.cli.commands.values():
        click.echo(f'{cmd.name}:{cmd.help}')


if __name__ == '__main__':
    try:
        completion()
    except:
        pass
