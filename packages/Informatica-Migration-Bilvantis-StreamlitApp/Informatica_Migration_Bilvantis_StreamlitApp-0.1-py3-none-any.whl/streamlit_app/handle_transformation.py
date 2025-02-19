class TransformationHandler:
    def __init__(self,target):
        self.target = target    

    def handle_router(self):
        prompt = f"""
        For a Router Transformation:
        - Generate separate {self.target} CTEs for each output group based on router conditions.
        - Use transformation metadata for grouping rows.
        - Go through the all Group Condition carefully, All the records which do not match any Group Condition should be included in the DEFAULT group. 
        - The conditions in the defualt group should be opposite of All group conditions(If True is present in a group then here it should be False and vise versa).
        """
        return prompt


    def handle_joiner(self):
        prompt = f"""
        For a Joiner Transformation:
        - Write a {self.target} SQL JOIN query based on transformation metadata conditions.
        - Ensure proper join type (INNER, OUTER) and correct alignment of columns.
        """

        return prompt

    def handle_aggregator(self):
        prompt = f"""
        For an Aggregator Transformation:
        - Generate a {self.target} SQL query with aggregate functions (e.g., SUM, AVG, COUNT) based on metadata.
        - Group by required columns and compute specified outputs.
        """

        return prompt

    def handle_filter(self):
        prompt =  f"""
        For a Filter Transformation:
        - Write a {self.target} SQL WHERE clause based on the filter conditions in the metadata.
        - Ensure correct column references and logical operations.
        - Include `DEFAULT` conditions and other required `WHERE` conditions as specified in the transformation details.
        """

        return prompt

    def handle_expression(self):
        prompt = f"""
        For an Expression Transformation:
        - Generate a {self.target} SQL SELECT statement with calculated columns based on transformation expressions.
        - Map inputs to outputs using expressions defined in metadata.
        - Replace invalid {self.target} functions with equivalent {self.target} functions/ regenerate the equivalent logic retaining the previous logic. 
        (like ISNULL, NVL, DECODE, etc. will not work in {self.target}, so we need to replace them with equivalent functions retaining the previous logic).
        - Ensure correct column references and logical operations.
        - While generating CTE if any lookups are encountered, **perform left join ** on the lookup table, for conditioning refer connectors and use alias like FROMINSTANCE.FROMFIELD AS TOFIELD in TOINSTANCE .
                
        Your task is to analyze the JSON metadata of Informatica mappings, specifically focusing on **variable ports** within transformations like **Expression, Aggregator, and Joiner**, and generate optimized SQL or cloud-native code to replicate the same logic in the target cloud environment.  

        ❌ Avoid These SQL Mistakes:
        🚨 1. No Self-Referencing in Case Conditions:
        Do not generate conditions that try to reference previously derived variables within the same transformation step, such as:

        CASE 
            WHEN ABC = v_ABC 
                AND EFG != v_qwe THEN 1
            WHEN ABC = v_ABC THEN v_prev_flag + 1
            ELSE 1
        END AS Flag
        ❌ Wrong: SQL does not allow referencing a column that is created in the same computation step.

        🚨 2. No Use of LAG() or LEAD() on Derived Columns:

        Do not generate LAG(SRTTRANS.Flag) in SQL, as Flag is derived in the same query.
        This results in an invalid reference that SQL cannot process correctly.
        🚨 3. No Recursive Condition Evaluations:

        SQL does not support Informatica-style looped condition evaluations inside a transformation.
        ✅ Correct Approach: Use ROW_NUMBER() for Sequencing
        Instead of incorrect variable-based logic, always apply window functions like ROW_NUMBER() with the correct partitioning and ordering.

        🚨 4. Handling Winner-Loser Scenarios without Self-Referencing:
        - If a column references its own derived value (e.g., `PREV_Winner` referring to `WINNER`), rewrite the logic to use **window functions**.
        - **Correct SQL Approach:**
        🚨If we are comparing the previous values upto and if previous value is null, then consider the previous previous value(use MAX to ignore nulls)

        SELECT 
            AB_SITE,
            FLAG,
            CASE 
                WHEN FLAG = 1 THEN AB_SITE
                ELSE MAX(CASE WHEN FLAG = 1 THEN AB_SITE END)
                    OVER (ORDER BY ACCOUNT_ID, B_SITE) 
            END AS Summer,
            CASE 
                WHEN FLAG > 1 THEN AB_SITE
                ELSE ''
            END AS Winter
        FROM Testgroup;

        🎯 Expected SQL Output
        
        SELECT 
            ABC,
            EFG,
            ROW_NUMBER() OVER (
                PARTITION BY ABC, EFG 
                ORDER BY ABC, EFG, KLM DESC, 
                        PLM DESC, OKN DESC, IJB DESC, GHI ASC
            ) AS FLAG
        FROM Source_Table;

        ### **Input Format (JSON)**  
        The input will be a JSON object containing **transformation details**, including ports and their expressions.  

        #### **Example JSON Input:**
        """
        {
            "transformation": {
                "name": "EXP_Sample",
                "type": "Expression",
                "ports": [
                    {
                        "name": "VAR_TOTAL",
                        "datatype": "integer",
                        "expression": "VAR_TOTAL + INPUT_AMOUNT"
                    },
                    {
                        "name": "VAR_COUNTER",
                        "datatype": "integer",
                        "expression": "VAR_COUNTER + 1"
                    },
                    {
                        "name": "VAR_IS_FIRST_ROW",
                        "datatype": "integer",
                        "expression": "IIF(VAR_PREV_ID != INPUT_ID, 1, 0)"
                    },
                    {
                        "name": "VAR_PREV_ID",
                        "datatype": "string",
                        "expression": "INPUT_ID"
                    },
                    {
                        "name": "OUTPUT_TOTAL",
                        "datatype": "integer",
                        "expression": "VAR_TOTAL"
                    },
                    {
                        "name": "OUTPUT_COUNTER",
                        "datatype": "integer",
                        "expression": "VAR_COUNTER"
                    },
                    {
                        "name": "OUTPUT_IS_FIRST_ROW",
                        "datatype": "integer",
                        "expression": "VAR_IS_FIRST_ROW"
                    }
                ]
            }
        }
        """
        ### **Output Format (Optimized SQL without Self-Referencing Issues)**  
        The LLM should analyze the JSON and generate **equivalent SQL logic** that avoids self-referencing by using **window functions, subqueries, or CTEs**.  

        #### **Example Correct SQL Output (BigQuery/Snowflake)**
        
        WITH ProcessedData AS (
            SELECT 
                INPUT_AMOUNT,
                INPUT_ID,
                SUM(INPUT_AMOUNT) OVER (ORDER BY <ordering_column> ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS OUTPUT_TOTAL,
                ROW_NUMBER() OVER (ORDER BY <ordering_column>) AS OUTPUT_COUNTER,
                LAG(INPUT_ID) OVER (ORDER BY <ordering_column>) AS PREV_ID
            FROM 
                Source_Table
        )
        SELECT 
            INPUT_AMOUNT,
            INPUT_ID,
            OUTPUT_TOTAL,
            OUTPUT_COUNTER,
            CASE 
                WHEN PREV_ID != INPUT_ID THEN 1 
                ELSE 0 
            END AS OUTPUT_IS_FIRST_ROW
        FROM ProcessedData;
        """
        return prompt

    def handle_lookup(self):
        prompt = f"""
        For a Lookup Transformation:
        - Generate CTE for lookup table based on metadata.
        - Ensure proper key mappings and output field assignments.
        - Use the exact lookup table name provided in the transformation details.
        - Construct the Left join condition **strictly as specified** in the transformation details.   
        - If {self.target} SQL override is provided, use as it is and do not consider lookup source filters.

        """

        return prompt

    def handle_sequence_generator(self):
        prompt = f"""
        For a Sequence Generator Transformation:
        - Generate {self.target} SQL logic for creating a sequence based on metadata.
        - Ensure the sequence is unique and increments as defined.
        
        """
        return prompt

    def handle_sorter(self):
        prompt = f"""
        For a Sorter Transformation:
        - Write a {self.target} SQL ORDER BY clause based on sort key(s) from metadata.
        - Specify ascending or descending order as per transformation details.
        - If Distinct is enabled, use the DISTINCT and No ORDER BY clause should be used.
        
        """
        return prompt

    def handle_update_strategy(self):
        prompt =  f"""
        For an Update Strategy Transformation:
        - Write {self.target} SQL logic to handle updates and inserts based on strategy.
        - Ensure proper WHERE conditions for updates.

        """

        return prompt

    def handle_union(self):
        prompt = f"""
        For a Union Transformation:
        - Write {self.target} SQL UNION or UNION ALL query to combine multiple input datasets.
        - Ensure column alignment and data type consistency across inputs.

        """
        return prompt

    def handle_source_qualifier(self):
        prompt = f"""
        - Make 100 % sure that If sql query is provided in the json data, use it as is. Otherwise, generate a {self.target} SQL query to read data from the using the connector data with alias present in it.
        - Include any source-specific filters or joins as required.

        """

        return prompt

    def handle_target(self):
        prompt = f"""
        For a Target Transformation:
        - Define the INSERT or UPDATE {self.target} SQL query to write data to the target table.
        - Ideally the output of the recent transformation should be used as the input for the target transformation.
        - Ensure column mapping and constraints are honored.

        """

        return prompt

    def handle_transaction_control(self):
        prompt = f"""
        For a Transaction Control Transformation:
        - Generate {self.target} SQL logic to commit or rollback transactions.
        - Ensure proper handling of transaction boundaries.

        """

        return prompt

    def handle_stored_procedure(self):
        prompt = f"""
        For a Stored Procedure Transformation:
        - Define the {self.target} SQL call to invoke the stored procedure with parameters.
        - Ensure parameter mapping is accurate.

        """

        return prompt

    def handle_normalizer(self):
        prompt = f"""
        For a Normalizer Transformation:
        - Generate {self.target} SQL logic to denormalize or normalize data as specified.
        - Ensure mapping of multiple inputs to a flattened output.

        """

        return prompt

    def handle_rank(self):
        prompt = f"""
        For a Rank Transformation:
        - Write {self.target} SQL logic to assign ranks to rows based on sort keys.
        - Ensure ties are handled as per transformation logic.

        """

        return prompt

    def handle_xml_source_qualifier(self):
        prompt =  f"""
        For an XML Source Qualifier Transformation:
        - Define logic to parse XML data and map it to relational fields.
        - Use transformation metadata to extract required fields.

        """
        return prompt

    def handle_xml_target(self):
        prompt =  f"""
        For an XML Target Transformation:
        - Define logic to write relational data to an XML structure.
        - Write required insert statements according to the available data produced in XML chunk.
        - Use metadata for field mapping and hierarchy generation.

        """
        return prompt

    def handle_java_transformation(self):
        prompt = f"""
        For a Java Transformation:
        - Generate logic to handle complex transformations using Java code.
        - Include metadata for inputs, outputs, and transformation logic.

        """
        return prompt

    def handle_sql_transformation(self):
        prompt = f"""
        For a {self.target} SQL Transformation:
        - Write {self.target} SQL script to handle logic for the transformation.
        - Use metadata for {self.target} SQL inputs and outputs.

        """
        return prompt

    def handle_mapplet(self):
        prompt = f"""
        For a Mapplet Transformation:
        - Define logic for reusing a group of transformations.
        - Ensure inputs and outputs are mapped correctly.

        """
        return prompt

    def handle_mapplet_input(self):
        prompt = f"""
        For a Mapplet Input Transformation:
        - Define the mapping of input fields to the mapplet logic.

        """

        return prompt

    def handle_mapplet_output(self):
        prompt = f"""
        For a Mapplet Output Transformation:
        - Map output fields from the mapplet logic to downstream targets.

        """
        return prompt

    def handle_external_procedure(self):
        prompt = f"""
        For an External Procedure Transformation:
        - Define the procedure logic and its integration points.

        """
        return prompt

    def handle_custom_transformation(self):
        prompt = f"""
        For a Custom Transformation:
        - Write logic for the custom operation as defined in metadata.
        - Include input, output, and operational details.
        
        """

        return prompt

    def handle_active_transformation(self):
        prompt = f"""
        For an Active Transformation:
        - Ensure logic modifies row counts or formats dynamically.
        - Define active logic based on transformation metadata.

        """

        return prompt
    
    def handle_input_transformation(self):
        prompt = f"""
        For an Input Transformation:
        - Take input from previous CTE refering from connectors(frominstance) and just pass it out, nothing else.
        - Use proper aliasing like 'frominstance.fromfield as tofield' from the connectors

        """

        return prompt
    def General(self):
        prompt = f"""   """

        return prompt
    
    # ['Transaction Control',
    #  'Update Strategy',
    #  'Sorter',
    #  'Router',
    #  'Joiner',
    #  'Expression',
    #  'Filter',
    #  'Aggregator',
    #  'Lookup Procedure',
    #  'Source Qualifier']

# Read the YAML file
import yaml
with open("target_config.yaml", "r") as file:
    transformations = yaml.safe_load(file)

target = transformations.get('transformations', {}).get('Target', None)

# Instantiate the TransformationHandler
handler = TransformationHandler(target)

transformation_functions = {
        "General":handler.General,
        "Router": handler.handle_router,
        "Joiner": handler.handle_joiner,
        "Aggregator": handler.handle_aggregator,
        "Filter": handler.handle_filter,
        "Expression": handler.handle_expression,
        "Lookup Procedure": handler.handle_lookup,
        "Sequence Generator": handler.handle_sequence_generator,
        "Sorter": handler.handle_sorter,
        "Update Strategy": handler.handle_update_strategy,
        "Union": handler.handle_union,
        "Source Qualifier": handler.handle_source_qualifier,
        "Target": handler.handle_target,
        "Transaction Control": handler.handle_transaction_control,
        "Stored Procedure": handler.handle_stored_procedure,
        "Normalizer": handler.handle_normalizer,
        "Rank": handler.handle_rank,
        "XML Source Qualifier": handler.handle_xml_source_qualifier,
        "XML Target": handler.handle_xml_target,
        "Java Transformation": handler.handle_java_transformation,
        "SQL Transformation": handler.handle_sql_transformation,
        "Mapplet": handler.handle_mapplet,
        "Mapplet Input": handler.handle_mapplet_input,
        "Mapplet Output": handler.handle_mapplet_output,
        "External Procedure": handler.handle_external_procedure,
        "Custom Transformation": handler.handle_custom_transformation,
        "Active Transformation": handler.handle_active_transformation,
        "Input Transformation":handler.handle_input_transformation,
    }