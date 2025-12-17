"""
Modulo responsabile della persistenza dei dati.
Attualmente supporta il salvataggio su CSV.
"""

import csv
from pathlib import Path
from typing import Iterable, Dict, Any, List


DEFAULT_COLUMNS: List[str] = [
    "library_id",
    "start_date",
    "active_time",
    "platforms",
    "description",
    "brand",
    "product_name",
    "img",
    "link",
]


def normalize_platforms(platforms: Any, separator: str = ",") -> str:
    """
    Converte platforms in una stringa CSV-safe.
    Atteso: set / list / tuple di stringhe.
    """
    if not platforms:
        return ""
    try:
        return separator.join(sorted(platforms))
    except TypeError:
        return str(platforms)


def prepare_row(card: Dict[str, Any], columns: List[str]) -> Dict[str, Any]:
    """
    Restituisce una riga pronta per il CSV,
    garantendo la presenza di tutte le colonne.
    """
    row = {}
    for col in columns:
        value = card.get(col, "")

        if col == "platforms":
            value = normalize_platforms(value)
        row[col] = value
    return row


def save_to_csv(
    data: Iterable[Dict[str, Any]],
    output_path: str | Path,
    columns: List[str] = DEFAULT_COLUMNS,
    overwrite: bool = True,
    encoding: str = "utf-8",
) -> None:
    """
    Salva una collezione di card su file CSV.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    mode = "w" if overwrite else "a"

    with output_path.open(mode, newline="", encoding=encoding) as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter=";")

        if overwrite:
            writer.writeheader()

        for card in data:
            writer.writerow(prepare_row(card, columns))
