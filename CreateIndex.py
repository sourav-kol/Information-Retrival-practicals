from ReadFile import GetFiles

# file = GetFiles("D:\\Users\\lenovo\\Documents\\InfoRet\\files")
# file.openFile()

if __name__ == '__main__':
    file = GetFiles()

    filePath = "D:\\Users\\lenovo\\Documents\\InfoRet\\files"
    outputPath = "D:\\Users\\lenovo\\Documents\\InfoRet\\outputFiles"

    indexDict = {}
    indexStop = []

    indexDict = file.openfile(True, indexDict,filePath)
    # uncomment when writing to file
    # file.writeIndexFile(indexDict,outputPath,"index.txt")

    # file.openfile(False,False,indexDict,outputPath)

    indexStop = file.get_stopwords(outputPath, "stopwords.txt")
    # print(indexStop)

    indexDict = file.eliminateStopwords(indexDict, indexStop)

    # uncomment when writing to file
    # file.writeIndexFile(indexDict,outputPath, "index1.txt")

    query = input("enter the query...\n")
    # query = 'goa goa while'

    #split the query
    #take each element form the query find docs corresponding to it
    #keep the docs in list as well as take care tht it dosen't repeat
    query_doc = file.process_query(query, indexDict)

    #empty list/sequences are always false
    if query_doc:
        print("\nfinal doc list: \n ",query_doc)
    else:
        print("sorry... no documents found")


