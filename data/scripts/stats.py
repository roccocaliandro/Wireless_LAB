from statistics import mean, stdev
DIR = "./Wireless_LAB/data/texts/"
FILES = [
    "ethTcpMax", "ethTcpMaxR", 
    "wifiTcpMax", "wifiTcpMaxR", 
    "mixTcpMax", "mixTcpMaxR", 
    "ethUdpMax", "ethUdpMaxR",
    "wifiUdpMax", "wifiUdpMaxR",
    "mixUdpMax", "mixUdpMaxR"
]

def readLine(file) -> float:
    line = file.readline()
    try:
        return float(line[38:42])
    except ValueError:
        return 0
    
def readFile(pathFile) -> list[float]:

    file = open(pathFile + ".txt")
    while (file.readline()[:5] != "[ ID]"):
        continue

    values = []
    for _ in range(20):
        values.append(readLine(file))

    file.close()
    return values
    
def stats(nums: list[float]):
    if not nums:
        return None
    return {
        "count": len(nums),
        "min": min(nums),
        "max": max(nums),
        "mean": mean(nums),
        "dev": stdev(nums) if len(nums) > 1 else 0.0,
    }

def main():

    allStats = []

    for name in FILES:
        pathFile = DIR + name
        values = readFile(pathFile)
        s = stats(values)
        allStats.append(s)
    
    print("Name\t\tAvg\tMax\tMin\tDev")
    for stat in allStats:
        name = FILES[allStats.index(stat)]
        print(f"{name}\t{stat['mean']:.2f}\t{stat['max']:.2f}\t{stat['min']:.2f}\t{stat['dev']:.2f}")



main()

