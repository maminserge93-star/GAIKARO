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
# On ne garde qu'une architecture pour le test, c'est plus sûr
android.archs = arm64-v8a
android.allow_backup = True
# On force l'utilisation de la branche stable pour éviter les erreurs de dossiers
p4a.branch = master

# Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
