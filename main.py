import os

#TODO : add a feature for change directory anywhere
os.chdir("../exampeles")

files =tuple(os.listdir().sort())
new_name = input()
print(files)
for i in range(len(files)):
    x = i+0
    f = open(files[i])
    print(files[i]+" :")
    print(f.read())
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    os.rename(files[i],f"{new_name}{x}.txt")
    f.close()

print(os.listdir())