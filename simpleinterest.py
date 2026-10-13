import sys


def simInt(principal, interest, time):
    return (principal * interest * time) / 100


if __name__ == "__main__":
    
    p = int(sys.arg[1])
    i = int(sys.arg[2])
    t = int(sys.arg[3])

   
    print("Simple interest: ", simInt(p, i, t))