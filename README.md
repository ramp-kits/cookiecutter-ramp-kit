# RAMP kit boilerplate

This is the official RAMP kit boilerplate to help you setup a kit for your project.

## Initializing a new kit

1. install [`cookiecutter`][cc], a Python library for project templates
  ```bash
  pip install cookiecutter
  ```
  or use [alternative methods][ccinstall].

2. run the following command and follow the terminal instructions
  ```bash
  cookiecutter gh:ramp-kits/cookiecutter-ramp-kit
  ```
  Additional information on the prompted variables can be found [here](#Template-variables).

## Getting the instructions

You'll find a `INSTRUCTIONS.md` file at the base of the repo, with a checklist of items to complete the setup of your RAMP kit.
This file has been specifically tuned given the task and type of input data you specified for your project, especially links to [existing RAMP kits][kits] with related problems and from which you will be able to take inspiration to finalize yours.

## Template variables

During the set up of the template, you'll be prompted for
- your name
- your email address (best is the one used with `git`)
- a GitHub username (yours if you want to keep it private, otherwise leave the default one `ramp-kits`)
- the project name (spaces can be used)
- the project slug = directory name of GitHub (must be concise and use **underscore for spacing**)
- a short project description
- the main task of your project
- the type of input data
- the choice of an open source license (or not)

This information will be used to **set up the project** (inner text and links) but will **neither be collected nor tracked**.

## Acknowledgements

Powered by [`cookiecutter`][cc]

[cc]: https://github.com/audreyr/cookiecutter
[ccinstall]: https://cookiecutter.readthedocs.io/en/latest/installation.html
[kits]: https://github.com/ramp-kits
