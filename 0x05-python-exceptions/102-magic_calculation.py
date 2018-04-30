#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1,3):
            try:
                if(i > a):
                    raise Exception("Too far")
                else:
                    result += (a**b) / i
            except:
                result = a + b
                break
    return(result)

if __name__ =="__main__":
    import dis
    dis.dis(magic_calculation)
