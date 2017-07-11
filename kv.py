import click
import json
import os


items = {}


def get_file_path():
    dir = os.getenv('XDG_DATA_HOME')
    if dir is not None:
        file = os.path.join(dir, 'kv.json')
    else:
        home = os.getenv('HOME')
        file = os.path.join(home, '.kv.json')

    return file


def load_items():
    global items
    try:
        with open(get_file_path()) as f:
            items = json.load(f)
    except FileNotFoundError:
        pass


def save_items():
    global items
    with open(get_file_path(), 'w') as f:
        json.dump(items, f)


@click.group()
def cli():
    load_items()


@cli.command()
@click.argument('key')
@click.argument('value')
def add(key, value):
    """Add a new key:value pair."""
    if key in items:
        raise KeyError(f'Key "{key}" already exists.')

    items[key] = value
    click.echo(f'Added key "{key}" with value "{value}".')
    save_items()


@cli.command()
@click.argument('key')
def get(key):
    """Get the value for a given key."""
    try:
        click.echo(items[key])
    except KeyError:
        raise KeyError(f'Key "{key}" not found.')


@cli.command()
@click.argument('key')
def delete(key):
    """Delete a key:value pair."""
    try:
        del items[key]
        save_items()
        click.echo(f'Deleted key "{key}".')
    except KeyError:
        raise KeyError(f'Key "{key}" not found.')


@cli.command()
@click.argument('key')
@click.argument('value')
def change(key, value):
    """Change the value of an existing key."""
    if key not in items:
        raise KeyError(f'Key "{key}" not found.')

    prev = items[key]
    items[key] = value
    click.echo(f'Changed value of key "{key}" from "{prev}" to "{value}".')
    save_items()


@cli.command()
def list():
    """List all key:value pairs."""
    if len(items) == 0:
        click.echo('No items found.')
        return

    for k, v in sorted(items.items(), key=lambda x: x[0]):
        click.echo(f'{k} -> {v}')


if __name__ == '__main__':
    try:
        cli()
    except Exception as e:
        click.echo(e)
