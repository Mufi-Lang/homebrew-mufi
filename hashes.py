import requests
import hashlib

TAG = "next-experimental"
VERSION = "0.8.0"

links = [
    f"https://github.com/Mustafif/MufiZ/releases/download/{TAG}/mufiz_{VERSION}_x86_64-linux.zip",
    f"https://github.com/Mustafif/MufiZ/releases/download/{TAG}/mufiz_{VERSION}_aarch64-macos.zip",
    f"https://github.com/Mustafif/MufiZ/releases/download/{TAG}/mufiz_{VERSION}_x86_64-macos.zip"
]

for link in links:
    response = requests.get(link)
    hash = hashlib.sha256(response.content).hexdigest()
    print(f"{link.split('/')[-1]}: {hash}")
