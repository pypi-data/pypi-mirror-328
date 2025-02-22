# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [PEP 440](https://www.python.org/dev/peps/pep-0440/)
and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.5] - 2025-02-19

### Fixed
- CLI issues with bucket/prefix for S3 upload (resolves [#32](https://github.com/opera-adt/dist-s1/issues/32)).
- Included `__main__.py` testing for the SAS entrypoint of the CLI; uses the cropped dataset to test the workflow.
- Includes `dist-s1 run_sas` testing and golden dataset comparision.
- Updates to README regarding GPU environment setup.

## [0.0.4]

### Added 
- Minimum working example of generation fo the product via `dist-s1 run`
- Integration of `dist-s1-enumerator` to identify/localize the inputs from MGRS tile ID, post-date, and track number
- Notebooks and examples to run end-to-end workflows as well as Science Application Software (SAS) workflows
- Docker image with nvidia compatibility (fixes the cuda version at 11.8)
- Download and application of the water mask (can specify a path or request it to generate from UMD GLAD LCLUC data).
- Extensive instructions in the README for various use-case scenarios.
- Golden dataset test for SAS workflow
- Allow user to specify bucket/prefix for S3 upload - makes library compatible with Hyp3.
- Ensure Earthdata credentials are provided in ~/.netrc and allow for them to be passed as suitable evnironment variables.
- Create a GPU compatible docker image (ongoing) - use nvidia docker image.
- Ensures pyyaml is in the environment (used for serialization of runconfig).
- Update equality testing for DIST-S1 product comparison.

### Fixed
* CLI issues with hyp3 

### Changed
- Pyproject.toml file to handle ruff

## [0.0.3]

### Added

- Python 3.13 support
- Updated dockerimage to ensure on login the conda environment is activated
- Instructions in the README for OPERA delivery.
- A `.Dockerignore` file to remove extraneous files from the docker image
- Allow `/home/ops` directory in Docker image to be open to all users

## [0.0.2]

### Added

- Pypi delivery workflow
- Entrypoint for CLI to localize data via internet (the SAS workflow is assumed not to have internet access)
- Data models for output data and product naming conventions
- Ensures output products follow the product and the tif layers follow the expected naming conventions
  - Provides testing/validation of the structure (via tmp directories)

### Changed

- CLI entrypoints now utilize `dist-s1 run_sas` and `dist-s1 run` rathern than just `dist-s1`. 
  - The `dist-s1 run_sas` is the primary entrypoint for Science Application Software (SAS) for SDS operations. 
  - The `dist-s1 run` is the simplified entrypoint for external users, allowing for the localization of data from publicly available data sources.

## [0.0.1]

### Added

- Initial internal release of the DIST-S1 project. Test github release workflow
