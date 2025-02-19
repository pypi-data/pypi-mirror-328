import heapq
from collections import defaultdict
import xml.etree.ElementTree as ET
from pyvis.network import Network
import networkx as nx
import xml.etree.ElementTree as ET
from collections import defaultdict
import xml.etree.ElementTree as ET
from collections import defaultdict

def extract_graph_with_mapplets(file_path):
    """Extract a hierarchical graph that groups mapplet transformations under their parent mapplet."""
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Main graph structure for topological sort
    graph = defaultdict(set)
    # Dictionary to store mapplet hierarchies
    mapplet_contents = defaultdict(list)
    # Track which transformations belong to which mapplet
    transformation_to_mapplet = {}
    # Store input and output transformations of each mapplet
    mapplet_io = {}

    # Collect all instances to include unconnected nodes
    all_instances = set()
    
    # First pass: identify mapplets, their transformations, and input/output transformations
    for mapplet in root.findall(".//MAPPLET"):
        mapplet_name = mapplet.get("NAME")
        if mapplet_name:
            all_instances.add(mapplet_name)
            input_transformation = None
            output_transformation = None
            
            for transform in mapplet.findall(".//TRANSFORMATION"):
                transform_name = transform.get("NAME")
                transform_type = transform.get("TYPE")
                # if transform_type == "Mapplet":
                #     print(transform_name)
                #     continue

                if transform_name:
                    all_instances.add(transform_name)
                    mapplet_contents[mapplet_name].append(transform_name)
                    transformation_to_mapplet[transform_name] = mapplet_name

                    # Identify Input and Output transformations
                    if transform_type == "Input Transformation":
                        input_transformation = transform_name
                    elif transform_type == "Output Transformation":
                        output_transformation = transform_name

            # Store input and output transformation mappings
            mapplet_io[mapplet_name] = {
                "input": input_transformation,
                "output": output_transformation
            }

    # Add non-mapplet instances
    for instance in root.findall(".//INSTANCE"):
        instance_name = instance.get("NAME")
        if instance_name and instance_name not in transformation_to_mapplet:
            all_instances.add(instance_name)
    
    # Second pass: build connections
    for connector in root.findall(".//CONNECTOR"):
        from_instance = connector.get("FROMINSTANCE")
        from_instance_type = connector.get("FROMINSTANCETYPE")
        to_instance = connector.get("TOINSTANCE")
        to_instance_type = connector.get("TOINSTANCETYPE")

        # Replace from_instance if it's a mapplet
        if from_instance_type == "Mapplet" and from_instance in mapplet_io:
            from_instance = mapplet_io[from_instance]["output"] or from_instance  # Use Output Transformation

        # Replace to_instance if it's a mapplet
        if to_instance_type == "Mapplet" and to_instance in mapplet_io:
            to_instance = mapplet_io[to_instance]["input"] or to_instance  # Use Input Transformation

        if from_instance and to_instance:
            # Add to the main graph for topological sort
            graph[from_instance].add(to_instance)
            
            # Ensure both instances exist in the graph
            all_instances.add(from_instance)
            all_instances.add(to_instance)
    
    # Add all unconnected nodes to the graph
    for instance in all_instances:
        graph.setdefault(instance, set())

    return {
        'main_graph': {k: list(v) for k, v in graph.items()},
        'mapplet_contents': dict(mapplet_contents),
        'transformation_to_mapplet': transformation_to_mapplet
    }


def topological_sort_for_graph(graph_data):
    """Perform topological sort on the graph while maintaining mapplet hierarchy."""
    # Use the main_graph for topological sorting
    graph = graph_data['main_graph']
    in_degree = defaultdict(int)
    
    for node in graph:
        in_degree[node]  # Ensure all nodes are present
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Identify unconnected nodes
    unconnected_nodes = [node for node in graph if not graph[node] and in_degree[node] == 0]
    unconnected_nodes.sort()  # Sort for deterministic output

    # Initialize the heap with zero in-degree nodes (excluding unconnected nodes)
    zero_in_degree = [node for node in in_degree if in_degree[node] == 0 and node not in unconnected_nodes]
    heapq.heapify(zero_in_degree)

    topological_order = unconnected_nodes[:]  # Start with unconnected nodes

    while zero_in_degree:
        current = heapq.heappop(zero_in_degree)
        topological_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(zero_in_degree, neighbor)

    if len(topological_order) != len(in_degree):
        raise ValueError("Graph has a cycle; topological sorting is not possible.")

    return topological_order


def topological_sort_for_transformation(graph_data):
    """Perform topological sort on the graph while removing mapplets from the final order."""
    graph = graph_data['main_graph']
    mapplet_contents = graph_data['mapplet_contents']  # Mapplet names
    in_degree = defaultdict(int)

    # Compute in-degree for each node
    for node in graph:
        in_degree[node]  # Ensure all nodes are present
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Identify unconnected nodes that are not mapplets
    unconnected_nodes = [node for node in graph if not graph[node] and in_degree[node] == 0 and node not in mapplet_contents]
    unconnected_nodes.sort()  # Sort for deterministic output

    # Initialize heap with zero in-degree nodes (excluding unconnected and mapplets)
    zero_in_degree = [node for node in in_degree if in_degree[node] == 0 and node not in mapplet_contents and node not in unconnected_nodes]
    heapq.heapify(zero_in_degree)

    topological_order = unconnected_nodes[:]  # Start with unconnected nodes

    while zero_in_degree:
        current = heapq.heappop(zero_in_degree)

        if current in mapplet_contents:
            continue  # Skip mapplets in the final output

        topological_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0 and neighbor not in mapplet_contents:
                heapq.heappush(zero_in_degree, neighbor)

    if len(topological_order) != len([node for node in in_degree if node not in mapplet_contents]):
        raise ValueError("Graph has a cycle; topological sorting is not possible.")

    return topological_order

def visualize_hierarchical_graph(graph_data, topo_order):
    net = Network(height="700px", width="100%", directed=True, notebook=False)
    
    main_graph = graph_data['main_graph']
    mapplet_contents = graph_data['mapplet_contents']
    transformation_to_mapplet = graph_data['transformation_to_mapplet']
    
    # Compute in-degree for visual categorization
    in_degree = defaultdict(int)
    for from_node, to_nodes in main_graph.items():
        for to_node in to_nodes:
            in_degree[to_node] += 1

    # Identify sources, targets, and unconnected nodes
    sources = {node for node in main_graph if in_degree[node] == 0 and main_graph[node]}
    targets = {node for node in main_graph if not main_graph[node] and in_degree[node] > 0}
    unconnected_nodes = {node for node in main_graph if not main_graph[node] and in_degree[node] == 0}
    
    # Calculate metrics
    total_nodes = len(topo_order)
    num_sources = len(sources)
    num_targets = len(targets)
    num_mapplets = len(mapplet_contents)
    num_unconnected = len(unconnected_nodes)
    num_intermediate = total_nodes - (num_sources + num_targets + num_unconnected)
    
    metrics = {
        'total_nodes': total_nodes,
        'source_nodes': num_sources,
        'target_nodes': num_targets,
        'mapplet_nodes': num_mapplets,
        'unconnected_nodes': num_unconnected,
        'intermediate_nodes': num_intermediate
    }
    
    # Modified options for better visualization
    options = """
    {
        "nodes": {
            "font": {
                "size": 14,
                "face": "arial"
            }
        },
        "edges": {
            "color": "#2B2B2B",
            "width": 2,
            "arrows": {
                "to": {
                    "enabled": true,
                    "scaleFactor": 0.8
                }
            },
            "smooth": {
                "type": "cubicBezier",
                "roundness": 0.65
            }
        },
        "layout": {
            "hierarchical": {
                "enabled": true,
                "direction": "LR",
                "nodeSpacing": 200,
                "levelSeparation": 250
            }
        },
        "physics": {
            "enabled": false
        },
        "interaction": {
            "hover": true,
            "navigationButtons": true,
            "keyboard": {
                "enabled": true
            }
        }
    }
    """
    net.set_options(options)
    
    def wrap_text(text, max_length=15):
        return "\n".join([text[i:i+max_length] for i in range(0, len(text), max_length)])
    
    # Add nodes in topological order
    for node in topo_order:
        # Check if node is a mapplet
        if node in mapplet_contents:
            # Add mapplet as an expandable container
            net.add_node(
                node,
                label=wrap_text(node),
                color="#FFA500",  # Orange for mapplets
                shape="box",
                size=50,
                borderWidth=3,
                font={"size": 20, "color": "black", "bold": True},
                title=f"Click to expand/collapse\nContains {len(mapplet_contents[node])} transformations"
            )
            
            # Add transformations with parent mapplet ID
            for transform in mapplet_contents[node]:
                transform_id = f"{node}_{transform}"  # Create unique ID for the transformation
                net.add_node(
                    transform_id,
                    label=wrap_text(transform),
                    color="#95A5A6",  # Grey for transformations
                    shape="dot",
                    size=30,
                    hidden=True,  # Initially hidden
                    physics=False,
                    title=f"Transformation: {transform}\nParent Mapplet: {node}"
                )
                
                # Add edge from mapplet to transformation
                net.add_edge(node, transform_id, hidden=True)
        
        elif node not in transformation_to_mapplet:  # Only add if not already part of a mapplet
            # Determine node color based on type
            if node in sources:
                color = "#FF6B6B"  # Red for source nodes
            elif node in targets:
                color = "#4ECDC4"  # Cyan for target nodes
            elif node in unconnected_nodes:
                color = "#90EE90"  # Light green for unconnected nodes
            else:
                color = "#95A5A6"  # Grey for intermediate nodes
            
            net.add_node(
                node,
                label=wrap_text(node),
                color=color,
                shape="dot" if node in sources or node in targets else "box",
                size=40,
                font={"size": 18, "color": "black", "bold": True},
                borderWidth=2
            )
    
    # Add main graph edges
    for from_node, to_nodes in main_graph.items():
        for to_node in to_nodes:
            # Handle edges involving mapplet transformations
            from_mapplet = transformation_to_mapplet.get(from_node)
            to_mapplet = transformation_to_mapplet.get(to_node)
            
            if from_mapplet and to_mapplet:
                # Both nodes are transformations in mapplets
                if from_mapplet == to_mapplet:
                    # Internal mapplet connection
                    net.add_edge(f"{from_mapplet}_{from_node}", f"{to_mapplet}_{to_node}", hidden=True)
                else:
                    # Connection between different mapplets
                    net.add_edge(from_mapplet, to_mapplet)
            elif from_mapplet:
                # Only from_node is in a mapplet
                net.add_edge(from_mapplet, to_node)
            elif to_mapplet:
                # Only to_node is in a mapplet
                net.add_edge(from_node, to_mapplet)
            else:
                # Neither node is in a mapplet
                net.add_edge(from_node, to_node)
    
    # Add JavaScript for expand/collapse functionality
    expand_collapse_js = """
    <script>
    network.on("click", function(params) {
        if (params.nodes.length === 1) {
            var nodeId = params.nodes[0];
            var clickedNode = network.body.data.nodes.get(nodeId);
            
            // Check if it's a mapplet node (orange color)
            if (clickedNode.color.background === "#FFA500") {
                var allNodes = network.body.data.nodes.get();
                var allEdges = network.body.data.edges.get();
                var updateArray = [];
                var edgeUpdateArray = [];
                
                // Toggle child nodes
                allNodes.forEach(function(node) {
                    if (node.id.startsWith(nodeId + "_")) {
                        node.hidden = !node.hidden;
                        updateArray.push(node);
                    }
                });
                
                // Toggle related edges
                allEdges.forEach(function(edge) {
                    if (edge.from === nodeId || edge.to === nodeId || 
                        edge.from.startsWith(nodeId + "_") || edge.to.startsWith(nodeId + "_")) {
                        edge.hidden = !edge.hidden;
                        edgeUpdateArray.push(edge);
                    }
                });
                
                // Update the network
                network.body.data.nodes.update(updateArray);
                network.body.data.edges.update(edgeUpdateArray);
                network.fit(); // Adjust view to show all visible nodes
            }
        }
    });
    </script>
    """
    
    net.html += expand_collapse_js
    
    return net, metrics

import xml.etree.ElementTree as ET
from collections import defaultdict

def extract_metadata_from_xml(xml_file):
    """Extract metadata from an XML file with proper mapplet handling."""
    metadata = {
        "repository": None,
        "folder": None,
        "mappings": [],
        "mapplets": [],
        "targets": []
    }
    
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Extract repository details
    repository_element = root.find("REPOSITORY")
    if repository_element is not None:
        metadata["repository"] = repository_element.get("NAME")
    
    # Extract folder details
    folder_element = root.find("FOLDER")
    if folder_element is not None:
        metadata["folder"] = folder_element.get("NAME")
    
    # Store Input and Output Transformations of mapplets
    mapplet_io = {}
    for mapplet in root.findall(".//MAPPLET"):
        mapplet_name = mapplet.get("NAME")
        input_transformation = None
        output_transformation = None
        
        for transform in mapplet.findall(".//TRANSFORMATION"):
            transform_name = transform.get("NAME")
            transform_type = transform.get("TYPE")
            
            if transform_type == "Input Transformation":
                input_transformation = transform_name
            elif transform_type == "Output Transformation":
                output_transformation = transform_name
        
        mapplet_io[mapplet_name] = {
            "input": input_transformation,
            "output": output_transformation
        }
    
    # Extract mappings and transformations
    mappings = []
    for mapping in root.findall(".//MAPPING"):
        mapping_name = mapping.get("NAME")
        transformations = []
        
        for transformation in mapping.findall(".//TRANSFORMATION"):
            trans_name = transformation.get("NAME")
            trans_type = transformation.get("TYPE")
            trans_metadata = {
                "Name": trans_name,
                "Type": trans_type,
                "Details": []
            }
            
            for child in transformation:
                tag_name = child.tag
                attributes = child.attrib
                keys_to_remove = ['PICTURETEXT', 'PRECISION', 'SCALE', 'DEFAULTVALUE', 'DESCRIPTION']
                for key in keys_to_remove:
                    attributes.pop(key, None)
                text_content = child.text.strip() if child.text else ""
                trans_metadata["Details"].append({
                    "Tag": tag_name,
                    "Attributes": attributes,
                    "Text": text_content
                })
            
            connectors = mapping.findall('.//CONNECTOR[@TOINSTANCE="{}"]'.format(trans_name))
            connectors_info = []
            for connector in connectors:
                from_instance = connector.get("FROMINSTANCE")
                from_instance_type = connector.get("FROMINSTANCETYPE")
                to_instance = connector.get("TOINSTANCE")
                to_instance_type = connector.get("TOINSTANCETYPE")
                
                if from_instance_type == "Mapplet" and from_instance in mapplet_io:
                    from_instance = mapplet_io[from_instance]["output"] or from_instance
                if to_instance_type == "Mapplet" and to_instance in mapplet_io:
                    to_instance = mapplet_io[to_instance]["input"] or to_instance
                
                connectors_info.append({
                    "TOINSTANCE": to_instance,
                    "FROMINSTANCE": from_instance,
                    "FROMFIELD": connector.get("FROMFIELD"),
                    "TOFIELD": connector.get("TOFIELD"),
                })
            
            trans_metadata["Connectors"] = connectors_info
            transformations.append(trans_metadata)
        
        mappings.append({
            "MappingName": mapping_name,
            "Transformations": transformations
        })
    metadata["mappings"] = mappings
    
    # Extract mapplets and transformations
    mapplets = []
    for mapplet in root.findall(".//MAPPLET"):
        mapplet_name = mapplet.get("NAME")
        transformations = []
        
        for transformation in mapplet.findall(".//TRANSFORMATION"):
            trans_name = transformation.get("NAME")
            trans_type = transformation.get("TYPE")
            trans_metadata = {
                "Name": trans_name,
                "Type": trans_type,
                "Details": []
            }
            
            for child in transformation:
                tag_name = child.tag
                attributes = child.attrib
                keys_to_remove = ['PICTURETEXT', 'PRECISION', 'SCALE', 'DEFAULTVALUE', 'DESCRIPTION']
                for key in keys_to_remove:
                    attributes.pop(key, None)
                text_content = child.text.strip() if child.text else ""
                trans_metadata["Details"].append({
                    "Tag": tag_name,
                    "Attributes": attributes,
                    "Text": text_content
                })
            
            connectors = mapplet.findall('.//CONNECTOR[@TOINSTANCE="{}"]'.format(trans_name))
            connectors_info = []
            for connector in connectors:
                from_instance = connector.get("FROMINSTANCE")
                from_instance_type = connector.get("FROMINSTANCETYPE")
                to_instance = connector.get("TOINSTANCE")
                to_instance_type = connector.get("TOINSTANCETYPE")
                
                if from_instance_type == "Mapplet" and from_instance in mapplet_io:
                    from_instance = mapplet_io[from_instance]["output"] or from_instance
                if to_instance_type == "Mapplet" and to_instance in mapplet_io:
                    to_instance = mapplet_io[to_instance]["input"] or to_instance
                
                connectors_info.append({
                    "TOINSTANCE": to_instance,
                    "FROMINSTANCE": from_instance,
                    "FROMFIELD": connector.get("FROMFIELD"),
                    "TOFIELD": connector.get("TOFIELD"),
                })
            
            trans_metadata["Connectors"] = connectors_info
            transformations.append(trans_metadata)
        
        mapplets.append({
            "MappletName": mapplet_name,
            "Transformations": transformations
        })
    metadata["mapplets"] = mapplets
    
    # Extract target instances
    for instance in root.findall(".//INSTANCE"):
        instance_metadata = {
            "Name": instance.get("NAME"),
            "Type": instance.get("TYPE"),
            "TransformationName": instance.get("TRANSFORMATION_NAME"),
            "TransformationType": instance.get("TRANSFORMATION_TYPE")
        }
        if instance_metadata["TransformationType"] == "Target Definition":
            metadata["targets"].append(instance_metadata['Name'])
    
    return metadata

def get_target_connectors(xml_file):
    """
    Extract target table names and connectors where TOINSTANCE matches target tables.
    
    :param xml_file: Path to the Informatica XML file.
    :return: Dictionary with target table names and connectors.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    metadata = {"targets": [], "connectors": []}
    
    # Extract INSTANCE tags for target tables
    for instance in root.findall(".//INSTANCE"):
        instance_metadata = {
            "Name": instance.get("NAME"),
            "Type": instance.get("TYPE"),
            "TransformationName": instance.get("TRANSFORMATION_NAME"),
            "TransformationType": instance.get("TRANSFORMATION_TYPE")
        }
        if instance_metadata["TransformationType"] == "Target Definition":
            metadata["targets"].append(instance_metadata['Name'])
    
    # Extract connectors for the identified target tables
    for connector in root.findall(".//CONNECTOR"):
        to_instance = connector.get("TOINSTANCE")
        if to_instance in metadata["targets"]:
            metadata["connectors"].append({
                "TOINSTANCE": to_instance,
                "FROMINSTANCE": connector.get("FROMINSTANCE"),
                "FROMFIELD": connector.get("FROMFIELD"),
                "TOFIELD": connector.get("TOFIELD"),
            })
    
    return metadata


def extract_cte_from_informatica_xml(xml_filepath, transformation_name):
    """
    Extracts the Transformation name and FROMINSTANCE transformations from an Informatica XML file 
    for the given transformation name, including unconnected nodes.

    Args:
    xml_filepath (str): Path to the Informatica XML file.
    transformation_name (str): Name of the transformation to search for.

    Returns:
    dict: A dictionary with transformation names as keys and FROMINSTANCE transformations as values.
    """
    tree = ET.parse(xml_filepath)
    root = tree.getroot()

    output = set()
    all_transformations = set()
    connected_transformations = set()

    # Extract all transformations
    for transformation in root.findall(".//TRANSFORMATION"):
        transformation_name_attr = transformation.get("NAME")
        if transformation_name_attr:
            all_transformations.add(transformation_name_attr)

    # Iterate through CONNECTOR elements to find connected transformations
    for connector in root.findall(".//CONNECTOR"):
        to_instance = connector.get("TOINSTANCE")
        from_instance = connector.get("FROMINSTANCE")

        if to_instance:
            connected_transformations.add(to_instance)
        if from_instance:
            connected_transformations.add(from_instance)

        # If the TOINSTANCE matches the transformation_name, extract FROMINSTANCE details
        if to_instance == transformation_name:
            output.add(from_instance)

    # Identify unconnected transformations
    unconnected_transformations = all_transformations - connected_transformations

    return output | unconnected_transformations