class Library(object):
    def __init__(self):
        self.all_shelves = []
        self.all_books = []
    def all_books(self):
        print "The library contains the following books:"
        for book in self.all_books:
            print books

class Shelf(object):
    def __init__(self, name, library):
        self.name = name
        self.book_on_shelf = []
        library.all_shelves.append(self.name)
    def location_book(self):
        print "***", self.name, "***" 
        for book in self.book_on_shelf:
            print book

class Book(object):
    def __init__(self, title, library):
        self.title = title
        library.all_books.append(self.title)
    def enshelf(self, shelf):
        shelf.book_on_shelf.append(self.title)
    def unshelf(self, shelf):
        shelf.book_on_shelf.remove(self.title)

#TEST
library = Library()
computer_science = Shelf('Computer Science', library)
chemistry = Shelf('Chemistry', library)
other = Shelf('Other', library)

applied_cryptography = Book('Applied Cryptography', library)
artificial_intelligence_a_modern_approach = Book('Artificial Intelligence', library)
physical_chemistry = Book('Physical Chemistry', library)

applied_cryptography.enshelf(computer_science)
artificial_intelligence_a_modern_approach.enshelf(computer_science)
computer_science.location_book()

physical_chemistry.enshelf(chemistry)
chemistry.location_book()

applied_cryptography.unshelf(computer_science)
computer_science.location_book()

