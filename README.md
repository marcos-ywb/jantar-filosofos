# Seminário: O Problema do Jantar dos Filósofos

![Licença: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Sumário
- [1. Introdução](#1-introdução)
- [2. Objetivo](#2-objetivo)
- [3. Metodologia](#3-metodologia)
  - [3.1 Estrutura do Projeto](#31-estrutura-do-projeto)
  - [3.2 Configurações Principais](#32-configurações-principais)
- [4. Funcionamento](#4-funcionamento)
- [5. Resultados](#5-resultados)
- [6. Conclusão](#6-conclusão)
- [7. Instalação](#7-instalação)
  - [7.1 Pré-requisitos](#71-pré-requisitos)
  - [7.2 Clonando o repositório](#72-clonando-o-repositório)
  - [7.3 Criando um ambiente virtual](#73-criando-um-ambiente-virtual)
  - [7.4 Ativando o ambiente virtual](#74-ativando-o-ambiente-virtual)
  - [7.5 Instalando dependências](#75-instalando-dependências)
  - [7.6 Executando o projeto](#76-executando-o-projeto)
- [8. Referências](#8-referências)
- [9. Licença](#9-licença)

---

## 1. Introdução
O problema do **Jantar dos Filósofos** é um clássico da computação concorrente criado por **Edsger Dijkstra** em 1965.  
Ele ilustra de forma simples os desafios de **sincronização** e **alocação de recursos** entre processos que competem por recursos compartilhados.

Neste seminário, apresentamos a implementação prática do problema utilizando **Python** e **threads**, com geração de estatísticas e visualização dos resultados.

---

## 2. Objetivo
- Demonstrar os conceitos de **concorrência**, **deadlock** e **starvation**;
- Implementar uma simulação com múltiplos filósofos competindo por recursos (garfos);
- Registrar métricas e estatísticas sobre o comportamento do sistema;
- Criar gráficos para visualizar os resultados.

---

## 3. Metodologia
A implementação foi feita em **Python**, utilizando:
- **threading**: para simular os filósofos como threads concorrentes;
- **Locks (mutex)**: para representar os garfos e garantir exclusão mútua;
- **Matplotlib**: para geração dos gráficos de cada “frame”;
- **Sistema de logs**: para registrar as estatísticas em cada execução.

### 3.1. Estrutura do Projeto
```
jantar-filosofos/
├── frames/ # Pasta onde são salvos os gráficos (frames)
│ └── .gitkeep # Arquivo para garantir que a pasta seja versionada mesmo vazia
├── logs/ # Pasta onde são salvos os logs da simulação
│ └── .gitkeep # Arquivo para garantir que a pasta seja versionada mesmo vazia
└── main.py # Código principal da simulação
```

### 3.2. Configurações Principais
- `NUM_FILOSOFOS`: Número de filósofos na mesa  
- `TEMPO_SIMULACAO`: Tempo total de simulação (segundos)  
- `TAXA_PENSAR`: Distribuição exponencial do tempo de “pensar”  
- `TAXA_COMER`: Distribuição exponencial do tempo de “comer”  

---

## 4. Funcionamento
Cada filósofo alterna entre **pensar** e **comer**. Para comer, ele precisa adquirir **dois garfos** (à esquerda e à direita).  
A simulação registra:
- Quantidade de refeições por filósofo;
- Tempo médio de espera antes de comer;
- Gráficos mostrando as estatísticas em tempo real.

---

## 5. Resultados
A simulação gera:
- **Gráficos (frames)** mostrando o número de refeições por filósofo ao longo do tempo;
- Arquivos de log em **logs/** com informações detalhadas de cada frame.

Esses dados podem ser usados para analisar:
- Se houve **deadlock**;
- Se algum filósofo sofreu **starvation** (ficou muito tempo sem comer);
- Distribuição de recursos entre os processos.

---

## 6. Conclusão
O **Problema do Jantar dos Filósofos** mostra a importância de políticas adequadas de **sincronização** para evitar problemas de concorrência.  
Com essa implementação, é possível visualizar e registrar o comportamento dos processos em tempo real, tornando o estudo mais didático e prático.

---
## 7. Instalação

Passo a paso para instalar e executar o projeto:

### 7.1. Pré-requisitos

- Python 3.10+ instalado
- pip atualizado
- (Opcional) Git para clonar o repositório

### 7.2. Clonando o repositório
```bash
git clone https://github.com/seu-usuario/jantar-filosofos.git
cd jantar-filosofos
```

### 7.3. Criando um ambiente virtual
```bash
python3 -m venv .venv
```

### 7.4. Ativando o ambiente virtual
```bash
source .venv/bin/activate #Linux
.venv\Scripts\activate #Windows
```
### 7.5. Instalando dependências
```bash
pip install -r requirements.txt
```

### 7.6. Executando o projeto
```bash
python main.py
```
---
## 8. Referências

- Dijkstra, E. W. (1965). *Solution of a problem in concurrent programming control.*

---
## 9. Licença
Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).