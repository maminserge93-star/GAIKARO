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
# On garde l'architecture la plus courante
android.archs = arm64-v8a
android.allow_backup = True
# Branche stable
p4a.branch = master

# --- FIXATIONS DE VERSIONS POUR ÉVITER L'ERREUR LICENCE/AIDL ---
android.sdk = 34
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0
# -----------------------------------------------------------

# Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
