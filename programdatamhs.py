# Program Data Mahasiswa
class Student:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = self.hitung_nilai_akhir()
    
    def hitung_nilai_akhir(self):
        return (self.tugas * 0.30) + (self.uts * 0.35) + (self.uas * 0.35)

def main():
    students = []
    
    while True:
        print("\nMasukkan data mahasiswa:")
        nama = input("Nama : ")
        nim = input("NIM : ")
        nilai_tugas = float(input("Nilai Tugas : "))
        nilai_uts = float(input("Nilai UTS : "))
        nilai_uas = float(input("Nilai UAS : "))
        
        student = Student(nama, nim, nilai_tugas, nilai_uts, nilai_uas)
        students.append(student)
        
        tambah = input("Tambah data(y/t)? ")
        if tambah.lower() == 't':
            break
    
    # Menampilkan hasil
    print("\n" + "="*70)
    print("| No |    Nama    |   NIM   | Tugas | UTS | UAS | Akhir |")
    print("="*70)
    
    for idx, student in enumerate(students, 1):
        print(f"| {idx:2} | {student.nama:<10} | {student.nim:^7} | {student.tugas:^5} | {student.uts:^3} | {student.uas:^3} | {student.nilai_akhir:^5.2f} |")
    
    print("="*70)

if __name__ == "__main__":
    main()