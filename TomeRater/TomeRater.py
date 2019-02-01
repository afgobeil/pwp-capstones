class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.book = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email has been updated")

    def __repr__(self):
        return "User {0}, email:{1}, books read: {2}".format(self.name,self.email, str(len(self.book)))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.get_email()
    
    def read_book(self, book, rating = None):
        self.book[book] = rating
        
    def get_average_rating(self):
        values = 0
        if len(self.book) == 0:
            return 0
        length = 0
        for rating in self.book.values():
            if rating != None:
                values += rating
                length += 1
        return values/length    
    
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The isbn of book {0} has been updated".format(self.title))
        
    def add_rating(self, rating):
        if rating != None:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
    
    def __eq__(self, other_book):
        return self.title == other_book.get_title() and self.isbn == other_book.get_title()
    
    def get_average_rating(self):
        values = 0
        if len(self.ratings) == 0:
            return values
        for rating in self.ratings:
            values += rating
        return values/len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def __repr__(self):
        return "{0}".format(self.title)

    
class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{0} by {1}".format(self.title, self.author)
    
    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{0}, a {1} manual on {2}".format(self.title, self.level, self.subject)
    

class TomeRater(object):
    def __init__(self):
        self.users = {} #key = user email value = User object
        self.books = {} #key = book object value = number of users who have read it
        
    def create_book(self, title, isbn):
        return Book(title, isbn)
    
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating = None):
        try:
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            nb_user = self.books.get(book, 0)
            self.books[book] = nb_user + 1               
        except KeyError:
            print("No user with email {0}".format(email))

    def add_user(self, name, email, user_books = None):
        user = User(name, email)
        self.users[email] = user
        if user_books != None :
            for book in user_books:
                self.add_book_to_user(book, email)
    
    
    #analysis method
    def print_catalog(self):
        print("CATALOG:")
        for key in self.books.keys():
            print(key)

    def print_users(self):
        print("USERS:")
        for user in self.users.values():
            print(user)
            
    def most_read_book(self):
        most_read = None
        nb_most_read = 0
        for book, nb_read in self.books.items():
            if nb_read > nb_most_read:
                most_read = book
                nb_most_read = nb_read
        return most_read
    
    def highest_rated_book(self):
        highest_rated_book = None
        highest_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_rated_book = book
                highest_rating = rating
        return highest_rated_book
    
    def most_positive_user(self):
        highest_rating = 0
        user_highest_rating = None
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > highest_rating:
                highest_rating = rating
                user_highest_rating = user
        return user_highest_rating
    
            