from __future__ import annotations
from pathlib import Path
from typing import List, Union

def load_spoiler_phrases(path: Union[str, Path]) -> List[str]:
    p = Path(path)
    phrases: List[str] = []
    for line in p.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            phrases.append(s)
    return phrases
