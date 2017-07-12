import click
import kv


@click.group()
def completion():
    pass


@completion.command()
def list_commands():
    for c in kv.cli.commands.values():
        click.echo(f'{c.name}:{c.help}')


@completion.command()
@click.argument('cmd')
def list_keys(cmd):
    if cmd in ['add', 'list']:
        return
    else:
        kv.load_items()
        for k, v in sorted(kv.items.items(), key=lambda x: x[0]):
            click.echo(f'{k}:{v}')


if __name__ == '__main__':
    try:
        completion()
    except:
        pass
