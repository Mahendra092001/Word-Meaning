from datetime import date

def writeData(word, meaning):
    file = open(r'C:\Users\Reaper\Desktop\WordMeaningProject\WordMeaningFile.txt', 'a+')
    
    #Check if the current date already exists in the file
    currentCursorPosition = file.tell()
    today = date.today()
    
    condition = False
    while(not (condition or currentCursorPosition == 0)):
        # while(file.read(1) != "\n"):
        #     currentCursorPosition -= 1
        #     file.seek(currentCursorPosition)
        
        currentCursorPosition -= 1
        file.seek(currentCursorPosition)
        
        condition = (file.read(16) == f'Date: {str(today)}')

    #Write to file accordingly
    file.seek(0, 2)
    if(condition):
        file.write(f'\n{word}: {meaning}')
    else:
        strIfBegin = "" if file.tell() == 0 else "\n\n"
        file.write(f'{strIfBegin}Date: {str(today)}\n{word}: {meaning}')

writeData('Home', 'place to live in')