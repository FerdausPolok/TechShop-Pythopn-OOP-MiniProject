print("Hi")
print("Test")

def solve(pos):
    if pos==0:
        return 0
    print(pos)
    return  (solve(pos-1)+pos)+ solve(pos-1)

print(solve(5))