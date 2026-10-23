# ADBroom artwork

<p align="center"><img src="adbroom-icon.png" width="192" alt="ADBroom"></p>

The Android TV / magic wand artwork is shared by the standalone TV launcher and repository documentation. The transparent cutout preserves the rounded silhouette; it must remain square and be resized proportionally.

| File | Purpose |
| --- | --- |
| `source.png` | Original artwork supplied by Tahsin Sungur, including its white surround |
| `adbroom-icon.png` | 1024 × 1024 transparent master for documentation and platform assets |
| `../../res/drawable-*/launcher_icon.png` | Android density variants: mdpi 96, hdpi 144, xhdpi 192, xxhdpi 288, xxxhdpi 384 pixels |
| `../../res/drawable/banner.xml` | 320 × 180 dp TV banner with the shared icon centered on a blue gradient |

Do not flatten the master onto white, stretch it to fill a banner, or apply a second rounded mask. Rounded corners and the transparent surrounding margin are already part of the master. Android's application icon and fallback app cards use `@drawable/launcher_icon`.

The background extraction uses the built-in imagegen tool; platform resizing uses `sips`. No generation service is involved when building or running ADBroom. The exact extraction instruction is recorded in [EDIT-PROMPT.md](EDIT-PROMPT.md).

After updating the transparent master, regenerate the committed Android PNGs on macOS:

```sh
bash scripts/prepare-icons.sh
```

Run this command from the repository root. Normal Mac and launcher builds use the prepared files; the Android build remains independent of macOS tools.
