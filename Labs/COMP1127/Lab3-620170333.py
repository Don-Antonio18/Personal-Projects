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
b1 = makebook("9780262510875","Struc. & Interp of Comp. Prog.",["Abelson H.","Sussman G.","Sussman J."],12, 7340.00,"CS text", 1996)
b2 = makebook("0216874068000","Algebra & No. Sys",["Hunter, J."],30,1040.00,"Math text", 1985)
b3 = makebook("9780521644082","Haskell School of Expr.",["Hudak, P."],1,3455.00,"CS text", 2000)

# code to create a uwi_bookshop
uwiBookshop = bookshop()
add_book(b1, uwiBookshop)
add_book(b2, uwiBookshop)
add_book(b3, uwiBookshop)