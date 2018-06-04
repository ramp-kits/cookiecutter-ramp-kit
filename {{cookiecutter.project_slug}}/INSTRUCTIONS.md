Instructions for setting up a RAMP kit
======================================

**Hi, thank you for using RAMP !**

_Please find below personalised instructions (based on your choices) to guide you through the setup of a RAMP kit._

To get an interactive version of these instructions, use [`pandoc`][pandoc] to convert this document to HTML
```
pandoc --to html INSTRUCTIONS.md > INSTRUCTIONS.html
```

---

You have freshly started a RAMP kit project entitled `{{cookiecutter.project_slug}}`.

The structure of the project should be (with minor differences depending on your choices).

```
{{cookiecutter.project_slug}}/
├── .editorconfig
├── .gitignore
├── .travis.yml
├── INSTRUCTIONS.md
├── LICENSE
├── README.md
├── download_data.py
├── environment.yml
├── problem.py
├── {{cookiecutter.project_slug}}_starting_kit.ipynb
└── requirements.txt
```


Setup checklist
---------------

1. [git(hub)](#1.-Version-the-project)
2. [`.environment.yml` & `requirements.txt`](#2.-Install-dependencies)
3. [`problem.py`](#3.-Fill-in-the-`problem.py`)
4. [`submissions/starting_kit`](#4.-Write-a-`starting_kit`-submission)
5. [`download_data.py`](#5.-Create-the-`download_data.py`-script)
6. [`{{cookiecutter.project_slug}}_starting_kit.ipynb`](#6.-Modify-the-notebook)
7. [`.travis.yml`](#7.-Activate-continuous-integration-for-the-kit)


### 1. Version the project

- go to [`https://github.com/{{cookiecutter.github_username}}/new`][newrepo]   
  to create a new **empty** repository called `{{cookiecutter.project_slug}}`.

- commit the project
  ```
  cd {{cookiecutter.project_slug}}
  git init
  git remote add origin https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
  git add .   # thanks to the .gitignore, the INSTRUCTIONS will not be versioned
  git commit -m "Initial commit"
  git push -u origin master
  ```

### 2. Install dependencies

- with [conda][miniconda] => `environment.yml`
  ```
  conda env create -f environment.yml     # use environment.yml to create the '{{cookiecutter.project_slug}}' env
  source activate {{cookiecutter.project_slug}}     # activate the virtual env
  ```
- without `conda` => `requirements.txt` (best to use a **virtual environment**)
  ```
  python -m pip install -r requirements.txt
  ```

This will install the [`ramp-workflow`][rampwf] library as well as commonly used Python libraries.

### 3. Fill in the `problem.py`

TBD

#### List of existing ramp-kits related to your problem

TBD


### 4. Write a `starting_kit` submission

TBD

### 5. Create the `download_data.py` script

TBD

### 6. Modify the notebook

The starting kit [notebook]({{cookiecutter.project_slug}}_starting_kit.ipynb) should detail step-by-step the scientific context, the motivations for the project, the challenge workflow and metrics and the instructions for the participants to submit their contributions.

The notebook present in the base directory `{{cookiecutter.project_slug}}_starting_kit.ipynb` is a copy of the one used for the [Mars crater detection kit][mars] so you can start with a model and reuse the technical parts.

**Best practice**: put the notebook images in a separate directory `{{cookiecutter.project_slug}}/img` and link them from the notebook.

### 7. Activate continuous-integration for the kit

The project already contains a list of instructions for setting up the continuous integration with [Travis][travis].
This is a way to ensure the whole workflow can run from one end to another without a flaw on a neutral machine.

To enable these builds, follow the instructions [here][travisinstr].

When you commit a modification to your project, Travis will then

- spawn a kernel
- install [Miniconda][miniconda]
- install the Python dependencies (among which `ramp-workflow`)
- clone this very project
- download the data
- run `ramp_test_submission` on the `starting_kit` submission

On top of the [README.md][readme] file, a small badge will let you know if the build passed (green) or failed (red)
and if it failed, you will have access to the terminal output by clicking on it.


[pandoc]: http://pandoc.org/installing.html
[newrepo]: https://github.com/{{cookiecutter.github_username}}/new
[miniconda]: https://conda.io/miniconda.html
[rampwf]: https://github.com/paris-saclay-cds/ramp-workflow
[cookie]: https://github.com/audreyr/cookiecutter
[mars]: https://github.com/ramp-kits/mars_craters
[travis]: https://travis-ci.org/
[travisinstr]: https://docs.travis-ci.com/user/getting-started/#To-get-started-with-Travis-CI
[readme]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
