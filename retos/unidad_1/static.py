"""Book catalog management system. Static Representation"""

# Scenario: Representing a library catalog.
# Task: Create a program using a static data structure (like a list or dictionary)
# to store information about books in a library catalog.
# The program should allow users to:
# - Add new books: Include title, author, ISBN, and genre.
# - Search for books: By title, author, or ISBN.
# - Display all books: In a formatted way.

# Using a dictionary to store book information
catalog = {}


def add_book(title, author, isbn, genre):
    """
    Add a book to the catalog.

    Args:
        title (str): Book title.
        author (str): Book author.
        isbn (str): Book ISBN.
        genre (str): Book genre.
    """
    catalog[isbn] = {"title": title, "author": author, "genre": genre}


def search_book(query):
    """
    Search for books by title, author, or ISBN.

    Args:
        query (str): The search term.

    Returns:
        list: A list of matching books.
    """
    results = []
    for isbn, book_data in catalog.items():
        if (
            query in book_data["title"]
            or query in book_data["author"]
            or query == isbn
        ):
            results.append(book_data)
    return results


def display_catalog():
    """
    Display all books in the catalog.
    """
    print("-" * 80)
    print("Book Catalog")
    print("-" * 80)

    for isbn, book_data in catalog.items():
        print(
            f"ISBN: {isbn}, "
            f"Title: {book_data['title']}, "
            f"Author: {book_data['author']}, "
            f"Genre: {book_data['genre']}"
        )


# Example usage
add_book("The Lord of the Rings", "J.R.R. Tolkien", "9780547928227", "Fantasy")
add_book("Don Quijote de la Mancha", "Miguel de Cervantes", "9788491050293", "Clásico")
add_book("Cien años de soledad", "Gabriel García Márquez", "9780307474728", "Realismo mágico")
add_book("La sombra del viento", "Carlos Ruiz Zafón", "9788408172171", "Misterio")
add_book("Los detectives salvajes", "Roberto Bolaño", "9788433971772", "Novela contemporánea")
add_book("Rayuela", "Julio Cortázar", "9788437603266", "Ficción experimental")

LIBRO_BUSCADO = "Quijote"
search_results = search_book(LIBRO_BUSCADO)

if not search_results:
    print(f"No se encontró el libro: {LIBRO_BUSCADO}")
else:
    print("Se encontró el libro:")
    for book in search_results:
        print(f"{book['title']} de {book['author']} (Género: {book['genre']})")
    print()

display_catalog()
