import tkinter as tk

# Exemple de listes de données et de code
dataline = ["a", "b", "c"]
codeline = ["x", "y", "z"]


# Fonction pour parcourir les listes et afficher les variables et leurs valeurs
def next_button():
    global dataline_index, codeline_index
    if dataline_index < len(dataline):
        var_label.config(text=f"{dataline[dataline_index]} = {eval(codeline[codeline_index])}")
        dataline_index += 1
        codeline_index += 1


# Création de la fenêtre principale
root = tk.Tk()

# Ajout du label pour afficher les variables et leurs valeurs
var_label = tk.Label(root, text="", font=("Arial", 14))
var_label.pack()

# Ajout du bouton "Next"
next_button = tk.Button(root, text="Next", command=next_button)
next_button.pack()

# Initialisation des index pour parcourir les listes
dataline_index = 0
codeline_index = 0

# Démarrage de la boucle principale de l'interface graphique
root.mainloop()
