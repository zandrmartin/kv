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
      delete  Deletes key:value pairs.
      get     Get the value for a given key.
      list    List all key:value pairs.
      set     Set a value for a key.


## License

BSD 2-clause
