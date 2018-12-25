try:
    from direct.showbase.ShowBase import ShowBase
except ImportError:
    print "Failed"

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

app = MyApp()
app.run()
