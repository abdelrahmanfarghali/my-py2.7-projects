#import costumer
import urllib2
import datetime

now = datetime.datetime.now()
names = "http://localhost/date/names.html"
prices = "http://localhost/date/prices.html"
payments = "http://localhost/date/payments.html"
change = "http://localhost/date/change.html"

urllib2.urlopen(names)
urllib2.urlopen(prices)
urllib2.urlopen(payments)
urllib2.urlopen(change)
listname = []
listprice = []
listchange = []
listpayed = []
class Costumer:
    id
    price = listprice[id]
    payed = listpayed[id]
    change = listchange[id]
    name = listname[id]
    def show_name(self):
        return name
def Fill(id):
    a = ""
    b = 0
    c = 0
    d = c-b
    return a,b,c,d
def Display(s):
    hito = Costumer(Fill(Display(s)))
    form = {"costumer" : s, "payment" : hito.show_name() , "datetime" : str(now)}
    string = "Costumer {costumer}   {payment}  {datetime}".format(**form)
    print string
    return s
Display(raw_input())
