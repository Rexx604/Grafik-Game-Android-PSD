import pandas as pd
import matplotlib.pyplot as plt

def muat_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        return None

def bersihkan_dan_proses_data(df):
    top_10 = df.sort_values(by='total ratings', ascending=False).head(10)
    return top_10

def buat_dan_simpan_grafik(top_10, out_populer, out_growth):
    top_10_reversed = top_10.iloc[::-1]
    
    # -------------------------------------------------------------
    # OUTPUT 1: GRAFIK POPULARITAS & RATING
    # -------------------------------------------------------------
    fig1, axes1 = plt.subplots(2, 1, figsize=(14, 12))
    
    bars1 = axes1[0].barh(top_10_reversed['title'], top_10_reversed['total ratings'], color='#440154')
    axes1[0].set_title('Top 10 Game Android Berdasarkan Total Ratings & Installs', fontsize=14, fontweight='bold')
    axes1[0].set_xlabel('Total Ratings (dalam Puluhan Juta)', fontsize=12)
    axes1[0].grid(axis='x', linestyle='--', alpha=0.7)
    
    for bar, row in zip(bars1, top_10_reversed.itertuples()):
        axes1[0].text(bar.get_width(), bar.get_y() + bar.get_height()/2, f"  [Installs: {row.installs}]", 
                    va='center', ha='left', fontsize=10, fontweight='bold', color='darkred')

    bars2 = axes1[1].barh(top_10_reversed['title'], top_10_reversed['average rating'], color='#3b528b')
    axes1[1].set_title('Rating Rata-Rata (Average Rating) dari Top 10 Game Terpopuler', fontsize=14, fontweight='bold')
    axes1[1].set_xlabel('Rating Rata-Rata (Skala 1-5)', fontsize=12)
    axes1[1].set_xlim(0, 5)
    axes1[1].grid(axis='x', linestyle='--', alpha=0.7)
    
    for bar, row in zip(bars2, top_10_reversed.itertuples()):
        axes1[1].text(0.1, bar.get_y() + bar.get_height()/2, f"Rating: {row._5:.1f}/5.0", 
                    va='center', ha='left', fontsize=10, color='white', fontweight='bold')

    plt.tight_layout()
    plt.savefig(out_populer, dpi=300)
    plt.show()
    plt.close()

    # -------------------------------------------------------------
    # OUTPUT 2: GRAFIK PERSENTASE PERTUMBUHAN (GROWTH)
    # -------------------------------------------------------------
    fig2, axes2 = plt.subplots(2, 1, figsize=(14, 12))
    
    bars3 = axes2[0].barh(top_10_reversed['title'], top_10_reversed['growth (30 days)'], color='#21918c')
    axes2[0].set_title('Persentase Pertumbuhan Game dalam 30 Hari Terakhir', fontsize=14, fontweight='bold')
    axes2[0].set_xlabel('Pertumbuhan (%)', fontsize=12)
    axes2[0].grid(axis='x', linestyle='--', alpha=0.7)
    
    for bar in bars3:
        axes2[0].text(bar.get_width(), bar.get_y() + bar.get_height()/2, f"  {bar.get_width():.1f}%", 
                    va='center', ha='left', fontsize=10, fontweight='bold')

    bars4 = axes2[1].barh(top_10_reversed['title'], top_10_reversed['growth (60 days)'], color='#5ec962')
    axes2[1].set_title('Persentase Pertumbuhan Game dalam 60 Hari Terakhir', fontsize=14, fontweight='bold')
    axes2[1].set_xlabel('Pertumbuhan (%)', fontsize=12)
    axes2[1].grid(axis='x', linestyle='--', alpha=0.7)
    
    for bar in bars4:
        axes2[1].text(bar.get_width(), bar.get_y() + bar.get_height()/2, f"  {bar.get_width():.1f}%", 
                    va='center', ha='left', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig(out_growth, dpi=300)
    plt.show()
    plt.close()

def simpan_hasil_analisis(df, top_10, output_txt_path):
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write("==================================================\n")
        f.write("      RINGKASAN STATISTIK DATA GAME ANDROID      \n")
        f.write("==================================================\n\n")
        f.write(f"Total Sampel Data Game : {len(df)} game\n")
        f.write(f"Rata-rata Total Ratings Keseluruhan : {df['total ratings'].mean():.2f}\n")
        f.write(f"Rating Tertinggi di Dataset        : {df['average rating'].max()}\n")
        f.write(f"Rating Terendah di Dataset         : {df['average rating'].min()}\n\n")
        f.write("--------------------------------------------------\n")
        f.write("      DAFTAR TOP 10 GAME ANDROID TERPOPULER       \n")
        f.write("--------------------------------------------------\n")
        for idx, row in enumerate(top_10.itertuples(), 1):
            f.write(f"{idx}. {row.title}\n")
            f.write(f"   - Total Ratings   : {row._3:,}\n")
            f.write(f"   - Jumlah Installs  : {row.installs}\n")
            f.write(f"   - Average Rating  : {row._5}/5\n")
            f.write(f"   - Growth 30 Days  : {row._6}%\n")
            f.write(f"   - Growth 60 Days  : {row._7}%\n")
            f.write(f"   - Kategori        : {row.category}\n\n")