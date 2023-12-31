from dotenv import load_dotenv
import os

# Carrega o arquivo .env
load_dotenv(".env")

# Configurações da APP
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DEBUG = os.getenv("DEBUG")

# Configurações da API
URL_API = os.getenv("URL_API")
HEADERS_API = {'x-token': os.getenv("X_TOKEN"), 'x-key': os.getenv("X_KEY")}

# Configuração dos endpoints
ENDPOINT_LOGIN = os.getenv("ENDPOINT_LOGIN")
ENDPOINT_FUNCIONARIO = os.getenv("ENDPOINT_FUNCIONARIO")
ENDPOINT_CLIENTE = os.getenv("ENDPOINT_CLIENTE")
ENDPOINT_PRODUTO = os.getenv("ENDPOINT_PRODUTO")
ENDPOINT_AUTH = os.getenv("ENDPOINT_AUTH")

SESSION_TIME = os.getenv("SESSION_TIME")