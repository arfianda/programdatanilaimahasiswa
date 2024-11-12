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
    print("\n" + "="*72)
    print("| {0:^4} | {1:^15} | {2:^7} | {3:^7} | {4:^5} | {5:^5} | {6:^7} |".format(
        "No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
    print("="*72)
    
    for idx, student in enumerate(students, 1):
        print("| {0:^4} | {1:<15} | {2:^7} | {3:^7} | {4:^5} | {5:^5} | {6:^7.2f} |".format(
            idx, 
            student.nama,
            student.nim,
            student.tugas,
            student.uts,
            student.uas,
            student.nilai_akhir
        ))
    
    print("="*72)

if __name__ == "__main__":
    main()