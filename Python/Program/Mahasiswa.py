from SivitasAkademik import SivitasAkademik


class Mahasiswa(SivitasAkademik):

    __nim = ""
    __prodi = ""
    __fakultas = ""

    def __init__(self, nik="", nama="", gender="", asal_universitas="", email_edu="", nim="", prodi = "", fakultas=""):
        super().__init__(nik, nama, gender, asal_universitas, email_edu)
        self.__nim = nim
        self.__fakultas = fakultas
        self.__prodi = prodi

    def set_nim(self, nim):
        self.__nim = nim

    def get_nim(self):
        return self.__nim

    def set_fakultas(self, fakultas):
        self.__fakultas = fakultas

    def get_fakultas(self):
        return self.__fakultas

    def display_data(self):
        super().display_data()
        print("| NIM                 : ", self.__nim)
        print("| Fakultas            : ", self.__fakultas)
        print("| [Agr] Program Studi : ", self.__prodi.kode_prodi, " - ", self.__prodi.nama_prodi)
