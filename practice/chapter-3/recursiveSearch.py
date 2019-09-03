#Recursively search for an array that contains an array

box1 = [1]
box2 = [box1, 3,4]
box3 = [5]
box4 = [box3]

main_box = [box1,box2,box3,box4]

def is_a_key(item,searching):
    if item == searching:
        return True


def is_a_box(item):
    if isinstance(item, list):
        return True
    else:
        return False


def look_for_item(searching,main_box):

    for item in main_box:
        if is_a_box(item):
            look_for_item(searching,item)
        elif is_a_key(item,searching):
            print ('found the key', item)


print(main_box)
look_for_item(1,main_box)

