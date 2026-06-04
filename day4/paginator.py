'''Write a generator for paginated DB results'''
def paginated(records,pageSize):
    '''Return records in small pages using a generator'''
    for i in range(0,len(records),pageSize):
        yield records[i:i+pageSize]
def main():
    '''Display paginated database records'''
    db=["user1","user2","user3","user4","user5","user6","user7","user8","user9","user10"]
    print("paginated results:\n")
    for page_no,page in enumerate(paginated(db,2),start=1):
        print(f"Page {page_no}:{page}")
main()