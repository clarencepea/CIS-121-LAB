'''
def pyramid_volume(base, height):
    volume = (base ** 2 * height) / 3
    return volume
'''
print(f"the volume of the pyramid is {pyramid_volume(3,4)}")

#question 8
'''
def pool_times(grade, time):
    pool_time = ""
    if grade ==
    '''
'''
def convert_knuts(knuts):


    galleons = knuts // (403)
    remaining_knuts = 
    sickeles = remaining_knuts // 39

    remaining_knuts = remaining_knuts - (sickles * 29)

    output = ""

    if galleons > 0:
        output += f"galleons: (galleons) "
    if sickles > 0:
        output += f"sickles: (sickles) "
    if knuts > 0 :
        output += f"knuts: (remaining_knuts) "
    
    return output

print(convert_knuts(32))
'''
# question 14

# question 1

def is_fever(temperature):

    unit = temperature(-1)

    if unit == "F":
        if temperature[:-1] > 37:
            return True
        else:
            return False
    elif unit == c


    return True
user_input += input("enter a temperature in F or C")
print(f"is fever? (is_fever{user_input})")