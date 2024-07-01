from DAOS.dao import DAO
from entidades.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance (aluno.matricula, str)):
            super().add(aluno.matricula, aluno)
    
    def update(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance (aluno.matricula, str)):
            super().update(aluno.matricula, aluno)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)
