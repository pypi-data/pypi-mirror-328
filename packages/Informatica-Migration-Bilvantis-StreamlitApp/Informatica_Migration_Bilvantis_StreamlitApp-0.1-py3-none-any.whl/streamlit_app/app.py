import streamlit as st
import tempfile
from metadata_topology import extract_graph_with_mapplets, topological_sort_for_graph, visualize_hierarchical_graph, topological_sort_for_transformation
from handle_transformation import *
from process import process_xml_file
import time
import os
import yaml

TARGET_CONFIG_FILE = "target_config.yaml"
MODEL_CONFIG_FILE = "model_config.yaml"

# Configure Streamlit Page
st.set_page_config(
    page_title="Migration from Informatica to Cloud",
    layout="wide",
    initial_sidebar_state="auto"
)

def update_yaml_target(selected_target):
    """Updates the target in the YAML file."""
    with open(TARGET_CONFIG_FILE, "r") as file:
        transformations = yaml.safe_load(file)

    transformations['transformations']['Target'] = selected_target  # Update the target

    with open(TARGET_CONFIG_FILE, "w") as file:
        yaml.safe_dump(transformations, file, default_flow_style=False)

def update_yaml_llm(selected_model):
    """Updates the target in the YAML file."""
    with open(MODEL_CONFIG_FILE, "r") as file:
        llms = yaml.safe_load(file)

    llms['llms']['model'] = selected_model  # Update the model

    with open(MODEL_CONFIG_FILE, "w") as file:
        yaml.safe_dump(llms, file, default_flow_style=False)

# Read initial YAML configuration
with open(TARGET_CONFIG_FILE, "r") as file:
    transformations = yaml.safe_load(file)

target = transformations.get('transformations', {}).get('Target', None)

# load the llm model to be used from the yaml
with open(MODEL_CONFIG_FILE, "r") as file:
    llms = yaml.safe_load(file)

model = llms.get('llms', {}).get('model', None)

# **Dropdown to select the target platform**
target_options = ["Snowflake", "BigQuery", "PySpark", "Databricks"]
selected_target = st.selectbox("Select Target Platform:", target_options, index=target_options.index(target) if target in target_options else 0)

# If the target has changed, update the YAML file
if selected_target != target:
    update_yaml_target(selected_target)
    st.rerun()  # Refresh the page to reflect changes

# **Dropdown to select the target platform**
llm_options = ["gemini-2.0-flash", "gpt-4o"]
selected_llm = st.selectbox("Select LLM Model for Migration:", llm_options, index=llm_options.index(model) if model in llm_options else 0)

# If the target has changed, update the YAML file
if selected_llm != model:
    update_yaml_llm(selected_llm)
    st.rerun()  # Refresh the page to reflect changes

def download_sql(final_query):
    """Creates and allows the download of a .sql file."""
    sql_file = "generated_query.sql"
    with open(sql_file, "w") as file:
        file.write(final_query)
    return sql_file

def display_graph_metrics(metrics):
    st.markdown("<h2 style='text-align: center; color: #1f77b4;'>📊 Node Statistics</h2>", unsafe_allow_html=True)
    
    # Custom CSS for metric labels
    st.markdown("""
        <style>
        [data-testid="stMetricLabel"] {
            font-size: 3.2rem;
            font-weight: 600;
        }
        </style>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Nodes", metrics['total_nodes'])
        st.metric("Source Nodes", metrics['source_nodes'])
    
    with col2:
        st.metric("Target Nodes", metrics['target_nodes'])
        st.metric("Intermediate Nodes", metrics['intermediate_nodes'])

# Streamlit App Title
st.title(f"📌 Migration from Informatica to {selected_target}")

# Initialize session state for query
if 'final_query' not in st.session_state:
    st.session_state.final_query = None

# File Upload
uploaded_file = st.file_uploader("Upload XML File", type="xml")
output_folder = "output/streamlit_queries"

if uploaded_file:
    basename = os.path.basename(uploaded_file.name)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as temp_file:
        temp_file.write(uploaded_file.read())
        file_path = temp_file.name

    graph = extract_graph_with_mapplets(file_path)

    try:
        # Run the topological sort
        topo_order = topological_sort_for_graph(graph)
        topo_order_for_trans = topological_sort_for_transformation(graph)
        
        st.success("✅ Topological Sorting Successful!")
        st.write("**Topological Order:**", " → ".join(topo_order_for_trans))

        # Visualize the graph
        net, metrics = visualize_hierarchical_graph(graph, topo_order)
        display_graph_metrics(metrics)
        html_path = "graph.html"
        net.save_graph(html_path)
        
        # Store the graph HTML content in session state
        if 'graph_html' not in st.session_state:
            st.session_state.graph_html = open(html_path, "r").read()

        # Display the graph saved in session state
        st.components.v1.html(st.session_state.graph_html, height=600, scrolling=True)

        # Query Generation Button
        if st.button("Generate Query"):
            with st.spinner("⏳ Generating Query..."):
                st.session_state.final_query = process_xml_file(file_path, basename, output_folder)
            st.success("✅ Query Generated Successfully!")

        # Display query area and buttons if query exists
        if st.session_state.final_query:
            st.subheader("Generated Query:")
            st.text_area("Generated Query", st.session_state.final_query, height=600)

            # Download button
            sql_file = download_sql(st.session_state.final_query)
            with open(sql_file, "rb") as file:
                st.download_button(
                    label="Download SQL Query",
                    data=file,
                    file_name="generated_query.sql",
                    mime="text/sql"
                )

    except ValueError as e:
        st.error(e)
