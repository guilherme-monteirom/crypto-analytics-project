# Crypto Analytics Project

Projeto desenvolvido para coletar, armazenar e analisar dados do mercado de criptomoedas utilizando uma arquitetura de dados evolutiva.

A solução realiza a extração de dados através da API da CoinGecko, transforma as informações utilizando Python e Pandas e armazena o histórico em um banco SQLite para posterior análise.

---

## objetivo

o objetivo desde projeto é construir uma pipeline de dados voltada para Analytics, contemplando:

- Consumir dados de APIs REST
- Construir pipelines de ingestão e transformação de dados
- Armazenar históricos para análises temporais
- Aplicar SQL em bases geradas por APIs
- Desenvolver dashboards e métricas analíticas
- Evoluir gradualmente para PostgreSQL e Azure
- Aplicar conceitos de ETL, ELT e Arquitetura Moderna de Dados

---

## Arquitetura Atual (V1)

CoinGecko API
→ Python (Requests)
→ Pandas
→ SQLite

1. Coleta dos dados da API CoinGecko
2. Conversão para DataFrame
3. Tratamento e transformação dos dados
4. Persistência em banco SQLite

## Dados coletados

- Preço das criptomoedas
- Market Cap
- Moeda de referência (USD, EUR e BRL)
- Data e hora da coleta
- Ticker dos ativos

## Tecnologias Utilizadas

- Python
- Requests
- Pandas
- SQLite
- SQL
- Git

---

## Estrutura do Projeto

```text
crypto-project/
|
|___ crypto_analysis.ipynb
|___ .env
|___ .gitignore
|___ README.md
|___ crypto_analytics.db
```

---

## Segurança

As credenciais da API não são armazenadas diretamente no código.

As chaves são carregadas através de variáveis de ambiente utilizando:

- .env
- python-dotenv
- os.getenv()

O arquivo .env é ignorado pelo Git através do arquivo .gitignore.

---

## Próximos Passos

### V2 - Analytics Layer
- Automatizar a coleta de dados
- Conectar o banco SQLite ao Power BI
- Criar dashboard de acompanhamento
- Implementar métricas em DAX
- Analisar evolução histórica das criptomoedas
- Market Cap

### V3 - Data Engineering Foundation
- Migrar armazenamento de SQLite para PostgreSQL
- Implementar modelagem de dados mais robusta
- Adicionar validações de qualidade de dados
- Padronizar estrutura do projeto em múltiplos arquivos Python

### V4 - Pipeline Evolution
- Adicionar múltiplas APIs
- Implementar carregamento incremental
- Criar sistema de logging e tratamento de erros
- Automatizar capturar periódicas

### V5 - Cloud & Modern Data Architecture
- Migrar pipeline para Azure
- Utilizar armazenamento em nuvem
- Implementar pipeline automatizada
- Conceitos de Data Lake e Lakehouse

## Autor

Guilherme Monteiro Morgado de Melo