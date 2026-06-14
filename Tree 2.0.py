List = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240]

def add(lists):
    if len(lists) == 0:
        return(0)
    return lists[0] + add(lists[1:])

print(add(List))