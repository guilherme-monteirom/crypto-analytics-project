# 🚀 Crypto Analytics Platform

Projeto pessoal desenvolvido para estudar e aplicar conceitos de Analytics, Analytics Engineering e Engenharia de Dados utilizando dados do mercado de criptomoedas.

A solução realiza a coleta automática de dados através da API da CoinGecko, armazena informações em PostgreSQL utilizando uma arquitetura em camadas (RAW e SILVER), aplica transformações com Python e Pandas e disponibiliza uma interface interativa em Streamlit para registro de movimentações e futura análise patrimonial.

---

# 🎯 Objetivo

O objetivo deste projeto é construir uma solução analítica completa para praticar:

- SQL
- Python
- Pandas
- PostgreSQL
- APIs REST
- Git e GitHub
- ETL / ELT
- Arquitetura Medallion
- Analytics Engineering
- Streamlit
- Visualização e análise de dados

Além do aprendizado técnico, o projeto está evoluindo para um Portfolio Analytics capaz de registrar operações, acompanhar patrimônio e analisar a evolução da carteira ao longo do tempo.

---

# 🏗️ Arquitetura Atual

```text
CoinGecko API
        │
        ▼
RAW Layer (PostgreSQL + JSONB)
        │
        ▼
Transformações em Pandas
        │
        ▼
SILVER Layer (PostgreSQL)
        │
        ▼
Streamlit Application
        │
        ▼
Portfolio Analytics
```

---

# 📦 Camadas do Projeto

## RAW Layer

Responsável por armazenar os dados exatamente como retornados pela API.

Características:

- PostgreSQL
- Coluna JSONB
- Histórico completo de coletas
- Sem transformação de negócio
- Persistência incremental

---

## SILVER Layer

Responsável pela transformação e padronização dos dados.

Características:

- Estrutura tabular
- Dados normalizados
- Inclusão de rastreabilidade através do `id_raw`
- Carga incremental
- Transformações realizadas com Pandas

---

## Portfolio Operations

Módulo responsável pelo registro das operações da carteira.

Funcionalidades atuais:

- Cadastro de compras
- Cadastro de vendas
- Persistência em PostgreSQL
- Validação de campos
- Resumo da operação registrada
- Integração com Streamlit

---

# 🔄 Carga Incremental

O processamento da camada SILVER utiliza carga incremental.

Fluxo:

```text
Consultar maior id_raw processado
        │
        ▼
Ler apenas novos registros da RAW
        │
        ▼
Transformar em Pandas
        │
        ▼
Inserir na SILVER
```

Isso evita reprocessamento desnecessário e permite crescimento escalável da base de dados.

---

# 📊 Dados Coletados

Atualmente o projeto armazena:

- Preço dos ativos
- Market Cap
- Valores em USD
- Valores em EUR
- Valores em BRL
- Data e hora da coleta
- Identificação dos ativos
- Histórico temporal

---

# 🖥️ Aplicação Streamlit

O projeto possui uma aplicação web desenvolvida em Streamlit.

Módulos atuais:

- Dashboard
- Movimentações
- Mercado

Em evolução para:

- Carteira
- Patrimônio
- Rentabilidade
- Performance histórica
- Indicadores analíticos

---

# 🛠️ Tecnologias Utilizadas

### Engenharia e Analytics

- Python
- Pandas
- SQL
- PostgreSQL
- JSONB
- Requests
- Psycopg2

### Aplicação

- Streamlit

### Segurança

- python-dotenv
- Variáveis de ambiente (.env)

### Versionamento

- Git
- GitHub

---

# 📁 Estrutura Atual

```text
crypto-analytics/
│
├── app.py
│
├── pages/
│   ├── dashboard.py
│   ├── movimentacoes.py
│   └── mercado.py
│
├── src/
│   ├── coleta_crypto_raw.py
│   └── transform_silver.py
│
├── notebooks/
│
├── .streamlit/
│   └── config.toml
│
├── README.md
├── .gitignore
└── .env
```

---

# 🔒 Segurança

Nenhuma credencial é armazenada diretamente no código.

O projeto utiliza:

- `.env`
- `python-dotenv`
- `os.getenv()`

Arquivos sensíveis são ignorados automaticamente através do `.gitignore`.

---

# 🚧 Roadmap

## Próximas Evoluções

### Portfolio Analytics

- Cálculo de posição por ativo
- Preço médio
- Patrimônio atual
- Rentabilidade
- Evolução temporal da carteira

### Dashboard Analytics

- KPIs de patrimônio
- Distribuição por ativo
- Evolução histórica
- Indicadores de desempenho

### Camada GOLD

- Métricas agregadas
- Modelagem para consumo analítico
- Integração futura com Power BI

### Cloud & Deploy

- Azure
- Hospedagem da aplicação
- Evolução para arquitetura em nuvem

---

# 👨‍💻 Autor

**Guilherme Monteiro Morgado de Melo**

Projeto criado para desenvolvimento profissional com foco em Analytics, Analytics Engineering e Engenharia de Dados.

