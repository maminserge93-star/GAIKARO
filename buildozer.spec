[app]
title = GAIKARO
package.name = gaikaro
package.domain = org.ideba
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy,kivymd,pillow

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Permissions pour tes PDF à Grand-Bassam
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
