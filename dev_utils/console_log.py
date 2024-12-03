import sys
import os

class DualOutput:
    def __init__(self, arquivo):
        self.terminal = sys.__stdout__
        self.arquivo = open(arquivo, 'a')

    def write(self, mensagem):
        self.terminal.write(mensagem)
        self.arquivo.write(mensagem)

    def flush(self):
        self.terminal.flush()
        self.arquivo.flush()

    def close(self):
        self.arquivo.close()

# Variável para armazenar o stdout original
_stdout_original = sys.stdout

def start_logging(log_file: str = 'output.log') -> None:
    """Inicia o redirecionamento de stdout para o arquivo especificado."""
    global _stdout_original
    sys.stdout = DualOutput(log_file)
    print("<output_log>")

def stop_logging(log_file: str = 'output.log', log_file_last_run: str = 'output_last_run.log') -> None:
    """Para o redirecionamento de stdout e restaura o stdout original."""
    global _stdout_original
    if isinstance(sys.stdout, DualOutput):
        print("</output_log>")
        sys.stdout.close()
        sys.stdout = _stdout_original
    # Salva a última execução após parar o logging
    save_last_execution(log_file, log_file_last_run)

def save_last_execution(log_file, log_file_last_run) -> None:
    """
    Salva o conteúdo da última execução delimitado por <output_log> e </output_log>
    em um arquivo separado.
    """
    if not os.path.exists(log_file):
        print(f"Log file {log_file} does not exist.")
        return

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Encontrar índices das marcações
        start_indices = [i for i, line in enumerate(lines) if '<output_log>' in line]
        end_indices = [i for i, line in enumerate(lines) if '</output_log>' in line]

        if not start_indices or not end_indices:
            print("Não foram encontrados blocos de execução no log.")
            return

        # Assumindo que cada <output_log> tem um correspondente </output_log>
        last_start = start_indices[-1]
        last_end = end_indices[-1]

        if last_end < last_start:
            print("Marcação </output_log> encontrada antes de <output_log>.")
            return

        # Extrair conteúdo da última execução
        last_execution = ''.join(lines[last_start:last_end + 1])

        # Salvar no arquivo separado
        with open(log_file_last_run, 'w', encoding='utf-8') as f:
            f.write(last_execution)

    except Exception as e:
        print(f"Ocorreu um erro ao salvar a última execução: {e}")
