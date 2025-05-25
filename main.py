class Wall:
    
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width

    def get_cost(self):
        cost = self.armor * self.height
        return cost

    def fortify(self):
        self.armor *= 2
        
class Archer:
    def __init__(self, name, health, num_of_arrows):
        self.name = name
        self.health = health
        self.num_of_arrows = num_of_arrows

    def get_shot(self):
        try:
            if self.health > 0:
                self.health -= 1
            else:
                raise Exception
        except Exception:
            return f"{self.name} is dead" 


    def shoot(self, target):
        try:
            if self.num_of_arrows < 1:
                raise Exception
            else:
                self.num_of_arrows -= 1
                return f"{self.name} shoots {target}"
        except Exception:
            return f"{self.name} is dead"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append((book.title, book.author))
    
    def remove_book(self, book):
        for library_book in self.books:
            if (book.title == library_book[0]) and (book.author == library_book[1]):
                self.books.remove(library_book)

    def search_books(self, search_string):
        self.found_books = []
        for library_book in self.books:
            if (search_string.lower() in library_book[0].lower()) or (search_string.lower() in library_book[1].lower()):
                self.found_books.append(library_book)
        for found_book in self.found_books:
            return f"Book title: {found_book[0]}, Book Author: {found_book[1]}"


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2*(self.__length + self.__width)


class Square(Rectangle):
    def __init__(self, length):
        self.__length = length
    
    def get_perimeter(self):
        return 4 * self.__length
    
    def get_area(self):
        return self.__length ** 2






