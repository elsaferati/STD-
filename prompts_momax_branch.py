"""
Prompt for the pre-classified MOMAX branch Lagerbestellung format.
"""

from prompts_shared import build_shared_output_contract


def build_user_instructions_momax_branch(source_priority: list[str]) -> str:
    return (
        "=== PRE-CLASSIFIED ORDER FORMAT ===\n"
        "This order is classified as: momax_branch.\n"
        "\n"
        "=== TASK ===\n"
        "Extract a MOEMAX/MOMAX branch Lagerbestellung order (email-first format).\n"
        f"SOURCE TRUST PRIORITY: {', '.join(source_priority).upper()}\n"
        "If conflicting values exist, trust sources in this order.\n"
        "\n"
        "=== MOMAX BRANCH SIGNALS ===\n"
        "- 'Lagerbestellung' in subject/body\n"
        "- Branch-store ordering language\n"
        "- TY/TYP and AUSF/AF style item encoding\n"
        "- Often email-only, but attachments may still exist; include valid extracted data\n"
        "\n"
        "=== FIELD MAPPING (MOMAX BRANCH) ===\n"
        "- 'Lagerbestellung' value => kom_nr\n"
        "- ILN fields map same as standard: ILN-Anl => iln_anl + adressnummer, ILN-Fil => iln_fil\n"
        "- 'Sachbearbeiter/in' or seller labels => seller\n"
        "- 'Filiale' and nearby branch address => store_name, store_address\n"
        "- Keep liefertermin/wunschtermin raw\n"
        "- If no explicit lieferanschrift is provided, infer from branch/delivery block when clear\n"
        "\n"
        "=== ITEM EXTRACTION (MOMAX BRANCH) ===\n"
        "- TY is synonym of TYP\n"
        "- TYP/TY with slash or hyphen can carry both model and article; split then apply universal rule\n"
        "- TYP with single numeric value => artikelnummer and empty modellnummer\n"
        "- Use AUSF/AF/AUF as modellnummer when present\n"
        "- Ignore ArtNr/Cikks for artikelnummer/modellnummer\n"
        "- Example: 'TYP: 82347/INEG61EG12' => artikelnummer 82347, modellnummer INEG61EG12\n"
        "- Example: 'TYP: ZB 00 84006' => modellnummer ZB00, artikelnummer 84006\n"
        "\n"
        "=== MOMAX-SPECIFIC GUARDRAILS ===\n"
        "- Do not reinterpret Lagerbestellung as generic standard XXLUTZ format\n"
        "- Favor branch-email item rows when present and coherent\n"
        "- Preserve branch context in kom_name/store_name if explicitly stated\n"
        "\n"
        + build_shared_output_contract()
    )
