import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

def get_base_path():
    # TEST DE SURVIE : On essaie plusieurs dossiers pour éviter le crash
    options = [
        os.path.expanduser('~'), # Dossier utilisateur
        '.',                     # Dossier courant
        '/sdcard/Download'       # Dossier téléchargement Android
    ]
    
    if 'ANDROID_ARGUMENT' in os.environ:
        try:
            from android.storage import app_storage_path
            return app_storage_path()
        except:
            return '/sdcard/Download'
    
    return os.path.dirname(__file__)

BASE_PATH = get_base_path()
DB_PATH = os.path.join(BASE_PATH, 'devis_data.db')

def initialiser_bdd():
    # On met un try/except total pour que l'appli ne ferme JAMAIS ici
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute('CREATE TABLE IF NOT EXISTS devis (id INTEGER PRIMARY KEY AUTOINCREMENT, nom_client TEXT, date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
        conn.close()
    except Exception as e:
        print(f"Erreur BDD ignoree pour eviter le crash: {e}")

def creer_pdf_devis(nom, items, total_str):
    nom_fichier = f"Devis_GAI_KARO_{nom.replace(' ', '_')}.pdf"
    chemin_pdf = os.path.join(BASE_PATH, nom_fichier)
    
    try:
        c = canvas.Canvas(chemin_pdf, pagesize=A4)
        v_olive = colors.Color(0.15, 0.2, 0.1)
        
        # LOGO : On verifie avec prudence
        try:
            chemin_logo = os.path.join(os.path.dirname(__file__), "assets", "logo_gai_karo.png")
            if os.path.exists(chemin_logo):
                c.drawImage(chemin_logo, 50, 770, width=50, height=50)
        except: pass # Si le logo rate, on continue sans lui
        
        c.setFillColor(v_olive)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(110, 800, "GAI-KARO")
        c.setFont("Helvetica-Bold", 12)
        c.drawString(110, 780, "Carreleur professionnel")
        
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.black)
        c.drawString(50, 765, "Siege social : GRAND-BASSAM")
        c.drawString(50, 750, "TEL : 01 73 59 28 13 / 07 98 53 95 51")
        c.drawRightString(550, 780, f"CLIENT : {nom.upper()}")
        c.drawRightString(550, 765, "Date : 24/04/2026")

        # Tableau
        y = 710
        c.setFillColor(v_olive)
        c.rect(50, y, 500, 20, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(55, y+5, "No"); c.drawString(90, y+5, "Designation"); c.drawString(330, y+5, "Qte"); c.drawString(400, y+5, "P.U"); c.drawString(480, y+5, "Montant")

        y -= 25
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 10)
        for i in items:
            c.drawString(55, y, i['n']); c.drawString(90, y, i['desc']); c.drawString(330, y, i['qte']); c.drawString(400, y, i['pu']); c.drawString(480, y, i['total'])
            y -= 20
        
        c.setFillColor(v_olive)
        c.setFont("Helvetica-Bold", 14)
        c.drawRightString(550, y-30, total_str)
        c.save()
        return chemin_pdf
    except:
        return "Erreur lors de la creation"