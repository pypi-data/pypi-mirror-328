# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2025 - 2025/02/20

- code clean up
- typing and linting improvements
- performance improvements (`_decodeRLE` takes approx half the time to decode)
- improve tests coverage
- add `native_convert:convert_xcf_to_flat_image` to drive gimp directly if it
  exists to do a conversion. Note this is highly experimental at present, though
  will likely export more accurately than gimpformats will

## 2024 - 2024/01/24

- more typing
- ruff linting
- code quality improvements

## 2023.1 - 2023/08/31

- Update deps

## 2023

- `binaryiotools` back in project

## 2022.0.1 - 2022/01/28

- Using pytest
- Fix `GimpGplPalette:decode` and `GimpGplPalette:encode`
- Fix `GimpGtpToolPreset:parenFileDecode`

## 2022 - 2022/01/23

- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Update deps
- Minor update to tests

## 2021.1.4 - 2021/12/10

- Raise `NotImplementedError` for XcfDocument save methods https://github.com/FHPythonUtils/GimpFormats/pull/10
- Fix regression in flattenAll when using layer group masks https://github.com/FHPythonUtils/GimpFormats/pull/11

Thanks https://github.com/hemebond for those!

- Raise raise `RuntimeError` in place of generalised `Exception`
- Minor code quality improvements

## 2021.1.2 - 2021/11/05

- Use pre-commit
- Rename tests (snake_case module names)
- Code quality improvements (fstrings etc)

## 2021.1.1 - 2021/09/13

- Update pillow

## 2021.1 - 2021/08/11

- Feature: https://github.com/FHPythonUtils/GimpFormats/issues/6
- Brought `renderWOffset` back in-house

## 2021.0.2 - 2021/06/08

- Tidy up
- pyupgrade
- rasterImageOffset -> blendmodes
- Work on tests a bit

## 2021.0.1 - 2021/04/16

- Fix #2
- Tidy up

## 2021 - 2021/03/18

- Update Pillow >= 8.1.1 due to high severity security vulnerabilities:
	- CVE-2021-27923
	- CVE-2020-35654
	- CVE-2020-35653
	- CVE-2021-27921
	- CVE-2021-27922
	- CVE-2020-35655

- 8 failed, 34 passed in 6.76 seconds ...
- Probably needs a re-write, but I don't have time.

## 2020.3 - 2020/10/29

- A bit of typing

## 2020.2.4 - 2020/05/17

- Update gpl reader to remove comments
- More work on saving xcf. Still doesn't work.

## 2020.2.3 - 2020/05/14

- Fix fatal read xcf bug (upstream)

## 2020.2.2 - 2020/05/10

- `BinaryIO` is now an external dependency `binaryiotools` as it provides many
	generalized methods that can be used to read a whole range of binary streams

## 2020.2.1 - 2020/05/08

- Added `blendmodes` as a dependency

## 2020.2 - 2020/05/07

- Massive backend changes. This is to make the development and maintenance
	processes easier as code files are a little smaller and contain one class (in
	most cases). Making them that bit more logical
- API breaking changes:
	- Lazy importing from gimpformats no longer works eg
	`from gimpformats import BinaryIO` you must import from the module file eg
	`from gimpformats.BinaryIO import BinaryIO` this will prevent the entire
	module from becoming unusable in the unlikely event of a serious bug in any
	of these module files
	- Module files with the exception of `gimpXcfDocument` are now in upper
	camel case eg `from gimpformats.binaryIO import BinaryIO` is now
	`from gimpformats.BinaryIO import BinaryIO` this is part of making the
	development and maintenance process more manageable. gimpXcfDocument is
	the exception as this is probably the reason you are using the module and
	should therefore mean that most will have an easier time migrating. This may
	change in the future
	- toBytes/ \_encode\_ (and other variants) are now encode\_
	- fromBytes/ \_decode\_ (and other variants) are now decode\_
- Adding layers is now possible!
- Saving writes but is far from complete. This requires lots of the toBytes/
	encode_ functions to be fixed and implemented. Currently, you will get an
	incomplete xcf with data such as the image version and size and that's about
	it.

## 2020.1.3 - 2020/05/07

- Fixed visibility issues
- Added more comments as I continue my 'onboarding process'

## 2020.1.2 - 2020/05/06

- Updated classifiers
- Added notes for development
- Added copy of xcf spec for dev
- Fix previously broken parts of BinaryIO

## 2020.1.1 - 2020/05/04

- Update author

## 2020.1 - 2020/05/03

- Attempted some fixes to gimpImageInternals.py
- Fix gimpIOBase.py
- Added image compositor and added a new test for a 'complex' image
- Now going to release under gimpformats

## 2020.0.2 - 2020/05/02

- Added documentation
- Project icon :smile:
- Used bracketree to process gtp tool preset
- Incorporated a fix from another fork

## 2020.0.1 - 2020/04/30

- Linting fixes
- Test fixes

## 2020 (0.1) - 2020/04

- Put this on pypi
