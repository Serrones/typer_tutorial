# typer_tutorial
First Typer experiments


## references

[Typer](https://typer.tiangolo.com/features/)

[Typer first steps](https://typer.tiangolo.com/tutorial/first-steps/)


## how to use

- build a docker image from Dockerfile `docker build -t <image_name> .`

- run a container from the builded image `docker run -it --rm --name typer_1 <image_name> bash`

## commands

- help `python typer_tutorial/main.py --help`

- hi `python typer_tutorial/main.py <name>`

- formal hi `python typer_tutorial/main.py <name> --formal`

- hi with lastname `python typer_tutorial/main.py <name> --last-name <lastname>`

- formal hi with lastname `python typer_tutorial/main.py <name> --last-name <lastname> --formal`