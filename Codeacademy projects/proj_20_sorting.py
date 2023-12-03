import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
for book in bookshelf:
  book["author_lower"] = book["author"].lower()
  book["title_lower"] = book["title"].lower()

def by_title_ascending(book_a, book_b):
  if book_a["title_lower"] > book_b["title_lower"]:
    return True
  else:
    return False
def by_author_ascending(book_a, book_b):
  if book_a["author_lower"] > book_b["author_lower"]:
    return True
  else:
    return False
def by_total_length(book_a, book_b):
  if len(book_a["title"]) + len(book_a["author"]) > len(book_a["title"]) + len(book_b["author"]):
    return True
  else:
    return False

sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)

for book in sort1:
  print(book["title"])

bookshelf_v1 = bookshelf.copy()

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

for book in sort_2:
  print(book["author"])

print("\n\n\n")
bookshelf_v2 = bookshelf.copy()


sorts.quicksort(bookshelf_v2, 0, len(bookshelf) -1, by_author_ascending)

for book in bookshelf_v2:
  print(book["author"])



long_bookshelf = utils.load_books('books_large.csv')

#sorts.bubble_sort(long_bookshelf, by_total_length)

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)