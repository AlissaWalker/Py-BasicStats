from alissa_package.stats import zcount, zmean, zmedian, zmode, zvariance, zstddev, zstderr, zcorr

s = [0, 1, 2, 3]
print(zcount(s))

s = [0, 1, 2, 3]
print(zmean(s))

s = [0, 1, 3, 3, 3, 5]
print(zmode(s))

s = [0, 1, 2, 3, 4]
print(zmedian(s))

s = [0, 1, 2, 3, 4]
print(zvariance(s))
# this doesnt round up

s = [0, 1, 2, 3, 4]
print(zstddev(s))

s = [0, 1, 2, 3, 4]
print(zstderr(s))

s = [0, 1, 2, 3, 4]
t = [0, 1, 2, 3, 4]
print(zcorr(s, t))
