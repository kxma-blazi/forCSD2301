## 2. เขียนโปรแกรมหาจำนวนที่หารด้วย 5 ลงตัวที่อยู่ระหว่าง 1 และ 10000 มีกี่จำนวน 
a = 0

  for i in range(1, 10001):
    if i % 5 == 0:
      a += 1
print("จำนวนที่หารด้วย 5 ลงตัวระหว่าง 1 ถึง 10000 มี", a,"จำนวน")
