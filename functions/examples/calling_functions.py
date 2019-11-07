

def make_small_string(x, name):
    return name + ": " + str(x)

def make_string(a, b, c): 
    result = ""
    
    result += make_small_string(a, "a") + "\n"
    result += make_small_string(b, "b") + "\n"
    result += make_small_string(c, "c") + "\n"

    return result

def do_output(a, b, c, file_path=""):
    output_result = make_string(a, b, c)
    if file_path == "":
        print(output_result)
    else: 
        f = open(file_path, "w")
        f.write(output_result)
        f.close()

do_output(1, 2, 3)
do_output(4, 5, 6, "test.txt")
