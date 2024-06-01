class Book:
    COVER_TYPES = ['HARD_COVER', 'SOFT_COVER']

    def __init__(self, book_name, book_cover, book_weight):
        self.book_name = book_name
        self.book_cover = book_cover
        self.book_weight = book_weight

    # def __str__(self):
    #     return f"Book name is : {self.book_name}. Cover type is: {self.book_cover}. Book weight is: {self.book_weight}"
    
    # def __repr__(self) -> str:
    #     return f"<Class: {self.__class__.__name__}. Instance Memory ID:{id(self)}>"
    
    @classmethod
    def hard_cover_book(cls, book_name, book_weight):
        return cls(book_name, cls.COVER_TYPES[0], book_weight)

    @classmethod
    def soft_cover_book(cls, book_name, book_weight):
        return cls(book_name, cls.COVER_TYPES[1], book_weight)
    
harry_potter = Book('Harry Potter', 'HARD_COVER', 500)
manusia_setengah_salmon = Book.soft_cover_book('Manusia Setengah Salmon', 200)
ayat_ayat_cinta = Book.hard_cover_book('Ayat-ayat Cinta', 700)
print(harry_potter)
print(manusia_setengah_salmon)
print(ayat_ayat_cinta)
print(id(ayat_ayat_cinta))

class Novel(Book):
        def __init__(self, book_name, book_cover, book_weight, book_publisher):
            super().__init__(book_name, book_cover, book_weight)
            self.book_publisher = book_publisher

ayat_ayat_cinta_2 = Novel('Ayat-ayat Cinta 2', 'HARD_COVER', 700, 'GRAMEDIA')
print(id(ayat_ayat_cinta_2))
print(ayat_ayat_cinta_2)