import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)


logging.debug("Verificando os dados do sistema")
logging.info("Sistema iniciado com sucesso")
logging.warning("Atenção: situação inesperada")
logging.error("Não foi possível executar a operação")
logging.critical("Falha crítica no sistema")
