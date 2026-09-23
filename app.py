# Class Pai
class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(f"Titulo:",self.titulo, "\nGenero:",self.genero)

# Classe Filha-1
class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print("FILME:", self.titulo,
              "| Genero:", self.genero,
              "| Duracao:", self.duracao,"min")

# Class Filha-2
class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print("SERIE:", self.titulo,
              "| Genero:", self.genero,
              "| Temporadas:", self.temporadas)

# Classe Filha-3
class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print("DOCUMENTARIO:", self.titulo,
              "| Genero:", self.genero,
              "| Tema:", self.tema)
class Podcast(Conteudo):
    def __init__(self,titulo,genero,apresentador):
        super().__init__(titulo,genero)
        self.apresentador = apresentador

    def exibir_info(self):
        super().exibir_info()
        print(f"Apresentador:",self.apresentador)

# Instanciamenro
catalogo = [
    Filme("Interestelar", "Ficcao", 169),
    Filme("Procurando Dore", "Animação", "179\n"),
    Serie("Stranger Things", "Ficcao", 4),
    Serie("La casa de Papel","Suspense","5\n"),
    Documentario("Nosso Planeta", "Natureza", "Vida selvagem"),
    Documentario("Animal Planet","Natureza","Vida selvagem\n"),
    Podcast("Pod Pa","Comedia","Monark"),
    Podcast("Flow","Informação","Alberto")
]
for item in catalogo:
    item.exibir_info()
