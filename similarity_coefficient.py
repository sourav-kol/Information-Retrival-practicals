import os
import math

class Similarity_coef:

    path = ""
    file_count = 0
    file_names = []

    def __init__(self, p):
        self.path = p

    def file_count_name(self):
        for (dir_path, directory, file_name) in os.walk(self.path, topdown=False):
            self.file_names = file_name
        self.file_count = len(self.file_names)

    def get_file_count(self):
        return self.file_count

    def get_file_names(self):
        return self.file_names

    def set_path(self,path):
        self.path = path

    def openfile(self, create_token, index):
        for tempName in self.file_names:
            content = open(self.path + "\\" + tempName, mode='r')
            if create_token:
                words = content.read().split(' ')
                for w in words:
                    index = self.createToken(w.lower(), tempName, index)
            else:
                print(content.read())
                return None
            content.close()

        return index

    def createToken(self, words, file_name, index):
        value = []
        file_index = self.get_file_index(file_name)

        if(words in index.keys()):
            value = index.get(words)
            old_val = value[file_index]
            value[file_index] = old_val+1
            index.update(words=value)
        else:
            value = self.initialize(self.file_count-1)
            value.insert(file_index, 1)
            index[words] = value

        return index

    def initialize(self, count):
        v = []
        for c in range(0, count):
           v.insert(c, 0)

        return v

    def get_file_index(self, name):
        count = 0
        for fn in self.file_names:
            if fn not in name:
                count += 1
            else:
                break
        return count

    #df
    def get_occurence_count(self,vec):
        count = 0
        for v in vec:
            if v >= 1:
                count += 1

        return count

    def calc_idf(self, index):
        dfIndex = {}
        for element in index:
            denom = self.get_occurence_count(index.get(element))
            df = math.log(self.file_count/denom, 10)
            df = round(df, 4)
            dfIndex[element] = df

        return dfIndex

    def calc_tfidf(self,v_index, df_indx, q_index):
        tfidf = self.initialize(len(v_index))
        tfidf_count = 0

        for element in v_index:
            value = v_index.get(element)
            temp_df = df_indx.get(element)
            in_count = 0

            idf_file = self.initialize(self.file_count+1)
            for val in value:
                idf_file[in_count] = val * temp_df
                in_count += 1
            query_fre = q_index.get(element)
            if query_fre != None:
                idf_file[in_count] = query_fre*temp_df
            tfidf[tfidf_count] = idf_file
            tfidf_count += 1

        return tfidf

    def calc_similarity_coefficient(self, tfidf, query, index):
        similarity_coeff = []
        tfidf_index = []
        temp_val = list(index.keys())

        for q in query:
            try:
                index = temp_val.index(q)
            except ValueError:
                index = -1

            if index != -1:
                tfidf_index.append(tfidf[index])

        # print(tfidf_index)
        iterator = 0
        size = self.file_count
        for file in range(0, self.file_count):
            temp_sc = 0.0
            for i in tfidf_index:
                temp_sc += i[iterator] * i[size]
                # print(i[iterator], i[size], size)
            similarity_coeff.append(round(temp_sc, 4))
            iterator += 1
        return similarity_coeff

    def rank(self, sm_c):
        ranked_dict = {}
        index = 0
        # ranked_list = []
        for f in self.file_names:
            ranked_dict[f] = sm_c[index]
            index += 1

        for i in sorted(ranked_dict.keys()):
            print(i)

        return ranked_dict

    def show_file_index(self):
        for f in self.file_names:
            print(f)

#      shipment
#  d1     d2    d3     Q
#[[0.1716, 0, 0.1716, 343], []]