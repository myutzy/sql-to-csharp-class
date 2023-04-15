import re

class_name = "MyClass"

def decapitalize_first_letter(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])]) 

def parse_sql_create_command(sql_create_command):
    column_regex = r'\[(.*?)\] \[(.*?)\](?:\((\d+)\))? (NULL|NOT NULL)'
    matches = re.findall(column_regex, sql_create_command)
    
    columns = []
    for match in matches:
        column_name, sql_type, max_length, is_nullable = match
        is_nullable = is_nullable == 'NULL'
        max_length = int(max_length) if max_length else None
        columns.append((column_name, sql_type, is_nullable, max_length))
        
    return columns

def sql_type_to_csharp_type(sql_type, is_nullable):
    # TODO: Implement additional SQL data types
    if sql_type in ["int", "smallint"]:
        return "int" + ("?" if is_nullable else "")
    elif sql_type in ["nvarchar", "varchar"]:
        return "string"
    elif sql_type == "float":
        return "double" + ("?" if is_nullable else "")
    elif sql_type == "bit":
        return "bool" + ("?" if is_nullable else "")
    else:
        raise ValueError(f"Unsupported SQL type: {sql_type}")

def create_csharp_class(class_name, columns):
    # Optionally apply any property template customizations here.
    property_template = '''private {csharp_type} _{private_column_name};

    {attributes}public {csharp_type} {column_name}
    {{
        get => _{private_column_name};
        set => _{private_column_name} = value;
    }}
    '''

    properties = []

    for column_name, sql_type, is_nullable, max_length in columns:
        csharp_type = sql_type_to_csharp_type(sql_type, is_nullable)
        private_column_name = decapitalize_first_letter(column_name)
        attributes = str()
        if max_length:
            attributes += f"[MaxLength({max_length})]\n    "
        property_line = property_template.format(csharp_type=csharp_type, column_name=column_name, private_column_name=private_column_name, attributes=attributes)
        properties.append(property_line)

    class_template = "public class {class_name}\n{{\n{properties}\n}}"

    properties_str = "\n".join("    " + prop for prop in properties)

    return class_template.format(class_name=class_name, properties=properties_str)

"""
Expected input format is the column portion of the SQL create script only, not the entire script.
Example Input.txt contents:

[CustomerId] [int] NOT NULL,
[FirstName] [nvarchar](50) NULL,
[LastName] [nvarchar] NULL,
[CompanyName] [nvarchar] NULL,
[PhoneNumber] [nvarchar] NULL,
[EmailAddress] [nvarchar] NULL
"""

with open('Input.txt', 'r') as file:
    column_definitions = file.read()

columns = parse_sql_create_command(column_definitions)
csharp_class = create_csharp_class(class_name, sorted(columns))

with open('Output.cs', 'w') as f:
    f.write(csharp_class)

print('Result saved to file.')