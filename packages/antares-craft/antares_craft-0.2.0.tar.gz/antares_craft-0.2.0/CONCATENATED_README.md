# antares_craft
[![github ci](https://github.com/AntaresSimulatorTeam/antares_craft/actions/workflows/ci.yml/badge.svg)](https://github.com/AntaresSimulatorTeam/antares_craft/actions/workflows/ci.yml)

## about

Antares Craft python library is currently under construction. When completed it will allow to create, update and read 
antares studies.

This project only supports antares studies with a version v8.8 or higher.



# Introduction

With antares-craft you can interact with studies using AntaresWeb API or in local mode.
To interact with AntaresWeb you need a token.

## AntaresWeb

### How to create a study

```
api_config = APIconf(api_host=antares_web.url, token=your_token, verify=False)
study = create_study_api("antares-craft-test", "880", api_config)
```

### How to point to an existing study

Not handled yet

## LOCAL

### How to create a study

    study = create_study_local("your_name", 880, {"local_path": "your_path", "study_name": "your_name"})

### How to point to an existing study

`study = read_study_local(study_path)`

## Apart from that every operation is the same no matter the environment you're targetting.

### How to create an area with given properties:

```
area_properties = AreaProperties(energy_cost_unsupplied=10)
study.create_area("fr", area_properties)
```

### How to access study areas

```
area_list = study.read_areas()
```

### install dev requirements

Install dev requirements with `pip install -r requirements-dev.txt`

### linting and formatting

To reformat your code, use this command line: `ruff check src/ tests/ --fix && ruff format src/ tests/`

### typechecking

To typecheck your code, use this command line: `mypy`

### integration testing

To launch integration tests you'll need an AntaresWebDesktop instance on your local env (since v0.2.0, use at least the **v.2.19.0**)  
To install it, download it from the last [Antares Web release](https://github.com/AntaresSimulatorTeam/AntaREST/releases) 
(inside the assets list).  
Then, unzip it at the root of this repository and rename the folder `AntaresWebDesktop`.  
*NB*: The expected folder structure is the following: `antares_craft/AntaresWebDesktop/config.yaml`

### tox
To use [tox](https://tox.wiki/) to run unit tests in multiple python versions at the same time as linting and formatting
with ruff and typing with mypy:  
1) As the dev requirements include [uv](https://docs.astral.sh/uv/) and `tox-uv` there is no need to install python 
versions, `uv` will do this for you.  
2) Use `tox -p` to run the environments in parallel to save time, this will create virtual environment with the 
necessary python versions the first time you run tox.

### mkdocs
Smallest beginning of `mkdocs` included more as proof of concept than anything, theme and logo copied from [Antares 
Simulator](https://github.com/AntaresSimulatorTeam/Antares_Simulator).  
1) To preview the docs on your local machine run `mkdocs serve`.  
2) To build the static site for publishing for example on [Read the Docs](https://readthedocs.io) use `mkdocs build`.
3) To flesh out the documentation see [mkdoc guides](https://www.mkdocs.org/user-guide/).


v0.2.0 (2025-02-20)
-------------------

### Compatiblity with AntaresWeb
This version is only compatible with AntaresWeb v2.19.0 and higher

### Breaking changes
- It is no longer possible to create a study while giving settings. The user will have to update them afterward.
- All user classes are now dataclasses and not Pydantic model.
- All user class (except for update) have no optional fields meaning it will be clearer for the users to see what they are really sending.
It will also silent typing issues inside user scripts
- New classes have been introduced for update. They are all optional which makes it also clear to understand which fields are updated.
- STStorage methods for updating matrices have been renamed `update_xxx` instead of `upload_xxx`.

Example of an old code:
```python
import AreaProperties

area_properties = AreaProperties()
area_properties.energy_cost_unsupplied = 10
area_properties.energy_cost_spilled = 4
area_fr = study.create_area("fr", area_properties)

new_properties = AreaProperties()
new_properties.energy_cost_unsupplied = 6
area_fr.update_properties(new_properties)
```

Example of a new code:
```python
import AreaProperties, AreaPropertiesUpdate

area_properties = AreaProperties(energy_cost_unsupplied=10, energy_cost_spilled=4)
area_fr = study.create_area("fr", area_properties)

new_properties = AreaPropertiesUpdate(energy_cost_unsupplied=6)
area_fr.update_properties(new_properties)
```

### Features
- API: add `import_study_api` method
- API: add update_thermal_matrices methods
- API: specify number of years to generate for thermal TS-generation

### Fixes
- LOCAL: `get_thermal_matrix` method checked the wrong path
- API: `read_renewables` method doesn't fail when settings are aggregated instead of clusters
- API: `read_settings` doesn't fail when horizon is a year
- API: disable proxy when using the Desktop version to avoid any issue

### Miscellaneous
- enforce strict type checking with mypy
- enforce override with mypy
- Moves all local and api related classes and methods outside the `model` package

v0.1.8_RC2 (2025-01-22)
-------------------
- upload renewable thermal matrices method added
- bug fix clusters/{area}/list.ini file was missing
- bug fix for input/thermal/series/{area}/{cluster}/series.txt /data.txt and modulation.txt, wrong path 
  at cluster creation


v0.1.8_RC1 (2025-01-22)
-------------------

- bug fixes for missing files when creating area
- wrong properties corrected (spread-unsupplied-energy-cost and spread-spilled-energy-cost)

v0.1.7 (2025-01-08)
-------------------

- move doc generation from ci.yml to publish.yml

v0.1.6 (2025-01-08)
-------------------

- Fix concatenate CONCATENATED_README.md files for single Readme at pypi.org 

v0.1.5 (2025-01-08)
-------------------

- Concatenate .md files for single Readme at pypi.org 

v0.1.4 (2025-01-07)
-------------------

- Allow read_areas method to read area parameters and ui
- Add output functionalities (get_matrix, aggregate_values)

v0.1.3 (2024-12-19)
-------------------

- Add project requirements inside `pyproject.toml` to use the package as is
- Add a subfolder "craft" inside src to rename the package `antares.craft` for users
- Add `py.typed` file to avoid mypy issues in projects importing the package

v0.1.2 (2024-12-18)
-------------------

### Features

- Read a study
- Read thermal, renewable clusters and short term storages properties
- Read load matrix
- Read link matrices
- Allow variant creation
- Allow to run simulation

v0.1.1 (2024-11-26)
-------------------

* update token and bump version to publish on PyPi.

v0.1.0 (2024-11-26)
-------------------

* First release of the project.

