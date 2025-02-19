import inspect
from pathlib import Path

from django.db.migrations import RunSQL


def get_sql_migration_operations(path: Path|str|None = None, vars: dict = None) -> list[RunSQL]:
    def get_ordered_files(directory: Path|str, *, ext: str = None, recursive: bool = False) -> list[Path]:
        if not isinstance(directory, Path):
            directory = Path(directory)

        if ext and not ext.startswith('.'):
            ext = f'.{ext}'

        def generate(directory: Path):
            for path in sorted(directory.iterdir(), key=lambda entry: (0 if entry.is_dir() else 1, entry.name)):
                if path.is_dir():
                    if recursive:
                        yield from generate(path)
                elif not ext or path.name.lower().endswith(ext):
                    yield path

        return [ path for path in generate(directory) ]

    def get_sql_and_reverse_sql(file: Path|str):
        sql = None
        reverse_sql = None

        with open(file, 'r', encoding='utf-8') as fp:
            while True:
                line = fp.readline()
                if not line:
                    break
                if vars:
                    for name, value in vars.items():
                        line = line.replace("{"+name+"}", value)

                if reverse_sql is None:
                    # search !reverse mark
                    stripped_line = line = line.strip()
                    if stripped_line.startswith('--') and stripped_line.lstrip(' -\t').startswith('!reverse'):
                        reverse_sql = line
                    else:
                        sql = (sql + '\n' if sql else '') + line
                else:
                    reverse_sql += '\n' + line

        return sql, reverse_sql

    if path is None:
        calling_module = inspect.getmodule(inspect.stack()[1][0])
        calling_file = Path(calling_module.__file__)
        path = calling_file.parent.joinpath(calling_file.stem).with_suffix('.sql')
        if not path.exists():
            path = calling_file.parent.joinpath(calling_file.stem).with_suffix('')
    elif isinstance(path, str) and path.startswith('sqlutils:'):
        scheme = path[len('sqlutils:'):]
        path = Path(__file__).resolve().parent.parent.joinpath('db', 'sqlutils', f'{scheme}.sql')

    if path.is_file():
        sql, reverse_sql = get_sql_and_reverse_sql(path)
        return [RunSQL(sql, reverse_sql)]
    elif path.is_dir():
        operations = []

        for path in get_ordered_files(path, ext='.sql', recursive=True):
            sql, reverse_sql = get_sql_and_reverse_sql(path)
            operations.append(RunSQL(sql, reverse_sql))

        return operations
    else:
        raise ValueError(f"Migration path not found: {path}")
