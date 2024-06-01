class Book:
    cover_types = ['Hard Cover', 'Soft Cover']

    def __str__(self):
        return f"The Book Name is {self.book_name}. The Book Cover is: {self.book_cover}. The book weight is: {self.book_weight}g"

    def __init__(self, book_name, book_cover, book_weight):
        self.book_name = book_name
        self.book_cover = book_cover
        self.book_weight = book_weight


    @staticmethod
    def print_book_name(name):
        print(f"The Book name is: {name}")

    @classmethod
    def print_book_name_v2(cls, name):
        print(f"The Book name is: {name}. The class is {cls}")

    @classmethod
    def create_hard_cover_book(cls, book_name, book_weight):
        return cls(book_name, cls.cover_types[0], book_weight)
        # return Book(book_name, cls.cover_types[0], book_weight)
    
    @classmethod
    def create_softcover_book(cls, book_name, book_weight):
        return cls(book_name, cls.cover_types[1], book_weight)
    
    @classmethod
    def show_cls_parameter(cls):
        print(cls)
    
class Novel(Book):
    def __init__(self, book_name, book_cover, book_weight):
        super().__init__(book_name, book_cover, book_weight)

    @classmethod
    def show_cls_parameter(cls):
        print("INI KELAS NOVEL")

    @staticmethod
    def print_book_name(name):
        print(f"Nama bukunya adalah {name}")

# learning_phyton = Book.create_hard_cover_book('Learning Phyton', 500)
# tes_cpns = Book.create_softcover_book("Test CPNS", 100)
# print(learning_phyton)
# print(tes_cpns)
# manusia_setengah_salmon = Novel('Manusia Setengah Salmon', 'Soft Cover', 300)
# print(manusia_setengah_salmon)
# Book.show_cls_parameter()
# Novel.show_cls_parameter()
Book.print_book_name("Matematika Kelas 12 SMA")
Novel.print_book_name("uud 1945")
# learning_phyton = Book("Learning Phyton", 'Hard Cover', 500)
# tes_cpns = Book("Test CPNS", 'Soft Cover', 100)
# Book.show_cls_parameter()
