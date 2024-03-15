import multiprocessing


def worker(num, temp_list):
    temp_list.append(num)


def main():
    with multiprocessing.Manager() as manager:
        temp_list = manager.list()
        jobs = []
        for i in range(20):
            p = multiprocessing.Process(target=worker, args=(i, temp_list))
            jobs.append(p)
            p.start()

        for proc in jobs:
            proc.join()

        print(temp_list)


if __name__ == "__main__":
    main()
