# Changelog

All notable changes to this project will be documented in this file.

## [v0.34.2](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/compare/v0.34.1...v0.34.2) (2021-08-31)

### Features

- Now all the font styles (`fixed`, `fixed-slab`, `mono`, `mono-slab`, `term`, `term-slab`, `gothic`, `ui`) and orthographies (`cl`, `hc`, `j`, `k`, `sc`, `tc`) of Sarasa Gothic is being patched ([47c74a5](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/commit/47c74a580cbb332b81104f8db6b4c44729b6d125))

### Revert

- Revert commit [5bcfd73](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/commit/5bcfd73fa38c6a79710d157629c590e190f9fdec), which store installed fonts as list.txt instead of raw font files, because it will break scoop's rollback to previous version feature ([182b32d](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/commit/182b32d237522f4961b994a2001dfdce9c4373ae))

## [v0.32.14](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/compare/v0.32.13...v0.32.14) (2021-07-25)

### ⚠ BREAKING CHANGES

- The release page now provide **a single `sarasa-mono-tc-nerd-font.zip` file includes all the font variants**, instead of a `.ttf` font file named `Sarasa-Mono-TC-Nerd-Font-Complete.ttf` in previous versions (`v0.32.13` and below)

### Features

- Now all the font variants (`Regular`, `Italic`, `Bold`, `Bold Italic`, `Light`, `Light Italic`, `Semibold`, `Semibold Italic`, `ExtraXlight`, `Extralight Italic`) of Sarasa Mono TC is being patched ([4cbe8b9](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/commit/4cbe8b964e618d559adcf6e9eaac9d6c0432a828))
- Add support for scoop's global installation ([ad4dba8](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/commit/ad4dba8e3944af382cf173a8d98fc2f923aa5633))

### Bugs Fixes

- Check if the font is being used by any process when using `scoop` to upgrade or uninstall ([c9a052f](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/commit/c9a052fd6a850ea296757f8ab77cdb093c4ec67a))
