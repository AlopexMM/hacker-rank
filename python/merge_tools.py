def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string)+1,k):
        seg = string[i:k+i]
        if seg != "":
            s = ""
            for c in seg:
                if c not in s:
                    s += c
            print(s)

if __name__ == "__main__":
    merge_the_tools("AABCAAADA", 3)