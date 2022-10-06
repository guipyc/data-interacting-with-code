# pylint: disable=missing-docstring, C0103



def directors_count(db):
    # return the number of directors contained in the database
    query = """
   SELECT COUNT(*)
FROM directors

   """
    db.execute(query)
    result = db.fetchone()
    return result[0]


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = """
   SELECT (name)
FROM directors
ORDER BY name ASC

   """
    db.execute(query)
    result = db.fetchall()
    result_list = []
    for elem in result:
        result_list.append(elem[0])
    return result_list


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = """SELECT title
    FROM movies
    WHERE movies.title LIKE 'love %'
    OR movies.title LIKE "% LOve"
    OR movies.title LIKE "% LOve %"
    OR movies.title LIKE "love, %"
    OR movies.title LIKE "% LOve, %"
    OR movies.title LIKE "% LOve."
    OR movies.title LIKE "% LOve'%"
    OR movies.title LIKE "love"
    ORDER BY title ASC
    """
    db.execute(query)
    result = db.fetchall()
    result_list = []
    for elem in result:
        result_list.append(elem[0])
    return result_list


def directors_named_like_count(db, name):
    query = f"""
    SELECT COUNT(name)
    FROM directors
    WHERE name LIKE '%{name}%'
    """
    db.execute(query)
    result = db.fetchone()
    return result[0]


def movies_longer_than(db, min_length):
    query = f"""
    SELECT *
    FROM movies
    WHERE minutes > {min_length}
    ORDER BY title ASC
"""
    db.execute(query)
    result = db.fetchall()
    result_list = []
    for elem in result:
        result_list.append(elem[0])
    return result_list
