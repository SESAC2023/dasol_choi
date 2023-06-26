#회사에 있는 사람

n = int(input())

workers = {}
for _ in range(n):
  name, status = input().split()
  if status == "enter":
    workers[name] = True
  else:
    del workers[name]

workers = sorted(workers.items(), reverse=True)
for worker in workers:
  print(worker[0])
