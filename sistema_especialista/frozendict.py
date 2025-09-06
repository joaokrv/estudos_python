"""
Shim minimal para a interface `frozendict.frozendict` usada por `experta`.
Este arquivo existe para contornar incompatibilidades de versões do pacote
`frozendict` com versões mais recentes do Python (collections.Mapping removido).

Implementação mínima: objeto imutável que implementa Mapping e é hashable.
"""
from collections.abc import Mapping

class frozendict(Mapping):
    """Implementação simples e imutável de um dicionário.

    Observação: é intencionalmente pequena — suficiente para uso em `experta`.
    """
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)
        self._hash = None

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"frozendict({self._data!r})"

    def __hash__(self):
        if self._hash is None:
            # ordena para garantir hash estável
            items = tuple(sorted(self._data.items()))
            self._hash = hash(items)
        return self._hash

    # métodos utilitários mínimos
    def to_dict(self):
        return dict(self._data)

    def copy(self):
        return frozendict(self._data)
