# opsgenie-logger

## Purpose
Provides logging handlers for OpsGenie

## Contribution Guidelines
 - The project is written to support Python 3.7 and should conform to the [Triax Python Standards](https://triaxtec.atlassian.net/wiki/spaces/EN/pages/499482627/Python+Guidelines).
 - Any changes should be covered with a unit test and documented in [CHANGELOG.md]

## Documentation
- Docs are hosted for the latest released version on the [PyPI server](https://pypi.api.triaxtec.com/docs/opsgenie-logger/)
- Most of the docs are auto-generated from docstrings.

## Release Process
1. Start a release with Git Flow
1. Ensure all tests pass with `poetry run pytest`
1. Update the version number in `pyproject.toml` and `__init__.py` with `dephell project bump`
1. Ensure all requirements are pointing to released versions
1. Update the release notes in [CHANGELOG.md]
    1. Move changes from "Unreleased" to a section with appropriate version #
    1. Add a link at the bottom of the page to view this version in Bitbucket.  It won't work until after the tag is created.
1. Commit both files
1. Create a pull request from the release branch to master
1. Get approval from all stakeholders
1. Open and merge the pull request
1. Create a tag on the merge commit with the release number
1. Upload to PyPi: `poetry publish -r triaxtec --build`
1. Update the docs: `poetry run python build_docs.py`

## Contributors 
 - Dylan Anthony <danthony@triaxtec.com>


[CHANGELOG.md]: docs/CHANGELOG.md
