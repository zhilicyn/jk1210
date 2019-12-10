from coonfig import BASE_DIR


def read_txt(filename):
    arr = []
    with open(BASE_DIR + "/data/"+filename,"r",encoding="utf-8") as f:
        # data = f.readlines()[1].split(",")
        # arr.append(tuple(data))
        # print(arr)
        # return arr
        for data in f.readlines():
            arr.append(tuple(data.strip().split(",")))
        return arr[1::]


if __name__ == '__main__':
    read_txt("employee_post.txt")