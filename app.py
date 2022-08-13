import streamlit as st
import streamlit.components.v1 as components
from collections import defaultdict
from pyvis.network import Network
import pandas as pd

st.title('Frictionless')
st.markdown('From Hitachi Vantara')

df = pd.read_csv("techRadar_data_large.csv")
df_text = pd.read_csv("techRadar_view.csv")

g = Network("500px", "100%", bgcolor="#3c4647", font_color="white")

# option = st.selectbox(
#      'What do you want to know  about',
#      df.tech.unique())
options = st.multiselect("Technologies: ",
                         df.tech.unique())
st.write("You selected", len(options), 'Technologies')

if options == ["All"]:
    df = df
    st.write("All")
    df_text = ["All about tech"]

else:
#     options = [option]
    df = df[df['tech'].isin(options)]
    df_text = df_text[df_text['tech'].isin(options)]


for _,tech,_,strategy in df.itertuples(index=False):
    if strategy == "Hold":
        draw_shape  = "dot"
    else:
        draw_shape = "star"
    g.add_node(tech, label=tech, color="#26d18f", shape = draw_shape)
for related in df.related:
    g.add_node(related, label=related, color="#8965c7")
g.add_edges(list(zip(df.tech, df.related)))
counts = df.related.value_counts()
for node in g.nodes:
    freq = str(counts.get(node['id'], 1))
    # nodes with a value will scale their size
    # nodes with a title will include a hover tooltip on the node
    node.update({"value": freq, "title": f"Frequency: {freq}"})
g.inherit_edge_colors("to")
for e in g.edges:
    edge_label = f'{e["from"]} ---> {e["to"]}'
    e.update({"title": edge_label})
g.barnes_hut(
    gravity=-17950,
    central_gravity=4.1,
    spring_length=220,
    spring_strength=.140,
    damping=.66,
    overlap=1
)
st.text(df_text.Text)
# st.write(df_text.Text)
g.show("radar_example.html")
HtmlFile = open("radar_example.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height = 800,width=800)
