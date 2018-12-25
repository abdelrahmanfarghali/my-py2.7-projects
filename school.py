class School:
    item = []
    price = []
    qty = []
class child(School):
    def add_item(self,item,price,qty):
        School.item.append(item)
        School.price.append(price)
        School.qty.append(qty)
