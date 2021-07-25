Sarasa Mono TC ⨯ Nerd Fonts
===

This project is a modified version of [adam7/delugia-code](https://github.com/adam7/delugia-code), which utilize GitHub Actions to automatically generate [Nerd fonts](https://github.com/ryanoasis/nerd-fonts) patched [Sarasa Mono TC font](https://github.com/be5invis/Sarasa-Gothic).

Installation
---

### Using [Scoop](https://scoop.sh) on Windows

- Add this repo as custom scoop bucket

```
scoop bucket add sarasa-nerd-font https://github.com/jonz94/Sarasa-Mono-TC-Nerd-Font
```

- Then `Sarasa-Mono-TC-Nerd-Font` can be installed as a scoop app

```
scoop install Sarasa-Mono-TC-Nerd-Font
```

### Manually install

Go to the [Releases page](https://github.com/jonz94/Sarasa-Mono-TC-Nerd-Font/releases) and download the `sarasa-mono-tc-nerd-font.zip` file.

Notable Changes
---

### [v0.32.14](https://github.com/jonz94/Sarasa-Mono-TC-Nerd-Font/compare/v0.32.13...v0.32.14) - 2021-07-25

#### Added

- Now all the font variants (`Regular`, `Italic`, `Bold`, `Bold Italic`, `Light`, `Light Italic`, `Semibold`, `Semibold Italic`, `ExtraXlight`, `Extralight Italic`) of Sarasa Mono TC is being patched
- Add support for scoop's global installation

#### Fixed

- Check if the font is being used by any process when using `scoop` to upgrade or uninstall

#### Breaking Change
- The release page now provide **a single `sarasa-mono-tc-nerd-font.zip` file includes all the font variants**, instead of a `.ttf` font file named `Sarasa-Mono-TC-Nerd-Font-Complete.ttf` in previous versions (`v0.32.13` and below)
