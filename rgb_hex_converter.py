"""
Codecademy < Learn Python 
10 Advanced Topics in Python
=====================================================
RGB-HEX Converter
=====================================================

The program should do the following:
    1. Prompt the user for the type of conversion they want
       - method to convert RGB to HEX
       - method to convert HEX to RGB
       - method that starts the prompt cycle
    2. Ask the user to input the RGB or HEX value
    3. Use Bitwise operators and shifting in order to convert the value
    4. Print the converted value to the user
"""

def rgb_hex():
    invalid_msg = "Invalid value entered."
    red = int(raw_input("Enter value for Red: "))
    if (red < 0 or red > 255):
        print invalid_msg
        return 
    green = int(raw_input("Enter value for Green: "))
    if (green < 0 or green > 255):
        print invalid_msg
        return 
    blue = int(raw_input("Enter value for Blue: "))
    if (blue < 0 or blue > 255):
        print invalid_msg
        return 
  
    val = (red << 16) + (green << 8) + blue
    print (hex(val)[2:]).upper()
  
def hex_rgb():
    hex_val = raw_input("Enter the hex value: ")
    if (len(hex_val) != 6):
        print "Invalid value entered. "
    else:
        hex_val = int(hex_val,16)
  
    two_hex_digits = 2**8
  
    blue = hex_val % two_hex_digits
    hex_val >>= 8
    green = hex_val % two_hex_digits
    hex_val >>= 8
    red = hex_val % two_hex_digits
  
    print "Red: %d, Green: %d, Blue: %d" % (red, green, blue)
  
def convert():
    while (True):
        option = raw_input("Enter '1' to convert RGB to HEX. Enter '2' to convert HEX to RGB. Enter 'X' to Exit: ")
    
        if (option == '1'):
            print "RGB to Hex..."
            rgb_hex()
        elif (option == '2'):
            print "Hex to RGB..."
            hex_rgb()
        elif (option == 'X' or option == 'x'):
            break
        else:
            print "Error"




def main():
    convert()

if __name__=="__main__":
    main()
