N = int(input())
A = set(map(int, input().split()))
N = int(input())
for _ in range(0, N):
    operations = input().split()
    other_set = set(map(int, input().split()))

    if operations[0] == "intersection_update":
        A.intersection_update(other_set)
    if operations[0] == "updated":
        A.update(other_set)
    if operations[0] == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)
    if operations[0] == "difference_update":
        A.difference_update(other_set)

print(sum(A))