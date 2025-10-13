
def SortList(List: list) -> None: 
    for i in range(0, len(List)): 
        for k in range(1, len(List) - i):
            if List[k][0] > List[k - 1][0]:
                Tmp = List[k];
                List[k] = List[k - 1];
                List[k - 1] = Tmp;


def reverse_sort_dictionary(Dict: dict) -> list:
    if not isinstance(Dict, dict):
        raise TypeError;
    Result = [];
    for Key in Dict: 
        TupleValue = Dict[Key];
        Result.append( (Key, TupleValue[0]) );
    SortList(Result);
    return Result;


