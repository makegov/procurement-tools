
MOD_DICT = {
    "A": {
        "fpds_description": "Additional Work (New Agreement, Justification Required)",
        "natural_language": "authorized additional work for",
    },
    "B": {
        "fpds_description": "Supplemental Agreement for work within scope",
        "natural_language": "agreed to modifications for within-scope work to",
    },
    "C": {
        "fpds_description": "Funding Only Action",
        "natural_language": "issued a funding-only action for",
    },
    "D": {
        "fpds_description": "Change Order",
        "natural_language": "issued a change order to",
    },
    "E": {
        "fpds_description": "Terminate for Default (complete or partial)",
        "natural_language": "terminated for default",
    },
    "F": {
        "fpds_description": "Terminate for Convenience (complete or partial)",
        "natural_language": "terminated for convenience",
    },
    "G": {
        "fpds_description": "Exercise an Option",
        "natural_language": "exercised an option to",
    },
    "H": {
        "fpds_description": "Definitize Letter Contract",
        "natural_language": "definitized a letter contract for",
    },
    "J": {
        "fpds_description": "Novation Agreement",
        "natural_language": "agreed to a novation for",
    },
    "K": {
        "fpds_description": "Close Out",
        "natural_language": "closed out"
    },
    "L": {
        "fpds_description": "Definitize Change Order",
        "natural_language": "definitized a change order to",
    },
    "M": {
        "fpds_description": "Other Administrative Action",
        "natural_language": "executed an administrative action for",
    },
    "N": {
        "fpds_description": "Legal Contract Cancellation",
        "natural_language": "canceled",
    },
    "P": {
        "fpds_description": "Rerepresentation of Non-Novated Merger/Acquisition",
        "natural_language": "modified the contractor's representations for",
    },
    "R": {
        "fpds_description": "Rerepresentation",
        "natural_language": "modified the contractor's representations for",
    },
    "S": {
        "fpds_description": "Change PIID",
        "natural_language": "changed the PIID to",
    },
    "T": {
        "fpds_description": "Transfer Action",
        "natural_language": "transferred"
    },
    "V": {
        "fpds_description": "Unique Entity ID or Legal Business Name Change - Non-Novation",
        "natural_language": "modified contractor information for",
    },
    "W": {
        "fpds_description": "Entity Address Change",
        "natural_language": "modified contractor information for",
    },
    "X": {
        "fpds_description": "Terminate for Cause",
        "natural_language": "terminated for cause",
    },
    "Y": {
        "fpds_description": "Add Subcontract Plan",
        "natural_language": "added a subcontract plan to",
    },
}

def interpret_reason_for_modification(code: str) -> str:
    return MOD_DICT[code]["natural_language"]
