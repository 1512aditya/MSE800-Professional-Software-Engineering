# This project is a simple Library Management System built using Object-Oriented Programming (OOP) in Python. 
# It consists of a base class LibraryItem, which defines common attributes like title and author, and a method
#  display_info() to show basic details. The Book class inherits from LibraryItem and adds a genre attribute,
#   overriding display_info() to include book-specific information, while the Magazine class also inherits 
#   from LibraryItem but introduces an issue_frequency attribute and customizes display_info() to display 
#   magazine details. The Library class manages a collection of these items, with methods to add, remove, 
#   and display all items, demonstrating composition since it holds multiple LibraryItem objects. Finally, 
#   the main() function showcases the system in action by creating a library, adding books and magazines, 
#   displaying them, removing an item, and then showing the updated collection. This implementation 
#   demonstrates key OOP concepts such as inheritance, polymorphism, encapsulation, and composition in a 
#   practical way.

class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"
        
class book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre
    
    def display_info(self):
        return f"[Book] Title: {self.title}, Author: {self.author}, Genre: {self.genre}"

class magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.issue_frequency = issue_frequency

    def display_info(self):
       return f"[Magazine] Title: {self.title}, Author: {self.author}, Issue Frequency: {self.issue_frequency}"

class library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item.title}")

    def remove_item(self, title):
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                print(f"Removed: {title}")
                return
        print(f"Item '{title}' not found in library.")

    def display_items(self):
        if not self.items:
            print("Library is empty.")
        else:
            print("\nLibrary Collection:")
            for item in self.items:
                print(item.display_info())

def main():
    l = library()

    # Create Book and Magazine objects
    book1 = book("1984", "George Orwell", "Dystopian")
    book2 = book("To Kill a Mockingbird", "Harper Lee", "Classic")
    mag1 = magazine("National Geographic", "Various", "Monthly")

    # Add items to the library
    l.add_item(book1)
    l.add_item(book2)
    l.add_item(mag1)
    
    l.display_items()

    # Remove an item
    l.remove_item("1984")

    # Display again
    l.display_items()

if __name__ == '__main__':
    main()