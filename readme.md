# Projeto Flask com API do Google Gemini

Este é um projeto de exemplo que demonstra como criar uma aplicação web simples com Flask que se integra à API do Google Gemini.
![image](https://github.com/user-attachments/assets/f1863149-f727-418c-863d-5bcf58ff5607)

## Requisitos

- Python 3.8 ou superior
- Git (para clonar o repositório)

## Configuração e Primeira Execução

Siga estas instruções para configurar e rodar o projeto localmente.

### 1. Clone o Repositório

```bash
git clone https://github.com/aeciobrito/ai-agents-study.git
cd <NOME_DA_PASTA_DO_PROJETO_QUE_NAO_SEI_COMO_FICA_SE_VIRA>
```

### 2. Crie e Ative o Ambiente Virtual

Um ambiente virtual (venv) isola as dependências do projeto, evitando conflitos com outras aplicações Python na sua máquina.

```bash
# Cria o ambiente virtual
python -m venv .venv
```

Agora, ative o ambiente. O comando varia dependendo do seu sistema operacional:
- Windows (PowerShell):

```bash
.\.venv\Scripts\Activate.ps1
```

- Windows (CMD):

```bash
.\.venv\Scripts\activate.bat
```

- macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Crie uma cópia do arquivo de exemplo .env.example e renomeie para .env:

- No Windows: copy .env.example .env

- No macOS/Linux: cp .env.example .env

Abra o arquivo .env e adicione suas chaves secretas:

```
# .env
GEMINI_API_KEY="COLE_SUA_CHAVE_API_DO_GEMINI_AQUI"
SECRET_KEY="PODE_GERAR_UMA_CHAVE_FORTE_AQUI"
```

### 5. Execute a Aplicação

Com o ambiente ativado e as variáveis configuradas, inicie o servidor Flask:

```bash
flask run
```
