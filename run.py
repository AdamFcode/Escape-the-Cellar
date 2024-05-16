# Function to open, read and close the story txt files
def read_story(filepath):
    f = open(filepath, "r")
    print(f.read())
    f.close()
