//class Perpustakaan
//{
//    private List<string> bookTitles;
//    private Dictionary<string, string> borrowedBooks;

//    public Perpustakaan()
//    {
//        bookTitles = new List<string>
//        {
//            "Cara Jadi Orang Kaya",
//            "Cara Dapat Chindo",
//            "Cara Menikahi Anime",
//            "Cara Menjadi Waras Kembali"
//        };
//        borrowedBooks = new Dictionary<string, string>();
//    }

//    public void DisplayBooks()
//    {
//        Console.WriteLine("Daftar Buku di Perpustakaan:");
//        foreach (var title in bookTitles)
//        {
//            Console.WriteLine("- " + title);
//        }
//    }

//    public void AddBook(string title)
//    {
//        bookTitles.Add(title);
//        Console.WriteLine($"Buku \"{title}\" telah ditambahkan ke perpustakaan.");
//    }

//    public void RemoveBook(string title)
//    {
//        if (bookTitles.Remove(title))
//        {
//            Console.WriteLine($"Buku \"{title}\" telah dihapus dari perpustakaan.");
//        }
//        else
//        {
//            Console.WriteLine("Buku tidak ditemukan.");
//        }
//    }

//    public void UpdateBook(string oldTitle, string newTitle)
//    {
//        int index = bookTitles.IndexOf(oldTitle);
//        if (index != -1)
//        {
//            bookTitles[index] = newTitle;
//            Console.WriteLine($"Buku \"{oldTitle}\" telah diperbarui menjadi \"{newTitle}\".");
//        }
//        else
//        {
//            Console.WriteLine("Buku tidak ditemukan.");
//        }
//    }

//    public void BorrowBook(string studentName, string bookTitle)
//    {
//        if (bookTitles.Contains(bookTitle) && !borrowedBooks.ContainsKey(bookTitle))
//        {
//            borrowedBooks[bookTitle] = studentName;
//            Console.WriteLine($"{studentName} telah meminjam buku \"{bookTitle}\".");
//        }
//        else
//        {
//            Console.WriteLine("Buku tidak tersedia atau sudah dipinjam.");
//        }
//    }

//    public void DisplayBorrowedBooks()
//    {
//        Console.WriteLine("\nDaftar Buku yang Dipinjam:");
//        foreach (var entry in borrowedBooks)
//        {
//            Console.WriteLine($"- {entry.Key} (Dipinjam oleh: {entry.Value})");
//        }
//    }
//}

//class Program
//{
//    static void Main()
//    {
//        Perpustakaan library = new Perpustakaan();
//        library.DisplayBooks();

//        Console.WriteLine("\n=== Siswa Meminjam Buku ===");
//        library.BorrowBook("Stanley", "Cara Menikahi Anime");
//        library.BorrowBook("Bintang", "Cara Jadi Orang Kaya");
//        library.DisplayBorrowedBooks();

//        Console.WriteLine("\n=== Pihak Perpustakaan Menambahkan Buku ===");
//        library.AddBook("Machine Learning for Beginners");

//        Console.WriteLine("\n=== Pihak Perpustakaan Menghapus Buku ===");
//        library.RemoveBook("Cara Dapat Chindo");

//        Console.WriteLine("\n=== Pihak Perpustakaan Memperbarui Judul Buku ===");
//        library.UpdateBook("Cara Jadi Orang Kaya", "Rahasia Menjadi Kaya Raya");

//        Console.WriteLine("\n=== Daftar Buku Terbaru ===");
//        library.DisplayBooks();
//    }
//}


//class Biodata
//{
//    public string Nama { get; private set; }
//    public string Prodi { get; private set; }
//    private string nim;
//    private Dictionary<string, string> prodiNimPrefix = new Dictionary<string, string>
//    {
//        { "Informatika", "30" },
//        { "Sistem Informasi", "10" },
//        { "Teknologi Informasi", "20" }
//    };

//    public Biodata(string nama, string prodi)
//    {
//        Nama = nama;
//        Prodi = prodi;
//    }

//    public void SetNIM(string nim)
//    {
//        if (prodiNimPrefix.ContainsKey(Prodi) && nim.Length == 12 && nim.Substring(8, 2) == prodiNimPrefix[Prodi])
//        {
//            this.nim = nim;
//            Console.WriteLine($"NIM {nim} berhasil diatur untuk {Nama}.");
//        }
//        else
//        {
//            Console.WriteLine("NIM tidak sesuai dengan program studi.");
//        }
//    }

//    public void DisplayBiodata()
//    {
//        Console.WriteLine($"Nama: {Nama}\nProdi: {Prodi}\nNIM: {(nim ?? "Belum diatur")}");
//    }
//}

//class Program
//{
//    static void Main()
//    {
//        Biodata mahasiswa1 = new Biodata("Aditya Bayu Pratama", "Informatika");
//        mahasiswa1.SetNIM("242410103033"); // Sesuai
//        mahasiswa1.DisplayBiodata();

//        Biodata mahasiswa2 = new Biodata("Shinta", "Sistem Informasi");
//        mahasiswa2.SetNIM("242410101046"); // Sesuai
//        mahasiswa2.DisplayBiodata();

//        Biodata mahasiswa3 = new Biodata("Aditya Sakti Prananda", "Teknologi Informasi");
//        mahasiswa3.SetNIM("242410102086"); // Sesuai
//        mahasiswa3.DisplayBiodata();
//    }
//}
