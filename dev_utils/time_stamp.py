from datetime import datetime

def time_stamp_str() -> str:
    # Retorna uma string com um timestamp no formato: "YYYYy_MMm_DDd_HHh_MMm_SSs_mmmms"
    # Usado para marcar o tempo de execução de funções
    now = datetime.now()
    milliseconds = now.microsecond / 1000
    milliseconds_formatted = f"{int(milliseconds // 1):03}.{int((milliseconds % 1) * 1000):03}"
    return f"{now.year}y_{now.month:02}m_{now.day:02}d_{now.hour:02}h_{now.minute:02}m_{now.second:02}s_{milliseconds_formatted}ms: "