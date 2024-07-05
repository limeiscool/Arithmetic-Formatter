def get_answer_in_str(num1, num2, op):
    if op == "+":
        return str(int(num1)+int(num2))
    else:
        return str(int(num1)-int(num2))

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    else:
        top_line=[]
        bottom_line=[]
        dash_line=[]
        answer_line=[]
        for str in problems:
            str_arr = str.split(' ')
            num1 = str_arr[0]
            op = str_arr[1]
            num2 = str_arr[2]
            if op != "-" and op != '+':
                return "Error: Operator must be '-' or '+'"
            else:
                if num1.isdigit() != True or num2.isdigit() != True:
                    return 'Error: Numbers must only contain digits.'
                else:
                    num1_length = len(num1)
                    num2_length = len(num2)
                    if num1_length > 4 or num2_length > 4:
                        return 'Error: Numbers cannot be more than four digits.'
                    else:
                        back_spacer="    "
                        add_to_top="  "
                        add_to_bot=op+" "
                        add_to_dashline=""
                        add_to_answerline=""
                        answer=get_answer_in_str(num1, num2, op)
                        if num1_length > num2_length:
                            space_add_bot = num1_length - num2_length
                            for x in range(space_add_bot):
                                add_to_bot+=" "
                            add_to_bot+=num2
                            add_to_top+=num1
                            for x in add_to_bot:
                                add_to_dashline+="-"
                            for x in range(len(add_to_dashline)-len(answer)):
                                add_to_answerline+=" "
                            add_to_answerline+=answer
                            top_line.append(add_to_top)
                            bottom_line.append(add_to_bot)
                            dash_line.append(add_to_dashline)
                            answer_line.append(add_to_answerline)
                        elif num2_length > num1_length:
                            space_add_top = num2_length - num1_length
                            for x in range(space_add_top):
                                add_to_top+=" "
                            add_to_top+=num1
                            
                            add_to_bot+=num2
                            for x in add_to_bot:
                                add_to_dashline+="-"
                            for x in range(len(add_to_dashline)-len(answer)):
                                add_to_answerline+=" "
                            add_to_answerline+=answer
                            top_line.append(add_to_top)
                            bottom_line.append(add_to_bot)
                            dash_line.append(add_to_dashline)
                            answer_line.append(add_to_answerline)
                        else:
                            add_to_top+=num1
                            add_to_bot+=num2
                            for x in add_to_bot:
                                add_to_dashline+="-"
                            for x in range(len(add_to_dashline)-len(answer)):
                                add_to_answerline+=" "
                            add_to_answerline+=answer
                            top_line.append(add_to_top)
                            bottom_line.append(add_to_bot)
                            dash_line.append(add_to_dashline)
                            answer_line.append(add_to_answerline)
        answer_arr=[]
        answer=""
        if show_answers == True:
            for each in [top_line, bottom_line, dash_line, answer_line]:
                answer_arr.append("    ".join(each))
            answer+="\n".join(answer_arr)
        else:
            for each in [top_line, bottom_line, dash_line]:
                answer_arr.append("    ".join(each))
            answer+="\n".join(answer_arr)
    return answer

            

                    
            



print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
