import argparse
import requests
from random import randrange
from zipfile import ZipFile

print('''
 /$$$$$$$   /$$$$$$  /$$$$$$$  /$$     /$$        /$$$$$$  /$$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$__  $$ /$$__  $$| $$__  $$|  $$   /$$/       /$$__  $$| $$__  $$|_  $$_/| $$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$ \  $$ /$$/       | $$  \__/| $$  \ $$  | $$  | $$  \ $$| $$      | $$  \ $$
| $$$$$$$ | $$$$$$$$| $$$$$$$   \  $$$$/        |  $$$$$$ | $$$$$$$/  | $$  | $$  | $$| $$$$$   | $$$$$$$/
| $$__  $$| $$__  $$| $$__  $$   \  $$/          \____  $$| $$____/   | $$  | $$  | $$| $$__/   | $$__  $$
| $$  \ $$| $$  | $$| $$  \ $$    | $$           /$$  \ $$| $$        | $$  | $$  | $$| $$      | $$  \ $$
| $$$$$$$/| $$  | $$| $$$$$$$/    | $$          |  $$$$$$/| $$       /$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$
|_______/ |__/  |__/|_______/     |__/           \______/ |__/      |______/|_______/ |________/|__/  |__/
                                                                                                                        
\t\t\t\t            $               $           
\t\t\t\t          $$                 $$         
\t\t\t\t         $$                   $$        
\t\t\t\t        $$                     $$       
\t\t\t\t        $$                     $$       
\t\t\t\t        $$                     $$       
\t\t\t\t         $$                   $$        
\t\t\t\t     $$  $$                   $$  $$    
\t\t\t\t    $$   $$                   $$   $$   
\t\t\t\t   $$     $$                 $$     $$  
\t\t\t\t   $       $$$             $$$       $  
\t\t\t\t   $$       $$$           $$$       $$  
\t\t\t\t   $$$       $$$  $$$$$  $$$       $$$  
\t\t\t\t    $$$$$$    $$$$$$$$$$$$$   $$$$$$$   
\t\t\t\t         $$$$$$$$$$$$$$$$$$$$$$         
\t\t\t\t    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    
\t\t\t\t   $$$ $$$$$$$$$$$$$$$$$$$$$$$$$$ $$$   
\t\t\t\t  $$$         $$$$$$$$$$$$         $$$  
\t\t\t\t $$         $$$$$$$$$$$$$$$$$        $$ 
\t\t\t\t $$     $$$$$$$$$$$$$$$$$$$$$$$$     $$ 
\t\t\t\t$$     $$$  $$$$$$$$$$$$$$$$  $$$     $$
\t\t\t\t $$    $$   $$$$$$$  $$$$$$$   $$    $$ 
\t\t\t\t  $    $$   $$$$$$$  $$$$$$$   $$    $  
\t\t\t\t   $   $$   $$$$$$$$$$$$$$$$   $$   $   
\t\t\t\t    $  $$    $$$$$$$$$$$$$$    $$  $    
\t\t\t\t       $$     $$$$$$$$$$$$     $$       
\t\t\t\t       $$       $$$$$$$$       $$       
\t\t\t\t        $$                    $$        
''')

parser = argparse.ArgumentParser(prog="Spider",
                                 description='''
                                 \n~~ BABY SPIDER ~~
                                 \n[$] Programa de Download de arquivos e automação da criação de scripts em R\n
                                 \n[@] Felipe Santos <-> https://github.com/FelipeSantos-cco/
                                 ''')

# Argumentos
parser.add_argument("-u", "--url",
                    type=str,
                    help="URL para Download",
                    required=True)

parser.add_argument("-e", "--extencao",
                    type=str,
                    help="Extenção do arquivo")

parser.add_argument("-z", "--zip",
                    help="Nome do arquivo A SER EXTRAIDO do .zip (Nome IGUAL ao que está dentro do pacote)",
                    action='store_true')

parser.add_argument("--zip-all",
                    help="Extrai todo o conteúo do .zip",
                    action='store_true')

parser.add_argument("--r-script",
                    help="Nome do script R para automação com o sem endereço",
                    action='store_true')

args = parser.parse_args()


def download_arquivo(url, nomeArquivo):
    try:
        with requests.Session() as req:
            arquivo = req.get(url)

            with open(nomeArquivo, 'wb') as f:
                f.write(arquivo.content)
                print(f'[ :) ]=> Download concluído. Arquivo: {nomeArquivo}')

    except ConnectionError as erro:
        print("[ :( ]=> Não foi possivel fazer o Download !")
        print("[ :( ]=> Erro:\n" + erro)
        exit()


def download_zip(url, nomeZIP):
    try:
        with requests.Session() as req:
            arquivo = req.get(url)

            with open(nomeZIP, 'wb') as f:
                f.write(arquivo.content)
                print(f'[ :) ]=> Donwload concluído. Arquivo: {nomeZIP}')

    except ConnectionError as erro:
        print("[ :( ]=> Não foi possivel fazer o Download !")
        print("[ :( ]=> Erro:\n" + erro)
        exit()


def extrair_zip_all(nomeZIP):
    try:
        z = ZipFile(pacoteZIP, 'r')
        z.extractall()
        z.close
        print("[ :) ]=> Extração Total Completa")

    except FileExistsError as erro:
        print("[ :( ]=> Não foi possível extrair o arquivo !")
        print("[ :( ]=> Erro:\n" + erro)
        exit()


if getattr(args, "zip"):
    pacoteZIP = f'zip_ID_{randrange(10, 99)}.zip'
    download_zip(args.url, pacoteZIP)

    if getattr(args, "zip_all"):
        extrair_zip_all(pacoteZIP)

elif getattr(args, "url"):
    arquivo = f'arquivo_ID_{randrange(10, 99)}.{args.extencao}'
    download_arquivo(args.url, arquivo)

    if getattr(args, "r_script"):
        scriptR = f'script_ID_{randrange(10, 99)}.r'

        codigoR = f'dados <- read.csv({arquivo})\nView(dados)'

        arquivo = open(scriptR, "x", encoding="utf-8")
        arquivo = open(scriptR, "a")
        arquivo.write(codigoR)
        arquivo.close()
        print(f'[ :) ]=> Script R criado com sucesso. Script: {scriptR}')
