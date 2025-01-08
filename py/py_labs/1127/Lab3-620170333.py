def makebook(isbn,title,authors,qtystck,saleprice,genre,year):
    """constructor - creates a book"""
    return [isbn,title,authors,qtystck,saleprice,genre,year]

def bookshop():
    """constructor- creates a new bookshop"""
    return ("bookshop",[])

def add_book(book,bookshop):
    """constructor - adds a book to the bookshop"""
    return bookshop[1].append(book)

# example books
b1 = makebook("9780262510875","Struc. & Interp of Comp. Prog.",\
            ["Abelson H.","Sussman G.","Sussman J."] ,12, 7340.00,"CS text", 1996)

b2 = makebook("0216874068000","Algebra & No. Sys",["Hunter, J."],30,1040.00,"Math text", 1985)

b3 = makebook("9780521644082","Haskell School of Expr.",["Hudak, P."],1,3455.00,"CS text", 2000)

# code to create a uwi_bookshop
uwiBookshop = bookshop()
add_book(b1, uwiBookshop)
add_book(b2, uwiBookshop)
add_book(b3, uwiBookshop)

"""  accessor functions in python which take a book as input and return
the corresponding attribute of a book. """
def get_books(bookshop):
    return bookshop[1]

def get_Isbn(book):
    return book[0]

def get_Title(book):
    return book[1]

def get_Authors(book):
    return book[2]

def get_Qty(book):
    return book[3]

def get_Saleprice(book):
    return book[4]

def get_Genre(book):
    return book[5]

def get_Year(book):
    return book[6]

""" Write a function coAuthors which takes a book as a parameter 
and returns the list of coauthors if the book is written by multiple authors, 
and returns an empty list if it is single
authored. """
def coAuthors(book):
    if not len(get_Authors(book)) >= 2: #base case if author count is NOT >= 2
        return []
    else:
        return get_Authors(book)[1:]



""" check_price takes isbn & bookshop as input and returns the corresponding
sale price of the book. If book doesnt exist error msg is printed """
def check_price(isbn, bookshop): 
    for book in get_books(bookshop):
        if isbn == get_Isbn(book):
            return get_Saleprice(book)
        else: 
            return "Book not found"
        
""" booksToReorder takes an integer representing reorderlevel + a bookshop.
All books in bookshop whos quantities are >= to the reorder are returned in a list.

For each book that needs to be reordered, only the isbn and titles are added to the list as tuples

eg. booksToReorder(15, uwiBookshop)
[('9780262510875', 'Struc. & Interp of Comp.Prog.'),
('9780521644082', 'Haskell School of Expr.')]

def booksToReorder(reorderlevel, bookshop):
    reorderlst = []
    for book in bookshop[1]:
        if(get_Qty(book) <= reorderlevel):
            reorderlst.append((get_isbn(book),get_Title(book)))
    return reorderlst

"""
def booksToReorder(reorderlevel, bookshop):
    reorderlst = []
    for book in bookshop[1]:
        if(get_Qty(book) <= reorderlevel):
            reorderlst.append((get_Isbn(book),get_Title(book)))
    return reorderlst

        

