# shared.py
# Este arquivo é utilizado para compartilhar variáveis entre os arquivos do projeto.
class SharedState:
    def __init__(self):
        self.run_mode = ""

shared_state = SharedState()
