import sys
import requests

file_path = "/tmp/web_page"

def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Erreur lors de la récupération de l'URL : {response.status_code}")

def write_content(content, file):
    f = open(file, "w", encoding="utf-8")
    f.write(content)
    f.close()

if len(sys.argv) != 2:
    print("Usage: python web_sync.py <URL>")
else:
    url_request = sys.argv[1]
    html_content = get_content(url_request)
    write_content(html_content, file_path)

print(f"Le contenu de la page a été téléchargé dans {file_path}.")