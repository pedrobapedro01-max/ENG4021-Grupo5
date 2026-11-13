# Sprint 9 — Três tarefas com código

Arquivos independentes, sem alterar o aplicativo principal.

## 1. Protótipo mobile — DIFÍCIL
**Entrega:** `sprint9/mobile/index.html`
- [x] Criar três telas navegáveis (início, treinos e alimentação)
- [x] Adaptar layout para celular com HTML e CSS
- [ ] Validar manualmente em navegador

## 2. Testes automatizados — DIFÍCIL
**Entrega:** `sprint9/testes/test_mobile.py`
- [x] Criar quatro testes de estrutura e navegação do protótipo
- [ ] Executar os testes e registrar o resultado
- [ ] Ampliar cobertura para o sistema principal, se necessário

**Comando:** `python -m unittest discover -s sprint9/testes -v`

## 3. Gerador independente de relatórios de treinos — DIFÍCIL
**Entrega:** `sprint9/relatorio-treinos/index.html`
- [x] Formulário para registrar treinos
- [x] Resumo automático de registros e séries
- [x] Exclusão e armazenamento local dos registros
- [x] Layout de impressão para salvar em PDF pelo navegador
- [ ] Validar manualmente em navegador

**Observação:** o gerador não consulta o banco do site e não usa registros reais do usuário; é um protótipo independente. Conferir duplicidade no Kanban antes de registrar.
