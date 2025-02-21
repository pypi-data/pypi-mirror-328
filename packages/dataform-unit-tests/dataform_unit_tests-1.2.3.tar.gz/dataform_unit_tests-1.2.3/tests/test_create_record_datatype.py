import unittest

from src.dataform_unit_testing.sql_unit_test_builder import create_record_datatype

class TestCreateRecordDatatype(unittest.TestCase):
    def test_single_row_record(self):
        """Test for 'Single Row Record'"""
        record = [
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<injured_individual STRING,injured_age STRING>>[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('24' AS STRING))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_multiple_rows_record(self):
        """Test for 'Multiple Rows Record'"""
        record = [
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"]
                    },
                    {
                        "injured_individual": ["Customer", "STRING"],
                        "injured_age": ["25", "STRING"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<injured_individual STRING,injured_age STRING>>[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('24' AS STRING)), (SAFE_CAST('Customer' AS STRING),SAFE_CAST('25' AS STRING))]"
        self.assertEqual(create_record_datatype(record), expected_output)

    
    def test_single_row_nested_record(self):
        """Test for 'Single Row Nested Record'"""
        record = [
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injuries": [[
                            {
                                "injury_1": ["Broken arm", "STRING"],
                                "injury_2": ["Bruised leg", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<injured_individual STRING,injured_age STRING,injuries ARRAY<STRUCT<injury_1 STRING,injury_2 STRING>>>>[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('Bruised leg' AS STRING))])]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_multiple_rows_nested_record(self):
        """Test for 'Multiple Rows Nested Record'"""
        record = [
                    {
                        "injured_individual": ["Nandoca", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injuries": [[
                            {
                                "injury_1": ["Broken arm", "STRING"],
                                "injury_2": ["Bruised leg", "STRING"]
                            }
                        ], "RECORD"]
                    },
                    {
                        "injured_individual": ["Customer", "STRING"],
                        "injured_age": ["24", "STRING"],
                        "injuries": [[
                            {
                                "injury_1": ["Broken leg", "STRING"],
                                "injury_2": ["Bruised arm", "STRING"]
                            }
                        ], "RECORD"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<injured_individual STRING,injured_age STRING,injuries ARRAY<STRUCT<injury_1 STRING,injury_2 STRING>>>>[(SAFE_CAST('Nandoca' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Broken arm' AS STRING),SAFE_CAST('Bruised leg' AS STRING))]), (SAFE_CAST('Customer' AS STRING),SAFE_CAST('24' AS STRING),[(SAFE_CAST('Broken leg' AS STRING),SAFE_CAST('Bruised arm' AS STRING))])]"
        self.assertEqual(create_record_datatype(record), expected_output)

    
    def test_escape_single_quote(self):
        """Test for 'Escape Single Quote'"""
        record = [
                    {
                        "injured_individual": ["Nandoca's", "STRING"],
                        "injured_age": ["24", "STRING"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<injured_individual STRING,injured_age STRING>>[(SAFE_CAST('Nandoca\\'s' AS STRING),SAFE_CAST('24' AS STRING))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_bytes(self):
        """Test for 'Bytes'"""
        record = [
                    {
                        "injured_individual": ["Nandoca's", "STRING"],
                        "injury_type_id": ["q4ah4e9w3/l5WQZ7cjxcJA==", "BYTES"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<injured_individual STRING,injury_type_id BYTES>>[(SAFE_CAST('Nandoca\\'s' AS STRING),FROM_BASE64('q4ah4e9w3/l5WQZ7cjxcJA=='))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_nested_json(self):
        """Test for 'Nested JSON'"""
        record = [
                    {
                        "injured_individual": ["Nandoca's", "STRING"],
                        "equipment_involved": ["{'key1': 'value1', 'key2': {'key3': 'value3'}}", "JSON"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<injured_individual STRING,equipment_involved JSON>>[(SAFE_CAST('Nandoca\\'s' AS STRING),JSON_OBJECT('key1', 'value1', 'key2', JSON_OBJECT('key3', 'value3')))]"
        self.assertEqual(create_record_datatype(record), expected_output)
    

    def test_geography(self):
        """Test for 'Geography'"""
        record = [
                    {
                        "injured_individual": ["Nandoca's", "STRING"],
                        "injury_location": ["POINT(-0.349498 51.48198)", "GEOGRAPHY"]
                    }
                ]
        expected_output = "ARRAY<STRUCT<injured_individual STRING,injury_location GEOGRAPHY>>[(SAFE_CAST('Nandoca\\'s' AS STRING),ST_GEOGFROMTEXT('POINT(-0.349498 51.48198)'))]"
        self.assertEqual(create_record_datatype(record), expected_output)


if __name__ == "__main__":
    unittest.main()
