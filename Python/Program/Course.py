class Course:

    def __init__(self, kode_mata_kuliah="", nama_mata_kuliah=""):
        self.kode_mata_kuliah = kode_mata_kuliah
        self.nama_mata_kuliah = nama_mata_kuliah

    def set_kode_mata_kuliah(self, kode_mata_kuliah):
        self.kode_mata_kuliah = kode_mata_kuliah

    def get_kode_mata_kuliah(self):
        return self.kode_mata_kuliah

    def set_nama_mata_kuliah(self, nama_mata_kuliah):
        self.nama_mata_kuliah = nama_mata_kuliah

    def get_nama_mata_kuliah(self):
        return self.nama_mata_kuliah

    def display_data(self):
        print("| Kode Mata Kuliah    : ", self.kode_mata_kuliah)
        print("| Nama Mata Kuliah    : ", self.nama_mata_kuliah)
