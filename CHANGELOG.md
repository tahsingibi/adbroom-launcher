# ADBroom Launcher release notes

## 1.2.1 — 2026-10-23

- Move the standalone launcher to `tahsingibi/adbroom-launcher`, with root-level source, build/test scripts and release assets.

- Fix stuck focus highlights when navigating recycled grid/row cards: reset reused cards and reconcile the single selected view before drawing, including window/dialog focus changes.
- Reuse card backgrounds and skip unchanged styles to keep navigation lightweight.
- Shared Android TV / magic wand icon with transparent rounded corners, density-specific Android assets and an updated TV banner.
- Standalone versioned APK and SHA-256 checksum in `dist/`; the Mac app is not needed for download, installation or use.
- Independent source/build in this repository and `launcher-v<version>` release channel.
- Existing signing identity and TV preferences preserved during the folder reorganization.
- About identity: Tahsin Sungur / tahsingibi / sungur.dev.

## 1.2.0

- Native grid/row layouts, favorites, custom names, collections, hidden apps and parental PIN.
- Appearance, wallpaper, clock, profile, language, input/network and optional media modules.
- Optional user-enabled Home routing and local revision-checked companion editor bridge.
