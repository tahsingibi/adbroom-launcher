# Launcher releases

Repository: [tahsingibi/adbroom-launcher](https://github.com/tahsingibi/adbroom-launcher). The Mac companion is maintained and released separately in [tahsingibi/adbroom](https://github.com/tahsingibi/adbroom).

1. Update `android:versionName` / increment `android:versionCode` in `AndroidManifest.xml`; complete `CHANGELOG.md`.
2. Use the existing signing identity in `.signing/development.jks`, or select the same release key with `LAUNCHER_KEYSTORE`, `LAUNCHER_KEY_ALIAS` and `LAUNCHER_STORE_PASSWORD`. Keep keys private.
3. Run `./build.sh`. It runs the ordering unit test and verifies the signed APK.
4. Commit and push `main`.
5. Create a GitHub Release with tag `launcher-v<version>` targeting that commit. Attach both `dist/ADBroomLauncher-<version>.apk` and the matching `.apk.sha256` file.

With authenticated GitHub CLI:

```sh
./scripts/release.sh             # Draft release
./scripts/release.sh --publish   # Public stable release
```

Alternatively use GitHub → Releases → Draft a new release. Use a stable public release for companion downloads; drafts and prereleases are not offered by the Mac app. An empty repo or a tag without APK/checksum assets is not enough.

The Mac app fetches this repository's release list, accepts only `launcher-v…` stable tags and verified `ADBroomLauncher-….apk` assets. Mac DMGs and unrelated repository URLs are rejected. Local builds and the private `.signing` directory are ignored by Git.
