from imageToAscii import imageToAscii
import os


def getAsciiPics(folder=str("ascii")):
    for picture in os.listdir(folder):
        imageToAscii(f"{folder}\\{picture}",300,False,"output.txt")

def delOutput():
    with open("output.txt", 'w') as f:
        f.write("")

if __name__ == "__main__":
    delOutput()
    getAsciiPics()