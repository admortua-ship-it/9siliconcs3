## Creating Classes for Publication, Book, and Magazine

class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @ property
    def get_title(self):
        return self.title

    @ property
    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Book(Publication):
    def __init__(self, title, author,number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages

    @ property
    def get_number_of_pages(self):
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages < 0:
            print("The number of pages must be positive.")
        else:
            self.number_of_pages = number_of_pages

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    @ property
    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, issue_number):
        if issue_number < 0:
            print("The issue number must be positive.")
        else:
            self.issue_number = issue_number

# Creating example objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

# Printing the information of the created example objects
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310) # Setting invalid value on attribute number_of_pages to test validation
book1.display_info()
print(f"Number of Pages: {book1.get_number_of_pages}")

print("\nMagazine Information:")
mag1.display_info()
print(f"Issue Number: {mag1.get_issue_number}")

# Footnote: The code was created with the help of the built-in Intellisense and Microsoft IntelliCodefeature of Visual Studio Code, which provided suggestions and auto-completions for class methods and properties.



# Test Results:
"""
Title: Journal of Experimental Psychology
Author: Ratchiff, R. & Van Dongen, H.

Book Information:
The number of pages must be positive.
Title: The Hobbit
Author: J.R.R. Tolkein
Number of Pages: 310

Magazine Information:
Title: National Geographic
Author: Various Authors
Issue Number: 202
"""