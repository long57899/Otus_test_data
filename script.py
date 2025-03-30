import json
import csv

def firts_method(books, peoples, output_file):
    """Это решение в случае если нам нужно передавать книги последовательно."""

    with open(books, 'r', encoding='utf-8') as f:
        books_list = list(csv.DictReader(f))
    
    with open(peoples, 'r', encoding='utf-8') as f:
        peoples_dict = json.load(f)
    
    for person in peoples_dict:
        if 'books' not in person:
            person['books'] = []
    
    for i, book in enumerate(books_list):
        person_index = i % len(peoples_dict)
        peoples_dict[person_index]['books'].append(book)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(peoples_dict, f, ensure_ascii=False, indent=2)


def second_method(books, peoples, output_file):
    """Это решение в случае если нам нужно передать книги группой."""
    
    with open(books, 'r', encoding='utf-8') as f:
        books_list = list(csv.DictReader(f))
    
    with open(peoples, 'r', encoding='utf-8') as f:
        peoples_dict = json.load(f)
    
    num_people = len(peoples_dict)
    num_books = len(books_list)
    books_per_person = num_books // num_people
    extra_books = num_books % num_people

    for i, person in enumerate(peoples_dict):
        start_idx = i * books_per_person + min(i, extra_books)
        end_idx = start_idx + books_per_person + (1 if i < extra_books else 0)

        if 'books' not in person:
            person['books'] = []

        person['books'] = books_list[start_idx:end_idx]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(peoples_dict, f, ensure_ascii=False, indent=2)


firts_method('books.csv', 'users.json', 'result_1.json')
second_method('books.csv', 'users.json', 'result_2.json')