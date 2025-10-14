
def cacti_number(CactiMap: list):
    if not isinstance(CactiMap, list):
        raise TypeError;
    Count = 0;
    ColLength = len(CactiMap);
    for y in range(0, ColLength): 
        RowLength = len(CactiMap[y]);
        for x in range(0, RowLength): 
            if CactiMap[y][x] == 0: 
                # check plantable slots
                IsPlantable = x - 1 < 0 or CactiMap[y][x - 1] == 0;
                IsPlantable = IsPlantable and (x + 1 >= RowLength or CactiMap[y][x + 1] == 0);
                IsPlantable = IsPlantable and (y - 1 < 0 or CactiMap[y - 1][x] == 0);
                IsPlantable = IsPlantable and (y + 1 >= ColLength or CactiMap[y + 1][x] == 0);
                if IsPlantable:
                    Count += 1;
                    CactiMap[y][x] = 1; # plant it so we don't forget
    return Count;

def Use():

    A = [ [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1] ]

    print(cacti_number(A));

Use();
