inp = open("input06.txt").readline().strip()

inp = [int(_) for _ in inp.split(",")]
buckets = [inp.count(i) for i in range(10)]
for i in range(256):

    bucketsB = [0 for _ in range(10)]
    for k in range(len(buckets)):
        if k == 0:
            bucketsB[6] += buckets[k]
            bucketsB[8] += buckets[k]
        else:
            bucketsB[k - 1] += buckets[k]
    buckets = bucketsB
print(sum(buckets))
