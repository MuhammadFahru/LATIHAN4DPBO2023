class ProgramStudi:
    
    def __init__(self, kode_prodi = "", nama_prodi = "", list_course = []):
        self.nama_prodi = nama_prodi
        self.kode_prodi = kode_prodi
        self.list_course = []
    
    def set_kode_prodi(self, kode_prodi):
        self.kode_prodi = kode_prodi

    def get_kode_prodi(self):
        return self.kode_prodi
    
    def set_nama_prodi(self, nama_prodi):
        self.nama_prodi = nama_prodi

    def get_nama_prodi(self):
        return self.nama_prodi

    def add_course(self, course):
        self.list_course.append(course)

    def show_course(self):
        print("| [Com] List Mata Kuliah")
        for course in self.list_course:
            print("| - ", course.nama_mata_kuliah)
    
    def display_data(self):
        print("| Kode Program Studi  : ", self.kode_prodi)
        print("| Nama Program Studi  : ", self.nama_prodi)
        self.show_course()
        print("+------------------------------------------+")