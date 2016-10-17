import docx2txt
import os

ABS_PATH = os.path.dirname(os.path.realpath(__file__))

def main():
    source = os.path.join(ABS_PATH, 'docs/')

    for root, dirs, filenames in os.walk(source):
        for f in filenames:
            filename, file_extension = os.path.splitext(f)

            directory = os.path.join(ABS_PATH, "images/%s" % filename)
            if not os.path.exists(directory):
                os.makedirs(directory)

            docx2txt.process("%s%s" % (source, f), directory)

if __name__ == "__main__":
    main()
