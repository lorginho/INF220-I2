catalog = {}  # Using a dictionary to store book information


def add_book(title, author, isbn, genre):
    catalog[isbn] = {"title": title, "author": author, "genre": genre}


def search_book(query):
    results = []
    for isbn, book_data in catalog.items():
        if query in book_data["title"] or query in book_data["author"] or query == isbn:
            results.append(book_data)
    return results


def display_catalog():
    for isbn, book_data in catalog.items():
        print(
            f"ISBN: {isbn}, Title: {book_data['title']}, Author: {book_data['author']}, Genre: {book_data['genre']}"
        )


# Example usage
add_book("The Lord of the Rings", "J.R.R. Tolkien", "9780547928227", "Fantasy")
add_book(
    "The Hitchhiker's Guide to the Galaxy",
    "Douglas Adams",
    "9780345391803",
    "Science Fiction",
)

search_results = search_book("Tolkien")
print(search_results)

display_catalog()
