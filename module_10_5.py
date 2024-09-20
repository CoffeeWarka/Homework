import datetime
import multiprocessing
def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        for readline in f:
            all_data.append(readline)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.datetime.now()
# for i in filenames:
#     read_info(i)
# end = datetime.datetime.now()
# print(end-start)
if __name__ == '__main__':

    with multiprocessing.Pool(processes=4) as pool:
        start_multi = datetime.datetime.now()
        pool.map(read_info, filenames)
    end_multi = datetime.datetime.now()
    print(end_multi - start_multi)