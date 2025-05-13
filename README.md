#  Détection d'accidents de voiture – Application Desktop

Ce projet académique a pour objectif de développer une application desktop capable de détecter automatiquement des accidents de la route à partir de flux vidéo ou webcam.  
Il combine des techniques de **vision par ordinateur** et de **deep learning**, intégrées dans une interface conviviale en **Tkinter**.

---

##  Fonctionnalités principales

-  Détection d’accidents à partir d’une vidéo locale ou d’un flux en temps réel (webcam) 
-  Affichage des images où un accident est détecté  
-  Interface utilisateur avec menu principal, navigation simple et actions directes  
-  Utilisation d’un modèle CNN entraîné avec TensorFlow / Keras  

---

##  Technologies utilisées

- **Python 3.7**
- **OpenCV** pour le traitement des flux vidéo  
- **TensorFlow / Keras** pour l’apprentissage automatique  
- **NumPy / Pandas** pour la manipulation de données  
- **Tkinter** pour l’interface graphique  
-  **YOLOv3** pour la détection rapide d’objets

---

## Aperçu de l’application

Menu principal de l’application :

![alt text](<Menu Principal.png>)
---

##  Installation

### 1. Cloner le projet :

```bash
git clone https://github.com/Yassine-Mahfoudh/accident-detection-app.git
cd accident-detection-app
``` 

### 2. Créer un environnement virtuel :
```bash

python -m venv venv
venv\Scripts\activate 
```
 ### 3. Installer les dépendances :

pip install -r requirements.txt

### 4.Lancer l’application

python main.py

Identifiants par défaut (si interface login activée) :

Utilisateur : Yassine   
Mot de passe : 1234

### Auteurs 
Projet réalisé en groupe dans le cadre du Master IA & Data Science (Février – Mai 2024)

Équipe projet :

Yassine Mahfoudh 

Achraf el Badri

Mohammed Bouftini