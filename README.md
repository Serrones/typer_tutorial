# typer_tutorial
First Typer experiments


## references

[Typer](https://typer.tiangolo.com/features/)

[Typer first steps](https://typer.tiangolo.com/tutorial/first-steps/)


## how to use

- build a docker image from Dockerfile `docker build -t <image_name> .`

- run a container from the builded image `docker run -it --rm --name typer_1 <image_name> bash`

## commands

- help `typer --help`

- hi `typer hello <name>`

- formal hi `typer hello <name> --formal`

- hi with lastname `typer hello <name> --last-name <lastname>`

- formal hi with lastname `typer hello <name> --last-name <lastname> --formal`

- goodbye `typer goodbye <name>`

- formal goodbye `typer goodbye <name> --formal`

- goodbye with lastname `typer goodbye <name> --last-name <lastname>`

- formal goodbye with lastname `typer goodbye <name> --last-name <lastname> --formal`