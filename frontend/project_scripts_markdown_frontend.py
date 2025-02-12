import os

def collect_requested_scripts(directory, requested_files, output_file):
    with open(output_file, 'w') as f:
        for file_name in requested_files:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                f.write(f"## {file_name}\n\n")
                f.write("```\n")  
                with open(file_path, 'r') as py_file:
                    f.write(py_file.read())
                f.write("\n```\n\n")  
            else:
                f.write(f"## {file_name}\n\n")
                f.write("_File not found_\n\n") 
    print(f"Requested scripts have been collected into '{output_file}'.")


# Lista os scripts que voce quer coletar (ex: 'script1.py', 'script2.py')
requested_files = [
    'index.html',
    'src/components/AccommodationCard.jsx',
    'src/components/FavoriteButton.jsx',
    'src/components/Footer.jsx',
    'src/components/Hero.jsx',
    'src/components/Layout.jsx',
    'src/components/Navbar.jsx',
    'src/components/SearchBar.jsx',
    'src/components/Spinner.jsx',
    'src/pages/AccommodationDetails.jsx',
    'src/pages/Favorites.jsx',
    'src/pages/Home.jsx',
    'src/services/api.js',
    'src/App.css',
    'src/App.jsx', 
    'src/index.css', 
    'src/main.jsx',  
    '.env',
    'Dockerfile'
    ] 
collect_requested_scripts('/root/busca-acomodacoes/frontend/', requested_files, 'frontend_output_scripts.txt')
