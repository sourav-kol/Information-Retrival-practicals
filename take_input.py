class Get_input:
    def get_query(self):
        # query = input("enter query here \n")
        query = "silver delivery "
        return query.split(" ")

    def construct_query_index(self):
        q_index = {}
        q = self.get_query()
        for words in q:
            if words in q_index.keys():
                value = q_index.get(words)
                q_index[words] = value + 1
            else:
                q_index[words] = 1

        return q_index

