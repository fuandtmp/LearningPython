# Create a function which get card number and amount stars before last 4 numbers
def get_hidden_card(number_of_card, index_of_stars = 4):
    stars = '*' * index_of_stars
    hidden_number = stars + str(number_of_card[-4:])
    return hidden_number
# Enter card number
print('Please, enter a card number:', end = ' ')

num = str(input())
# Use function get_hidden_number

num = get_hidden_card(num)

# Print result

print(num)
