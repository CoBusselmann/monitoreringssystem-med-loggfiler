

VALID_CATEGORIES = ("cpu", "ram", "disk")

class AlarmRule:
    def __init__(self, category, level):
        category = category.lower()
        # Gör om till små bokstäver så att användaren kan skriva med stora och små bokstäver med samma resultat.
        if category not in VALID_CATEGORIES:
            raise ValueError(f"Ogiltig kategori: {category}. Välj cpu, ram eller disk.")
            #Felhanterar input som ej är godkänt.
        level = float(level)
        #Felhantering för % nivån som användaren använder.
        if level < 0 or level > 100:
            raise ValueError("Nivån måste vara mellan 0 och 100.")
        #Sparar värdena i objekt
        self.category = category
        self.level = level