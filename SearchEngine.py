import sys
import os

# delete the search results in order to search and store the results again
if os.path.isfile('searchresult.txt'):
    os.remove('searchresult.txt')
    print("Search Results are cleared for a fresh search!")
else:
    print("File doesn't exists!")

# obtain the string to be searched which is passed in the command line and start a counter
string_to_search = str(sys.argv[1]).capitalize()
print(f'String to search: {string_to_search}')
s = " "
count = 0

# open the file
with open('newsarticles.txt', 'r') as search_engine:
    # read the file line by line
    for line in search_engine:
        # if a match is found for the searched string then add it to the counter and print it to line
        if string_to_search in line:
            count += 1
            with open('searchresult.txt','a') as results:
                results.write(f'{count}. {line}')
# print to command line the number of articles returned for the search string
print(f"{count} articles were found.")
print("Search results are written to the file - searchresults.txt")
