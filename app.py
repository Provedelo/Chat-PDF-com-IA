from PyPDF2 import PdfReader
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings


#Feita com a Open IA, troca para Ilhama depois e ver como sai
#Sidebar content
with st.sidebar:
    st.title('Chat IA com pdf')
    st.markdown('''
                ## Sobre
                App feito com IA 
                - rodando no pythonzao
                '''
                )
    add_vertical_space(5)
    st.write('Feito com base no odio')

def main():
    st.header("Fale com o Wiki Local")
   
    # Suba o arquivo PDF
    pdf = st.file_uploader("Upload", type='pdf')
    
    
    #St.write(PDF) ta vazio ou nao
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        #st.write(pdf_reader)
        
        #Leitura das pag no pdf
        text = " "
        for page in pdf_reader.pages: 
            text += page.extract_text()
            #st.write(text) <- imprime na tela o texto
        
        #Divisao do texto por blocos
        text_splitter = RecursiveCharacterTextSplitter(
             chunk_size = 1000, # tam da linha de caracteres
             chunk_overlap = 250, # intervalo de uma sentença pra outra, mantem contexto da conversa
             length_function = len, 
             is_separator_regex=False
        )
        chunks = text_splitter.split_text(text = text)
        st.write(chunks)
        
        #embeddings
        embeddings = OpenAIEmbeddings()
        

if __name__ == '__main__':
        main()