from PIL import Image
from streamlit_timeline import timeline
import streamlit as st, pandas as pd, numpy as np, plotly.express as px, time, os, plotly.graph_objects as go, streamlit.components.v1 as com

st.set_page_config(page_title="Dissertação", page_icon=":📰:", layout="wide")

img_lg = Image.open("images/logo.png")
uni_lg = Image.open("images/unilogo.png")

_RESUMO = """
	As novas tecnologias revolucionaram a forma como acedemos e utilizamos a informação mas também as relações entre os indivíduos e a forma como os profissionais 
da informação organizam o conhecimento. O surgimento das bibliotecas digitais são um exemplo dum mundo em constante evolução e servem-se da digitalização da 
informação para agir como veículos de suporte a processos de ensino / aprendizagem. Estes SI (S.I.) fornecem meios mais interativos para os utilizadores procurarem 
informações, permitindo o acesso a bases de dados e a transferência de informações mesmo a partir de locais remotos. Neste contexto, as bibliotecas digitais 
desempenham um papel fundamental na construção do conhecimento mediada pelas tecnologias de informação e comunicação (T.I.C.) e de forma a garantir um elevado 
desempenho e níveis de qualidade deste software torna-se necessário considerar um desenho de interfaces alinhado com diferentes contextos de uso. Este estudo propõe 
um desenho de interface centrado no utilizador como forma de reforçar a qualidade da interação entre o sistema e seus utilizadores com vista a melhoria contínua da 
sua usabilidade e das estratégias para a sua avaliação.
"""

res = """
_:blue[Palavras-Chave:] Bibliotecas digitais, Avaliação de Usabilidade, Desenho de Interfaces Centrado no Utilizador_
"""

_ABSTRACT = """
    New technologies have revolutionized the way we access and use information, but also the relationships between individuals and the way information professionals 
organize knowledge. The emergence of digital libraries is an example of a world in a constant evolution and uses the digitization of information to act as vehicles 
to support teaching/learning processes. These information systems (IS) provide more interactive means for users to search for information, allowing access to databases 
and the transfer of information even from remote locations. In this context, digital libraries play a fundamental role in the construction of knowledge mediated by 
information and communication technologies (ICT) and to guarantee high performance and quality levels of this software, it is necessary to consider an interface 
design aligned with different contexts of use. This study proposes a user-centered interface design as a way of reinforcing the quality of interaction between the 
system and its users, aiming at continuous improvement of its usability and strategies for its evaluation.
"""

abs = """
_:blue[Keywords:] Digital libraries, Usability Evaluation, User-Centered Design of Interfaces_
"""

def stream_data(x):
    if x == 1:
        for word in _RESUMO.split(" "):
            yield word + " "
            time.sleep(0.04)
        yield res

    if x == 2:
        for word in _ABSTRACT.split(" "):
            yield word + " "
            time.sleep(0.04)
        yield abs    

tab = pd.read_csv("t.csv", encoding='windows-1252')
gra = pd.read_csv("g.csv", encoding='windows-1252')
img = pd.read_csv("i.csv", encoding='windows-1252')
r1 = pd.read_csv("rsl1.csv", encoding='windows-1252')
r2 = pd.read_csv("rsl2.csv", encoding='windows-1252')
r3 = pd.read_csv("rsl3.csv", encoding='windows-1252')
r4 = pd.read_csv("rsl4.csv", encoding='windows-1252')
r5 = pd.read_csv("rsl5.csv", encoding='windows-1252')
ref = pd.read_csv("ref.csv", encoding="windows-1252")

st.header("Mestrado em Informação e Sistemas Empresariais")   
st.subheader("Novos Sistemas de Informação de Apoio ao Estudante/Formando")

c1, c2 = st.columns(2, gap="large")
with c1:
    com.iframe("https://lottie.host/embed/a483dff9-20a7-42d3-bd63-3f8a5943693e/r2b62ZERxg.json", height=500)

with c2:
    if st.sidebar.button("Resumo"):
        st.write(stream_data(1))
    if st.sidebar.button("Abstract"):
        st.write(stream_data(2))

st.warning("- Um Caso de Estudo de Avaliação de Usabilidade de uma Biblioteca Digital")
st.sidebar.image(uni_lg, caption="University Logos")

st.sidebar.markdown("Autora: ")
st.sidebar.latex("Íris Alexandra N. Correia")
st.sidebar.markdown("Dissertação orientada pelo Professor Doutor: ")
st.sidebar.latex("Vítor Jorge Ramos Rocio")
st.sidebar.markdown("Ano de Submissão: ")
st.sidebar.latex("2024")
st.sidebar.markdown("Área disciplinar do trabalho: ")
st.sidebar.latex("Sistemas De Informação")

col1, col2, col3 = st.columns(3, gap="large")
st.write("---")
with col1:
    simple = st.container()
    simple.info("Referências Bibliográficas", icon="🧾")
    simple.metric(label="Total:", value="", delta="302 Referências")
with col2:
    simple1 = st.container()
    simple1.info("1º Versão do Protótipo", icon="🔬")
    simple1.metric(label="Ficheiros da Avalição:", value="", delta="7 Ficheiros", help="Ficheiros com resultados da primeira avaliação de usabilidade")     
    show_gallery = simple1.button("Ver Arquivos")

    if show_gallery:
        st.session_state.show_gallery = not st.session_state.get("show_gallery", False)

    if st.session_state.get("show_gallery", False):
        folder_path = './au1'  # Replace with the actual path to your folder containing files
        filenames = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        num_cols = 3  # Adjust the number of columns for layout
        cols = st.columns(num_cols)
        for i, filename in enumerate(filenames):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "rb") as file:
                    col = cols[i % num_cols]
                    with col:
                        st.write(i+1," - ",filename)
                        st.download_button(label="Descarregar", data=file, file_name=filename)
            except PermissionError:
                # Skip files that cannot be accessed due to permissions
                continue
with col3:
    simple2 = st.container()
    simple2.info("2º Versão do Protótipo", icon="📹")
    simple2.metric(label="Ficheiros da Avalição:", value="", delta="19 Ficheiros", help=f"""Ficheiros com resultados da segunda avaliação de usabilidade""")
    show_gallery1 = simple2.button("Ver Ficheiros")

    if show_gallery1:
        st.session_state.show_gallery1 = not st.session_state.get("show_gallery1", False)

    if st.session_state.get("show_gallery1", False):
        folder_path1 = './au2'  # Replace with the actual path to your folder containing files
        filenames1 = [f for f in os.listdir(folder_path1) if os.path.isfile(os.path.join(folder_path1, f))]
        num_cols = 3  # Adjust the number of columns for layout
        cols = st.columns(num_cols)    
        for i, filename1 in enumerate(filenames1):
            file_path1 = os.path.join(folder_path1, filename1)
            try:
                with open(file_path1, "rb") as file:
                    col = cols[i % num_cols]
                    with col:
                        st.write(i+1," - ",filename1)
                        st.download_button(label="Descarregar", data=file, file_name=filename1)
            except PermissionError:
                    # Skip files that cannot be accessed due to permissions
                continue    


def render_data_with_toggle(df, key, chart_type='bar', group_columns=None):
    if f"{key}_view" not in st.session_state:
        st.session_state[f"{key}_view"] = 'table'

    if st.session_state[f"{key}_view"] == 'table':
        if st.button("Mostrar Gráfico", key=f"{key}_chart"):
            st.session_state[f"{key}_view"] = 'chart'
            st.rerun()
        else:
            st.write(df)
    else:
        if group_columns and len(group_columns) == 2:
            fig = go.Figure()
            for idx, column in enumerate(group_columns):
                if chart_type == 'pie':
                    fig.add_trace(go.Pie(labels=df[column].unique(), values=df.groupby(column).size(), name=column))
                else:
                    fig.add_trace(go.Bar(x=df[column].unique(), y=df.groupby(column).size(), name=column))
            
            fig.update_layout(barmode='group', title=f'{chart_type.capitalize()} Chart Grouped by {", ".join(group_columns)}')
            st.plotly_chart(fig)
        else:
            numeric_df = df.select_dtypes(include=[np.number])
            if numeric_df.empty:
                st.warning("No numeric data available to plot.")
            else:
                if chart_type == 'bar':
                    fig = px.bar(numeric_df)
                elif chart_type == 'line':
                    fig = px.line(numeric_df)
                st.plotly_chart(fig)
        if st.button("Mostrar Tabela", key=f"{key}_table"):
            st.session_state[f"{key}_view"] = 'table'
            st.rerun()

with st.container():
    tab1, tab2, tab3, tab4 , tab5= st.tabs(["Referências","Imagens","Tabelas","Gráficos","Timeline"])

with tab4:
    st.subheader("Gráficos")
    st.dataframe(gra)

with tab2:
    st.subheader("Imagens")
    st.dataframe(img)

with tab3:
    st.subheader("Tabelas")
    st.dataframe(tab)

with tab1:
    st.subheader("Referências")
    st.write("Revisão de Literatura: Usabilidade")
    render_data_with_toggle(r1, key="r1", chart_type='pie', group_columns=['Idioma', 'Ano de Publicação'])
    st.write("Revisão de Literatura: Experiência do Utilizador")
    render_data_with_toggle(r2, key="r2", chart_type='bar', group_columns=['Idioma', 'Ano de Publicação'])
    st.write("Revisão de Literatura: Desenho Centrado do Utilizador")
    render_data_with_toggle(r3, key="r3", chart_type='pie', group_columns=['Idioma', 'Ano de Publicação'])
    st.write("Revisão de Literatura: Bibliotecas digitais")
    render_data_with_toggle(r4, key="r4", chart_type='bar', group_columns=['Idioma', 'Ano de Publicação'])
    st.write("Revisão de Literatura: Design Science Research")
    render_data_with_toggle(r5, key="r5", chart_type='pie', group_columns=['Idioma', 'Ano De Publicação'])
    st.write("Bibliografia")
    st.dataframe(ref)

with tab5:
    with open('timeline.json', "r", encoding='utf-8') as f:
        data = f.read()

    timeline(data, height=800)