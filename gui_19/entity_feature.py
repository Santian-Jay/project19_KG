relation_head = {}
relation_tail = {}


class enti_feature:
    def __init__(self):
        print('a')

    def get_count(self):
        data = open("dataset/train2id.txt", "r")

        total = int(data.readline())

        for i in range(total):
            content = data.readline()
            head, tail, relation = content.strip().split()
            if (relation, head) not in relation_head:
                relation_head[relation, head] = []
            if (relation, tail) not in relation_tail:
                relation_tail[relation, tail] = []
        return len(relation_head), len(relation_tail)


ef = enti_feature()

efeature = enti_feature()
