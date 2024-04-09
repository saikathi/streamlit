import streamlit as st
from pyvis.network import Network

def main():
    st.title("Network Visualization App")

    # Create a pyvis network
    net = Network(height="500px", width="100%", bgcolor="#222222", font_color="white")

    # Add nodes
    net.add_node(1, label="Node 1")
    net.add_node(2, label="Node 2")
    net.add_node(3, label="Node 3")

    # Add edges
    net.add_edge(1, 2)
    net.add_edge(2, 3)
    net.add_edge(3, 1)

    # Show the network
    st.write("Visualization:")
    net.show("network.html")
    st.write(net)

if __name__ == "__main__":
    main()
