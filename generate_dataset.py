# Tyle mamy rekordów w pliku: 115 949 436

# Przykładowy rekord:
# Time, Duration, SrcDevice, DstDevice, Protocol, SrcPort, DstPort, SrcPackets, DstPackets, SrcBytes, DstBytes
# 118843, 64823,  Comp364445, Comp870517, 17, Port68697, Port28366, 12773, 15636, 1072932, 1438512

# Ilość rekordów w datasecie wynikowym
number_of_rows_from_original_dataset = 1000000

# Etap 1: Wybranie mniejszego podzbioru danych

netflow_file = open("netflow_day-02.csv", "r")
subdataset = open("output.csv", "w")

for i in range(0, number_of_rows_from_original_dataset):
    line = netflow_file.readline()
    subdataset.write(line)

netflow_file.close()
subdataset.close()

devices = []

for line in open("output.csv", "r"):
    device = line.split(",")[2]
    if device not in devices:
        devices.append(device)

# Etap 2: Odczytanie istniejących urządzeń z podzbioru danych

devicesFile = open("devices.txt", "w")
for device in devices:
    devicesFile.write(device + "\n")
devicesFile.close()

# Etap 3: Wybranie kilku urządzeń z listy, na których będzie wykonywany atak
number_of_devices_to_scan = 16
devices_to_scan = []
devicesFile = open("devices.txt", "r")
for i in range(0, number_of_devices_to_scan):
    device = devicesFile.readline()
    devices_to_scan.append(device.strip("\n"))
devicesFile.close()

# Etap 4: Utworzenie dodatkowych danych z przeprowadzonego ataku - skanowanie znanych portów

attack_dataset = open("attack.csv", "w")
open_ports = ["20", "21", "22", "23", "80", "443"]

# devices_to_scan = [ "Comp845403", "Comp333799", "Comp004336", "Comp209752",
#                     "Comp158783", "Comp847702", "Comp199697", "Comp672433", 
#                     "Comp240723", "Comp439974", "Comp939617", "Comp953664",
#                      "Comp012705", "Comp250941", "Comp269928","Comp663320",
#                      "Comp431564", "Comp485628", "Comp567269"]

start_time = 118845 # Ustalenie czasu, w którym atak miał miejsce
index = 0 # Numer skanowanego komputera i zarazem modyfikator czasu ataku

for device in devices_to_scan:
    for line in open("ports.txt", "r"):
        port = line.strip(" ")
        port = port.rstrip("\n")
        if port in open_ports:
            attack_dataset.write(str(start_time + index) + ",0,Comp364445," + device + ",6,Port68697,Port" + port + ",2,1,144,72\n")
        else:
            attack_dataset.write(str(start_time + index) + ",0,Comp364445," + device + ",6,Port68697,Port" + port + ",1,1,72,72\n")
    index += 1

attack_dataset.close()

# Etap 5: Połączenie oryginalnych danych z danymi z przeprowadzonego ataku

final_dataset = open("final.csv", "w")
original_dataset = open("output.csv", "r")


for i in range(0,33):
    final_dataset.write(original_dataset.readline())

for line in open("attack.csv", "r"):
    final_dataset.write(line)

for i in range(34,1000000):
    final_dataset.write(original_dataset.readline())

final_dataset.close()
original_dataset.close()




        