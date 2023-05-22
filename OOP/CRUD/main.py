from views import CreateMixin,ReadMixin,UpdateMixin,DeleteMixin
import json

class Product(CreateMixin,ReadMixin,UpdateMixin,DeleteMixin):
    def save(self):
        with open("data.json","w") as file:
            json.dump(self.objects,file,indent=4)
        return "Saved!"
    
class Comment(CreateMixin,ReadMixin,DeleteMixin):
    pass

smartphones=Product()
print(smartphones.post(title="Redmi Note 8 Pro",description="The Best Phone",qty=10,price=250))
print(smartphones.post(title="Redmi Note 10 Pro",description="Flagman of Redmi",qty=5,price=500))
print(smartphones.post(title="Iphone 14 Pro MAx",description="New cool and super phone",qty=5,price=900))
print(smartphones.post(title="Samsung S22 Ultra",description="The Best Phone for android Phone",qty=3,price=700))
print(smartphones.post(title="Iphone 11 Pro Max",description="Phone of the real man",qty=3,price=600))
print()
print()
print(smartphones.list())
print()
print(smartphones.detail(4))
print(smartphones.detail(15))
print(smartphones.patch(1,title="Redmi Note 10 Pro"))
print(smartphones.list())
print(smartphones.detail(1))
print(smartphones.delete(1))

print(smartphones.save())