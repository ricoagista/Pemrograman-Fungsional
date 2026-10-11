# Nama: Rico Shandika Jovial Agista
# NIM: 202410370110433
# Tema: Analitik Perbandingan Kualitas Wi-Fi 2.4 GHz vs 5 GHz pada Mobile Legends

import sys

# Menu (Tuple)
menu = ("Register", "Login", "Catat", "Riwayat", "Kalibrasi", "Hapus", "Logout", "Keluar")

# Auth (Dict) + Profil (Nested Dict) - 3 mock
akun   = {"Rico": "123", "Shandika": "456", "Jovial": "789"}
user_ids = {"Rico": 1, "Shandika": 2, "Jovial": 3}
profil = {
    "Rico":     {"nama": "Rico",     "phone": "0812", "role": "Analyst"},
    "Shandika": {"nama": "Shandika", "phone": "0821", "role": "Player"},
    "Jovial":   {"nama": "Jovial",   "phone": "0857", "role": "Coach"},
}

# Main Data (List of Dict) - 3 mock
# Alasan: tiap log punya atribut heterogen (str, int, bool) & jumlah dinamis,
#         sehingga List of Dict paling fleksibel dan mudah difilter per id (session lock).
log = [
    {"id": 1, "no": 1, "band": "2.4GHz", "ping": 45, "loss": 1, "stable": True},
    {"id": 2, "no": 1, "band": "5GHz",   "ping": 18, "loss": 0, "stable": True},
    {"id": 3, "no": 1, "band": "2.4GHz", "ping": 82, "loss": 5, "stable": False},
]

# Input validation (while + try-except)
def minta(p, t=str):
    while True:
        try:
            v = input(p).strip()
            if t is str and not v: raise ValueError
            return t(v)
        except ValueError:
            print("  [!] Input tidak valid.")

# Menu dengan Slicing (guest vs login)
def tampil(u=None):
    o = menu[0:2] + (menu[7],) if u is None else menu[2:7] + (menu[7],)
    for i, x in enumerate(o, 1): print(f"  {i}. {x}")
    return o

# Register
def register():
    u = minta("  Username : ")
    if u in akun: print("  [!] Sudah terdaftar."); return
    akun[u] = minta("  Password : ")
    user_ids[u] = max(user_ids.values()) + 1
    profil[u] = {"nama": minta("  Nama : "), "phone": minta("  HP : "), "role": minta("  Role : ")}
    print("  [OK] Terdaftar.")

# Login
def login():
    u = minta("  Username : ")
    if u in akun and akun[u] == minta("  Password : "):
        print(f"  [OK] Halo {profil[u]['nama']}"); return user_ids[u]
    print("  [!] Gagal login.")

# CRUD kontekstual - semua dibatasi session lock (id == uid)
def catat(uid):
    b = minta("  Band (2.4GHz/5GHz): ")
    if b not in ("2.4GHz","5GHz"): print("  [!] Band salah."); return
    p, l = minta("  Ping : ", int), minta("  Loss : ", int)
    no = 1 + sum(1 for x in log if x["id"] == uid)
    log.append({"id": uid, "no": no, "band": b, "ping": p, "loss": l, "stable": p < 50 and l < 2})
    print(f"  [OK] Log #{no} disimpan.")

def riwayat(uid):
    d = [x for x in log if x["id"] == uid]
    if not d: print("  (kosong)"); return
    for x in d: print(f"  #{x['no']} {x['band']} ping={x['ping']} loss={x['loss']} stable={x['stable']}")

def kalibrasi(uid):
    no = minta("  Nomor log : ", int)
    for x in log:
        if x["id"] == uid and x["no"] == no:
            x["ping"] = minta("  Ping baru : ", int)
            x["stable"] = x["ping"] < 50 and x["loss"] < 2
            print("  [OK] Kalibrasi berhasil."); return
    print("  [!] Tidak ditemukan.")

def hapus(uid):
    no = minta("  Nomor log : ", int)
    for i, x in enumerate(log):
        if x["id"] == uid and x["no"] == no:
            log.pop(i); print("  [OK] Dihapus."); return
    print("  [!] Tidak ditemukan.")

# Main
u = None
while True:
    o = tampil(u)
    p = minta("  Pilih : ", int)
    if not 1 <= p <= len(o): continue
    a = o[p - 1]
    if   a == "Register": register()
    elif a == "Login":    u = login() or u
    elif a == "Catat":    catat(u)
    elif a == "Riwayat":  riwayat(u)
    elif a == "Kalibrasi":kalibrasi(u)
    elif a == "Hapus":    hapus(u)
    elif a == "Logout":   print("  [OK] Logout."); u = None
    elif a == "Keluar":   sys.exit()