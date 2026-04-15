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

## Como Rodar

1. Baixe o repositório (.zip)  
2. Extraia e abra a pasta do projeto  
3. Abra o CMD dentro da pasta do projeto  

4. No primeiro terminal, execute:

/cd api_security
/python app.py


5. Abra outro CMD (também dentro da pasta do projeto) e execute:

/cd drone_simulation
/python simulation.py


6. Abra outro CMD e execute:

/cd dashboard
/python -m streamlit run app.py


7. A API deve estar rodando e o dashboard abrirá no navegador automaticamente
