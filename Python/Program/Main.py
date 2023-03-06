from Mahasiswa import Mahasiswa
from Dosen import Dosen
from ProgramStudi import ProgramStudi
from Course import Course

# Compsition : bersifat independen dan hanya digunakan oleh objek tersebut
# Aggregation : memiliki ketergantungan pada objek lain untuk dapat berfungsi

# +------------------------------------------------------+
# |        Contoh Composition dan Array of Object        |
# +------------------------------------------------------+
prodi1 = ProgramStudi("TI", "Teknik Informatika")
prodi2 = ProgramStudi("SI", "Sistem Informasi")

course1 = Course("MK01", "Algoritma dan Pemrograman")
course2 = Course("MK02", "Basis Data")
course3 = Course("MK03", "Jaringan Komputer")

prodi1.add_course(course1)
prodi1.add_course(course2)

prodi2.add_course(course1)
prodi2.add_course(course3)

print("+------------------------------------------+")
print("|           Data Program Studi 1           |")
print("+------------------------------------------+")
prodi1.display_data()
print("+------------------------------------------+")

print("+------------------------------------------+")
print("|           Data Program Studi 2          |")
print("+------------------------------------------+")
prodi2.display_data()
print("+------------------------------------------+")
# +------------------------------------------------------+

# +------------------------------------------------------+
# |          Contoh Inheritance dan Aggregation          |
# +------------------------------------------------------+

mhs1 = Mahasiswa("3273201234567890", "Muhammad Fahru Rozi", "Laki-laki", "UPI", "muhammadfahru@upi.edu", "2108927", prodi1, "FPMIPA")
print("+------------------------------------------+")
print("|            Data Mahasiswa 1              |")
print("+------------------------------------------+")
mhs1.display_data()
print("+------------------------------------------+")

mhs2 = Mahasiswa("3273201234567891", "Chelsea Islan", "Perempuan", "ITB", "chelseaislan@itb.ac.id", "2108901", prodi2, "FMIPA")
print("+------------------------------------------+")
print("|            Data Mahasiswa 2              |")
print("+------------------------------------------+")
mhs2.display_data()
print("+------------------------------------------+")

# +------------------------------------------------------+