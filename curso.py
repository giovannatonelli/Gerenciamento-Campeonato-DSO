class Curso:
    def __init__(self, codigo_curso, nome_curso):
        self.codigo_curso = codigo_curso
        self.nome_curso = nome_curso
        self.equipe = None  # Referência para a equipe associada ao curso

    def codigo_curso(self):
        return self.codigo_curso

    def codigo_curso(self, codigo_curso):
        self.codigo_curso = codigo_curso

    def nome_curso(self):
        return self.nome_curso

    def nome_curso(self, nome_curso):
        self.nome_curso = nome_curso

    def equipe(self):
        return self.equipe

    def equipe(self, equipe):
        self.equipe = equipe