# Monitoreringssystem
Ett terminalbaserat Pythonprogram som övervakar CPU-, RAM- och diskanvändning. Du kan ställa in larmgränser och köra övervakningen under en viss tid, ett antal mätningar eller tills du avbryter med `Ctrl+C`.

## Ansvarsområden
Följande ansvarar för de olika delarna av programmet och alla dess funktioner.
Monitoriseringssystem - Fredrik
Larmsystem - Oliver
Loggsystem & Huvudmeny - Erik

## Installation
Kräver Python 3.12 eller senare. Diskmätningen är inställd för Windows (`C:`).
Installera beroendet från projektets mapp med följande kommando:
python -m pip install -r requirements.txt

## Användning
WIP - Här får vi fylla på

## Filer
- `huvudmeny.py` - huvudmeny för programmet
- `Monitoreringssystem.py` – övervakning och larmkontroll.
- `menu.py` – meny för larmkonfiguration.
- `alarm.py` – hantering och lagring av larm.
- `loggsystem.py` – loggning av händelser och larm.
- `requirements.txt` – det externa beroendet `psutil`.
