"""
Copyright 2025 Neeraj Morar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import re
import json

from pathlib import Path

def create_record_datatype(record_data):
    """
    Takes a JSON converted into a Python dictionary which represents a SQL STRUCT and 
    converts it into SQL representation.

    Args:
        record_data (list of dict): The JSON object which is contained as Python list object, each 
        item is a dict representing a row of data.

    Returns:
        str: A SQL string representing the JSON object provided as SQL STRUCT
    """
    columns_and_dtypes = {}
    for col, col_val in record_data[0].items():
        columns_and_dtypes[col] = col_val[1]
    record = "ARRAY<STRUCT<"
    for col, dtype in columns_and_dtypes.items():
        if dtype != "RECORD":
            record += f"{col} {dtype},"
        else:
            record_split = create_record_datatype(record_data[0][col][0]).split("[")
            record += f"{col} {record_split[0]},"
    record = record[:-1]
    record += ">>["

    elements = []
    for x in record_data:
        element = "("
        for col, col_val in x.items():
            if col_val[1] != "RECORD":
                if col_val[0] is None:
                    value_to_use = "NULL"
                else:
                    col_val_cleaned = col_val[0].replace("'", "\\'")
                    value_to_use = f"'{col_val_cleaned}'"
                
                converted_sql_string = process_complex_datatypes(col_val[1], col_val[0])
                if converted_sql_string:
                    element_value = f"{converted_sql_string},"
                else:
                    element_value = f"SAFE_CAST({value_to_use} AS {col_val[1]}),"
                element += element_value
            else:
                record_split = create_record_datatype(col_val[0]).split(">>")
                element += f"{record_split[1]},"
        element = element[:-1]
        element += ")"
        elements.append(element)

    record += ", ".join(elements)
    record += "]"

    return record


def build_rows(rows_to_build):
    """
    Takes a list of dicts, where each dict represents a SQL row of data. The key
    is the column name, the value is a list object, where the first item is the value
    for that column, and the second item is the datatype for that column

    Args:
        rows_to_build (list of dicts): The list containing dicts representing SQL rows

    Returns:
        str: A SQL string representing individual rows of data
    """
    rows = [] 
    no_of_rows = len(rows_to_build)
    for x in range(no_of_rows):
        columns = []
        for col, col_val in rows_to_build[x].items():
            if col_val[1] != "RECORD":
                if col_val[0] is None:
                    value_to_use = "NULL"
                elif "ARRAY<" in col_val[1]:
                    value_to_use = col_val[0]
                else:
                    col_val_cleaned = col_val[0].replace("'", "\\'")
                    value_to_use = f"'{col_val_cleaned}'"
                
                converted_sql_string = process_complex_datatypes(col_val[1], col_val[0])
                if converted_sql_string:
                    columns.append(f"{converted_sql_string} AS {col}")
                else:
                    columns.append(f"SAFE_CAST({value_to_use} AS {col_val[1]}) AS {col}")
            else:
                columns.append(f"{create_record_datatype(col_val[0])} AS {col}")
    
        columns_joined = ',\n\t'.join(columns)
        rows.append(columns_joined)
    
    return '\nUNION ALL\nSELECT\n\t'.join(rows)


def handle_bytes_datatype(col_value):
    """
    Takes a column that is a BigQuery Bytes datatype and casts it appropriately

    Args:
        col_value (str): The value which is supposed to be a bytes datatype

    Returns:
        str: A SQL string representation of the input data from the unit test converting the value to a Bytes datatype
    """
    return f"FROM_BASE64('{col_value}')"


def handle_json_datatype(col_value):
    """
    Takes a column that is a JSON data/object and casts it appropriately for BigQuery

    Args:
        col_value (str): The value which is supposed to be a JSON datatype

    Returns:
        str: A SQL string representation of the input data from the unit test converting the value to a JSON datatype
    """
    if isinstance(col_value, str):
        col_value = col_value.replace("'", '"')
        col_value = re.sub('(\w+)"(\w+)', "\\1'\\2", col_value, flags=re.MULTILINE)
        json_object = json.loads(col_value)
    else:
        json_object = col_value

    if isinstance(json_object, list):
        json_list = []
        for nested_json in json_object:
            json_list.append(build_json_object_str(nested_json))
        json_sql_str = ', '.join(json_list)
        json_sql_str = f"JSON_ARRAY({json_sql_str})"
    elif isinstance(json_object, dict):
        json_sql_str = build_json_object_str(json_object)
    return json_sql_str


def build_json_object_str(json_object):
    """
    Takes a JSON object and converts into a SQL string representation of it

    Args:
        json_object (dict): A Python dict representing the JSON object to parse

    Returns:
        str: A SQL string representation of the input data from the unit test converting the value to a JSON datatype
    """
    string_pairs = []
    for key, value in json_object.items():
        if isinstance(value, dict):
            string_pairs.append(f"'{key}', {handle_json_datatype(value)}")
        else:
            if isinstance(value, str):
                value = value.replace("'", "\\'") 
                value = f"'{value}'"
            string_pairs.append(f"'{key}', {value}")

    json_sql_str = ', '.join(string_pairs)
    json_sql_str = f"JSON_OBJECT({json_sql_str})"
    return json_sql_str


def handle_geography_datatype(geo_value_string):
    """
    Takes a WKT Geo string and converts into a SQL string representation of it

    Args:
        geo_value_string (str): A string in WKT geographic format

    Returns:
        str: A SQL string representation of the input data from the unit test converting the value to a Geography datatype
    """
    e = Exception(f"Invalid Geography Value Provided: {geo_value_string}")
    geography_subtypes = ["POINT", "LINESTRING", "POLYGON", "MULTIPOINT", "MULTILINESTRING", "MULTIPOLYGON", "GEOMETRYCOLLECTION"]
    for subtype in geography_subtypes:
        matches = re.findall(f"^{subtype}", geo_value_string, flags=re.MULTILINE)
        if len(matches) == 1:
            additional_subtypes = geo_value_string.replace(subtype, "", 1)
            if any(second_sub in additional_subtypes for second_sub in geography_subtypes) and matches[0] != "GEOMETRYCOLLECTION":
                raise e
            else:
                return f"ST_GEOGFROMTEXT('{geo_value_string}')"
    
    raise e


def process_complex_datatypes(datatype, column_value):
    """
    Takes a datatype and evaluates if it's one of the complex datatypes to process

    Args:
        datatype (str): The datatype to check
        column_value (str): The column value to process if it's a complex datatype

    Returns:
        bool: True if it is a complex datatype, False if not
        str: A SQL string representation of the complex datatype, None if it isn't
    """
    if datatype == "BYTES":
        return handle_bytes_datatype(column_value)
    if datatype == "JSON":
        return handle_json_datatype(column_value)
    if datatype == "GEOGRAPHY":
        return handle_geography_datatype(column_value)

    return None


def create_input_ctes(test):
    """
    Takes a JSON converted into a Python dictionary and turns them into SQL
    CTEs.

    Args:
        test (dict): The JSON object which is contained as Python dict object.

    Returns:
        str: A SQL representation of the input data from the unit test as SQL CTEs
    """
    sql = []
    for table, row in test["input_data"].items():
        rows_joined = build_rows(row)
        sql.append(f"{table.replace('.', '_')} AS (\nSELECT\n\t{rows_joined}\n)")
    
    input_ctes = ',\n'.join(sql)
    return f"WITH {input_ctes},"


def create_expected_output_cte(test):
    """
    Takes a JSON converted into a Python dictionary and turns them into a SQL
    CTE.

    Args:
        test (dict): The JSON object which is contained as Python dict object.

    Returns:
        str: A SQL representation of the expected output data from the unit test as a SQL CTE
    """
    rows_joined = build_rows(test["expected_output"])
    return f"expected_output AS (\nSELECT\n\t{rows_joined}\n),"


def replace_table_refs_with_test_inputs(test, query_to_replace):
    """
    Takes the Dataform model to be tested and replaces table
    references with the input test data CTEs

    Args:
        test (dict): The JSON object which is contained as Python dict object.
        query_to_replace (str): The Dataform model being tested as a SQL string

    Returns:
        str: A SQL representation of the Dataform model with table references replaced 
        with input test data CTEs
    """
    for key in test["input_data"].keys():
        schema_and_table = key.split(".")
        query_to_replace = re.sub(f"\`.+?{schema_and_table[0]}\.{schema_and_table[1]}\`", f"{key.replace('.', '_')}", query_to_replace, flags=re.MULTILINE)

    columns_to_test = "SELECT "
    for key in test["expected_output"][0].keys():
        columns_to_test += f"{key},"
    columns_to_test = columns_to_test[:-1]
    
    query_to_replace = f"actual_output AS (\n{columns_to_test} FROM (\n{query_to_replace.strip()}\n))"
    
    return query_to_replace


def queries_to_test():
    """
    Returns the final portion of SQL CTEs which performs the unit test

    Args:
        None

    Returns:
        str: A SQL representation of the CTEs which performs the unit test
    """
    filepath = Path(__file__).parent / "final_test_ctes.txt"
    with open(filepath) as f:
        return f.read()
    

def build_test_to_submit(test, dataform_model_to_test):
    """
    Takes a JSON converted into a Python dictionary and turns into a SQL query
    which will be submitted to BigQuery

    Args:
        test (dict): The JSON object which is contained as Python dict object.
        dataform_model_to_test (str): The Dataform model being tested as a SQL string

    Returns:
        str: A SQL representation of the JSON unit test to submit to BigQuery
    """
    test_to_submit = create_input_ctes(test)
    test_to_submit += f"\n{create_expected_output_cte(test)}"
    test_to_submit += f"\n{replace_table_refs_with_test_inputs(test, dataform_model_to_test)},"
    test_to_submit += f"\n{queries_to_test()}"

    return test_to_submit
