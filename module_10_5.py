import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(file.readline())
    # print(all_data)


list_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start = time.time()

# # Линейный вызов
# local = [read_info(name) for name in list_names]

# Многопроцессный вызов
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        x = pool.map(read_info, list_names)

end = time.time()

print((time.strftime("%H:%M:%S", time.gmtime(end - start))), 'или так', end - start)