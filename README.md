# Monitoreringssystem
Ett terminalbaserat Pythonprogram som övervakar CPU-, RAM- och diskanvändning. Du kan ställa in larmgränser och köra övervakningen under en viss tid, ett antal mätningar eller tills du avbryter med `Ctrl+C`.

## Ansvarsområden
Följande ansvarar för de olika delarna av programmet och alla dess funktioner.
Monitoriseringssystem - Fredrik
Larmsystem - Oliver
Loggsystem - Erik

## Installation
Kräver Python 3.12 eller senare. Diskmätningen är inställd för Windows (`C:`).
Installera beroendet från projektets mapp med följande kommando:
python -m pip install -r requirements.txt

## Användning
Användaren presenteras med en meny där man får välja vad man ska göra.
Om användaren väljer val 1 så kommer man till Larm-konfigurationssystemet där man blir presenterad med en ny meny med 5 olika val: 
* Lägga till alarm - Välj typ av alarm man vill lägga till och sedan vilken larmnivå
* Ta bort alarm - Välj vilket alarm du vill ta bort
* Visa alla aktiva larm
* Skicka larm till Monitoreringssystem - Sparar alarmen till en fil som monitoreringssystemet kan läsa ifrån
* Avsluta - Återgår till hvuudmenyn

Om användaren väljer val 2 så kommer man till Monitoreringssystem där man blir presenterad med en ny meny med 3 olika val:
* Ladda alarm - Hämtar larmnivåer från filen som Larm-konfigurationssystemet sparar värdena i
* Starta monitoreringssession - Här får man välja hur man ska monitorera, om det är i X antal sekunder, X antal iterationer eller oändligt. När man har valt det så startar monitoriseringen och man ser resultatet i terminalen. 
* Återgå till huvudmeny 


## Filer
- `huvudmeny.py` - huvudmeny för programmet
- `Monitoreringssystem.py` – övervakning och larmkontroll.
- `menu.py` – meny för larmkonfiguration.
- `alarm.py` – hantering och lagring av larm.
- `loggsystem.py` – loggning av händelser och larm.
- `requirements.txt` – visar vilka externa paket som behövs för att köra programmet.
