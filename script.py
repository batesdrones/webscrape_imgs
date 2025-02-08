import os
import requests

def download_images(emojis, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Referer": "https://imgur.com/"
    }
    
    for emoji in emojis:
        name = emoji["name"]
        url = emoji["src"]
        file_path = os.path.join(output_folder, f"{name}.png")
        
        print(f"Downloading {name} from {url}...")
        
        response = requests.get(url, stream=True, headers=headers)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Saved {name}.png to {output_folder}")
        else:
            print(f"Failed to download {name} from {url}")

if __name__ == "__main__":
    emojis = [
        {"name": "1train", "src": "https://i.imgur.com/5w147gb.png"},
        {"name": "2train", "src": "https://i.imgur.com/WbQXY6L.png"},
        {"name": "3train", "src": "https://i.imgur.com/vgF9PMQ.png"},
        {"name": "9train", "src": "https://i.imgur.com/bWepskg.png"},
        {"name": "ntrain", "src": "https://i.imgur.com/Y5vukLP.png"},
        {"name": "rtrain", "src": "https://i.imgur.com/zUGeskm.png"},
        {"name": "qtrain", "src": "https://i.imgur.com/7BRayd1.png"},
        {"name": "wtrain", "src": "https://i.imgur.com/kUnS3Ko.png"},
        {"name": "atrain", "src": "https://i.imgur.com/Uh6c4sD.png"},
        {"name": "ctrain", "src": "https://i.imgur.com/SMIYfnv.png"},
        {"name": "etrain", "src": "https://i.imgur.com/OM1OEUM.png"},
        {"name": "ltrain", "src": "https://i.imgur.com/S6NeJtj.png"},
        {"name": "4train", "src": "https://i.imgur.com/fadogYd.png"},
        {"name": "5train", "src": "https://i.imgur.com/K05HApQ.png"},
        {"name": "6train", "src": "https://i.imgur.com/bRrwqkM.png"},
        {"name": "7train", "src": "https://i.imgur.com/S9CVRlJ.png"},
        {"name": "btrain", "src": "https://i.imgur.com/LA41bPi.png"},
        {"name": "dtrain", "src": "https://i.imgur.com/b5sLbv0.png"},
        {"name": "ftrain", "src": "https://i.imgur.com/lvSg9sv.png"},
        {"name": "mtrain", "src": "https://i.imgur.com/0FZ6kum.png"},
        {"name": "jtrain", "src": "https://i.imgur.com/3U4eNxl.png"},
        {"name": "ztrain", "src": "https://i.imgur.com/momyYjI.png"},
        {"name": "strain", "src": "https://i.imgur.com/1BJvHdC.png"},
        {"name": "gtrain", "src": "https://i.imgur.com/ur7mAno.png"},
        {"name": "ttrain", "src": "https://i.imgur.com/yuAyaqC.png"},
    ]
    
    output_folder = input("Enter the output destination folder (default: ./nycsubway_emojis): ") or "nycsubway_emojis"
    download_images(emojis, output_folder)
