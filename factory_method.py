from abc import ABC, abstractmethod


class Localizer(ABC):
    """Abstract Product: Represents translations for specific languages."""

    @abstractmethod
    def localize(self, msg):
        """Translate the given message."""
        pass


class FrenchLocalizer(Localizer):
    """Concrete Product: Represents translations for French."""
    def __init__(self):
        self.translations = {
          "car": "voiture",
          "bike": "bicyclette",
          "cycle": "cyclette"
        }

    def localize(self, msg):
        """Translate the message to French."""
        return self.translations.get(msg, msg)

class SpanishLocalizer(Localizer):
    """Concrete Product: Represents translations for Spanish."""
    def __init__(self):
        self.translations = {
          "car": "coche",
          "bike": "bicicleta",
          "cycle": "ciclo"
        }

    def localize(self, msg):
        """Translate the message to Spanish."""
        return self.translations.get(msg, msg)

class EnglishLocalizer(Localizer):
    """Concrete Product: Represents translations for English."""
    def localize(self, msg):
        """Return the message as is (no translation)."""
        return msg
    
a = SpanishLocalizer()
car = a.localize('car')
print(car)