● 08/08/2026

● DATASCRIPPER

Este é um bot para Telegram desenvolvido em Python que permite registrar seus gastos diários de forma simples e rápida diretamente em uma planilha do Google Sheets.

📌 Funcionalidades 📌

💰 Registro fácil de despesas: Envie apenas Descrição Valor (separados por espaço) (exemplo: Almoço 35.90 ou Mercado 150)
📊 Integração automática com o Google Sheets: Todos os registros recebem a data atual e são adicionados em tempo real na sua planilha
🔒 Controle de acesso opcional: Possibilidade de restringir o uso do bot apenas para IDs específicos do Telegram
💬 Resposta interativa: Responde saudações e instruções amigáveis para mensagens que não estejam no formato de gasto


======================= Como Executar o Projeto =======================

● Instale dependências necessárias no terminal (Termux)

• pkg update && pkg upgrade -y -------------------------------------- (update e upgrade do termux)
• pkg install python libffi openssl rust clang make -y -------------- (instalação do python e compiladores)
• pip install --upgrade pip ----------------------------------------- (atualização do pip)
• pip install python-telegram-bot gspread google-auth --------------- (bibliotecas necessárias para o bot rodar com Google)
• termux-setup-storage ---------------------------------------------- (para permissão e armazenamento, arquivos, execução)

● Windows Powershell (O sistema já baixa as bibliotecas pré-compiladas, não sendo necessário instalar compiladores como clang ou rust):

• python --version -------------------------------------------------- (verifica se o Python está instalado no Windows)
• python -m pip install --upgrade pip ------------------------------- (atualização do gerenciador de pacotes pip)
• pip install python-telegram-bot gspread google-auth --------------- (bibliotecas necessárias para o bot rodar com Google)
• Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -------- (permite executar scripts Python sem bloqueios de segurança do Windows)

=======================================================================

● Configure o acesso ao Google Sheets ▶▷

▷ Acesse o Google Cloud Console e crie um projeto gratuito.

• Ative as APIs Google Sheets e Google Drive.

• Crie uma Conta de Serviço, gere uma chave no formato JSON e baixe-a.

• Renomeie esse arquivo baixado para credenciais.json e salve-o na mesma pasta do bot.py (coloque os dois na mesma pasta).

• Abra sua planilha no Google Sheets e compartilhe-a com o e-mail da conta de serviço (ele termina com @...gserviceaccount.com), dando permissão de Editor.

=======================================================================

● Edite o código python (bot.py)

▷ Abra o arquivo bot.py em qualquer editor de texto (como VS Code ou Bloco de Notas) e preencha as duas informações principais:

• TOKEN_DO_TELEGRAM: Cole o seu token que você recebeu do BotFather.

• NOME_DA_PLANILHA: Digite o nome exato da sua planilha do Google Drive.

● Coloque o bot para rodar no terminal, rode o comando:

python datascripper.py

Agora é só abrir a conversa com seu bot no Telegram e enviar suas despesas no formato:

Mercado 150 ou Almoço 32.50 (Descrição seguida do Valor)


