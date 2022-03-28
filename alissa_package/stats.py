from typing import List


def zcount(data: List[float]) -> float:
    return float(len(data))


def zmean(data: List[float]) -> float:
    return sum(data) / zcount(data)


def zmode(data: List[float]) -> float:
    return max(set(data), key=data.count)


def zmedian(data: List[float]) -> float:
    data_sorted = sorted(data)
    data_len = len(data)
    index = (data_len - 1) // 2
    if (data_len % 2):
        return data_sorted[index]
    else:
        return float((data_sorted[index] + data_sorted[index + 1]) / 2.0)


def zvariance(data: List[float]) -> float:
    n = zcount(data) - 1
    mean = sum(data) / n
    deviations = []
    for x in data:
        deviations.append(abs(mean -x) ** 2)
    return sum(deviations) / n



def zstddev(data: List[float]) -> float:
    import math
    return float(math.sqrt(zvariance(data)))


def zstderr(data: List[float]) -> float:
    return zstddev(data) / zcount(data)


def zcorr(datax: List[float], datay: List[float]) -> float:

    return cov(datax, datay) / (zstddev(datax) * zstddev(datay))

def readDataFiles(file):
    setA, setB = [], []
    with open(file) as f:
        new_line = f.readline()
        for line in f:
            row = line.split(',')
            setA.append(float(row[0]))
            setB.append(float(row[1]))
    return setA, setB

def readDataSets(files):
    data = {}
    for file in files:
        csvs = readDataFiles(files)
        data[file] = csvs
    return data