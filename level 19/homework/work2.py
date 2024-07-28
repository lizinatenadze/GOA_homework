#for loop - ის დახმარებით 1 - დან 47 - მდე გამოიტანეთ რიცხვების ჯამი, გამოიყენეთ ( + )ოპერატორი, ხოლო შემდეგ განახორციელეთ იგივე რამ, ( * ) - ოპერატორზე.

total_num = 0
for i in range(1, 48):
    total_num += i

print("რიცხვების ჯამი (1-დან-47-მდე):", total_num)



total_product = 0
for i in range(1, 48):
    total_product *= i

print("რიცხვების გამრავლება (1-დან-47-მდე):", total_product)