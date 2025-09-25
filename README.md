# Studien-Dashboard

## Installationsanleitung

**Projektname:** Studien-Dashboard  
**Autor:** Omar Abdullah (Matrikelnummer: 102210158)  

---

### Systemvoraussetzungen
- Windows 10 oder höher  
- Python 3.x (empfohlen: 3.11)  
- Git (optional, falls direkt vom Repository geklont wird)  

---

### 1. Repository herunterladen
**Option A – über Git**
```bash
git clone https://github.com/omaraldulimay/Studium-Dashboard.git
cd Studium-Dashboard
```

**Option B – ZIP herunterladen**
- GitHub-Repo als ZIP herunterladen  
- Entpacken in gewünschten Ordner  

---

### 2. Virtuelle Umgebung erstellen & aktivieren
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

---

### 4. Anwendung starten
```bash
python main.py
```

---

### 5. Beispiel-Daten verwenden
- Beispieldateien befinden sich im Ordner **/data**  
- Testlauf mit Beispieldaten:
```bash
python main.py --input data/beispiel.json
```

---

### 6. Hinweise
- Falls Bibliotheken fehlen:
```bash
pip install <paketname>
```
- Programm getestet unter Windows 11 + Python 3.11  
