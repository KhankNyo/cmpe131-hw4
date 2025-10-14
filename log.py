import time;

def timestamp(Fn):
    def Wrapper(*Args, **KWArgs):
        print(time.ctime());
        Fn(*Args, **KWArgs);
    return Wrapper;

@timestamp
def __test__():
    print("himom");

# __test__();
