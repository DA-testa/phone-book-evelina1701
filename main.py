# Evelīna Geikina 221RDB068 14.grupa
# python3
import random

class Query:
    def __init__(self):
        # Inicializē prime un multiplier ar nejaušiem skaitļiem un inicializē ierakstu skaitu un sarakstu
        self.prime = random.randint(0,10000019)
        self.multiplier = random.randint(0,263)
        self.record_count = 1000
        self.records = [[] for _ in range(self.record_count)]

    def hashFunction(self,text):
        # Lai aprēķinātu ieraksta atrašanās vietu, tiek definēta hash funkcija
        reply = 0
        for i in reversed(text):
            reply = (reply * self.multiplier + ord(i)) % self.prime
        return reply % self.record_count

    def add(self,num,name):
        # Tiek aprēķināta ieraksta atrašanās vieta. Ja tajā vietā jau ir ierakstīta informācija, tad
        # tā tiek aizvietota ar jaunu ierakstu, pretējā gadījumā tiek izveidots jauns ieraksts
        hashedNum = self.hashFunction(str(num))
        record = self.records[hashedNum]
        for j in range(len(record)):
            if record[j][0] == num:
                record[j] = (num,name)
                return
        record.append((num,name))

    def delete(self,num):
        # Tiek aprēķināta ieraksta atrašanās vieta. Ja tajā vietā ir ierakstīta informācija, tad
        # tā tiek dzēsta, pretējā gadījumā nekas netiks izdarīts
        hashedNum = self.hashFunction(str(num))
        record = self.records[hashedNum]
        for j in range(len(record)):
            if record[j][0] == num:
                del record[j]
                return

    def find(self,num):
        # Tiek aprēķināta ieraksta atrašanās vieta. Ja tajā vietā ir ierakstīta vajadzīgā informācija, tad
        # tiks atgriezts personas vārds, pretējā gadījumā tiks izvadīts "not found"
        text = "not found"
        hashedNum = self.hashFunction(str(num))
        record = self.records[hashedNum]
        for j in range(len(record)):
            if record[j][0] == num:
                return record[j][1]
        return text

if __name__ == '__main__':
    # Izveido klases Query objekts
    phoneBook = Query()
    # Tiek ievadīts komandu skaits
    n = int(input())
    # Tiek izveidots saraksts metodes 'find' rezultātu saglabāšanai
    answer = []
    # Tiek apstrādātas visas komandas, kuras tika ievadītas
    for i in range(n):
        query = input().split()
        if query[0] == "add":
            phoneBook.add(int(query[1]),query[2])
        elif query[0] == "del":
            phoneBook.delete(int(query[1]))
        elif query[0] == "find":
            answer.append(phoneBook.find(int(query[1])))
    # Tiek izvadītas visas metodes 'find' atbildes
    for j in range(len(answer)):
        print(answer[j])

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

 # write_responses(process_queries(read_queries()))