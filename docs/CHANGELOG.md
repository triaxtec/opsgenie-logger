# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.5] - 2019-10-17
### Added
- MIT license and additional PyPI metadata (no functional changes)

## [0.1.4] - 2019-10-02
### Changed
- Improved deduplication by using source of exception (when log is for an exception) instead of log point for alias

## [0.1.3] - 2019-10-01
### Changed
- Fill in OpsGenie description with result of `self.format` instead of limiting to exception strings

## [0.1.2] - 2019-09-27
### Changed
- Allow `level` param to `OpsGenieHandler` to accept string of log level

## [0.1.1] - 2019-09-27
### Added
- `level` param to `OpsGenieHandler` specifying the minimum log level a log must be to send it to OpsGenie

## 0.1.0 - 2019-09-27
Initial version


[Unreleased]: https://github.com/triaxtec/opsgenie-logger/compare/master...develop
[0.1.4]: https://github.com/triaxtec/opsgenie-logger/releases/tag/v.0.1.4
[0.1.3]: https://github.com/triaxtec/opsgenie-logger/releases/tag/v.0.1.3
[0.1.2]: https://github.com/triaxtec/opsgenie-logger/releases/tag/v.0.1.2
[0.1.1]: https://github.com/triaxtec/opsgenie-logger/releases/tag/v.0.1.1
[0.1.0]: https://github.com/triaxtec/opsgenie-logger/releases/tag/v.0.1.0
