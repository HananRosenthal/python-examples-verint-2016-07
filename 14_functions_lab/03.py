
def tens_digit_sum(*nums):
    list=[]
    for number in nums:
        if type(number) is int:
            list.append(number)
    return  sum( [ (int(x/10)%10) for x in list] )

print(tens_digit_sum(140,220,1120))

