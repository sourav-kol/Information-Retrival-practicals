import os


class GetFiles:


    def __init__(self):
        print()

    def openfile(self, create_token, index, path):
        for (dir_path, directory, file_name) in os.walk(path, topdown=False):
            for tempName in file_name:
                content = open(path + "\\" + tempName, mode='r')
                if create_token:
                    words = content.read().split(' ')
                    for w in words:
                        index = self.createToken(w.lower(), tempName, index)
                else:
                    print(content.read())
                    return None
                content.close()

        return index

    def get_stopwords(self, path, file_name):
        content = open(path+"\\"+file_name)
        return content.read().split("\n")

    def createToken(self, words,file_name, index):
        value = []
        if(words in index.keys()):
            value = index.get(words)
            if(file_name not in value):
                value.append(file_name)
                index.update(words=value)
        else:
            value.append(file_name)
            index[words] = value

        return index



    def writeIndexFile(self, index, path,filename):
        output = open(path+"\\"+filename, "a")

        for w in index:
            data = w
            content = index.get(w)
            for element in content:
                data = data + " " + element
            output.write(data)
            output.write("\n")
        output.close()

    def eliminateStopwords(self, dict, stop):
        for s in stop:
            if s in dict.keys():
                dict.pop(s)
        return dict

    def process_query(self, query, index):
        doc_list = []
        query_word = query.split(' ')
        for q in query_word:
            if q in index.keys():
                word_list = index.get(q)
                doc_list = self.insert_list(word_list, doc_list)
                # print(q, doc_list)
        return doc_list

    def insert_list(self, doclist, finallist):
        for w in doclist:
            if w not in finallist:
                finallist.append(w)

        return finallist

