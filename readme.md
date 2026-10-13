# Web Path Finder

Script em Python para testar caminhos de uma aplicação web utilizando uma wordlist. O programa substitui o marcador `{hack}` na URL por cada entrada do arquivo, realiza requisições HTTP e compara o tamanho das respostas com uma requisição de referência para identificar possíveis caminhos relevantes.

## Funcionalidades

- Requisições HTTP com a biblioteca `requests`.
- Reutilização de conexões com `requests.Session()`.
- Leitura de wordlists linha por linha.
- Exibição do status HTTP e do tamanho da resposta.
- Comparação com uma resposta de referência.
- Opção para exibir somente resultados com tamanhos diferentes da referência.

## Requisitos

- Python 3.10 ou superior.
- Biblioteca `requests`.

## Instalação

Clone o repositório ou baixe os arquivos do projeto.

Instale a dependência:

```bash
python -m pip install requests
```

## Como usar

Execute o script passando três argumentos:

```bash
python main.py "<URL>" "<FILENAME>" "<CONDITION>"
```

### Parâmetros

| Parâmetro | Descrição |
|---|---|
| `url` | URL contendo o marcador `{hack}`, que será substituído por cada entrada da wordlist. |
| `filename` | Caminho do arquivo de texto com a wordlist. |
| `condition` | Use `True` para exibir somente respostas cujo tamanho seja diferente da referência. Qualquer outro valor exibe todos os resultados. |

### Exemplo

```bash
python main.py https://httpbin.org/{hack} wordlist.txt True
```

or

```bash
python main.py https://{hack}.httpbin.org/ wordlist.txt True
```

O arquivo `wordlist.txt` deve conter um caminho por linha:

```text
admin
login
dashboard
robots.txt
api
```

## Como funciona

1. O programa realiza uma requisição de referência substituindo `{hack}` por `9999`.
2. Registra o status HTTP e o tamanho da resposta de referência.
3. Lê cada entrada da wordlist.
4. Substitui `{hack}` pela entrada atual e realiza uma requisição.
5. Exibe o status HTTP e o tamanho da resposta.
6. Quando `condition` é `True`, mostra somente as respostas cujo tamanho difere da referência.

**Importante:** uma resposta com tamanho diferente não confirma, por si só, que um caminho existe. Redirecionamentos, páginas de erro personalizadas e conteúdo dinâmico também podem alterar o tamanho da resposta.

## Uso autorizado

Utilize a ferramenta somente em aplicações próprias ou em sistemas para os quais você tenha autorização explícita para realizar testes de segurança.

## Tecnologias

- Python
- Requests
- HTTP/HTTPS
