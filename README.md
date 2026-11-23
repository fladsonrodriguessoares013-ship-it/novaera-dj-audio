# NovaEra City — Serviço de áudio do DJ

## Deploy no Render
1. Crie um repositório no GitHub e envie os arquivos desta pasta (na raiz do repositório).
2. No Render: New > Web Service > conecte o repositório.
3. Runtime: Python; Build: `pip install -r requirements.txt`; Start: `gunicorn --bind 0.0.0.0:$PORT app:app`. Escolha o plano disponível.
4. Abra `https://SEU-SERVICO.onrender.com/health` para testar.
5. No console do servidor MTA, configure o setting do recurso: `set tequilaGTA5.youtubeResolverURL https://SEU-SERVICO.onrender.com/resolve` (substitua tequilaGTA5 pelo nome real da pasta do recurso). Reinicie o recurso após configurar. Alternativamente, adicione `<setting name="youtubeResolverURL" value="https://SEU-SERVICO.onrender.com/resolve" />` dentro do meta.xml do recurso, se o seu recurso utiliza essa configuração.

## Como o áudio funciona
O mod existente faz GET `/resolve?id=ID_DO_VIDEO` e espera JSON `{"url":"https://.../audio.mp3"}`. Este serviço usa um catálogo de links diretos de áudio para os quais você tem autorização de uso. Edite `catalog.json`, exemplo:
`{"dQw4w9WgXcQ":"https://seu-dominio.example/musica-autorizada.mp3"}`
O ID no exemplo é apenas ilustrativo e não inclui áudio.

Este serviço **não baixa, extrai nem converte áudio do YouTube**. Sem uma URL de áudio autorizada no catálogo, responde 404. Isso não resolve automaticamente qualquer link do YouTube.

## Nota
O Render Free pode suspender serviços inativos. Áudio deve estar hospedado em URL HTTPS acessível pelos clientes MTA; servidores que exigem cookies ou autenticação podem não tocar.
