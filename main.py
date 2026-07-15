import os
from utils import muat_data, bersihkan_dan_proses_data, buat_dan_simpan_grafik, simpan_hasil_analisis

def main():
    csv_path = os.path.join("dataset", "android-games.csv")
    grafik_populer = "grafik_popularitas.png"
    grafik_growth = "grafik_pertumbuhan.png"
    teks_out = "hasil_analisis.txt"
    
    dataset = muat_data(csv_path)
    if dataset is None:
        return
        
    top_10_games = bersihkan_dan_proses_data(dataset)
    
    # Memproses visualisasi menjadi 2 output jendela layar terpisah
    buat_dan_simpan_grafik(top_10_games, grafik_populer, grafik_growth)
    
    simpan_hasil_analisis(dataset, top_10_games, teks_out)

if __name__ == "__main__":
    main()