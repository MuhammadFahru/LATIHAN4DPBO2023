#include <iostream>
using namespace std;

class Course {
public:
    string kode_matkul;
    string nama_matkul;

    Course(string kode_matkul, string nama_matkul) {
        this->kode_matkul = kode_matkul;
        this->nama_matkul = nama_matkul;
    }
};