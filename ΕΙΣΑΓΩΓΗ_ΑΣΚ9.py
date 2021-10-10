ascii_file = open('ascii.txt', 'r')

lines = ascii_file.readlines()
keep = []
for l in lines:
    temp = l.split(" ")
    for item in temp:
        k = ""
        for char in item:
            if char.isalpha():
                k += char
        if len(k) > 0:
            keep.append(k)

keep2 = []
ascii_codes = []
for word in keep:
    i = 0
    temp_code = []
    for each_char in word:
        ascii_code = ord(each_char)
        temp_code.append(ascii_code)
        if ascii_code % 2 == 0 and i == len(word) - 1:
            keep2.append(word)
            for v in temp_code:
                ascii_codes.append(v)
        i += 1

mikr = 256 #Η μεγιστη αριθμητικη τιμη ενος αριθμου στο δεκαδικο συστημα στο ASCII ειναι 255.
meg = -1 #Η ελαχιστη αριθμητικη τιμη ενος αριθμου στο δεκαδικο συστημα στο ASCII ειναι 0.

for value in ascii_codes:
    if value < mikr:
        mikr = value
    if value > meg:
        meg = value

diafora = meg - mikr
print("Η μεγαλύτερη διαφορά είναι:", diafora)