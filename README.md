# CICIDS2017---IPSML

Intrusion Detection System (IDS) menggunakan **LightGBM** berbasis dataset **CICIDS2017** untuk integrasi dengan **Snort ML**.

## 📁 Struktur Folder

CICIDS2017---IPSML/
│
├── data/
│ ├── raw/ ← Dataset mentah (.csv per hari)
│ └── processed/ ← Dataset hasil preprocessing
│
├── notebooks/ ← Jupyter notebooks untuk analisis & model
│
├── models/ ← Model LightGBM tersimpan (.pkl)
│
├── utils/ ← Fungsi bantu preprocessing
│
└── README.md

## ⚙️ Langkah Penggunaan
1. Clone repo
2. Letakkan dataset di `data/raw/`
3. Jalankan notebook `01_data_preprocessing.ipynb`
4. Lanjutkan ke `03_lightgbm_training.ipynb` untuk training model

## 🧠 Model
Menggunakan **LightGBM** dengan teknik:
- Imbalance handling (`class_weight`)
- Feature selection berdasarkan importance
- Evaluasi menggunakan F1-score dan confusion matrix
