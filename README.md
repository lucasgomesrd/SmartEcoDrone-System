# Smart Eco Drone System

## Visão Geral
O **Smart Eco Drone System** é um projeto de engenharia mecatrônica voltado para **monitoramento ambiental inteligente**, integrando simulação de drone, análise de dados, segurança da informação e visualização em dashboard.

A proposta é demonstrar, de forma prática, como tecnologias modernas podem ser utilizadas para **coleta, transmissão segura e análise de dados ambientais em tempo real**, com foco em sustentabilidade.

---

## Objetivo
Desenvolver um sistema integrado capaz de:

- Simular a coleta de dados ambientais via drone
- Processar e analisar informações automaticamente
- Garantir segurança na transmissão dos dados
- Exibir informações em um dashboard interativo

---

## Arquitetura do Sistema

```text
[ Drone (Simulação) ]
          ↓
[ API Segura (Flask + Token) ]
          ↓
[ Módulo de Análise de Dados ]
          ↓
[ Dashboard (Visualização) ]

---

## Como rodar
1 Baixe o repositório .zip
2 Extraia e Abra a pasta
3 abra o cmd dentro da pasta selecionada
4 digite dentro do cmd
          cd api_security
          python app.py
5 abra outro cmd  (importante estar dentro da pasta indicada)
          cd drone_simulation
          python simulation.py
6 abra outro cmd
          cd dashboard
          python -m streamlit run app.py
7 deve aparecer a api funcionando
          
