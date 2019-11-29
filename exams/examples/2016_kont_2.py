DTC = " ,.ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

def load_bin(filename):
    binstring = ""
    try:
        f = open(filename, "r")

        for line in f: 
            binstring += line.strip()
        
        f.close()
    except:
        print("Error: Could not open file", filename)
    return binstring

def bin_to_dec(binary): 
    decimal = 0
    reversed_binary = binary[::-1]
    for i in range(len(reversed_binary)):
        decimal += int(reversed_binary[i]) * 2**i 
    return decimal

def dec_to_char(dec):
    if dec < len(DTC): 
        return DTC[dec]
    else: 
        return ""

def bin_to_txt(binstring): 
    txt = ""
    for i in range(0, len(binstring), 5):
        decimal = bin_to_dec(binstring[i:i+5])
        txt    += dec_to_char(decimal)
    return txt

def main():
    print("Binary-to-text converter")
    b_file      = input("Name of binary file to load from: ")
    b_string    = load_bin(b_file)
    txt         = bin_to_txt(b_string)
    t_file      = input("Name of text file to save to: ")
    try:
        f = open(t_file, "w")

        f.write(txt)

        f.close()

        print(b_file, "has been converted and saved to", t_file)
    except:
        print("Error: Could not write to file", t_file)


main()