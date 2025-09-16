# Seminário: O Problema do Jantar dos Filósofos

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
- Sistema de logs: para registrar as estatísticas em cada execução.

### 3.1 Estrutura do Projeto

```
jantar-filosofos/
├── frames/                  # Pasta onde são salvos os gráficos (frames)
├── log.txt                  # Arquivo de logs da simulação
└── main.py                  # Código principal da simulação
```

### 3.2 Configurações Principais
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
- Um arquivo **log.txt** com informações detalhadas de cada frame.

Esses dados podem ser usados para analisar:
- Se houve **deadlock**;
- Se algum filósofo sofreu **starvation** (ficou muito tempo sem comer);
- Distribuição de recursos entre os processos.

---

## 6. Conclusão
O **Problema do Jantar dos Filósofos** mostra a importância de políticas adequadas de **sincronização** para evitar problemas de concorrência.  
Com essa implementação, é possível visualizar e registrar o comportamento dos processos em tempo real, tornando o estudo mais didático e prático.

---

## 7. Referências
- Dijkstra, E. W. (1965). *Solution of a problem in concurrent programming control.*
- Tanenbaum, A. S. *Modern Operating Systems.*
- Stallings, W. *Operating Systems: Internals and Design Principles.*
