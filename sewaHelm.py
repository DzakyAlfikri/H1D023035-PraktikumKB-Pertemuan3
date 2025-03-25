import datetime
from tabulate import tabulate

# Struktur data: Dictionary untuk menyimpan data helm
helm_stock = {
    "H001": {"nama": "Helm Full Face", "harga": 20000, "status": "Tersedia"},
    "H002": {"nama": "Helm Open Face", "harga": 15000, "status": "Tersedia"},
    "H003": {"nama": "Helm Modular", "harga": 25000, "status": "Tersedia"}
}

# Struktur data: List untuk menyewa transaksi
transaksi = []

def tampilkan_helm():
    headers = ["Kode", "Nama Helm", "Harga Sewa/hari", "Status"]
    data = []
    for kode, info in helm_stock.items():
        data.append([kode, info["nama"], f"Rp {info['harga']}", info["status"]])
    print(tabulate(data, headers=headers, tablefmt="grid"))

def sewa_helm():
    tampilkan_helm()
    kode_helm = input("Masukkan kode helm yang ingin disewa: ").upper()
    
    # Struktur kontrol: Pengecekan ketersediaan helm
    if kode_helm in helm_stock and helm_stock[kode_helm]["status"] == "Tersedia":
        nama_pelanggan = input("Masukkan nama pelanggan: ")
        lama_sewa = int(input("Masukkan lama sewa (hari): "))
        total_biaya = helm_stock[kode_helm]["harga"] * lama_sewa
        
        # Struktur data: Menyimpan transaksi
        transaksi.append({
            "kode_helm": kode_helm,
            "nama_pelanggan": nama_pelanggan,
            "tanggal_sewa": datetime.datetime.now().strftime("%d-%m-%Y"),
            "lama_sewa": lama_sewa,
            "total_biaya": total_biaya
        })
        
        # Update status helm
        helm_stock[kode_helm]["status"] = "Disewa"
        print(f"\nBerhasil menyewa {helm_stock[kode_helm]['nama']} selama {lama_sewa} hari.")
        print(f"Total biaya: Rp {total_biaya}")
    else:
        print("Helm tidak tersedia atau kode tidak valid.")

def kembalikan_helm():
    kode_helm = input("Masukkan kode helm yang dikembalikan: ").upper()
    
    # Struktur kontrol: Pengecekan apakah helm sedang disewa
    if kode_helm in helm_stock and helm_stock[kode_helm]["status"] == "Disewa":
        helm_stock[kode_helm]["status"] = "Tersedia"
        print(f"{helm_stock[kode_helm]['nama']} berhasil dikembalikan.")
    else:
        print("Helm tidak sedang disewa atau kode tidak valid.")

def riwayat_transaksi():
    if not transaksi:
        print("Belum ada transaksi.")
        return
    
    headers = ["No", "Kode Helm", "Nama Pelanggan", "Tanggal Sewa", "Lama Sewa", "Total Biaya"]
    data = []
    for idx, trx in enumerate(transaksi, 1):
        data.append([
            idx,
            trx["kode_helm"],
            trx["nama_pelanggan"],
            trx["tanggal_sewa"],
            f"{trx['lama_sewa']} hari",
            f"Rp {trx['total_biaya']}"
        ])
    print(tabulate(data, headers=headers, tablefmt="grid"))

def main():
    print("=== Sistem Penyewaan Helm ===")
    while True:
        print("\nMenu:")
        print("1. Tampilkan Daftar Helm")
        print("2. Sewa Helm")
        print("3. Kembalikan Helm")
        print("4. Riwayat Transaksi")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        # Struktur kontrol: Pilih Menu
        if pilihan == "1":
            tampilkan_helm()
        elif pilihan == "2":
            sewa_helm()
        elif pilihan == "3":
            kembalikan_helm()
        elif pilihan == "4":
            riwayat_transaksi()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
