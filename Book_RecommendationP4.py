import pandas as pd

books_df = pd.read_csv('Project_4/books.csv')

class Rec():
    def __init__(self,books_store):
        self.books = books_store
        self.first = True
        self.interface()

    def search_books(self,keyword):
        self.first = False
        keyword = [key.lower() for key in keyword]
        tag = {'title':keyword[0],'authors':keyword[1],'publisher':keyword[2]}
        results = self.books[
            (books_df['title'].str.lower().str.contains(keyword[0])) &
            (books_df['authors'].str.lower().str.contains(keyword[1])) &
            (books_df['publisher'].str.lower().str.contains(keyword[2]))
        ]

        self.display_books(results,tag)

    def display_books(self,books,keyword):
        if not len(books):
            print("\n No books found.\n")
        else:
            for index, book in books.iterrows():
                print(f" Title: {book['title']}")
                print(f" Author: {book['authors']}")
                print(f" Average Rating: {book['average_rating']}")
                print(f" ISBN: {book['isbn']}")
                print(f" ISBN13: {book['isbn13']}")
                print(f" Language: {book['language_code']}")
                if 'num_pages' in book: print(f" Number of Pages: {book['num_pages']}")
                print(f" Ratings Count: {book['ratings_count']}")
                print(f" Text Reviews Count: {book['text_reviews_count']}")
                print(f" Publication Date: {book['publication_date']}")
                print(f" Publisher: {book['publisher']}")
                print('\n')
        print(f' Total Books Found ({",".join([f" {i}:{keyword[i]}" for i in keyword if keyword[i]!=""])} ): {len(books)}\n')
        self.interface()

    def interface(self):
        if self.first:
            print( "Welcome to the Book Recommendation Program!")
        else:
            print(" Another Search?")

        print(" Enter a keyword to search for books: \n")
        auth = input(" Enter author's name: ")
        pub = input(" Enter publisher's name: ")
        title = input(" Enter book's title: ")
        keyword=[title,auth,pub]
        self.search_books(keyword)

book_search = Rec(books_store=books_df)


