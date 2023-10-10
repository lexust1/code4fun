# Сдать решение задачи A-Грузовик

# Вы - водитель грузовика с открытым кузовом. В кузове два груза:
# пианино и холодильник. Пианино необходимо доставить в институт,
# холодильник в общежитие. В каждое из этих мест ведет отдельная дорога,
# начинающаяся от перекрестка, на котором Вы стоите, других дорог в
# мире нет. Известно, что по дороге в институт есть мост, на котором
# действует ограничение максимальной допустимой массы автомобиля с
# грузом, а по дороге в общежитие есть туннель с ограничением высоты.
# Требуется определить, возможно ли доставить грузы или нет (разумеется,
# сгружать их, где попало, Вам запрещено).
#
# Формат входных данных
# На вход подается 8 чисел натуральных чисел (каждое < 100), каждое в
# новой строке, в следующем порядке: вес грузовика без груза, высота
# платформы кузова (на которой стоят грузы), вес пианино, высота
# пианино, вес холодильника, высота холодильника, максимальный
# допустимый вес на мосту, максимальная допустимая высота в туннеле
#
# Примечание: пианино и холодильник заведомо возвышаются над кабиной
# грузовика, т.е. высоту кабины можно в расчет не принимать.
#
# Формат выходных данных
# Вывести YES если доставка возможна и NO в противном случае.
#
# Примеры
# Ввод	Вывод
# 1       NO
# 1
# 5
# 10
# 5
# 10
# 10
# 10
#
#
# Ввод	Вывод
# 1       YES
# 1
# 5
# 10
# 5
# 10
# 11
# 11
def create_input_data():
    arr = []
    print(
        "Input the following parameters:\n"
        "- truck weight,\n"
        "- platform height,\n"
        "- piano weight,\n"
        "- piano height,\n"
        "- refrigerator weight,\n"
        "- refrigerator height,\n"
        "- bridge MAW,\n"
        "- tunnel MAH.\n"
        "Use Whitespace + Enter to quit."
    )
    while True:
        inp = input()
        if inp == ' ':
            break
        arr.append(int(inp))
    return arr


def estimate_logistics(arr):
    # The truck weight.
    truck_weight = arr[0]
    # The platform height.
    platform_height = arr[1]
    # The piano weight.
    piano_weight = arr[2]
    # The piano height.
    piano_height = arr[3]
    # The refrigerator weight.
    fridge_weight = arr[4]
    # The refrigerator height.
    fridge_height = arr[5]
    # The bridge MAW.
    bridge_maw = arr[6]
    # The tunnel MAH.
    tunnel_mah = arr[7]
    # Temp variables to simplify conditions.
    total_weight = truck_weight + piano_weight + fridge_weight
    truck_and_piano_height = platform_height + piano_height
    truck_and_fridge_height = platform_height + fridge_height
    # Any road is possible. No problems with weight and height.
    if (total_weight < bridge_maw and
        max(truck_and_piano_height, truck_and_fridge_height) < tunnel_mah):
        return "YES"
    # The problem with weight.
    # The road to the dormitory and deliver the fridge.
    # Then the road to the university and deliver the piano.
    elif (total_weight > bridge_maw and
          total_weight - fridge_weight < bridge_maw and
          max(truck_and_piano_height, truck_and_fridge_height) < tunnel_mah):
        return "YES"
    # The problem with height.
    # The road to the university and deliver the piano.
    # Then the road the to dormitory and deliver the fridge.
    elif (total_weight < bridge_maw and
          fridge_height < tunnel_mah):
        return "YES"
    # The problems with weight and height. It is impossible to deliver.
    else:
        return "NO"


def main():
    # print(create_input_data())
    arr = create_input_data()
    print(estimate_logistics(arr))


if __name__ == "__main__":
    main()
