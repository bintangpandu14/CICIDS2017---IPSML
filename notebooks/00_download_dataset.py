# notebooks/00_download_dataset.ipynb

import os
import gdown

# Pastikan folder tujuan ada
os.makedirs("../data/raw", exist_ok=True)

# Daftar file dari Google Drive (ganti ID sesuai file kamu)
files = {
    "Monday-WorkingHours.pcap_ISCX.csv": "1DJeVZFJJdEL3U-hLzOowlLR9pfTUg9z9",
    "Tuesday-WorkingHours.pcap_ISCX.csv": "1-de0MDylKteM4M1Y5oH3djuvlBv1DoL9",
    "Wednesday-WorkingHours.pcap_ISCX.csv": "1sM5TSX-oAjbbA57_Y1zuWiIKoOYZTxw-",
    "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv": "1qoMFQiz36iFMBo_aZ_74GX0pZUvbWfAJ",
    "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv": "1CN-VKqTyxjkGjIw0a8HmiE5F1sqFcwOH",
    "Friday-WorkingHours-Morning.pcap_ISCX.csv": "1d0D2Z3ykkCWLvqlN4hVEdsqCMVVhwSpF",
    "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv": "1fSgMOFVy9zdOfJhC_Abv6LCdbrUYI9R6",
    "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv": "1-0w9Vw60QEFlUjVIYecG8JYxnF7WB2Ga",
    "wednesday.pcap":"1d2XWgkvD2RaKIDmMGLDbqi3Yfz_9N9qX",
    # tambahkan file lain di sini
}

# Download satu per satu
for filename, file_id in files.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    output = f"../data/raw/{filename}"
    if not os.path.exists(output):
        print(f"⬇️ Downloading {filename} ...")
        gdown.download(url, output, quiet=False)
    else:
        print(f"✅ {filename} sudah ada, skip.")
