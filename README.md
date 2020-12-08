**THIS PROJECT IS NO LONGER MAINTAINED**

# opsgenie-logger
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Build Status](https://travis-ci.org/triaxtec/opsgenie-logger.svg?branch=develop)](https://travis-ci.org/triaxtec/opsgenie-logger)

A Python logging handler for Atlassian OpsGenie.

## Basic Usage

```python
import logging

from opsgenie_logger import OpsGenieHandler


logger = logging.getLogger()
handler = OpsGenieHandler(api_key="integration_api_key", team_name="my_team", level=logging.ERROR)
logger.addHandler(handler)
logger.error("This will go to OpsGenie!")
try:
    raise ValueError("This is a problem")
except ValueError:
    logger.exception("This stack trace is going to OpsGenie")
```

## Contribution Guidelines
 - Any changes should be covered with a unit test and documented in [CHANGELOG.md]

## Release Process
1. Start a release with Git Flow
1. Update the version number using Semantic Versioning in `pyproject.toml` and `__init__.py`
1. Ensure all dependencies are pointing to released versions
1. Update the release notes in [CHANGELOG.md]
    1. Move changes from "Unreleased" to a section with appropriate version #
    1. Add a link at the bottom of the page to view this version in GitHub.
1. Commit and push any changes
1. Create a pull request from the release branch to master
1. Ensure all checks pass (e.g. CircleCI)
1. Open and merge the pull request
1. Create a tag on the merge commit with the release number

## Contributors 
 - Dylan Anthony <danthony@triaxtec.com>


[CHANGELOG.md]: docs/CHANGELOG.md
