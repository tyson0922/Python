katok = []
      
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1]=friend

while len(katok)<=10:
    
    data = input("추가할 데이터 ==> ")
    add_data(data)
    print(katok)
