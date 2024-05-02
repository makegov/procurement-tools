
class Socioeconomic:
    """"""

    categories_descriptions = {
        "HUBZone": "HUBZone",
        "SDVOSB": "Service-Disabled Veteran-Owned Small Business",
        "SDB": "Small Disadvantaged Business",
        "VOSB": "Veteran-Owned Small Business",
        "WOSB": "Woman-Owned Small Business",
        "SB": "Other Small Business",
    }
    categories_map = {
        "05": "SB",  # Alaskan Native Corporation Owned Firm
        "1B": "SB",  # Tribally Owned Firm
        "A2": "WOSB",  # Woman Owned Business
        "8C": "WOSB",  # Joint Venture Women-Owned Small Business
        "8D": "WOSB",  # Economically Disadvantaged Joint Venture Women-Owned Small Business
        "8W": "WOSB",  # Economically Disadvantaged Women-Owned Small Business
        "A5": "VOSB",  # Veteran Owned Business
        "QF": "SDVOSB",  # Service-Disabled Veteran Owned Business
        "XX": "HUBZONE",  # SBA Certified HUBZone Small Business Concern
        "JX": "HUBZONE",  # Self Certified HUBZone Joint Venture
        "A6": "SDB",  # SBA 8(a) Participant
        "27": "SDB",  # Self Certified Small Disadvantaged Business
    }

    business_types_map = {}
    for k, v in categories_map.items():
        business_types_map[v] = business_types_map.get(v, []) + [k]

    @staticmethod
    def get_business_types_from_categories(categories):
        """Takes a list of broad socioeconomic categories and returns a list of business_types"""
        if isinstance(
            categories, str
        ):  # But I'm nice, so I'm willing to accept strings too
            categories = [categories]
        categories = [c.upper() for c in categories]
        return [
            business_type
            for business_type, category in Socioeconomic.categories_map.items()
            if category in categories
        ]

    @staticmethod
    def get_category_for_business_type(business_type):
        """Takes single business_type and returns its broad socioeconomic category, if it has one"""
        return Socioeconomic.categories_map.get(business_type)

    @staticmethod
    def get_categories_from_business_types(business_types):
        """Takes a list of business_types and returns broad socioeconomic categories"""
        result = []

        for business_type in business_types:
            if business_type in Socioeconomic.categories_map:
                category = Socioeconomic.categories_map[business_type]
                if category not in result:
                    result.append(category)
        return result
