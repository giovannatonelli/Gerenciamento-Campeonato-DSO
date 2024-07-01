from DAOS.dao import DAO
from entidades.arbitro import Arbitro

class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__('arbitros.pkl')

    def add(self, arbitro: Arbitro):
        if((arbitro is not None) and isinstance(arbitro, Arbitro) and isinstance (arbitro.cpf, str)):
            super().add(arbitro.cpf, arbitro)
    
    def update(self, arbitro: Arbitro):
        if((arbitro is not None) and isinstance(arbitro, Arbitro) and isinstance (arbitro.cpf, str)):
            super().update(arbitro.cpf, arbitro)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)
