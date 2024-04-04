import numpy as np

data=np.random.randint(0,10,size=(3,3,2))
print("array 3 dimensi:")
print(data)

#ambil data berdasarkan indeks berikut:
result_a = data[0][1][0]
result_b = data[1][1][1]
result_c = data[0][2][1]

print("\nData pada indeks yang diminta:")
print("data[0][1][0] =", result_a)
print("data[1][1][1] =", result_b)
print("data[0][2][1] =", result_c)