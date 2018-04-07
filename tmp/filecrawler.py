import glob, os
path = "./"
# os.walk(directory)
# os.chdir(directory)
# for file in glob.glob("*.py"):
#     print(file)
formats = ["mp4", "avi", "webm", "m2t", "gif"]
for extension in formats:
    for filename in glob.iglob(path + '**/*.{}'.format(extension), recursive=True):
        print(filename)