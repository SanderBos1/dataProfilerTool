from marshmallow import Schema, fields

class CSVUploadSchema(Schema):
    """
    Schema for validating and deserializing input data related to CSV file processing.

    This schema defines the expected structure and data types for the input fields:
    - `csvSeperator`: Character used to separate values in the CSV file.
    - `headerRow`: The row index where the header is located in the CSV file.
    - `quoteChar`: Character used for quoting fields in the CSV file.

    Each field has a default value which will be used if the field is not provided in the input.
    """

    csvSeperator = fields.Str(load_default=',')
    headerRow = fields.Int(load_default=0)
    quoteChar = fields.Str(load_default='"')
