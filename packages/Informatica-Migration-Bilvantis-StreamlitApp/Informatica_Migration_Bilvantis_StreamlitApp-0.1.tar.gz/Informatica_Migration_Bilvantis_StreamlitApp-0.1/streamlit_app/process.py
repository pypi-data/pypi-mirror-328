import xml.etree.ElementTree as ET
import sys,os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import traceback
import time
import streamlit as st

from handle_transformation import transformation_functions
from metadata_topology import *
import yaml

# Load environment variables
load_dotenv("/home/rajesh/Desktop/informaticia/.env",override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# load the Traget technology  from yaml
with open("target_config.yaml", "r") as file:
    transformations = yaml.safe_load(file)

target = transformations.get('transformations', {}).get('Target', None)

# load the llm model to be used from the yaml
with open("model_config.yaml", "r") as file:
    llms = yaml.safe_load(file)

model = llms.get('llms', {}).get('model', None)
if model == "gpt-4o":
    llm = ChatOpenAI(model=model, temperature=0, openai_api_key=OPENAI_API_KEY)
elif model == "gemini-2.0-flash":
    llm = ChatGoogleGenerativeAI(model=model, temperature=0, google_api_key=GOOGLE_API_KEY)

def process_transformation(repository, folder, transformation, reference_query, target):

    trans_type = transformation["Type"]
    
    if trans_type not in transformation_functions:
        trans_type = "General"
    
    if trans_type in transformation_functions:
        prompt =f"""
        
        I will provide information about transformations extracted from an Informatica mapping, including connectors and transformation details. Additionally, a reference query may be provided for guidance.  

        Your task is to write the equivalent {target} SQL query for the transformations, strictly following these rules:  

        ### General Rules:  
        1. **CTE Usage**:  
        - Write each transformation or logical group in its own **Common Table Expression (CTE)**.    
        - Dont not add SELECT statemets after each CTE.
        - For each Transformation generate one CTE except Router Transformation where multiple CTEs are required.
        - If a lookup transformation is encountered, only reference it directly using the "FROM" clause of the reference query. Do not add any queries from the reference query to the current transformation.
        - While generating CTE if any lookups are encountered, **perform left** join using connector info for conditioning refer connectors and use alias like FROMINSTANCE.FROMFIELD AS TOFIELD in TOINSTANCE.
        - While generating any Transformation CTE if router CTE need to be refered in the FROM clause, Do not refer the router CTE, instead refer the group name present for that CTE from reference query in the FROM clause. (The group can be identified by checking the common field name present in the current transformation and the router group).
        - Output only the {target} SQL code without any additional explanations or comments. 
        - Make 100% sure that no other transformation queries present in reference query are provided in the current output but only reffered thier names if required.
        - Also ensure there are no invalid {target} functions present if present replace with equivalent {target} functions/ regenerate the equivalent logic retaining the previous logic. 
        (like ISNULL, NVL, DECODE, etc. will not work in {target}, so we need to replace them with equivalent functions retaining the previous logic).

        2. **Field Aliases**:  
        - Always use **aliasing**(FROMINSTANCE.FROMFIELD AS TOFIELD in TOINSTANCE) provided in **connectors** present for fields and tables in all CTEs.  

        3. **{target}-Compatible Functions**:
        - If any logic/function present in the transformation, those need to be converted into equivalenct big queruy functions.
        - if any function which are not valid in {target}, use the equivalent one.
        - Highlight and replace any invalid or unsupported functions with the correct {target} equivalents.

        ### Handling Transformations:  

        4. **Sequence and Dependencies**:  
        - Maintain the correct sequence and flow of CTEs based on the dependency of transformations refering from connectors.  
        - Reference CTE names wherever required. Avoid standalone SELECT statements after transformations.
        - Ensure that the final result is obtained from the last CTE. 
        
        5. **Minimal Assumptions**:  
        - Use **only the table names, fields, and logic explicitly mentioned** in the transformation details.  
        - Do not introduce extraneous fields, logic, or tables unless explicitly provided.  
        
        ### Transformation Details:
        """
        prompt += transformation_functions[trans_type]()
        prompt +=f"""
        Details Provided:

        - Project Name: {repository}
        - Dataset Name: {folder}
        - Transformation Name: {transformation['Name']}
        - Transformation Type: {transformation['Type']}
        """
        # print("\n\n\n",prompt,"\n\n\n")
        for detail in transformation["Details"]:
            prompt += f"  - Tag: {detail['Tag']}, Attributes: {detail['Attributes']}, Text: {detail['Text']}\n"

        prompt += "\nConnectors (indicating relationships between transformations):\n"
        for connector in transformation["Connectors"]:
            prompt += f"  - TOINSTANCE: {connector['TOINSTANCE']}, FROMINSTANCE: {connector['FROMINSTANCE']}, FROMFIELD: {connector['FROMFIELD']}, TOFIELD: {connector['TOFIELD']}\n"

        prompt+= f" ### Reference Query:: \n{reference_query}" 

        prompt+=f"""
        ### Output:  
        Provide the requested {target} SQL query adhering to the rules above. Ensure:  
        - Correctness and completeness.  
        - Readability and performance optimization.  
        - Adherence to {target} standards.  
        """
        # Initialize LLM and call it
        # llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=OPENAI_API_KEY)
        response = llm.invoke(prompt)
        print("Generated SQL query for transformation:",transformation["Name"],"\n")
        st.write("Generated SQL query for transformation:",transformation["Name"],"\n")
        return response.content
    else:
        print(f"Transformation type {trans_type} is not supported.")
        return None


def completeness_layer(xml_file_path, query, target):

    prompt=f"""
    - I will Provide you the Queries where each transformation has its own CTE, 
    - I want you to combine all CTEs present for each transformation into single CTE without even changing any single logic from the query(by retaining only one with and seperate each with comma). 
    - Also add the Target CTE at the end of the respective transformation with target table alias based on the connector info, target table names along with connectors are present in the following dictionary.
    - Output only the {target} SQL code without any additional explanations or comments. 
    ### Query Provided:
    {query}


    ### Target_Tables and Connector Info:
    {get_target_connectors(xml_file_path)}

    """
    # Initialize LLM and call it
    st.write("Adding Target CTEs......\n")
    llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=OPENAI_API_KEY)
    response = llm.invoke(prompt)
    finale = response.content.replace("```sql","").replace("```","")
    return finale

def main(xml_file_path, target):
    # Extract metadata from the XML file
    metadata = extract_metadata_from_xml(xml_file_path)
    if not metadata:
        print("Failed to extract metadata. Please check the XML file.")
        return ""

    final_query = ""
    
    transformation_mapplet = []
    for mapplet in metadata['mapplets']:
        # print(mapplet)
        transformation_mapplet.append(mapplet['Transformations'])

    for mapping in metadata['mappings']:
        print(f"Mapping: {mapping['MappingName']}\n")
        st.write(f"Mapping: {mapping['MappingName']}\n")
        final_query += f"-- Mapping: {mapping['MappingName']}\n\n"

        # Resolve transformation order
        transformations = mapping["Transformations"]
        for mplt in transformation_mapplet:
            transformations.extend(mplt)

        try:
            graph = extract_graph_with_mapplets(xml_file_path)
            resolved_order = topological_sort_for_transformation(graph)

            # Logic to add the lookup transformations into the resolved order and remove the transformations tag which are not present in the metadata
            all_transformation_present = [t["Name"] for t in transformations]
            # print(f"\nTransformations present in metadata: {all_transformation_present}")

            # Step 1: Remove items from resolved_order that are not in all_transformation_present
            # print(f"\nResolved transformation order: {resolved_order}")
            resolved_order = [item for item in resolved_order if item in all_transformation_present] ### source and targets are getting removed from the resolved order
            print(f"\nResolved transformation order -------------: {resolved_order}")

            # Step 2: Add items to the start of resolved_order that are in all_transformation_present but not in resolved_order
            # unconnected_lookup_items = [item for item in all_transformation_present if item not in resolved_order]

            # # print(f"\nLookup items: {unconnected_lookup_items}")


            # resolved_order = unconnected_lookup_items + resolved_order
            # st.write(f"\nResolved transformation order: {resolved_order}\n")
            # print(f"\nlookup added resolved transformation order: {resolved_order}\n")

            # print(f"\nResolved transformation order: {resolved_order}\n")
        except Exception as e:
            # import traceback
            # trc = traceback.print_exc()
            print(f"Error resolving transformation order: {e}")
            # print(f"Error resolving transformation order: {trc}")
            final_query += f"-- Error resolving transformation order: {e}\n\n"
            continue

        ##### Generating Query
        ref_query_dict = {}
        for trans_name in resolved_order:
            transformation = next((t for t in transformations if t["Name"] == trans_name), None)
            if not transformation:
                print(f"Transformation {trans_name} not found in metadata.")
                continue

            print(f"Transformation: {transformation['Name']} (Type: {transformation['Type']})")
            st.write(f"Transformation: {transformation['Name']} (Type: {transformation['Type']})")

            final_query += f"-- Transformation: {transformation['Name']} (Type: {transformation['Type']})\n\n"

            # Generate SQL Query for transformation
            ref_trans = extract_cte_from_informatica_xml(xml_file_path, trans_name)
            print("\n\n\t\t-- ",ref_trans)
            ref_query = ""
            for cte in ref_trans:
                ref_query += ref_query_dict.get(cte,"No Reference Query Present")
            # print("\n\n\t\t-- ",ref_query)
            try:
                query = process_transformation(metadata['repository'], metadata['folder'], transformation, ref_query, target)
                # print("process_transformation(metadata['repository'], metadata['folder'], transformation, final_query)")
                final_query += query + "\n\n" + "*" * 50 + "\n\n"
                print("\n\n",query, "\n\n")
            except Exception as e:
                import traceback
                trace = traceback.print_exc()
                print(f"Error generating SQL query for {transformation['Name']}: {e}\n\n{trace}")
                final_query += f"-- Error generating SQL Query: {e}\n\n"
                final_query += "\n\n" + "*" * 50 + "\n\n"
            
            ref_query_dict[trans_name] = query

    ### making it single cte and adding target ctes at the end of the respective transformation
    # final_query = completeness_layer(xml_file_path, final_query, target)
    return final_query


def process_xml_file(xml_file_path,basename, output_folder):
    try:
        # Run the validation and correction loop for all transformations
        final_query = main(xml_file_path, target)

        # Create the output folder  if they don't exist
        os.makedirs(output_folder, exist_ok=True)

        # Generate timestamp prefix
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        # Prepare output file name with timestamp
        output_file_name = f"{timestamp}_{os.path.splitext(basename)[0]}.txt"
        output_file_path = os.path.join(output_folder, output_file_name)
        
        # Save the output
        with open(output_file_path, "w") as output_file:
            output_file.write(final_query)
        
        print(f"Saved SQL queries to: {output_file_path}")

        return final_query
    except Exception as e:
        print(f"Error processing {xml_file_path}: {e}")
