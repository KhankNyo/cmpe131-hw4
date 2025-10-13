def Partition(Array, Start, Length): 
    

def sort(Array, Start, Length):
    if Length < 2:
        return;
    PartitiionIndex = Partition(Array, Start, Length);
    sort(Array, Start, PartitionIndex);
    sort(Array, Start + PartitionIndex + 1, Length - PartitionIndex - 1);
    return;

def merge_list(a, b): 
    c = a + b;
    sort(c, 0, length(c));

