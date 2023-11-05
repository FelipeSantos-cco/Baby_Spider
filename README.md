# BABY SPIDER 🕷️🕸️ <br>Em Desenvolvimento 🚧
<p align="center">
<img src="https://github.com/FelipeSantos-cco/Baby_Spider/assets/125617308/2991bc54-b302-4cc2-b3d3-a313aa87dff1" width=17% height=17%> 
</p>

## Crawler em formato de utilitário de linha de comando para extrair dados de forma mais rápida e simples.

## Modo de usar
Antes de tudo, de uma olhada no help:
```sh
python spider.py -h
```

Se você tiver o link de download de um CSV por exemplo, dentro do repositório `Baby_Spider`, faça:
```sh
python spider.py --url "https://exemplo.com/arquivo.csv" -e csv
```

Se o arquivo for um JSON ou qualquer outro formato, substitua o valor do parametro `-e`
```sh
python spider.py --url "https://exemplo.com/arquivo.json" -e json
```

e se quiser criar um script importando esse arquivo, adicione o `--r-script` para gerar automaticamente:
```sh
python spider.py --url "https://exemplo.com/arquivo.csv" -e csv --r-script
```

Caso você tem o link de um ZIP, faça o seguinte comando:
```sh
python spider.py --url "https://exemplo.com/pacote.zip" -z
```

Se quiser extrair todo o conteúdo desse pacote zip, adicione o parametro --zip-all
```sh
python spider.py --url "https://exemplo.com/pacote.zip" -z --zip-all
```


## "Instalação"
1. Clone o projeto
```sh
git clone https://github.com/FelipeSantos-cco/Baby_Spider.git
```
2. Entre no repositório que foi clonado
```sh
cd Baby_Spider
```
3. Instale as dependencias do projeto
```sh
pip install -r requirements.txt
```

### Desenvolvimento em:
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>

---

### Caso queira contribuiur ao projeto, faça um fork que ficarei extremamente feliz ❤️😄
