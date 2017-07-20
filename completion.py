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
@click.argument('args', nargs=-1)
def complete(cmd, args):
    cmds = [k for k in kv.cli.commands if k not in ('set', 'list')]

    if cmd not in cmds:
        return

    if cmd != 'delete' and len(args) == 1:
        return

    kv.pairs.load()
    for k, v in sorted(kv.pairs.items(), key=lambda x: x[0]):
        if k not in args:
            click.echo(f'{k}:{v}')


if __name__ == '__main__':
    try:
        completion()
    except:
        pass
