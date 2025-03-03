# 15 phương thức liên quan đến chuỗi :
from audioop import reverse

chuoi = 'Python Project'
#1  in hoa tất cả các kí tự trong chuỗi thành chữ viết hoa
print(chuoi.upper())
#2  in hoa tất cả các kí tự trong chuỗi thành chữ viết thường
print(chuoi.lower())
#3 kiểm tra xem chuỗi có phải kiểu chữ in hoa hay không(trả về True nếu đúng, False nếu sai)
print(chuoi.isupper())
#4 kiểm tra xem chuỗi có phải kiểu chữ thường hay không(trả về True nếu đúng, False nếu sai)
print(chuoi.islower())
#5 lấy kí tự ở vị trí trong chuỗi
print(chuoi[1])
#6 in hoa chữ đầu tiên của chuỗi
print(chuoi.capitalize())
#7 đếm kí tự trong chuỗi
print(len(chuoi))
#8 kiểm tra xem kí tự có trong chuỗi hay không
print('Python' in chuoi )
#9 kiểm tra xem kí tự này không có trong chuỗi lâ đúng hay không
print('Python' not in chuoi )
#10 kiểm tra xem tất cả kí tự trong chuỗi có phải đều là số hay không
print(chuoi.isnumeric())
#11 thay thế kí tự trong chuỗi
print(chuoi.replace('Python', 'C++'))
#12 tạo bản sao của chuỗi
print(chuoi[:])
#12.1 lấy các kí tự từ vị trí này đến vị trí kia
print(chuoi[3:6])
#12.2 lấy các kí tự từ vị trí đầu đến vị trí chỉ định
print(chuoi[:7])
#12.3 lấy các kí tự từ vị trí chỉ định đến vị trí cuối
print(chuoi[5:])
#12.4 lấy các kí tự từ vị trí này đến vị trí kia với bước nhảy là step
print(chuoi[1:5:1])
#13 bỏ các kí tự muốn loại bỏ ở 2 đầu của chuỗi:
print(chuoi.strip('Python'))
#14 tách chuỗi:
print(chuoi.split())
#15 viết hoa các chữ cái đầu của các từ trong chuỗi:
print(chuoi.title())


#15 phương thức liên quan tới list :
list = ['java','C','C++','Python' ]
list_1 = [1,2,3,4,5,6]
#1 in ra phần tử muốn in muốn in:
print(list_1[3])
#2 thêm 1 phần tử muốn in vào cuối danh sách:
list.append('loc')
print(list)
#3 thêm nhiều phần tử muốn  in vào cuối danh sách:
list.extend(list_1)
print(list)
#4 xóa phần tử ra khỏi danh sách  :
list.remove('C++')
print(list)
#5 thêm 1 phần tử vào vị trí chỉ định trong list :
list.insert(5,2)
print(list)
#6 xóa toàn bộ các phần tử trong list :
list.clear()
print(list)
#7 xóa 1 phần tử nhất định trong list :
list_1.pop(1)
print(list)
#8 nối list :
list_2 = list_1 + list
print(list_2)
#9 in ra độ dài của list:
print(len(list_1))
#10 trả về bản sao của list:
print(list_1.copy())
#11 đếm số lần xuất hiện của thành phần trong list:
print(list_1.count(3))
#12 trả về vị trí xuất hiện đầu tiên của phần tử có giá trị chỉ định:
print(list_1.index(6))
#13 thêm phần tử vào vị trí muốn thêm trong list :
list.insert(2,'Python')
#14 in ra phần tử nhỏ nhất trong list :
print(min(list_1))
#15 in ra phần tử lớn nhất trong list:
print(max(list_1))
#16 đảo vị trí các phần tử trong list :
list.reverse()



try :
    x = int(input())
    y = int(input())
    result = x/y
except ZeroDivisionError :
    print('Loi khong the chia  cho 0')
else:print(result)


try:
    z = int(input())
except ValueError :
    print('Loi ko phai la so nguyen')





int()
float()
str()
bool()



n = input('nhập một chuỗi các số, cách nhau bởi dấu cách:')
numbers = n.split()
for num in numbers :
    try:
        interger_num = int(num)
        float_num = float(interger_num)
        print(f'số {interger_num} là số nguyên, đã chuyển thành số thục:{float_num}')
    except ValueError :
        print(f'{num} không phải là số nguyên')





x = input('nhập một chuỗi các số, cách nhau bằng dấu cách:')
y = x.split()
float_numbers = []
for i in y:
    try:
        #chuyển dổi từng phần tử thành só nguyên trước , sau đó chuyển thành số thực
        interger_nums = int(i)
        float_nums = float(interger_nums)
        float_numbers.append(float_nums) #lưu vào danh sách số thực
    except ValueError :
        print(f'nếu {i} ko phải là số nguyên,bỏ qua')
print('đã chuyển thành các số thực:',float_numbers)





'ord(c): Lấy mã ASCII của ký tự c.'
'chr(): Chuyển mã ASCII thành ký tự tương ứng.'



