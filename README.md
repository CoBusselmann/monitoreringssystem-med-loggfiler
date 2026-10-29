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
Användaren presenteras med en huvudmeny där man får välja vad man ska göra.
Alla val som användaren gör loggas automatiskt till en loggfil.

1. Starta Larm-konfigurationssystem
    Om användaren väljer val 1 så kommer man till Larm-konfigurationssystemet där man blir presenterad med en ny meny med 5 olika val: 
    1. Lägga till alarm - Välj typ av alarm man vill lägga till och sedan vilken larmnivå
        * Välj vilket alarm du vill lägga till
        1. CPU
        2. RAM
        3. Disk
            * Ange sedan en larmnivå 0-100
    2. Ta bort alarm - Välj vilket alarm du vill ta bort
        * Välj vilket alarm du vill ta bort
    3. Visa alla aktiva larm
    4. Skicka larm till Monitoreringssystem - Sparar alarmen till en fil som monitoreringssystemet kan läsa ifrån
    5. Avsluta - Återgår till hvuudmenyn

2. Starta Monitoriseringssystem
    Om användaren väljer val 2 så kommer man till Monitoreringssystem där man blir presenterad med en ny meny med 3 olika val:
    1. Ladda alarm - Hämtar larmnivåer från filen som Larm-konfigurationssystemet sparar värdena i.
    2. Starta monitoreringssession - Här får man välja hur man ska monitorera, om det är i X antal sekunder, X antal iterationer eller oändligt. När man har valt det så startar monitoriseringen och man ser resultatet i terminalen.
        * Välj hur du vill bestämma längd av monitorisering
        1. Tid
            * Ange sedan längden i sekunder
        2. Iterationer
            * Ange sedan längden i iterationer
        3. Oändligt
            * Avbryts med CTRL-C
    3. Återgå till huvudmenyn

3. Avsluta


Det finns även möjlighet att köra programmet med kommandoradargument, här ett exempel:
- `py huvudmeny.py 1 1 1 50 5 2 1 2 1 10`

Det här exemplet lägger till ett CPU-alarm på 50% för att sedan gå in i monitoreringssystemet och laddar in alarmet och startar sedan en monitoreringssession i 10 sekunder.


## Filer
- `huvudmeny.py` - huvudmeny för programmet
- `Monitoreringssystem.py` – övervakning och larmkontroll.
- `menu.py` – meny för larmkonfiguration.
- `alarm.py` – hantering och lagring av larm.
- `loggsystem.py` – loggning av händelser och larm.
- `requirements.txt` – visar vilka externa paket som behövs för att köra programmet.
- `user_input.py` - möjliggör CLI
