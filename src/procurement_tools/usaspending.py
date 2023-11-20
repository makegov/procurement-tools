from hashlib import md5
import uuid


class USASpending:
    @classmethod
    def convert_uei_to_hash(cls, uei: str, level: str = "P") -> str:
        """Convert a UEI into a Hash for USASpending.gov"""
        uei_string = ("uei-" + uei).upper()
        m = md5(bytes(uei_string.encode()))
        return f"{str(uuid.UUID(m.hexdigest()))}-{level}"

    @classmethod
    def get_usaspending_URL(cls, uei: str, level: str = "P") -> str:
        """Replaces a UEI with a USASpending.gov recipient profile URL"""
        uei_hash = cls.convert_uei_to_hash(uei, level)
        return f"https://www.usaspending.gov/recipient/{uei_hash}/latest"
