from .far import FAR
from .periodic_table import PeriodicTable
from .sam import SAM
from .sbir import SBIR
from .uei import UEI
from .usaspending import USASpending
from .glossary import Glossary
from .socioeconomic import Socioeconomic
from .translations import interpret_reason_for_modification

Glossary()

__all__ = [
    "FAR",
    "Glossary",
    "PeriodicTable",
    "SAM",
    "SBIR",
    "Socioeconomic",
    "UEI",
    "USASpending",
    "interpret_reason_for_modification",
]
3