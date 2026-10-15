class Publication:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  def display_Info(self):
    print("Publication Information:")
    print("Title:", self.title)
    print("Author:", self.author)
    print("")

class Book(Publication):
  def __init__(self, title, author, number_of_pages):
    super().__init__(title, author)
    self.__number_of_pages = number_of_pages
  def display_Info(self):
      print("Book Information:")
      print("Number of pages must be positve")
      print("Title:", self.title)
      print("Author:", self.author)
      print("Number of Pages:", self.__number_of_pages)
      print("")

class Magazine(Publication):
  def __init__(self, title, author, issue_number):
    super().__init__(title, author)
    self.__issue_number = issue_number
  def display_Info(self):
      print("Magazine Information:")
      print("Title:", self.title)
      print("Author:", self.author)
      print("Issue Number:", self.__issue_number)
      print("")

Publication1A = Publication("Example Title 1A", "Example Author 1A")
Publication1B = Publication("Example Title 1B", "Example Author 1B")
Book1A = Book("Example Title 2A", "Example Author 2A", "Page Number")
Book1B = Book("Example Title 2B", "Example Author 2.1", "Page Number^2")
Magazine1A = Magazine("Example Title 3A", "Example Author 3A", "Issue Number")
Magazine1B = Magazine("Example Title 3B", "Example Author 3B", "Issue Number^2")
Publication1A.display_Info()
Book1A.display_Info()
Magazine1A.display_Info()
Publication1B.display_Info()
Book1B.display_Info()
Magazine1B.display_Info()

#Sir, I dont fully understand how to make the page number positive only, and not negative
#Also po sir, I couldn't make the title and author of the publication private, because when I made it private, the super().__init__() function wouldn't work.
#Thank you sir!
