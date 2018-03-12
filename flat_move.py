import os

print('=== Flat Move ===')

# Reading input
valid_path = False
while not valid_path:
    data_path = input('Enter data path: ')
    valid_path = os.path.isdir(data_path)

move_path = input('Enter move path: ')
if not os.path.isdir(move_path):
    os.mkdir(move_path)

# Begin of iteration
count = 0
for root, dirs, files in os.walk(data_path):
    for f in files:
        count += 1
        file_path = os.path.join(root, f)
        new_path = os.path.join(move_path, f)
        file_name, ext = os.path.splitext(new_path)

        # Resolving same name files
        attempt = 1
        temp = new_path
        while os.path.isfile(temp):
            temp = file_name + ' (' + str(attempt) + ')' + ext
            attempt += 1

        if attempt > 1:
            new_path = temp

        # Moving file
        print(str(count) + ': Moving ' + file_path + ' to ' + new_path)
        os.rename(file_path, new_path)

# Result
print('\n' + str(count) + ' files moved')
