import operator


def get_hashmap_value_percentage(hash_map, records_quantity):
    for key in hash_map:
        hash_map[key] = (hash_map[key] / records_quantity) * 100

    return hash_map


def generate_file_with_dst_port_statistics(input_file):
    ports_hash_map, records_quantity = count_dst_port_quantity(input_file)
    ports_hash_map_percentage = get_hashmap_value_percentage(ports_hash_map, records_quantity)

    ports_hash_map_percentage_sorted_descending = dict( sorted(ports_hash_map_percentage.items(), key=operator.itemgetter(1), reverse=True))
    
    statistics_file = open("Analiza portow docelowych.txt", "w")
    
    for key in ports_hash_map_percentage_sorted_descending:
        statistics_file.write("Procentowy udzial w ruchu sieciowych dla portu " + str(key) + " : " + str(ports_hash_map_percentage_sorted_descending[key]) + " %\n")

    statistics_file.close()



def count_dst_port_quantity(input_file):
    ports_hash_map = {}
    records_quantity = 0

    input_file.seek(0,0) # ustawienie wskaznika pliku na jego poczatek

    for line in input_file:
        record_array = line.split(",")
        dst_port = record_array[6]
        records_quantity += 1
        if not dst_port.isnumeric():
            dst_port = dst_port[4:]

        if dst_port in ports_hash_map.keys():
            ports_hash_map[dst_port] += 1
        else:
            ports_hash_map[dst_port] = 1

    return ports_hash_map, records_quantity



def generate_file_with_src_device_statistics(input_file):
    src_device_hash_map, records_quantity = count_src_device_quantity(input_file)
    src_device_hash_map_percentage = get_hashmap_value_percentage(src_device_hash_map, records_quantity)

    src_device_hash_map_percentage_sorted_descending = dict( sorted(src_device_hash_map_percentage.items(), key=operator.itemgetter(1), reverse=True))
    
    statistics_file = open("Analiza urzadzen zrodlowych.txt", "w")
    
    for key in src_device_hash_map_percentage_sorted_descending:
        statistics_file.write("Procentowy udzial w ruchu sieciowych dla urzadzenia " + str(key) + " : " + str(src_device_hash_map_percentage_sorted_descending[key]) + " %\n")

    statistics_file.close()



def count_src_device_quantity(input_file):
    src_device_hash_map = {}
    records_quantity = 0

    input_file.seek(0,0) # ustawienie wskaznika pliku na jego poczatek

    for line in input_file:
        record_array = line.split(",")
        src_device = record_array[2]
        records_quantity += 1

        if src_device in src_device_hash_map.keys():
            src_device_hash_map[src_device] += 1
        else:
            src_device_hash_map[src_device] = 1

    return src_device_hash_map, records_quantity



def generate_file_with_dst_device_statistics(input_file):
    dst_device_hash_map, records_quantity = count_dst_device_quantity(input_file)
    dst_device_hash_map_percentage = get_hashmap_value_percentage(dst_device_hash_map, records_quantity)

    dst_device_hash_map_percentage_sorted_descending = dict( sorted(dst_device_hash_map_percentage.items(), key=operator.itemgetter(1), reverse=True))
    
    statistics_file = open("Analiza urzadzen docelowych.txt", "w")
    
    for key in dst_device_hash_map_percentage_sorted_descending:
        statistics_file.write("Procentowy udzial w ruchu sieciowych dla urzadzenia " + str(key) + " : " + str(dst_device_hash_map_percentage_sorted_descending[key]) + " %\n")

    statistics_file.close()



def count_dst_device_quantity(input_file):
    dst_device_hash_map = {}
    records_quantity = 0

    input_file.seek(0,0) # ustawienie wskaznika pliku na jego poczatek

    for line in input_file:
        record_array = line.split(",")
        dst_device = record_array[3]
        records_quantity += 1

        if dst_device in dst_device_hash_map.keys():
            dst_device_hash_map[dst_device] += 1
        else:
            dst_device_hash_map[dst_device] = 1

    return dst_device_hash_map, records_quantity



def generate_file_with_number_of_src_devices_connected_to_individual_dst_divices(input_file):
    dst_device_hash_map = {}
    input_file.seek(0,0)

    for line in input_file:
        record_array = line.split(",")
        src_device = record_array[2]
        dst_device = record_array[3]

        if dst_device in dst_device_hash_map.keys():
            if src_device not in dst_device_hash_map[dst_device]:
                dst_device_hash_map[dst_device].append(src_device)
        else:
            src_device_list = [src_device]
            dst_device_hash_map[dst_device] = src_device_list

    dst_device_hash_map_quantities = dst_device_hash_map

    statistics_file = open("Liczba polaczen z hostami.txt", "w")

    for key in dst_device_hash_map_quantities:
        dst_device_hash_map_quantities[key] = len(dst_device_hash_map_quantities[key])

    dst_device_hash_map_quantities_sorted_descending = dict( sorted(dst_device_hash_map_quantities.items(), key=operator.itemgetter(1), reverse=True))

    for key in dst_device_hash_map_quantities_sorted_descending:
        statistics_file.write("Host " + key + " otrzymal pakiety od " + str(dst_device_hash_map_quantities_sorted_descending[key]) + " urzadzen.\n")


    statistics_file.close()



def main():

    input_file = open("attack.txt", "r")

    #generate_file_with_dst_port_statistics(input_file)
    #generate_file_with_src_device_statistics(input_file)
    #generate_file_with_dst_device_statistics(input_file)
    generate_file_with_number_of_src_devices_connected_to_individual_dst_divices(input_file)


    input_file.close()

    return 0



if __name__ == "__main__":
    main()

