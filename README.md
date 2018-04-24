# RAMP kit boilerplate

This is the official RAMP kit boilerplate using [`cookiecutter`][cc] to help you setup a kit for your project.

## Initializing a new kit

1. install [`cookiecutter`][cc] a Python library for project templates
  ```bash
  pip install cookiecutter
  ```
  or [alternative methods][ccinstall].

2. run the following command and follow the instructions in your terminal
  ```bash
  cookiecutter gh:ramp-kits/cookiecutter-ramp-kit
  ```

You'll be prompted for:
- your name
- your email address (best is the one used with `git`)
- a GitHub username (yours if you want to keep it private, otherwise leave the default one `ramp-kits`)
- the project name (spaces can be used)
- the project slug = directory name of GitHub (must be concise and use **underscore for spacing**)
- a short project description
- the main task of your project
- the type of input data
- the choice of an open source license (or not)

**This information will be used to set up the project (inner text and links)  will not be collected or tracked**


[ccinstall]: https://cookiecutter.readthedocs.io/en/latest/installation.html
[cc]: https://github.com/audreyr/cookiecutter
