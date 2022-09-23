import crawl

a = input("1:cse\n2:hust\n")
if a == "1":
    res = crawl.get_CSE_notices()
    for i in res:
        print(i + ":" + res[i])
elif a == "2":
    res = crawl.get_HUST_notice()
    for i in res:
        print(i + ":" + res[i])