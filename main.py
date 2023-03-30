# python3
import random

class Query:
    def __init__(self):
        self.prime = random.randint(0,10000019)
        self.multiplier = random.randint(0,263)
        self.b_count = 1000
        self.b = [[] for _ in range(self.b_count)]

# def read_queries():
#     n = int(input())
#     return [Query(input().split()) for i in range(n)]

# def write_responses(result):
#     print('\n'.join(result))

# def process_queries(queries):
#     result = []
#     # Keep list of all existing (i.e. not deleted yet) contacts.
#     contacts = []
#     for cur_query in queries:
#         if cur_query.type == 'add':
#             # if we already have contact with such number,
#             # we should rewrite contact's name
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     contact.name = cur_query.name
#                     break
#             else: # otherwise, just add it
#                 contacts.append(cur_query)
#         elif cur_query.type == 'del':
#             for j in range(len(contacts)):
#                 if contacts[j].number == cur_query.number:
#                     contacts.pop(j)
#                     break
#         else:
#             response = 'not found'
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     response = contact.name
#                     break
#             result.append(response)
#     return result

    def hashFunction(self,text):
        reply = 0
        for i in reversed(text):
            reply = (reply * self.multiplier + ord(i)) % self.prime
        return reply % self.b_count

    def add(self,num,name):
        hashedNum = self.hashFunction(str(num))
        bucket = self.b[hashedNum]
        for j in range(len(bucket)):
            if bucket[j][0] == num:
                bucket[j] = (num,name)
                return
        bucket.append((num,name))

    def delete(self,num):
        hashedNum = self.hashFunction(str(num))
        bucket = self.b[hashedNum]
        for j in range(len(bucket)):
            if bucket[j][0] == num:
                del bucket[j]
                return

    def find(self,num):
        text = "not found"
        hashedNum = self.hashFunction(str(num))
        bucket = self.b[hashedNum]
        for j in range(len(bucket)):
            if bucket[j][0] == num:
                return bucket[j][1]
            return text

if __name__ == '__main__':
    # write_responses(process_queries(read_queries()))
    phoneBook = Query()
    n = int(input())
    answer = []
    for i in range(n):
        query = input().split()
        if query[0] == "add":
            phoneBook.add(int(query[1]),query[2])
        elif query[0] == "del":
            phoneBook.delete(int(query[1]))
        elif query[0] == "find":
            answer.append(phoneBook.find(int(query[1])))

    for j in range(len(answer)):
        print(answer[j])
