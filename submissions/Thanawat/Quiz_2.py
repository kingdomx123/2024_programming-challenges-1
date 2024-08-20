import string

def is_pangram(s):
    s = s.lower()
    
    for char in string.ascii_lowercase:
        if char not in s:
            return False
    
    return True

def longest_word(s):
    words = s.split()
    
    longest = max(words, key=len)
    
    return longest

while True:
    input_string = input("กรุณากรอกข้อความของท่าน: ")

    if is_pangram(input_string):
        print("สตริงนี้เป็น Pangram")
        print("คำที่ยาวที่สุดคือ:", longest_word(input_string))
        break
    else:
        print("สตริงนี้ไม่เป็น Pangram")
        print("กรุณากรอกใหม่อีกครั้ง")
