class Library:
    def __init__(self, books:list = None ):
        self.books = books if books is not None else []
        
    def add_book(self, book:str):
        self.books.append(book)
        print(f"{book} successfully added! ")
    
    def list_books(self):
        if self.books:
            print(*(i for i in self.books), sep = "\n")
        else:
            print(f"no books in the library")
    
    def remove_book(self, book:str):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed")
            
        else:
            print(f"{book} not found")
        
    def book_exists(self, book)->bool:
        if book in self.books:
            return True
            print(f"{book} is available")
            
        else:
            return False
            print(f"{book} is not available")
            
    
        
        
jts: Library = Library()

jts.add_book("think straight")
jts.list_books()
jts.remove_book("think straight")