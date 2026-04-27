[app]
title = GAI-KARO Devis
package.name = gaikaro_devis
package.domain = org.gaikaro
source.dir = .
source.include_exts = py,png,jpg,kv,db
version = 1.0

# MODIFICATION ICI : sqlite3 retiré car inclus dans python3
requirements = python3,kivy==2.2.1,reportlab,pillow

orientation = portrait
fullscreen = 0

# MODIFICATION ICI : Permissions optimisées
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.archs = arm64-v8a

# AJOUT : Pour éviter les erreurs de compilation sur Colab
android.accept_sdk_license = True
android.skip_update = False
# (list) Permissions (On ajoute le stockage de maniere agressive)
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (list) Services Kivy (On force l'utilisation de SDL2)
requirements = python3,kivy==2.2.1,reportlab,pillow,android
[buildozer]
log_level = 2
bin_dir = ./bin