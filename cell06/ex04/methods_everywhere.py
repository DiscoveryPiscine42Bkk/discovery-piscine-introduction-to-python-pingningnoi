import sys

def shrink(s):
    """ตัดสตริงให้เหลือ 8 ตัวอักษรแรกแล้วแสดงผล"""
    print(s[:8])

def enlarge(s):
    """เติมอักขระ 'Z' จนความยาวครบ 8 ตัวแล้วแสดงผล"""
    needed_z = 8 - len(s)

    result = s + ('Z' * needed_z)
    print(result)

parameters = sys.argv[1:]
num_parameters = len(parameters)

if num_parameters < 1:
    print("none")
else:
    for param in parameters:
        length = len(param)
        
        if length > 8:
            shrink(param)
        elif length < 8:
            enlarge(param)
        else:
            print(param)