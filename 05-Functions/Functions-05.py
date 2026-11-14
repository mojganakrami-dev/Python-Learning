
# آموزش جامع و پیشرفته توابع (Functions) در پایتون

# تعریف تابع: تابع یک بلوک کد سازمان‌یافته، مشخص و قابل‌استفاده مجدد است که یک کار خاص را انجام می‌دهد. تابع فقط زمانی اجرا می‌شود که آن را صدا بزنیم (Call) کنیم

# ساختار پایه یک تابع در پایتون

# برای تعریف تابع در پایتون از کلمه کلیدی def ( مخفف define) استفاده می‌کنیم:
    
# def نام_تابع(ورودی‌ها):
    # بدنه تابع (دستوراتی که باید اجرا شوند)
    # دستورات حتماً باید تو رفتگی (Indentation) داشته باشند
#    return خروجی_تابع  # اختیاری

def say_hello():
    print("سلام! به دنیای توابع پایتون خوش آمدی! 👋")

# صدا زدن (Call کردن) تابع

say_hello()

# تابع دوم
 
def say_hello():
    print("Hello Python!")

say_hello()

#=======================================================

def say_hello():
    print("Hello Python!")
    
# هیچ پیامی چاپ نمی‌شود!
# چون تابع فقط تعریف شده و هنوز فراخوانی نشده است.

# فرض کن می‌خواهیم نام افراد مختلف را دریافت کنیم و به آن‌ها سلام کنیم.

# توابع می‌توانند ورودهایی به نام پارامتر دریافت کنند تا با داده‌های مختلف کار کنند.

def greet_user(name):
    print(f"سلام {name} عزیز! روزت بخیر ☀️")

# صدا زدن تابع با آرگومان‌های مختلف
greet_user("سارا")
greet_user("علی")

# Parameter (پارامتر): متغیری که هنگام تعریف تابع داخل پرانتز قرار می‌گیرد؛ مثل name
# Argument (آرگومان): مقداری که هنگام فراخوانی به تابع می‌دهیم؛ مثل "Ali".

# ================================================================================

# چند ورودی برای یک تابع

def calculate_sum(a, b):
    result = a + b
    print(f"مجموع {a} و {b} برابر است با: {result}")

calculate_sum(10, 20)  # خروجی: مجموع 10 و 20 برابر است با: 30


# فرض کنیم می‌خواهیم میانگین سه عدد را محاسبه کنیم.

def average(a, b, c):
    result = (a + b + c) / 3
    return result

answer = average(15, 18, 20)

print(answer)

# نسخه حرفه‌ای‌تر:

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/ len(numbers)

scores = [18, 16, 20, 14, 19]

result = calculate_average(scores)

print(result)

# فرض کن می‌خواهیم دو عدد را جمع کنیم و سپس حاصل را در عدد دیگری ضرب کنیم.

def add(a, b):
    return a + b

def multiply(number, factor):
    return number * factor

result = multiply(add(10, 20), 5)

print(result)

# - print: برای نمایش اطلاعات به کاربر.

# - return: برای تحویل نتیجه به بخش دیگری از برنامه.

# خیلی وقت‌ها تابع فقط یک کار رو چاپ نمی‌کنه، بلکه یک نتیجه رو تولید می‌کنه که می‌خوایم توی ادامه برنامه‌مون ازش استفاده کنیم. برای این کار از return استفاده می‌کنیم.

# نکته بسیار مهم: دستور return اجرای تابع را متوقف می‌کند و مقدار را برمی‌گرداند. هر کدی بعد از return در آن بلوک نوشته شود، اجرا نخواهد شد!



def test():
    print("Step 1")

    return 100

    print("Step 2")


result = test()

print(result)


# تابع با رسیدن به return متوقف شد.بنایراین Step 2 نمایش داده نمی شود

# در پایتون، اگر تابع به دستور return نرسد یا return بدون مقدار داشته باشد، مقدار None برگردانده می‌شود.

# همچنین تابع می‌تواند چند دستور return در مسیرهای مختلف داشته باشد:
    
def check_number(number):

    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

    else:
        return "Zero"


print(check_number(10))
print(check_number(-5))
print(check_number(0))    


#===================================================================================

# طراحی تابع با منطق واقعی

# فرض کن می‌خواهیم تابعی بسازیم که نمرات دانش‌آموزان را دریافت کند و وضعیت تحصیلی آن‌ها را مشخص کند.

def student_status(scores):
    
    if len(scores) == 0:
        return "No scores available"
    
    average = sum(scores) / len(scores)
    
    if average >= 17:
        return "Excellent"
    
    elif average >= 10:
        return "Passed"
    
    else:
        return "Failed"

student_1 = [18, 19, 17]
student_2 = [12, 14, 15]
student_3 = [5, 8, 9]

print(student_status(student_1))
print(student_status(student_2))
print(student_status(student_3))

#==============================================================================

# برگرداندن چند مقدار از یک تابع
def calculator(numbers):
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum

data = [10, 20,30,40,50]

result = calculator(data)

print(result)

# آرگومان‌های پیش‌فرض (Default Arguments)

# گاهی می‌خوایم یک تابع مقداری پیش‌فرض داشته باشه تا اگر کاربر ورودی نداد، برنامه دچار خطا نشه و از مقدار پیش‌فرض استفاده کنه.

def user_profile(username, role="کاربر عادی"):
    print(f"نام کاربری: {username} | نقش: {role}")

user_profile("reza_99")                  # از نقش پیش‌فرض استفاده می‌کند
user_profile("admin_Sara", "مدیر سیستم")   # مقدار جدید جایگزین می‌شود

# مثال دوم

def greet(name, message="Welcome"):

    return f"{message}, {name}!"


print(greet("Ali"))
print(greet("Sara", "Good morning"))


# فرض کن می‌خواهیم تابعی برای محاسبه قیمت نهایی یک محصول بنویسیم.

def calculate_price(price, tax=10):
    final_price = price + (price * tax / 100)
    return final_price


print(calculate_price(1000))
print(calculate_price(1000, 20))

# مثال کاربردی‌تر:

def calculate_salary(base_salary, bonus=0, tax=10):
    total = base_salary + bonus
    final_salary = total - (total * tax / 100)

    return final_salary


salary = calculate_salary(
    base_salary=30000000,
    bonus=5000000,
    tax=10
)

print(salary)

# نکته حرفه‌ای: پارامترهای دارای مقدار پیش‌فرض باید بعد از پارامترهای بدون مقدار پیش‌فرض قرار بگیرند.



# آرگومان‌های با نام (Keyword Arguments)

# وقتی تابعی چند تا ورودی داره، می‌تونید موقع صدا زدن، صراحتاً بگید کدوم مقدار برای کدوم پارامتره (ترتیب دیگه مهم نیست):

def describe_pet(animal_type, pet_name):
    print(f"من یک {animal_type} دارم که اسمش {pet_name} است.")

# استفاده از Keyword Arguments
describe_pet(pet_name="پشمالو", animal_type="گربه")


def introduce(name, age, city):
    print(name, age, city)



def create_account(username, age, city):

    return {
        "username": username,
        "age": age,
        "city": city
    }


user = create_account(
    city="Tehran",
    username="mohammad",
    age=30
)

print(user)

#===================================================================================
# ترفندهای حرفه‌ای: *args و **kwargs

# گاهی اوقات نمی‌دونی قراره چند تا ورودی به تابع فرستاده بشه. پایتون اینجا برات جادو می‌کنه!

# *args: برای دریافت تعداد نامشخصی از آرگومان‌های معمولی (به صورت Tuple).

# **kwargs: برای دریافت تعداد نامشخصی از آرگومان‌های کلیدی یا همون Key-Value (به صورت Dictionary).

# مثال *args (جمع زدن بی‌نهایت عدد!)

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))          # خروجی:6
print(sum_all(10, 20, 30, 40, 50)) # خروجی: 150

#مثال دوم
def add_numbers(*args):

    print(args)

    return sum(args)


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))
print(add_numbers(1, 2, 3, 4, 5, 6))


# مثال **kwargs (اطلاعات اختیاری کاربر)

def show_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_user_info(name="مریم", age=25, city="تهران", job="برنامه‌نویس")


def show_user(**kwargs):

    print(kwargs)


show_user(
    name="Ali",
    age=25,
    city="Tehran",
    job="Programmer"
)

# مثال واقعی: سیستم ثبت‌نام کاربران

def register_user(**user_data):

    print("User Registration")

    for key, value in user_data.items():
        print(f"{key}: {value}")


register_user(
    username="mohammad",
    email="test@example.com",
    age=30,
    country="Iran"
)

# ترکیب حرفه‌ای هر دو

def build_report(title, *numbers, unit="Rial", **details):
    
    print("Title:", title)
    print("Numbers:", numbers)
    print("Average:", sum(numbers) / len(numbers) if numbers else None)
    print("Unit:", unit)
    print("Details:", details)


build_report(
    "Financial Report",
    100,
    200,
    300,
    unit="Dollar",
    year=2026,
    department="Sales"
)

# ===================================================================

# فضای نام و حافظه توابع

number = 100

def calculate():
    
    number = 50
    
    print(number)
    
calculate() #خروجی می شود 50و 100
# دو متغیر مستقل با یک نام داریم:

    # یکی در فضای نام سراسری.
    # دیگری در فضای نام محلی تابع.
    
# ============================================================================

# First-Class Functions و Higher-Order Functions

# تابع خودش یک شیء است

def square(x):
    return x * 2

my_function = square

print(my_function(5))

#==============================================================================

# تابع به‌عنوان ورودی

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def calculator(a, b, operation):
    return operation(a,b)

print(calculator(2, 4, add))
print(calculator(2, 4, multiply))

# =============================================================================

# تابع به‌عنوان خروجی

def create_multiplier(factor):

    def multiplier(number):

        return number * factor

    return multiplier


double = create_multiplier(2)

triple = create_multiplier(3)

print(double(10))
print(triple(10))
      

# توابع ناشناس یا لامبدا (Lambda Functions)

# توابع lambda توابع کوچک و یک‌خطی هستند که معمولاً اسم ندارند و برای کارهای کوتاه و سریع استفاده میشن:
    
# ساخت یک تابع لامبدا برای به توان ۲ رساندن یک عدد
square = lambda x: x ** 2

print(square(5))  # خروجی: 25

# Map

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 10 , numbers))

print(result)

# Filter

numbers = [10, 15, 20, 25, 30]

result = list(filter(lambda x: x > 20, numbers))
print(result)

# Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)

# برای تبدیل ساده عناصر، map و برای فیلترکردن، filter مناسب‌اند؛ اما گاهی List Comprehension خواناتر است.

# Closure

# Closure یعنی تابع داخلی بتواند به متغیرهای محیط تابع بیرونی دسترسی داشته باشد، حتی وقتی اجرای تابع بیرونی تمام شده است.

def create_counter():

    count = 0

    def counter():

        nonlocal count

        count += 1

        return count

    return counter


counter = create_counter()

print(counter())
print(counter())
print(counter())

# کاربرد Closure:
#- ساخت شمارنده‌ها
#- نگهداری وضعیت
#- ساخت توابع پیکربندی‌شده
#- پیاده‌سازی دکوراتورها

# =============================================================================
 # دکوراتور چیست؟
 
 # دکوراتور تابعی است که قابلیت‌های تابع دیگری را بدون تغییر مستقیم کد اصلی آن توسعه می‌دهد.
 
from functools import wraps


def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Function started")

        result = func(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper


@logger
def add(a, b):

    return a + b


print(add(10, 20)) 

# دکوراتور پارامتردار

from functools import wraps


def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            result = None

            for _ in range(times):

                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):

    print(f"Hello {name}")


greet("Ali")

#==============================================================================

# Recursion و Generator
# تابع بازگشتی

def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# Generator

def generate_numbers(n):

    for i in range(n):

        yield i


for number in generate_numbers(5):

    print(number)
    
# پروژه نهایی؛ سیستم تحلیل داده

# هدف: ساخت سیستم تحلیل نمرات دانش‌آموزان.

from statistics import mean


def validate_scores(scores):

    if not scores:
        raise ValueError("Scores cannot be empty")

    if not all(
        isinstance(score, (int, float))
        and not isinstance(score, bool)
        and 0 <= score <= 20
        for score in scores
    ):
        raise ValueError("Invalid scores")

    return True


def calculate_average(scores):

    validate_scores(scores)

    return mean(scores)


def calculate_status(average):

    if average >= 17:
        return "Excellent"

    elif average >= 10:
        return "Passed"

    return "Failed"


def create_report(name, scores):

    average = calculate_average(scores)

    return {
        "name": name,
        "average": round(average, 2),
        "status": calculate_status(average),
        "highest": max(scores),
        "lowest": min(scores)
    }


students = {
    "Ali": [18, 17, 19],
    "Sara": [20, 19, 18],
    "Reza": [8, 9, 10],
    "Mina": [14, 15, 16]
}


reports = [
    create_report(name, scores)
    for name, scores in students.items()
]


for report in reports:

    print(report)

   
