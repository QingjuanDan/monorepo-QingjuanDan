from fastapi import FastAPI, Body, Query, Path, HTTPException

app = FastAPI()

BOOKS = [
    {
        "title": "The Sun Also Rises",
        "author": "Ernest Hemingway",
        "category": "fiction",
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "fiction",
    },
    {"title": "Skin in the Game", "author": "Nassem Talib", "category": "non-fiction"},
]


@app.get("/api")
def firstApi():
    return {"msg": "hello_worldxxx"}


@app.get("/books/{path_param}")
def firstApiV2(path_param: str):
    return {"msg": path_param}


@app.get("/books/")
def firstApiV3(category: str):
    res = []
    for book in BOOKS:
        if book.get("category").lower() == category.lower():
            res.append(book)
    return res


@app.get("/books/by_category_and_author")
def get_book_by_category_and_author(
    path_param: str = Path(..., description="Category"),
    author: str = Query(None, description="Author"),
):
    res = []
    for book in BOOKS:
        if book.get("category").lower() == path_param.lower():
            if author is None or author.lower() == book.get("author").lower():
                res.append(book)
    return res


@app.post("/books/create_book")
def firstApiV4(new_book=Body()):
    return {"msg": new_book}


@app.put("/books/update_book/{title}")
def update_book(
    title: str, updated_book: dict = Body(..., description="Updated book details")
):
    for book in BOOKS:
        if book.get("title") == title:
            book.update(updated_book)
            return {
                "msg": f"Book with title '{title}' updated successfully",
                "book": updated_book,
            }
    raise HTTPException(status_code=404, detail=f"Book with title '{title}' not found")


@app.delete("/books/delete_book/{title}")
def delete_book(title: str):
    for i, book in enumerate(BOOKS):
        if book.get("title") == title:
            deleted_book = BOOKS.pop(i)
            return {
                "msg": f"Book with title '{title}' deleted successfully",
                "deleted_book": deleted_book,
            }
    raise HTTPException(status_code=404, detail=f"Book with title '{title}' not found")
