# یادگیری حلقه ها در پایتون

for i in range(1, 6):
    print(i)
    
# ساختار حلقه for

# for variable in sequence:
#   instructions

# for :  شروع کننده حلثه
# variable : متغیری که در هر مرحله مقدار جدید می‌گیرد
# in : یعنی از داخل مجموعه
# sequence : مجموعه‌ای از داده‌ها
# instruction : دستورات داخل حلقه: کارهایی که در هر تکرار انجام می‌شوند

for name in ["Ali", "Sara", "Reza"]:
    print(name)
#==============================================================================
# تابع range؛ یکی از مهم‌ترین ابزارهای حلقه

# تابع range() برای تولید دنباله‌ای از اعداد استفاده می‌شود.

# سه شکل مهم دارد:

    #حالت اول: range(stop)
    
for i in range(5):
    print(i)

# حالت دوم: range(start, stop)

for i in range(2, 7):
    print(i)
    
# حالت سوم: range(start, stop, step)

for i in range(2, 11, 2):
    print(i)
    
for i in range(10, 0, -1):
    print(i)
    
# نکته کلیدی: مقدار شروع وارد دنباله می‌شود، اما مقدار پایان وارد نمی‌شود.

#================================================================================

# استفاده از حلقه for روی انواع داده‌ها

# یکی از قابلیت‌های قدرتمند پایتون این است که حلقه for فقط برای اعداد نیست.

# می‌توانیم روی رشته، لیست، تاپل، مجموعه و دیکشنری حلقه اجرا کنیم.

# الف) حلقه روی رشته (String)

word = "Python"

for letter in word:
    print(letter)
    
# شمارش تعداد حروف a در یک متن.

text = "banana"

count = 0

for letter in text:
    if letter == "a":
        count += 1

print(count)

# ب) حلقه روی لیست (List)

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
    

# مثال کاربردی: محاسبه مجموع اعداد لیست.

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print(total)

# ج) حلقه روی تاپل (Tuple)

colors = ("red", "green", "blue")

for color in colors:
    print(color)
    
# د) حلقه روی مجموعه (Set)

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)
    
# هـ) حلقه روی دیکشنری (Dictionary)

student = {
    "name": "Ali",
    "age": 20,
    "score": 18
}

for key in student:
    print(key)
    
for value in student.values():
    print(value)
    
for (key,value) in student.items():
    print(key,value)

#========================================================================

# دستور enumerate؛ شماره‌گذاری اعضای یک مجموعه

# گاهی می‌خواهیم هم به عضو لیست دسترسی داشته باشیم و هم شماره آن را بدانیم.


students = ["Ali", "Sara", "Reza"]

for index,name in enumerate(students):
    print(index,name)
    
# اگر بخواهیم شماره‌گذاری از ۱ شروع شود:
    
for index, name in enumerate(students, start=1):
    print(index, name)
    
# دستور zip؛ پیمایش هم‌زمان چند لیست

names = ["Ali", "Sara", "Reza"]

scores = [18, 20, 15]

for name,score in zip(names,scores):
    print(name,score)
    
# نکته پیشرفته: zip() به‌طور معمول تا پایان کوتاه‌ترین مجموعه پیش می‌رود.

a = [1, 2, 3, 4]
b = ["A", "B"]

for x, y in zip(a, b):
    print(x, y)
    
#===============================================================================

# -===========================حلقهwhile======================

# گاهی تعداد دفعات تکرار را از ابتدا نمی‌دانیم.

#مثلاً:
# تا زمانی که رمز عبور درست وارد نشده، دوباره درخواست کن
# تا زمانی که موجودی حساب مثبت است، عملیات برداشت را انجام بده
# تا زمانی که کاربر گزینه خروج را انتخاب نکرده، برنامه ادامه پیدا کند.

# ساختار:   
     
# while condition:
#  instructions

# تا زمانی که شرط درست (True) است، دستورات داخل حلقه را اجرا کن

number = 1

while number <= 5:
    print(number)
    number += 1
    
# حلقه while با شرط‌های پیچیده‌تر

age = 15

while age < 18:
    print("You are under 18")
    age += 1

print("You are an adult")

#==================================================================================

# دستورات کنترلی حلقه‌ها

# دستور break؛ خروج فوری از حلقه

# فرض کن می‌خواهیم اعداد ۱ تا ۱۰ را چاپ کنیم، اما به محض رسیدن به عدد ۵ حلقه تمام شود.

for i in range(1, 11):

    if i == 5:
        break

    print(i)
    
# دستور continue؛ رد کردن یک تکرار

# فرض کن می‌خواهیم اعداد ۱ تا ۱۰ را چاپ کنیم، اما عدد ۵ نمایش داده نشود.

for i in range(1, 11):

    if i == 5:
        continue

    print(i)
    
# دستور pass؛ فعلاً هیچ کاری نکن!

# دستور pass زمانی استفاده می‌شود که بخواهیم ساختار کد را بنویسیم، اما هنوز نمی‌خواهیم دستوری در آن قرار دهیم.

if age >= 18:
    pass
else:
    print("Under 18")



# دستور else در حلقه‌ها؛ نکته‌ای که خیلی‌ها نمی‌دانند!

# می‌توانیم بعد از حلقه for یا while از else استفاده کنیم.

for i in range(5):
    print(i)
else:
    print("Loop finished")
    

for i in range(5):

    if i == 3:
        break

    print(i)

else:
    print("Loop finished")
    

# بررسی وجود یک عدد در لیست. 

numbers = [10, 20, 30, 40]

target = 50

for number in numbers:

    if number == target:
        print("Found")
        break

else:
    print("Not Found")
#===============================================================================
    
# حلقه تو در تو یعنی قرار دادن یک حلقه داخل حلقه دیگر

for i in range(3):

    for j in range(2):

        print(i, j)
        
# ساخت جدول ضرب

for i in range(1,6):
    
    for j in range(1,6):
        
        print(i*j , end="\t")
        
    print()
    
# end="\t" باعث می‌شود بعد از چاپ هر عدد، به‌جای رفتن به خط بعد، فاصله تب ایجاد شود.

# print() خالی بعد از حلقه داخلی باعث رفتن به خط بعد می‌شود.

#ساخت الگوی ستاره‌ای

for i in range(1,6):
    
    for j in range(i):
        
        print("*", end = "")
    
    print()

# محاسبه مجموع، میانگین، بیشترین و کمترین مقدار

scores = [15, 18, 20, 12, 17, 19]

# محاسبه مجموع:
    
total = 0

for score1 in scores:
     total =+ score1

print(total)

# محاسبه میانگین:
total = 0

for score in scores:
    total += score

average = total / len(scores)

print(average)
    
# پیدا کردن بزرگ‌ترین عدد با حلقه:
    
scores = [15, 18, 20, 12, 17, 19]

# تعیین مقدار اولیه بزرگ‌ترین عدد
maximum = scores[0]

for score in scores:
    if score > maximum:
        maximum = score

print(maximum)

# پیدا کردن کوچک‌ترین عدد:

minimum = scores[0]

for score in scores:
    if score < minimum:
        minimum = score

print(minimum)

# شمارش اعداد زوج و فرد

numbers = [10, 15, 22, 31, 40, 55, 60]

even_count = 0
odd_count = 0

for number in numbers:

    if number % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)

#=======================================================

# جست‌وجو در لیست با حلقه

numbers = [10, 20, 30, 40, 50]

target = 30

found = False

for number in numbers:

    if number == target:
        found = True
        break

if found:
    print("Number found")

else:
    print("Number not found")
    
# در این برنامه از متغیر بولی (Boolean) استفاده کردیم.

# متغیر found دو حالت دارد:
    
# True: عدد پیدا شده است

# False: عدد پیدا نشده است
#===================================================================

# استفاده از حلقه برای تغییر اعضای لیست 

numbers = [1, 2, 3, 4]

for number in numbers:
    number = number * 2

print(numbers)

# خروجی :   [1, 2, 3, 4] 

# چرا لیست تغییر نکرد؟

# چون در این مثال متغیر number فقط مقدار عضو را دریافت کرده و با تغییر آن، عضو اصلی لیست تغییر نکرده است. 

numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

# روش حرفه‌ای‌تر با enumerate:

numbers = [1, 2, 3, 4]

for index, number in enumerate(numbers):
    numbers[index] = number * 2

print(numbers)

# روش List Comprehension

numbers = [1, 2, 3, 4]

numbers = [number * 2 for number in numbers]

print(numbers)

#=======================================================================

# List Comprehension؛ روش حرفه‌ای و کوتاه‌نویسی

# فرض کن می‌خواهیم اعداد ۱ تا ۱۰ را داخل یک لیست قرار دهیم.
 
#   روش معمولی:
    
numbers = []

for i in range(1,11):
    numbers.append(i)
    
print(numbers)

# روش کوتاه‌تر:
    
numbers = [i for i in range(1,11)]

print(numbers)

# ساختار کلی:
    
# new_list = [expression for item in iterable]

# یعنی:
    
# یک لیست جدید بساز.
# اعضای مجموعه را یکی‌یکی دریافت کن.
# روی هر عضو عملیات موردنظر را انجام بده.
# نتیجه را داخل لیست جدید قرار بده.

squares = [i**2 for i in range(1, 6)]

print(squares)

# فقط اعداد زوج

even_number = [i for i in range(1,11) if i % 2==0 ]
print(even_number)

#تبدیل نام‌ها به حروف بزرگ

names = ["ali", "sara", "reza"]

upper_name = [name.upper() for name in names]

print(upper_name)

#========================================================

#استفاده از شرط else در Comprehension

numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if number % 2 == 0 else "Odd"
     for number in numbers
    ]

print(result)

#===========================================================

# حلقه‌های پیشرفته و کاربردی

# حلقه با چند شرط

# مثال: پیدا کردن اعدادی که هم زوج هستند و هم بزرگ‌تر از ۱۰.

numbers = [5, 12, 15, 20, 25, 30]

for number in numbers:
    
    if number > 10 and number % 2 == 0:
        
        print(number)
        
# حلقه روی لیست‌های چندبعدی

scores = [
    [18, 19, 20],
    [15, 16, 17],
    [20, 20, 19]
]

# هر لیست داخلی، نمرات یک دانش‌آموز را نشان می‌دهد.

# برای پیمایش تمام نمرات:
    
for row in scores:

    for score in row:

        print(score)
        
# حالا میانگین نمرات هر دانش‌آموز:
    
for row in scores:

    average = sum(row) / len(row)

    print(average)
    
# حلقه while برای دریافت رمز عبور

password = ""

while password != "1234":

    password = input("Enter password: ")

print("Access granted")

# ساخت ماشین‌حساب ساده با حلقه
while True:

    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":

        if num2 == 0:
            print("Cannot divide by zero")

        else:
            print("Result:", num1 / num2)
    
 







    
    


    
