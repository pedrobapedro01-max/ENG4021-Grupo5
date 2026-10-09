# BioForm — tarefas da sprint

Implementações independentes em HTML e CSS, para integração posterior.

- **Fácil:** `404.html` — tela para rota inexistente. O servidor ainda precisa configurar o retorno HTTP 404 e ajustar o link inicial.
- **Média:** `cadastro-validacao.html` — validação nativa de campos obrigatórios, formato do e-mail e tamanho mínimo de senha. Comparação das senhas e validação definitiva ficam para o servidor Python.
- **Média:** `editar-perfil.html` — interface de edição com validação HTML nativa. Não salva dados nem altera usuários reais.

## Como testar
Abra os arquivos HTML no navegador. Para testar o cadastro, experimente campos vazios, e-mail inválido, senha com menos de 8 caracteres . Para testar a edição, altere nome/e-mail e clique em Salvar.

## Integração
Estes protótipos não usam JavaScript, Flask nem banco de dados. O formulário de cadastro faz POST de demonstração, mas não há servidor configurado para recebê-lo; use apenas dados fictícios. O grupo deverá integrar as páginas às rotas, ao estilo existente e às operações seguras de autenticação e persistência. Não usar senhas reais nos testes.
