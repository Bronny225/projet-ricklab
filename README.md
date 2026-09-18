# 🔬 RickLab / LAB-ASSISTANT 3000: Advanced Laboratory Automation & Biometric Security System

> *"Empreinte vocale validée. Bienvenue dans le labo, chef."* — Rick-OS

---

## 📋 Présentation du Projet
**RickLab** est un système intelligent de contrôle d'accès et d'automatisation de laboratoire hautement sécurisé, inspiré de l'univers de *Rick & Morty*. Développé dans le cadre d'un projet collaboratif, il combine l'intelligence artificielle, l'électronique embarquée sur Arduino et une interface web/logicielle synchronisée.

---

## 🚀 Fonctionnalités Clés & Architecture

### 1. 🎙️ Sécurité Biométrique Vocale & Intelligence Artificielle
* Traitement vocal et pilotage centralisé par scripts Python.
* Pipeline d'analyse et gestion de l'interface avec le matériel.
* **En cas de succès :** Validation et ouverture du portail/vortex.
* **En cas d'intrusion :** Déclenchement d'une alarme critique.

### 2. 💡 Éclairage Progressif par Détection de Proximité
* Capteur de présence relié au système Arduino.
* Plus l'utilisateur avance dans le laboratoire, plus les lumières s'allument séquentiellement.

### 3. 🌀 Contrôle du Vortex Interdimensionnel
* Intégration d'actionneurs pilotés pour simuler l'ouverture et la fermeture d'un vortex.

### 4. 🖥️ Synchronisation Interface Graphique & Pont de Communication
* Une **Interface Web/GUI** dédiée (`interface.html`).
* Un système de pont (`pont_interface`) pour assurer la communication en temps réel et la gestion des requêtes.

---

## 📂 Structure du Dépôt GitHub

```text
projet-ricklab/
│
├── interface.html          # Interface graphique web / front-end du laboratoire
├── main.py                 # Script principal d'exécution et de logique
├── pont_interface          # Module de pont de communication et gestion des requêtes
└── README.md               # Documentation officielle du dépôt
