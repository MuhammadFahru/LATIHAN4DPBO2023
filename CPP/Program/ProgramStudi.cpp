using namespace std;
#include <bits/stdc++.h>
#include <vector>
#include "Course.cpp"

class ProgramStudi
{
public:
    string nama_prodi;
    string kode_prodi;
    vector<Course> courses;
    
    // Constructor
    ProgramStudi()
    {
        this->nama_prodi = "";
        this->kode_prodi = "";
    }

    ProgramStudi(string nama_prodi, string kode_prodi)
    {
        this->nama_prodi = nama_prodi;
        this->kode_prodi = kode_prodi;
    }

    // Setter & Getter

    void setNamaProdi(string nama_prodi)
    {
        this->nama_prodi = nama_prodi;
    }

    string getNamaProdi()
    {
        return nama_prodi;
    }

    void setKodeProdi(string kode_prodi)
    {
        this->kode_prodi = kode_prodi;
    }

    string getKodeProdi()
    {
        return kode_prodi;
    }

    void add_course(Course course) {
        courses.push_back(course);
    }

    // Destructor
    ~ProgramStudi() {}
};