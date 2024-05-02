import os, yaml

SOURCES = [
    os.path.join(os.path.dirname(__file__), "data/18f_glossary.yml"),
    os.path.join(os.path.dirname(__file__), "data/agencies.yml"),
    os.path.join(os.path.dirname(__file__), "data/supplemental_glossary.yml"),
]

TERMS = {}
ACRONYMS = []

def load_terms(source):
    try:
        with open(source, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
            for k, v in data["glossary"].items():
                term = str(k).lower().strip()
                if term not in TERMS:
                    if str(k).isupper():
                        ACRONYMS.append(k)
                    v["term"] = str(k).strip()
                    v["description"] = v["description"].strip()
                    TERMS[term] = v
            
    except Exception as err:
        raise err

for source in SOURCES:
    load_terms(source)

ACRONYMS = sorted(ACRONYMS)


class Glossary:

    @staticmethod
    def get_acronyms():
        """returns a list of acronyms from the glossary"""
        return ACRONYMS
        
    @staticmethod
    def lookup_by_term(term):
        """ """
        term = term.lower()
        if TERMS.get(term):
            return [TERMS.get(term)]
        return []

    @staticmethod
    def lookup_by_term_fuzzy(text):
        """ """
        text = text.lower()
        return [
            item for item in TERMS.values() if text in item["description"].lower()
        ]

    @staticmethod
    def find_terms(term=""):
        """ """
        res = Glossary.lookup_by_term(term)
        return res
