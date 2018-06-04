{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
[![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?branch=master)][travis]
{%- endif %}

_Authors: {{ cookiecutter.full_name }}_

{{ cookiecutter.project_short_description }}

## Set up

1. clone this repository
  ```
  git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
  cd {{ cookiecutter.project_slug }}
  ```

2. install the dependancies
  - with [conda](https://conda.io/miniconda.html)
  ```
  conda install -y -c conda conda-env     # First install conda-env
  conda env create                        # Use environment.yml to create the 'astrophd_tutorial' env
  source activate {{ cookiecutter.project_slug }}       # Activates the virtual env
  ```
  - without `conda` (best to use a **virtual environment**)
  ```
  python -m pip install -r requirements.txt
  ```

3. download the data
  ```
  python download_data.py        # quick-test data for testing ~16Mo
  ```

4. get started with the [dedicated notebook]({{ cookiecutter.project_slug }}_starting_kit.ipynb).

## New submissions

1. create a new submission "<new_sub>" by building on the existing ones
  ```
  cp -r submissions/starting_kit submissions/<new_sub>
  ```
2. modify the `*.py` files in  `submissions/<new_sub>` with your favorite editor

3. test the submission with
  ```
  ramp_test_submission --quick-test --submission <new_sub>
  ```
4. if the job complete, you can submit the code in the sandbox of [ramp.studio][ramp]


{% if is_open_source %}
## License

{{ cookiecutter.open_source_license }} : see [LICENSE file](LICENSE)
{% endif %}

## Credits

This package was created with [Cookiecutter][cookie] and the [`ramp-kits/cookiecutter-ramp-kit`][kit] project template
issued by the [Paris-Saclay Center for Data Science][cds].

[travis]: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
[ramp]: https://ramp.studio/events/{{ cookiecutter.project_slug }}
[cookie]: https://github.com/audreyr/cookiecutter
[kit]: https://github.com/ramp-kits/cookiecutter-ramp-kit
[cds]: https://www.datascience-paris-saclay.fr/
