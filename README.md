# kv

A simple CLI key:value store.

## Setup

1. `pip install -r requirements.txt`
2. `alias kv='python3 kv.py'`
3. `fpath=(/path/to/kv $fpath)` to set up zsh tab-completion. (optional)

## Usage

    Usage: kv.py [OPTIONS] COMMAND [ARGS]...

    Options:
    --help  Show this message and exit.

    Commands:
    add     Add a new key:value pair.
    change  Change the value of an existing key.
    delete  Delete a key:value pair.
    get     Get the value for a given key.
    list    List all key:value pairs.


## License

BSD 2-clause
