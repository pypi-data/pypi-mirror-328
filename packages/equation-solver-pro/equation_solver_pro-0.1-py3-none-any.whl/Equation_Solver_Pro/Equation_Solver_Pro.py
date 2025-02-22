import re  

def equation(e):
    # Handling different parts of the equation
    f = re.findall(r'(.*)[\+\-\*/].*=.*', e)  # Left part before operator
    s = re.findall(r'.*([\+\-\*/]).*=.*', e)  # Operator (+, -, *, /)
    t = re.findall(r'.*[\+\-\*/](.*)=.*', e)  # Right side of the operator
    h = re.findall(r'.*[\+\-\*/].*=(.*)', e)  # The result after "="
    
    try:
        # Handling case where 'x' is on the right side of the operator
        if f[0] != "x":
            # Handle addition, subtraction, multiplication, and division
            if s[0] == "+":
                k = int(h[0])
                l = int(f[0])
                print("x=", k - l)
            elif s[0] == "-":
                p = int(h[0])
                q = int(f[0])
                print("x=", q - p)
            elif s[0] == "*":
                p = int(h[0])
                q = int(f[0])
                print("x=", p / q)  # For integer division
            elif s[0] == "/":
                p = int(h[0])
                q = int(f[0])
                print("x=", q / p)  # For multiplication when 'x' is the divisor

        else:
            # Handle cases where 'x' is on the left side of the operator
            if s[0] == "+":
                j = int(h[0])
                b = int(t[0])
                print("x=", j - b)
            elif s[0] == "-":
                a = int(h[0])
                b = int(t[0])
                print("x=", a + b)
            elif s[0] == "*":
                a = int(h[0])
                b = int(t[0])
                print("x=", a / b)  # For integer division
            elif s[0] == "/":
                a = int(h[0])
                b = int(t[0])
                print("x=", b * a )  

    except Exception:
        print("Please use this format only: x+a=b, x-a=b, x*a=b, x/a=b, a+x=b, a-x=b, a*x=b, or a/x=b")
if __name__ == "__main__":
    # Example usage:
    equation("x+5=10")  
    equation("10-x=5")   
    equation("x*2=8")    
    equation("20/x=5")   
    equation("5+x=23")
    equation("x-10=56")
    equation("5*x=50")
    equation("x/5=11")
