import sys
import requests
import time

file_path = "/tmp/web_"

start_time = time.time()


def get_content(url):
    print(f"Téléchargement {url}")
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

            urlFile = file_path+url_formatted
            write_content(html_content, urlFile)

end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")