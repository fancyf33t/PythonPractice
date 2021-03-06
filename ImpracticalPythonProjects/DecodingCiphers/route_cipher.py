"""
Load the ciphertext string
convert ciphertext into a cipherlist to split out individual wordsprint
get input for the number of columns and rows
get input for the keu
convert key into a list to split out individual numbers
create a new list for the translation matrix
for every number in the key:
    create a new list and append every n items (n = # of rows) from the cipherlist
    use the sign of key number to decide whether to read the row forward or backward
    using the chosen direction, add the new list to the matrix. the index of each new list is based on the column number used in the key
create a new string to hold translation results
for range of rows:
    for the nested list in translation matrix:
        remove the last word in nested list
        add the word to the translation string
print the translation string
"""

print('nothing')

ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
# split elements into words not letters
cipherlist = list(ciphertext.split())

# initialize variables
COLS = 4
ROWS = 5
key = '-1 2 -3 4' # neg number means read UP column vs DOWN
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS
# turn key_int into list of integers:
key_int = [int(i) for i in key.split()]

# turn columns into items in list of lists:
for k in key_int:
    if k < 0: # reading bottom-to-top of column
        col_items = cipherlist[start:stop]
    elif k > 0: # reading top-to-bottom of column
        col_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS
print("\nciphertext = {}".format(ciphertext))
print("\ntranslation matrix =", * translation_matrix, sep="\n")
print("\nkey length = {}".format(len(key_int)))

# loop through nested lists popping off last item to new list:
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ''

print("\nplaintext = {}".format(plaintext))