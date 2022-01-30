import os
from bs4 import BeautifulSoup

def main():
    path = input("Please enter the directory where the files are located at (example: 'D:\code\learncpp-download'): ")# "D:\code\learncpp-download"
    for filename in os.listdir(path):
        if filename.endswith(".html"):
            print(filename)
            print("rename to")
            fname = os.path.join(path, filename)
            
            with open(fname, "r", encoding="utf8", errors='ignore') as f:
                soup = BeautifulSoup(f.read(), "lxml")
                lesson_num = soup.find("h1").get_text(strip=False).split(">")[0].split(" ")[0].replace(".","-")
                title = lesson_num + "_" + filename
                print(title)
                
            os.rename(path + "/" + filename, path + "/" + title)
        print("\n")

if __name__ == '__main__':
    main()
