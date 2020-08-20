def add(*args):
    sum = 0
    return sum + args


def sub(*args):
    dif = args
    return dif - args

def mul(*args):
    mul = 1
    return mul * args

if __name__ == '__main__':
    while True:
        print("Please intoduce an operator and two operands:")
        list_op_op = input()
        list_op_op = list_op_op.lower().split('')
        operator = list_op_op[1]
        for i in range(2,len(list_op_op)):
            operands = list_op_op[i]
            if operator == 'add':
                print("x+y ={add(operands)}")
            elif operator == 'sub':
                print(f'x-y = {sub(operands)}')
            elif operator == 'mul':
                printf(f'x*y = {mul(operands)}')
            elif operator == 'end':
                break;
