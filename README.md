<p align="center"><img src="assets/icon.png" width="112" alt="ADBroom Launcher"></p>

# ADBroom Launcher

Android TV / Google TV için hızlı, native ve reklamsız ana ekran. **Mac uygulaması gerekmez.** Android 6.0+; Java ve Android'in kendi arayüz bileşenleriyle çalışır. INTERNET izni, WebView ve analitik içermez.

**Türkçe** · [English](README.en.md) · [Son sürümü indir (APK)](https://github.com/tahsingibi/adbroom-launcher/releases/latest) · [Mac uygulaması](https://github.com/tahsingibi/adbroom)

## Kurulum ve kullanım

[Son sürümdeki](https://github.com/tahsingibi/adbroom-launcher/releases/latest) `ADBroomLauncher-<sürüm>.apk` dosyasını TV'ye aktararak kur. Aynı yayındaki `.apk.sha256` dosyası sağlama toplamıdır. ADB ile de kurabilirsin:

```sh
adb connect <TV-IP>:5555
adb -s <TV-IP>:5555 install -r ADBroomLauncher-1.2.1.apk
adb -s <TV-IP>:5555 shell am start -n io.github.adbroom.launcher/.HomeActivity
```

Launcher ayarlarından varsayılan ana ekranı seç. OK uygulamayı açar, uzun OK uygulama seçeneklerini açar. Menü ile sıralamaya gir, yön tuşlarıyla taşı, OK ile kaydet, Geri ile iptal et.

Izgara/yatay sıra, favoriler, özel adlar, koleksiyonlar, gizleme, duvar kâğıdı, saat, modüller ve ebeveyn PIN'i TV kumandasından yönetilir. İsteğe bağlı Mac editörü aynı ayarları ve sıralamayı düzenler; tercihler TV'de saklanır. Home yönlendirmesi ve medya erişimi kullanıcı tarafından TV sistem ayarlarından açılır; destek TV'ye göre değişir.

## Klasörler ve derleme

- `src/`, `res/`: launcher kaynakları ve Android görselleri.
- `tests/`: birim, emülatör ve odak regresyon testleri.
- `assets/icon.png`: ikonların üretildiği şeffaf ana görsel (`scripts/prepare-icons.sh`).
- `scripts/`, `docs/`: görsel/yayın yardımcıları ve teknik notlar.
- `build/`, `dist/`: yerel çıktılar; Git'e eklenmez.

JDK 17+, Python 3 ve Android SDK platform/build-tools 35+ gerekir. Gerekirse `JAVA_HOME` ve `ANDROID_SDK_ROOT` ayarla. Swift veya Mac reposuna ihtiyaç yoktur:

```sh
./build.sh
```

Çıktılar: `build/ADBroomLauncher.apk`, `dist/ADBroomLauncher-1.2.1.apk` ve `.apk.sha256`.

Güncellemeler için mevcut `.signing/development.jks` kimliğini koru. Yayın kimliği `LAUNCHER_KEYSTORE`, `LAUNCHER_KEY_ALIAS`, `LAUNCHER_STORE_PASSWORD` değişkenleriyle seçilebilir. Anahtar Git'e eklenmez.

## Testler ve yayın

Derleme sıralama birim testini çalıştırır. Yalnızca geçici emülatörde:

```sh
python3 tests/smoke.py --adb "$ANDROID_SDK_ROOT/platform-tools/adb"
python3 tests/features.py --adb "$ANDROID_SDK_ROOT/platform-tools/adb"
bash tests/focus.sh emulator-5580
```

[Yayın rehberi](docs/RELEASING.md) · [Sürüm notları](CHANGELOG.md) · [MIT](LICENSE)

Tahsin Sungur · [X/tahsingibi](https://x.com/tahsingibi) · [sungur.dev](https://sungur.dev)

Android robotu, Google tarafından paylaşılan çalışmadan [Creative Commons 3.0 Atıf Lisansı](https://creativecommons.org/licenses/by/3.0/) koşullarıyla kullanılır.
