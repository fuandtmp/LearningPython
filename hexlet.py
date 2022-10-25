# define function which get string, get number of index in string and slice that and add
# three dot in end of line
def truncate(get_str, amount_char):
    text = get_str[0:amount_char] + '...'
    return text

# define two variables which get string and index for function "truncate"
some_text = 'Moya testovaya funcia'
index = int(4)


# Print result
print(truncate(some_text, index))
