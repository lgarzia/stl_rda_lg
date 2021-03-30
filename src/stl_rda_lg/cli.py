import typer

app = typer.Typer()


@app.callback()  ##not sure what this does yet
def callback():
    """
    Package built to explore STL Data Region Alliance Data
    """


@app.command()
def run():
    import streamlit.cli as stcli
    import sys
    import os

    fdir = os.path.dirname(__file__)
    fpath = os.path.join(fdir, "strlit", "main.py")
    """ Calls the streamlit application"""
    typer.echo("test command")
    sys.argv = ["streamlit", "run", fpath]
    typer.echo(fpath)
    sys.exit(stcli.main())


@app.command
def download():
    # idea is to download data

    pass
