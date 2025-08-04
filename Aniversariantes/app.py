import streamlit as st
import pandas as pd
from datetime import datetime as dt
import email_sender as es  # Importa o módulo email_sender
# Importa a classe GmailSender do arquivo enviar.py
import email_sender
import pytz



# Título do app
st.title("Calendário de Comemorações 🎂")

# Upload do arquivo
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])

if uploaded_file is not None:
    # Carrega o conteúdo do Excel com pandas
    df = pd.read_excel(uploaded_file) 

    # Exibe o dataframe
    st.write("Dados carregados:")
    #st.dataframe(df)

    # Título do app
    st.title("🎂 Aniversariantes do mês")

        # Garante que a coluna de datas está em formato de data
    df['Nascimento'] = pd.to_datetime(df['Nascimento'])
    st.dataframe(df)
        # Filtra aniversariantes do mês atual
    fuso_br = pytz.timezone('America/Sao_Paulo')

# Pega a data atual com fuso
    data_atual_br = dt.now(fuso_br)
  

# Converte para datetime do pandas
    data_convertida = pd.to_datetime(data_atual_br.strftime('%Y-%m-%d'), format='%Y-%m-%d')

# Obtém o dia
    mes_atual = data_convertida.month
    dia_atual = data_convertida.day
    # Filtra os aniversariantes do mês atual

    aniversariantes_mes = df[df['Nascimento'].dt.month == mes_atual]
    aniversariante_dia = aniversariantes_mes[aniversariantes_mes['Nascimento'].dt.day == dia_atual]
    print("Aniversariantes encontrados:", aniversariantes_mes)
    if not aniversariantes_mes.empty:
        st.success(f"🎈 Encontramos {len(aniversariantes_mes)} aniversariante(s) para o mês de {dt.now().strftime('%B')}!")
    # Exibe os aniversariantes do mês
        for _, row in aniversariantes_mes.iterrows():
            st.markdown(f"-Nome: **{row.iloc[0]}** 🎉- Cargo: ***{row.iloc[1]}*** - Nascimento: ***{row.iloc[2].strftime('%d/%m')}*** - {row.iloc[3]} ")
            nome = row.iloc[0]
            setor = row.iloc[1]
            email = row.iloc[3]
            data_nascimento = row.iloc[2]
            st.write(f"Nome: {nome}, Setor: {setor}, Email: {email}, Data de Nascimento: {data_nascimento.strftime('%d/%m/%Y')}")

            
    if not aniversariante_dia.empty:
        st.success(f"🎉 Hoje é aniversário de {len(aniversariante_dia)} pessoa(s)!")
        for _, row in aniversariante_dia.iterrows():
            
            st.markdown(f"- Nome: **{row.iloc[0]}** 🎉 - Cargo: ***{row.iloc[1]}*** - Nascimento: ***{row.iloc[2].strftime('%d/%m')}*** - {row.iloc[3]}")
            nome_1 = row.iloc[0]
            setor_1 = row.iloc[1]
            email_1 = row.iloc[3]
            
            assunto = f"Feliz Aniversário, {nome}!"
            corpo = f"Olá {nome_1},\n\nFeliz aniversário! Que seu dia seja repleto de alegrias e conquistas. Estamos felizes em celebrar este momento especial com você!\n\nAtenciosamente,\nSua equipe"      
            
            sender = es.GmailSender()
            sender.send_email(body=corpo, subject=assunto, to=email_1)

            st.success("E-mail enviado com sucesso! 🎉")

            
else:
    st.warning("😕 Ninguém faz aniversário hoje.")























