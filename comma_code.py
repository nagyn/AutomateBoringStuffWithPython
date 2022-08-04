def comma_code(input_list):
    output_string = ""
    for i in input_list:
        if i == input_list[0]:
            output_string = output_string + " " + str(i)
        elif i == input_list[-1]:
            output_string = output_string + " and " + str(i)
        else:
            output_string = output_string + ", " +str(i)
    return output_string



spam = ["apple","banana","tofu","cats"]
print(comma_code(spam))
