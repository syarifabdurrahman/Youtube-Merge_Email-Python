# get data
the_names = []
letter_path = r"starting_letter.txt"
invitated_name_path = r'names.txt'

with open(invitated_name_path, mode='r') as invited_names:
    lines = invited_names.read()
    list_of_name = lines.splitlines()
    the_names = [name for name in list_of_name]

with open(letter_path, mode='r') as letter_read:
    content_read = letter_read.read()
    for i, name in enumerate(the_names):
        x = content_read.replace('[name]', f'{name}')
        output = open(f"output\send_letter_to_{name}.txt", 'w')
        output.write(x)
