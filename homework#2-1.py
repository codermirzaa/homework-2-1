# Sade calculator proqrami
# Istifadeciden 2 reqem sorushsun, 3-cude operasiyani sorushsun eger `topla` dirsa toplasin, `cix` dirsa cixsin, `bolme` dirsa bolsun, `vurma` bu isharedirse reqemleri bir birine vursun. neticeni sonda ekrana cap elesin.

num1 = float(input("Birinci rəqəmi daxil edin: "))
num2 = float(input("İkinci rəqəmi daxil edin: "))

operation = input("Əməliyyatı daxil edin (topla, cix, bolme, vurma): ").strip().lower()

if operation == "topla":
    result = num1 + num2
elif operation == "cix":
    result = num1 - num2
elif operation == "bolme":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Sıfıra bölmək mümkün deyil!"
elif operation == "vurma":
    result = num1 * num2
else:
    result = "Düzgün əməliyyat daxil edilməyib!"

print("Nəticə:", result)
