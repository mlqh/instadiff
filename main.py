import zipfile
import ujson
    
def unzip(path):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall("./Extracted Data")

def main():
    print("Enter zipped file name:")
    filename = input()
    unzip(filename)
    
    
if __name__ == "__main__":
    main()