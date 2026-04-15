# Plano para transformar o Smart Eco Drone System em projeto real

## 1) Estruturar o projeto como produto (MVP)
- Definir um caso de uso único para o MVP (ex.: monitorar risco de calor e baixa umidade em área rural).
- Definir 3 métricas de sucesso: latência de ingestão, acurácia dos alertas e disponibilidade do sistema.
- Padronizar os contratos de dados (JSON Schema ou Pydantic) para todos os módulos.

## 2) Fortalecer cada módulo

### Drone Simulation
- Adicionar timestamp ISO-8601, `drone_id`, nível de bateria, altitude e velocidade.
- Simular leituras com ruído controlado e anomalias para testes.
- Exportar dados para fila/event bus (MQTT ou Kafka para produção; arquivo/HTTP para MVP).

### API Security
- Trocar token fixo por autenticação robusta (JWT com expiração curta + refresh).
- Validar payload com schema e rejeitar dados inválidos.
- Adicionar rate limit e logs de auditoria.
- Separar configuração por variáveis de ambiente (`.env`) e nunca hardcode de segredo.

### Data Analysis
- Evoluir de regra simples para pipeline com:
  - limpeza de dados,
  - cálculo de indicadores,
  - regras de alerta configuráveis,
  - histórico para tendência.
- Introduzir testes unitários para regras críticas.

### Dashboard
- Exibir métricas em tempo real (temperatura, umidade, status do drone).
- Mostrar mapa com localização e trilha.
- Exibir histórico e alertas com filtros por período e região.

## 3) Engenharia e qualidade
- Organizar em pacotes Python com `pyproject.toml`.
- Configurar lint/format (`ruff` + `black`) e tipagem (`mypy`).
- Criar CI (GitHub Actions) para testes, lint e build.
- Adicionar suíte mínima de testes automatizados.

## 4) Operação e confiabilidade
- Containerizar com Docker (API, análise e dashboard).
- Definir observabilidade mínima: logs estruturados, métricas e healthchecks.
- Criar ambientes `dev` e `prod` com configurações separadas.

## 5) Roadmap sugerido (4 semanas)
- Semana 1: padronização de dados + refactor da API + variáveis de ambiente.
- Semana 2: análise de dados com histórico e testes.
- Semana 3: dashboard em tempo real + mapa + filtros.
- Semana 4: CI/CD, Docker e documentação de implantação.

## 6) Definição de pronto (DoD)
- Todos os módulos com testes básicos e passing em CI.
- API autenticada, validada e com logs.
- Dashboard com dados ao vivo e histórico.
- Guia de execução local em até 10 minutos.
