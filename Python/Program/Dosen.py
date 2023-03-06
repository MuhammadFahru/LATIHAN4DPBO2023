from SivitasAkademik import SivitasAkademik


class Dosen(SivitasAkademik):

    __nip = ""
    __prodi = ""
    __fakultas = ""
    __pendidikan_terakhir = ""
    __keahlian = ""

    def __init__(self, nik="", nama="", gender="", asal_universitas="", email_edu="", nim="", prodi = "", fakultas="", pendidikan_terakhir="", keahlian=""):
        super().__init__(nik, nama, gender, asal_universitas, email_edu)
        self.__nip = nim
        self.__prodi = prodi
        self.__fakultas = fakultas
        self.__pendidikan_terakhir = pendidikan_terakhir
        self.__keahlian = keahlian

    def set_nim(self, nim):
        self.__nip = nim

    def get_nim(self):
        return self.__nip

    def set_fakultas(self, fakultas):
        self.__fakultas = fakultas

    def get_fakultas(self):
        return self.__fakultas
    
    def set_pendidikan_terakhir(self, pendidikan_terakhir):
        self.__pendidikan_terakhir = pendidikan_terakhir

    def get_pendidikan_terakhir(self):
        return self.__pendidikan_terakhir
    
    def set_keahlian(self, keahlian):
        self.__keahlian = keahlian

    def get_keahlian(self):
        return self.__keahlian

    def display_data(self):
        super().display_data()
        print("| NIP                 : ", self.__nip)
        print("| Fakultas            : ", self.__fakultas)
        print("| Pendidikan Terakhir : ", self.__pendidikan_terakhir)
        print("| Keahlian            : ", self.__keahlian)
        print("| [Agr] Program Studi : ", self.__prodi.kode_prodi, " - ", self.__prodi.nama_prodi)
