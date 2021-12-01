from random import randint, sample

def simulation(n_experiments):
    first_get_car = 0
    second_get_car = 0
    for i in range(n_experiments):
        n_doors = int(input("n_doors:"))
        car = randint(1, n_doors)
        door_list = [i for i in range(1, n_doors+1)]
        sheep_list = del_list(door_list,car)

        first_select = randint(1, n_doors)
        host_select = sample(del_list(sheep_list,first_select),1)[0]
        now_situation = del_list(door_list,host_select)
        second_select = sample(del_list(now_situation,first_select),1)[0]

        if first_select == car:
            first_get_car += 1
            pass
        elif second_select == car:
            second_get_car += 1
            pass
        pass
    first_frequency = first_get_car / n_experiments
    second_frequency = second_get_car / n_experiments
    return first_frequency, second_frequency

def del_list(list,value):
    l = list.copy()
    if value in l:
        l.remove(value)
        pass
    return l

if __name__ == "__main__":
    f, s = simulation(10000)
    print("first_frequency:", f)
    print("second_frequency:", s)