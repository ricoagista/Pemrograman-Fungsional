# Nama: Rico Shandika Jovial Agista
# NIM: 202410370110433

raw_grades = [
    ["Amel", 78, 80],
    ["Dika", 78, 82],
    ["Nisrina", 57, 65],
    ["Nayla", 60, 70],
    ["Fatih", 77, 72],
    ["Rani", 68, 55],
]

# 1. FUNCTION 1: Hitung Final Score & update data
#    Final Score = (Assignment * 0.4) + (Exam * 0.6)

def calculate_final_scores(data):
    hasil = []
    for student in data:
        nama = student[0]
        assignment = student[1]
        exam = student[2]
        final_score = (assignment * 0.4) + (exam * 0.6)
        hasil.append([nama, assignment, exam, final_score])
    return hasil

# 2. FUNCTION 2: Filter Lulus / Tidak Lulus
#    Syarat LULUS: Exam >= Assignment AND Final Score >= 70

def filter_pass_fail(processed_data):
    passed = []
    fail = []
    for student in processed_data:
        nama = student[0]
        assignment = student[1]
        exam = student[2]
        final_score = student[3]
        if exam >= assignment and final_score >= 70:
            passed.append(nama)
        else:
            fail.append(nama)
    return {"passed": passed, "fail": fail}

# Jalankan kedua function
all_updated = calculate_final_scores(raw_grades)
result_filter = filter_pass_fail(all_updated)

print("1. All Update Data")
print(all_updated)
print("\n2. Passed and Fail")
print(result_filter)

# 2. Konversi ke Tuple (NIM GANJIL -> gunakan 'passed')

NIM = "202410370110433"

if int(NIM) % 2 == 1:
    selected_names = result_filter["passed"]
    list_label = "Passed"
else:
    selected_names = result_filter["fail"]
    list_label = "Failed"

selected_tuple = tuple(selected_names)

print(f"\nConverted {list_label} Students Tuple:")
print(selected_tuple)
print("\nVerified Data Type:")
print(type(selected_tuple))


# 3. Recursive Function: hitung jumlah siswa TANPA loop / len()

def count_students_recursive(data, index=0):
    try:
        _ = data[index]
    except IndexError:
        return 0
    return 1 + count_students_recursive(data, index + 1)

# 4. verify_student dengan try-except-else

def verify_student(name, data, label):
    try:
        if name not in data:
            raise ValueError(f"Error: Student name '{name}' not found in the {label.lower()} list!")
    except ValueError as e:
        print(e)
    else:
        print(f"Student Found '{name}'")

# Output jumlah siswa secara rekursif
print(f"\nTotal Number of {list_label} Students (Calculated Recursively):")
print(count_students_recursive(selected_tuple))
print("-" * 60)

# Skenario A: cek nama yang ada di tuple
print("Scenario A")
if selected_tuple:
    verify_student(selected_tuple[0], selected_tuple, list_label)
else:
    print("Tuple kosong")

print("-" * 60)

# Skenario B: cek nama yang TIDAK ada di tuple
print("Scenario B")
if list_label == "Passed":
    verify_student("Nisrina", selected_tuple, list_label)
else:
    verify_student("Amel", selected_tuple, list_label)

# and assignment >= 60:

# Tampilkan hanya 2 nama pertama yang lulus
# print("2 nama pertama:", selected_tuple[:2])

# Tampilkan semua KECUALI nama pertama
# print("Tanpa yang pertama:", selected_tuple[1:])

# Tampilkan urutan terbalik
# print("Terbalik:", selected_tuple[::-1])

# Tampilkan 2 nama terakhir
# print("2 terakhir:", selected_tuple[-2:])
