import argparse
import requests


parser = argparse.ArgumentParser(prog="Spider",
                                 description='''
                                 Programa de Download de arquivos e automação da criação de scripts em R
                                 ''')

# Argumentos
parser.add_argument("-u", "--url",
                    type=str,
                    help="URL para Download")

parser.add_argument("--r-script",
                    type=str,
                    help="Nome do script R para automação")

args = parser.parse_args()


def download(url):
    print(url)
    try:
        with requests.Session() as req:
            print("Iniciando Download")
            arquivo = req.get(url)

            with open("arquivo", 'wb') as arq:
                arq.write(download.content)

    except ConnectionError as erro:
        print("Não foi possivel fazer o Download"+erro)

    except ConnectionAbortedError as erro:
        print("Conexão abortada"+erro)

download(args.url)
