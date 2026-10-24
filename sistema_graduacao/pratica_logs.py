import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%d/%m/%Y %H:%M:%S"
)

logger = logging.getLogger(__name__)

logging.info("Iniciando cadastro")

try:
    numero = 10
    resultado = numero / 0

except ZeroDivisionError:
    logger.exception("Não é possível fazer divisão por 0")

logger.info("Programa finalizado")