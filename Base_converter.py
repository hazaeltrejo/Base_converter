
import Conversions
def get_data():
    bases=[2,8,10,16]
    number=0
    base_to_work=0
    base_to_convert=0
    
    base_to_work=input("""\n\n select your base
    2-binary\n
    8-octal\n
    10-decimal\n
    16-hexadecimal\n
    """)
    
    number=input("\n introduce your number\n")

    base_to_convert=input("""\n\n select your base to convert
    2-binary\n
    8-octal\n
    10-decimal\n
    16-hexadecimal\n
    """)
    if base_to_work  and base_to_convert not in bases:
        print("sorry, your base is not supported")
        return
    return(base_to_work,base_to_convert)
def get_decimal_numbers(base_to_work,number):
    if base_to_work == 2:
        return Conversions.binary_to_decimal()
    elif base_to_work == 8:
        return Conversions.octal_to_decimal()
    elif base_to_work == 10:
        return int(number)
    elif base_to_work == 16:
        return Conversions.hexadecimal_to_decimal()
def convert(base_to_convert,number):
    if base_to_convert == 2:
        return Conversions.binary_to_decimal()
    elif base_to_convert == 8:
        return Conversions.octal_to_decimal()
    elif base_to_convert == 10:
        return int(number)
    elif base_to_convert == 16:
        return Conversions.hexadecimal_to_decimal()
if __name__ == '__main__':
    data=get_data()
    if data:
        number, base_to_work, base_to_convert = data
        decimal_number=get_decimal_numbers(base_to_work,number)
        result=convert(decimal_number,base_to_convert)
        print(result)

