import sys
import requests

dl_path = "/tmp/web_"


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
    urls_file = sys.argv[1]
    with open(urls_file, "r", encoding="utf-8") as file:
        urls = file.readlines()
        for url in urls:
            url = url.split("\n")[0]
            url_formatted = url.split("://")[1]
            html_content = get_content(url)

            urlFile = dl_path+url_formatted
            write_content(html_content, urlFile)
            print(f"Le contenu de la page a été téléchargé dans {urlFile}.")