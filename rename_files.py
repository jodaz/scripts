import os

path = input("Introduce path: ")
text_to_remove = input("Introduce text: ")

count = 0

for file in os.listdir(path):
    if (file.startswith(text_to_remove)):
        new_name = file.replace(text_to_remove, '')
        old_path = os.path.join(path, file)
        new_path = os.path.join(path, new_name)

        os.rename(old_path, new_path)
        print("Rename ", old_path, " to ", new_path)
        count += 1
    
print("Total files ", count)
