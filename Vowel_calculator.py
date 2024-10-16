def vo_con_cal(n):
    vowel=consonent=0
    for i in n:
        if i in ('a','e','i','o','u'):
            vowel+=1
        elif i.isalpha():
            consonent+=1
    print("Number of vowels: ", vowel)
    print("Number of consonent: ", consonent)

a=input("Enter the word: ")
vo_con_cal(a)
