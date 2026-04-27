from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock # AJOUTÉ pour le focus fluide
from logic import initialiser_bdd, creer_pdf_devis

# Style GAI-KARO (Fond gris très clair)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class DevisApp(App):
    def build(self):
        try:
            initialiser_bdd()
        except:
            pass
            
        self.lignes_refs = []
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # Titre App
        root.add_widget(Label(text="GAI-KARO : GESTION DEVIS", font_size='20sp', bold=True, color=(0.15, 0.2, 0.1, 1), size_hint_y=None, height=50))

        # Client
        self.nom_client = TextInput(hint_text="Saisir nom du client...", multiline=False, size_hint_y=None, height=45)
        root.add_widget(self.nom_client)

        # En-tête Tableau
        h_grid = GridLayout(cols=5, size_hint_y=None, height=40, spacing=1)
        titres = [("No", 0.1), ("Designation", 0.4), ("Qte", 0.1), ("P.U", 0.2), ("Montant", 0.2)]
        for t, w in titres:
            h_grid.add_widget(Label(text=t, bold=True, color=(0.15, 0.2, 0.1, 1), size_hint_x=w))
        root.add_widget(h_grid)

        # Zone de saisie
        self.grid_lignes = GridLayout(cols=1, size_hint_y=None, spacing=1)
        self.grid_lignes.bind(minimum_height=self.grid_lignes.setter('height'))
        scroll = ScrollView()
        scroll.add_widget(self.grid_lignes)
        root.add_widget(scroll)

        # Total
        self.lbl_total = Label(text="TOTAL : 0 FCFA", font_size='18sp', bold=True, color=(0.15, 0.2, 0.1, 1), size_hint_y=None, height=50)
        root.add_widget(self.lbl_total)

        # Bouton
        self.btn = Button(text="GENERER LE DEVIS", size_hint_y=None, height=60, background_color=(0.15, 0.2, 0.1, 1), bold=True)
        self.btn.bind(on_press=self.lancer_pdf)
        root.add_widget(self.btn)

        self.ajouter_ligne()
        return root

    def ajouter_ligne(self, *args):
        num = str(len(self.lignes_refs) + 1).zfill(2)
        row = GridLayout(cols=5, size_hint_y=None, height=45, spacing=2)
        
        n = Label(text=num, size_hint_x=0.1, color=(0,0,0,1))
        d = TextInput(hint_text="Travaux...", size_hint_x=0.4, multiline=False)
        q = TextInput(hint_text="0", size_hint_x=0.1, input_filter='int', multiline=False)
        p = TextInput(hint_text="0", size_hint_x=0.2, input_filter='int', multiline=False)
        t = Label(text="0", size_hint_x=0.2, color=(0,0,0,1), bold=True)

        def calcul(*a):
            try:
                vq = int(q.text) if q.text else 0
                vp = int(p.text) if p.text else 0
                t.text = str(vq * vp)
                self.lbl_total.text = f"TOTAL : {sum(int(l['t'].text) for l in self.lignes_refs)} FCFA"
            except: pass

        p.bind(text=calcul, on_text_validate=self.ajouter_ligne)
        q.bind(text=calcul)
        
        self.lignes_refs.append({'n': n, 'd': d, 'q': q, 'p': p, 't': t})
        for widget in [n, d, q, p, t]: row.add_widget(widget)
        self.grid_lignes.add_widget(row)
        
        # Focus avec un léger délai pour Android (plus stable)
        Clock.schedule_once(lambda dt: setattr(d, 'focus', True), 0.2)

    def lancer_pdf(self, instance):
        if not self.nom_client.text or self.lbl_total.text == "TOTAL : 0 FCFA":
            return
            
        items = [{'n': l['n'].text, 'desc': l['d'].text, 'qte': l['q'].text, 'pu': l['p'].text, 'total': l['t'].text} for l in self.lignes_refs if l['d'].text]
        
        # Appel de la fonction de création et récupération du chemin
        chemin = creer_pdf_devis(self.nom_client.text, items, self.lbl_total.text)
        
        # Nettoyage et Confirmation
        self.nom_client.text = ""
        self.grid_lignes.clear_widgets()
        self.lignes_refs = []
        self.lbl_total.text = "TOTAL : 0 FCFA"
        self.ajouter_ligne()
        self.btn.text = "DEVIS PRÊT !" # On change le texte du bouton

if __name__ == '__main__':
    DevisApp().run()