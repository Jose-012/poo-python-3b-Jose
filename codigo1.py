class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(
            "CONTEUDO:",
            self.titulo,
            "| Genero:",
            self.genero,
        )


class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print(
            "FILME:",
            self.titulo,
            "| Gênero:",
            self.genero,
            "| Duração:",
            self.duracao,
            "min\n",
        )


class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print(
            "SERIE:",
            self.titulo,
            "| Genero:",
            self.genero,
            "| Temporadas:",
            self.temporadas,
            "\n",
        )


class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print(
            "DOCUMENTARIO:",
            self.titulo,
            "| Genero:",
            self.genero,
            "| Tema:",
            self.tema,
            "\n",
        )


class Podcast(Conteudo):
    def __init__(self, titulo, genero, apresentador):
        super().__init__(titulo, genero)
        self.apresentador = apresentador

    def exibir_info(self):
        print(
            "PODCAST:",
            self.titulo,
            "| Gênero:",
            self.genero,
            "| Apresentador:",
            self.apresentador,
            "\n",
        )


catalogo = [
    Filme("Vida", "Ficcao", 169),
    Filme("Gato de Botas", "Animacao", 90),
    Serie("Rick and Morty", "Ficcao", 4),
    Serie("Round 6", "Suspense", 2),
    Documentario("Discovery Channel", "Natureza", "Vida selvagem"),
    Podcast("PodPah!", "Comédia", "Monark"),
]

for item in catalogo:
    item.exibir_info()
