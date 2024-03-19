a = {"홍길동",20,"서울시 마포구 서교동"}
print(a,type(a))
b = {
    "name":"홍길동",
    "age":20,
    "addr":"서울시 마포구 서교동"
}
print(b.items())
print(b.keys())
print(b.values())


# for row in b.items():
#     key,value=row
#     print(key,value)