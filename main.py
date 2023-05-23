import constants
import zipfile
import ujson
  
def unzip(path):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(constants.EXTRACTED_PATH)

def main():
    extensions = [constants.HTML, constants.JSON]
    
    print("Enter zipped file path: ")
    filename = input()
    print("Enter data type (HTML/JSON): ")
    data_type = 0 if input().lower() == "html" else 1
    unzip(filename)
    followers = open(constants.FOLLOWERS_PATH + extensions[data_type])
    following = open(constants.FOLLOWING_PATH + extensions[data_type])
    
    followers_dict = ujson.load(followers)
    print("hi")
    
    
if __name__ == "__main__":
    main()