
def allcaps(Fn): 
    def Wrapper(): 
        String = Fn();
        Result = String.upper();
        return Result;
    return Wrapper;

#
## with args: 
#def allcaps(Fn): 
#   def Wrapper(*Args, **KWArgs): # '*' is arg by pos, '**' is args by name, or 'KeyWordArgs'
#       String = Fn(*Args, **KWArgs);
#       Result = String.upper();
#       return Result;
#   return Wrapper;
#

