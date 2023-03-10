# Twemoji-Amazing 💡 ![](https://img.shields.io/badge/emoji%20count-3689-brightgreen)

**Like Font-Awesome, but for [Twitter Emojis](https://github.com/twitter/twemoji), and also, it's amazing!** 🌟

_An updated plug-and-play replacement for projects like [twemoji-awesome](https://github.com/ellekasai/twemoji-awesome)! Now with over 3,500 supported emojis!_

![twemoji-banner](twemoji-banner.png)

## Usage

### Getting the CSS file
You can either download the CSS file from the [Releases](https://github.com/SebastianAigner/twemoji-amazing/releases/latest) page, or use a CDN such as JsDelivr:
```
https://cdn.jsdelivr.net/gh/SebastianAigner/twemoji-amazing@1.2.0/twemoji-amazing.css
```

### Using the CSS classes

`<i class="twa twa-face-with-monocle">`

### Size Options

Like Font-Awesome (and Twemoji-Awesome), emoji sizes can be changed via `twa-lg`, `twa-2x`, `twa-3x`, `twa-4x`, and `twa-5x`.

### Finding Emojis

- Twemoji-Amazing uses [Emoji.json](https://github.com/amio/emoji.json) as its source of codepoints and descriptions.
- To find an emoji of your liking, check out the [official Emoji list](https://unicode.org/emoji/charts/emoji-list.html). Replace spaces with hyphens to get the class name! (e.g. "film projector" becomes `twa-film-projector` 📽)

_Note for Twemoji-Awesome users: Twemoji-Amazing is designed to be an almost-no-adjustments-needed replacement for twemoji-awesome. However, the naming scheme for twemoji-awesome was based on [Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet/), which is now outdated. This means some emojis might have changed names._

### Running the generator

`./gradlew run` will generate a fresh version of the twemoji-amazing file in the root directory of the project.

### Licenses & Other

License: [MIT](https://mit-license.org/).

Uses CSS snippets from [twemoji-awesome](https://github.com/ellekasai/twemoji-awesome), licensed under [MIT](http://ellekasai.mit-license.org/).

As per the Twemoji repository, the graphics are licensed under the CC-BY 4.0 which has a pretty good guide on [best practices for attribution](https://wiki.creativecommons.org/Best_practices_for_attribution). Please adhere to the [attribution requirements](https://github.com/twitter/twemoji#attribution-requirements) when using these emojis.
