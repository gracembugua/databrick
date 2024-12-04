## Write a query that will display the results below (Note:  be renamed but use the column names above). It should only show 2020 data and order by driver points.

query = """
SELECT 
    ra.race_year AS year,
    ra.race_name,
    ra.race_date AS date,
    c.circuit_location AS location,
    d.driver_name,
    d.driver_nationality,
    con.name AS team_name,
    re.grid,
    re.position,
    re.fastest_lap,
    re.time,
    re.points
FROM 
    results re
JOIN 
    races ra ON re.raceId = ra.raceId
JOIN 
    circuits c ON ra.circuitId = c.circuitId
JOIN 
    drivers d ON re.driverId = d.driverId
JOIN 
    constructors con ON re.constructorId = con.constructorId
WHERE 
    ra.race_year = 2020
ORDER BY 
    re.points DESC;
"""

## 2.	Write a Python function that checks whether a word or phrase is palindrome or not.


def is_palindrome(phrase):

    cleaned_phrase = phrase.replace(" ", "").lower()

    return cleaned_phrase == cleaned_phrase[::-1]


# 3.	Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

def is_pangram(sentence):

    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")

    sentence_set = set(sentence.lower())

    return alphabet_set.issubset(sentence_set)


# 4.	Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reverse_integer(num):

    str_num = str(num)

    if str_num[0] == '-':
        reversed_num = int('-' + str_num[:0:-1])
    else:
        reversed_num = int(str_num[::-1])

    return reversed_num


# 5.	Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.


def capitalize_words(sentence):

    capitalized_sentence = sentence.title()

    return capitalized_sentence