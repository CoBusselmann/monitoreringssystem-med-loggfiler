
import logging
from datetime import datetime
from pathlib import Path


class Loggsystem:
    def __init__(self):
        # Skapar mappen logs om den inte redan finns
        self.loggmapp = Path("logs")
        self.loggmapp.mkdir(exist_ok=True)

        # Skapar ett unikt filnamn med datum, tid och ID
        tid = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")

        self.filnamn = self.loggmapp / f"{tid}.log"

        # Skapar en logger för just denna session
        self.logger = logging.getLogger(f"logg_{tid}")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        # Bestämmer att loggen ska skrivas till fil
        try:
            self.filhanterare = logging.FileHandler(
            self.filnamn, encoding="utf-8"
            )
        except OSError as fel:
            print(f"Kunde inte skapa loggfilen: {fel}")
            raise

        # Varje loggrad får datum, tid, typ och meddelande
        formatmall = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        self.filhanterare.setFormatter(formatmall)
        self.logger.addHandler(self.filhanterare)

        self.info("Loggning har startat")

    def info(self, meddelande):
        # Loggar information som visas för användaren
        self.logger.info(meddelande)

    def anvandarval(self, meny, val):
        # Sparar vilket menyval användaren gjorde
        self.logger.info(f"ANVÄNDARVAL | {meny}: {val}")

    def funktion(self, namn):
        # Loggar när en funktion startas
        self.logger.info(f"FUNKTION | {namn}")

    def matning(self, cpu, ram, disk):
        # Loggar värden från monitoreringssystemet
        self.logger.info(
            f"MÄTNING | CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%"
        )

    def larm(self, kategori, niva):
        # Loggar när ett larm aktiveras
        self.logger.warning(
            f"LARM | {kategori.upper()} över {niva}%"
        )

    def data_laddad(self, data):
        # Loggar data som laddats från en fil
        self.logger.info(f"DATA LADDAD | {data}")

    def data_sparad(self, data):
        # Loggar data som sparats till en fil
        self.logger.info(f"DATA SPARAD | {data}")

    def fel(self, meddelande):
        # Loggar fel och felmeddelanden
        self.logger.error(meddelande)

    def avsluta(self):
        # Skriver sista raden och stänger loggfilen
        self.info("Loggsystem avslutat")
        self.logger.removeHandler(self.filhanterare)
        self.filhanterare.close()
