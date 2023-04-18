import os
import docx

# This will examine filenames under given directory and manipulate the filenames
# First look for `)(` and replace with `_`
# Then look for `(` and replace with `_`
# Then look for `)` and replace with `_`
# However if filename ends with `).doc` then replace with `.doc`
def manipulate_filename(directory):
    for filename in os.listdir(directory):
        if filename.endswith(").doc"):
            new_filename = filename.replace(")(", "_").replace("(", "_").replace(")", "").replace(").doc", ".doc")
        else:
            new_filename = filename.replace(")(", "_").replace("(", "_").replace(")", "_")
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


if __name__ == "__main__":
    directory = "C:\\Users\\yhk\\Documents\\GitHub\\socialservice-korea\\data"
    manipulate_filename(directory)
