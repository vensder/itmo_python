try:
    with open ('some_file') as f:
        pass
except FileNotFoundError as e:
    print('file not found\n' + str(e))

