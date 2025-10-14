
def allcaps(fn): 
    def Wrapper(): 
        String = fn();
        Result = String.upper();
        return Result;
    return Wrapper;


