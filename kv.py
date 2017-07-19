import click
import json
import os


class PairsCollection:
    def __init__(self):
        self.pairs = {}

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, key):
        return self.pairs[key]

    def __setitem__(self, key, value):
        self.pairs[key] = value

    def __delitem__(self, key):
        del self.pairs[key]

    def __iter__(self):
        return iter(self.pairs)

    def items(self):
        return iter(self.pairs.items())

    @property
    def file_path(self):
        if not hasattr(self, '_file_path'):
            dir = os.getenv('XDG_DATA_HOME')
            if dir is not None:
                self._file_path = os.path.join(dir, 'kv.json')
            else:
                home = os.getenv('HOME')
                self._file_path = os.path.join(home, '.kv.json')

        return self._file_path

    def load(self):
        try:
            with open(self.file_path) as f:
                self.pairs = json.load(f)
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.pairs, f)


pairs = PairsCollection()


@click.group()
def cli():
    pairs.load()


@cli.command()
@click.argument('key')
@click.argument('value')
def set(key, value):
    """Set a value for a key."""
    if key in pairs:
        prev = pairs[key]

        try:
            msg = 'Key "{k}" already exists with value "{v}". Overwrite?'
            if not click.confirm(msg.format(k=key, v=prev)):
                raise Exception(f'Key "{key}" not changed.')
        except click.exceptions.Abort:
            click.echo('')
            raise Exception(f'Key "{key}" not changed.')

    pairs[key] = value
    pairs.save()
    click.echo(f'Key "{key}" set to value "{value}".')


@cli.command()
@click.argument('key')
def get(key):
    """Get the value for a given key."""
    try:
        click.echo(pairs[key])
    except KeyError:
        raise KeyError(f'Key "{key}" not found.')


@cli.command()
@click.argument('keys', nargs=-1)
def delete(keys):
    """Deletes key:value pairs."""
    try:
        for key in keys:
            del pairs[key]
            click.echo(f'Deleted key "{key}".')
        pairs.save()
    except KeyError:
        raise KeyError(f'Key "{key}" not found.')


@cli.command()
def list():
    """List all key:value pairs."""
    if len(pairs) == 0:
        click.echo('No keys found.')
        return

    for k, v in sorted(pairs.items(), key=lambda x: x[0]):
        click.echo(f'{k} -> {v}')


if __name__ == '__main__':
    try:
        cli()
    except Exception as e:
        click.echo(str(e))
