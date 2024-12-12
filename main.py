def main() -> None:
    print("main")

    run_mode = "print_files"
    # Valores válidos:
    # run -> execução normal
    # debug -> execução com prints de debug (implemente no seu código)
    # print_files -> execução gera um arquivo JSON com o conteúdo dos arquivos da variável file_paths.
    #   o arquivo será gerado na pasta output_folder. 
    #   o JSON serve para ser compartilhado com LLMs como chatgpt e claude!!!

    log_file = "output.log"
    # Neste arquivo, serão salvas todas as saídas do programa.
    # Tudo o que é impresso no console, também será salvo neste arquivo.
    log_file_last_run = "output_last_run.log"
    # Neste arquivo, será salva somente a última execução do programa.

    if run_mode == "print_files":
        from dev_utils.print_json_for_llm_help import print_json_for_llm_help
        # Caminhos podem ser:
        # 1- relativos ao diretorio do projeto
        # 2- absolutos
        file_paths = [
            r"main.py",
            r"README.md",
            r"shared_vars.py",
            r"dev_utils/console_log.py",
            r"dev_utils/print_json_for_llm_help.py",
            r"dev_utils/time_stamp.py",
            r"output.log",
            r"output_last_run.log",
            ]
        output_folder = f"dev_utils/print_json_for_llm_help"
        print_json_for_llm_help(file_paths, output_folder)
        return

    # Variáveis globais substituem argumentos repetitivos.
    # Para acessar as variáveis globais, use:
    import shared_vars
    shared_vars.shared_state.run_mode = run_mode

    # Iniciando a escrita no arquivo de log
    from dev_utils.console_log import start_logging, stop_logging
    start_logging(log_file)

    # Importando a função de timestamp
    from dev_utils.time_stamp import time_stamp_str

    try:
        print(time_stamp_str() + "Starting Project")
        # >>>> Start your code here <<<<
    finally:
        stop_logging(log_file, log_file_last_run)

    
if __name__ == "__main__":
    print("starting Main.py")
    main()