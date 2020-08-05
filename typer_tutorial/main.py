import typer

app = typer.Typer()

@app.command()
def hello(name: str, last_name: str = '', formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        typer.echo(f'Good Day mr. {name} {last_name}')
    else:
        typer.echo(f'Hello {name} {last_name}')

@app.command()
def goodbye(name: str, last_name: str = '', formal: bool = False):
    """
    Say goodbye to NAME, optionally with a --lastname.

    If --formal is used, say goodbye very formally.
    """
    if formal:
        typer.echo(f'Goodbye mr. {name} {last_name}')
    else:
        typer.echo(f'See you {name} {last_name}')



if __name__ == '__main__':
    app()
