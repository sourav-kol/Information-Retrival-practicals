#write functions for :
# -----------------------
#get total number of files in a folder (d)                      (path)
#read files                                                     (path,filename)
#write to file                                                  (path,filename,content)
#contruct vector space index                                    (filecontent, index) -> index
#calculate 'tf' i.e. number of occurences of term in the file   (index,
#calculate 'df' i.e number of terms that contains terms
#idf = log( d / df )
#calculate tfidf
#similarity coefficent
#rank

from pratical3.similarity_coefficient import Similarity_coef
from pratical3.take_input import Get_input

if __name__ == '__main__':
    vector = {}
    df_index = {}
    query_index = {}

    files = Similarity_coef("D:\\Users\\lenovo\\Documents\\InfoRet\\files2")
    query = Get_input()

    files.file_count_name()

    vector = files.openfile(True, vector)
    total_files = files.get_file_count()

    print(total_files,"\n")
    # print(vector)

    df_index = files.calc_idf(vector)
    # print(df_index)

    query_index = query.construct_query_index()
    # print(query_index)

    tfidf = files.calc_tfidf(vector, df_index, query_index)
    # print(tfidf)

    sm_c = files.calc_similarity_coefficient(tfidf, query_index, vector)
    # print(sm_c)

    ranking = files.rank(sm_c)
    print(ranking)