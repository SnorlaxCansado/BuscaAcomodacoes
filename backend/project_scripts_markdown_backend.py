import os

def collect_requested_scripts(directory, requested_files, output_file):
    with open(output_file, 'w') as f:
        for file_name in requested_files:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                f.write(f"## {file_name}\n\n")
                f.write("```python\n")  
                with open(file_path, 'r') as py_file:
                    f.write(py_file.read())
                f.write("\n```\n\n")  
            else:
                f.write(f"## {file_name}\n\n")
                f.write("_File not found_\n\n") 
    print(f"Requested scripts have been collected into '{output_file}'.")


# Lista os scripts que voce quer coletar (ex: 'script1.py', 'script2.py')
requested_files = [
    'app/routes/__init__.py',
    'app/routes/accommodations.py',
    'app/__init__.py', 
    'app/config.py',
    'app/create_tables.py', 
    'app/crud.py', 
    'app/database.py', 
    'app/dependencies.py', 
    'app/main.py', 
    'app/models.py', 
    'app/populate_data.py',   
    'app/schemas.py'
    ] 
collect_requested_scripts('/root/busca-acomodacoes/backend/', requested_files, 'backend_output_scripts.txt')
