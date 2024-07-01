from DAOS.dao import DAO
from entidades.equipe import Equipe

class EquipeCampeonatoDAO(DAO):
    def __init__(self):
        super().__init__('equipescampeonato.pkl')

    def add(self, equipe: Equipe):
        if((equipe is not None) and isinstance(equipe, Equipe) and isinstance (equipe.nome, str)):
            super().add(equipe.nome, equipe)
    
    def update(self, equipe: Equipe):
        if((equipe is not None) and isinstance(equipe, Equipe) and isinstance (equipe.nome, str)):
            super().update(equipe.nome, equipe)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)
