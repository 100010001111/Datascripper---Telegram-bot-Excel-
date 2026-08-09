#importações de bibliotecas necessárias para o BOT

import os
import logging 
from datetime import datetime 
import gspread
from google.oauth2.service_account import Credentials #---------------------------------------------- para autenticar com o Google Sheets
from telegram import Update #------------------------------------------------------------------------ para lidar com as atualizações no telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes #-------- para criar o bot e lidar com os comandos do usuário e mensagens

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



TOKEN_DO_TELEGRAM = "INSIRA O TOKEN DO SEU BOT CRIADO NO TELEGRAM, AQUI"
USUARIOS_PERMITIDOS = []  #Coloque seu ID do Telegram aqui se quiser que apenas usuários específicos usem o BOT, exemplo [1668553563]



#Configuração do Google Sheets
#Um arquivo JSON 'credenciais.json' precisará ser inserido na mesma pasta que este script do bot
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"





#Digite o nome exato da sua planilha no Google Drive
NOME_DA_PLANILHA = "NOME DA SUA PLANILHA NO GOOGLE DRIVE"  



#salvar na planilha
def salvar_na_planilha(descricao, valor):
    try:
        #Autentica ao Google
        caminho_atual = os.path.dirname(os.path.abspath(__file__))
        credenciais = Credentials.from_service_account_file(os.path.join(caminho_atual, 'credenciais.json'), scopes=SCOPES)
        cliente = gspread.authorize(credenciais)
        
        #Abre a planilha pelo nome
        planilha = cliente.open(NOME DA SUA PLANILHA NO GOOGLE DRIVE).sheet1
        
        #Define a data atual formatada
        data_atual = datetime.now().strftime("%d/%m/%Y")
        
        #Adiciona a nova linha com: Data, Descrição e Valor
        planilha.append_row([data_atual, descricao, valor])
        return True
    except Exception as e:
        print(f"\n[ERRO GOOGLE SHEETS]: {e}\n")
        return False



#Serve para processar as mensagens recebidas, validar o formato e salvar lá na planilha 
async def processar_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    texto_recebido = update.message.text.strip()

    if USUARIOS_PERMITIDOS and user_id not in USUARIOS_PERMITIDOS:
        await update.message.reply_text("Acesso privado negado.")
        return

    #Tenta separar o texto enviado por espaços
    #Espera algo como: Mercado 150 ou Almoço 32.50
    partes = texto_recebido.rsplit(' ', 1)

    if len(partes) < 2:
        await update.message.reply_text(
            
            "⚠️ Formato inválido!\n"
            "Por favor, envie a descrição seguida do valor.\n"
            "Exemplo: `Mercado 150` ou `Gasolina 80.50`"
        )
        return

    
    descricao = partes[0]
    valor_texto = partes[1].replace(',', '.')  #Trocar a vírgula por ponto para o Python entender

    
    try:
        valor = float(valor_texto)
    except ValueError:
        await update.message.reply_text("O valor informado não parece ser um número válido. Exemplo certo: `Lanche 25.50`")
        return

    mensagem_status = await update.message.reply_text("⏳Salvando na planilha...")

    #Salva no google sheets
    sucesso = salvar_na_planilha(descricao, valor)

    if sucesso:
        await mensagem_status.edit_text(
            f"✅ *Atualizado com sucesso!*\n\n"
            f"📋 *Descrição:* {descricao}\n"
            f"💰 *Valor:* R$ {valor:.2f}\n"
            f"🙏 Obrigado pelo envio!"
        )
    else:
        await mensagem_status.edit_text("❌ Erro ao salvar na planilha. Verifique as credenciais e o nome do arquivo.")



#Comando de início do bot e mensagem de boas vindas 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Sou seu assistente de finanças pessoal. \n\n"
        "Sempre que gastar algo, me mande neste formato:\n"
        "`Descrição Valor` (Exemplo: *Almoço 35.90*)\n\n"
        "Eu irei anotar tudo direto na sua planilha do Google Sheets!"
    )



#Função principal para iniciar o BOT e configurar handlers 
def main():
    app = Application.builder().token(TOKEN_DO_TELEGRAM).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, processar_mensagem))
    
    print("Bot de Finanças iniciado! Pode enviar os gastos.")
    app.run_polling()

if __name__ == '__main__':
    main()