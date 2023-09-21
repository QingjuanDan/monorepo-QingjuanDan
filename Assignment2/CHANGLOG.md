# CHANGELOG.md for CustomJSON Package

## [1.0.2] - 2023-09-21

### Added
- Enhanced the README.md with more examples and detailed explanations.
- Added compatibility for newer Python versions.

### Fixed
- Solved an issue where `CustomJSONDecoder` wasn’t decoding datetime strings correctly.
- Addressed a bug causing incorrect decoding of range objects.

## [1.0.1] - 2023-09-25

### Added
- Improved error handling for incompatible types in `CustomJSONEncoder`.
- Introduced more comprehensive test coverage to ensure the reliability of the package.

### Changed
- Updated `CustomJSONDecoder` to utilize `dateutil.parser.isoparse` for more robust datetime parsing.

## [1.0.0] - 2023-09-21

### Added
- Initial release of the CustomJSON Package.
- Implemented `CustomJSONEncoder` for encoding `datetime.datetime` and `range` objects.
- Implemented `CustomJSONDecoder` for decoding previously unsupported types.
- Included utility functions `dumps` and `loads` for convenient usage.

### Changed
- Structured the codebase to be more modular and maintainable.

## Notes
This CHANGELOG.md file is a living document, and it should be updated whenever there are significant additions, changes, deprecations, removals, or fixes applied to the project.

### How to Update
- Start with the header of the new version.
- List the notable changes made, categorized as `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`.
- Always write the changes in a way that is understandable for the users of the package, focusing on the impact and avoiding too much technical jargon.

## Contribution
If you wish to contribute to this project, please refer to the contribution guidelines provided in the project repository, submit your changes, and update this CHANGELOG.md file accordingly.
