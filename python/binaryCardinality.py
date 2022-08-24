import re

def cardinalitySort(nums):
    cardinality_binary = {}
    for n in nums:
        b = bin(n)
        c = len(re.findall(r"1",b))
        if c in cardinality_binary.keys():
            cardinality_binary[c].append(n)
        else:
            cardinality_binary[c] = [n]

    result = []

    keys = cardinality_binary.keys()

    for key in sorted(keys,reverse=False):
        for v in sorted(cardinality_binary[key],reverse=False):
            result.append(v)  

    return result

if __name__ == "__main__":
    nums = list()
    with open("input004.txt","r") as input_file:
        nums = list(map(int,input_file.readlines()))

    with open("expectedoutput004.txt","r") as expected_file:
        lines = list(map(int,expected_file.readlines()))
        output = cardinalitySort(nums)
        if len(lines) == len(output):
            print("Have the same size")
        else:
            print(f"Expected output: {len(lines)}\nOutput: {len(output)}")
        for x in range(len(lines)):
            if lines[x] != output[x]:
                print(f"Expected: {lines[x]}\nOutput: {output[x]}")
                break
