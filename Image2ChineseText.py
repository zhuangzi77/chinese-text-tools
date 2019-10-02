#PNG2ChineseText.py
#This takes a folder of image files and creates a Chinese language text file in the parent directory.
#It works well with JPG and PNG files, getting modestly better results than Adobe Acrobat OCR. TIFF doesn't work. JPF had some garbled text.

#NB: The "tesseract_cmd" variable at the top of tesseract.py must be changed to the path I am using.
#tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os

need_help = input('''Starting Image2ChineseText.py.
Type h for help.  Otherwise, press any other key:  ''')
need_help = need_help.lower().strip()
if len(need_help) != 0:
    if need_help[0] == 'h':
        print('''
This program takes a folder of image files and creates a Chinese language text file in the parent directory.
It works with PNG and JPG files, but not TIFF files.
To use it:
1.  You must export your pdf into a folder as a series of image files.
2.  You must install pytesseract.
Details on tesseract may be found here:  https://github.com/madmaze/pytesseract
3.  You must add the following to your the location of the tesseract.exe file to your PATH.
On Windows machines, it will likely be found here:
'C:\Program Files\Program Files (x86)Tesseract-OCR\\tesseract.exe'
4.  You must change the tesseract_cmd variable in the tesseract.py file on your machine to match the specified PATH.
5.  The program is slow. It takes about 2 mins to convert one sheet of text.
6.  The folder (directory) you use should contain only image files.
''')

dirName = input(r'Carefully enter the absolute path for the directory where the files are located: ')
while os.path.isdir(dirName) == False: 
    dirName = input(r'Double-check and re-enter the path for the folder: ')

os.chdir(dirName)

print ('You selected: ' + os.getcwd())

resultText = open('..\\resultText.txt', 'a', encoding='utf-8')
folder =  os.path.abspath('.')
total = str(len(os.listdir()))
print ('There are a total of ' + total + ' files to be converted...')
print ('Converting image to text for the following files:')
print (os.listdir())

#Gets a list of files in the directory to iterate over.
files = os.listdir()
imageNum = 1

for file in files:
    file = os.path.abspath(file)
    pageBreak = 'Image number: ' + str(imageNum)
    resultText.write('\n\n' + pageBreak.center(41, '*') + '\n\n')
    addedText = pytesseract.image_to_string(Image.open(file), lang = 'chi_tra')
    resultText.write(addedText)
    print("Text added from image #" + str(imageNum), end='...')
    imageNum = imageNum + 1

resultText.close()

print('File written.')
print('Change the name of the "resultText.txt" file to avoid accidently overwriting it or appending new text to it.')
