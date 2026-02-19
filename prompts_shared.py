"""
Shared prompt fragments used by multiple order-format prompt files.
"""


def build_shared_output_contract() -> str:
    return (
        "=== REQUIRED OUTPUT FIELD NAMES ===\n"
        "Use these exact German field names:\n"
        "Header: ticket_number, kundennummer, adressnummer, kom_nr, kom_name, liefertermin, wunschtermin, bestelldatum, lieferanschrift, tour, store_name, store_address, seller, iln_anl, iln_fil, human_review_needed, reply_needed, post_case\n"
        "Items: artikelnummer, modellnummer, menge, furncloud_id\n"
        "\n"
        "=== UNIVERSAL ARTIKELNUMMER vs MODELLNUMMER RULE ===\n"
        "First character decides:\n"
        "- Starts with digit => artikelnummer\n"
        "- Starts with letter => modellnummer\n"
        "Apply this after splitting combined codes by '-', '/', or spaces.\n"
        "\n"
        "Label mapping:\n"
        "- TYP/TY value can be artikelnummer or a combined code to split\n"
        "- AUSF/AF/AUF value maps to modellnummer\n"
        "- Ignore ArtNr and Cikks for artikelnummer/modellnummer\n"
        "- For plus-joined code like 'SI9191TA-66364+ZB00-46518': use only first code before '+'\n"
        "\n"
        "=== EXTRACTION RULES ===\n"
        "1. Include all required keys, even if empty (empty string and confidence=0.0)\n"
        "2. Source values must be one of: pdf, email, image, derived\n"
        "3. Keep Liefertermin and Wunschtermin as raw text\n"
        "4. Extract all line items, do not collapse rows\n"
        "5. If furncloud id appears once and applies to all items, copy to all items\n"
        "6. Detect drawing marker '+++ WEITERE INFO SIEHE ZEICHNUNG+++' => header.human_review_needed.value=true\n"
        "7. Detect swap request like 'STATT TYP ... BITTE TYP ...' => header.reply_needed.value=true\n"
        "8. Detect postal-mail instruction ('per Post', 'per Brief') => header.post_case.value=true\n"
        "9. Return only valid JSON; do not add markdown text\n"
        "\n"
        "=== REQUIRED JSON STRUCTURE ===\n"
        "{\n"
        '  "message_id": "string",\n'
        '  "received_at": "ISO-8601",\n'
        '  "header": {\n'
        '    "ticket_number": {"value": "", "source": "email|derived", "confidence": 0.0},\n'
        '    "kundennummer": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "adressnummer": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "kom_nr": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "kom_name": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "liefertermin": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "wunschtermin": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "bestelldatum": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "lieferanschrift": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "tour": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "store_name": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "store_address": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "seller": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "iln_anl": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "iln_fil": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '    "human_review_needed": {"value": false, "source": "derived", "confidence": 1.0},\n'
        '    "reply_needed": {"value": false, "source": "derived", "confidence": 1.0},\n'
        '    "post_case": {"value": false, "source": "derived", "confidence": 1.0}\n'
        '  },\n'
        '  "items": [\n'
        '    {\n'
        '      "line_no": 1,\n'
        '      "artikelnummer": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '      "modellnummer": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '      "menge": {"value": 1, "source": "pdf|email|image|derived", "confidence": 0.0},\n'
        '      "furncloud_id": {"value": "", "source": "pdf|email|image|derived", "confidence": 0.0}\n'
        '    }\n'
        '  ],\n'
        '  "status": "ok|partial|failed",\n'
        '  "warnings": [],\n'
        '  "errors": []\n'
        "}\n"
    )
