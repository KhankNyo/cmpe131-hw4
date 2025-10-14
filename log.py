import time;

def timestamp(Fn):
    def Wrapper(*Args, **KWArgs):
        print(time.ctime());
        Fn(*Args, **KWArgs);
    return Wrapper;

