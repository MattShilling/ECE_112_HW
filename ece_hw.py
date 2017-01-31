# . . . . . . . . . . . . . . . .
#
#   CREATED BY MATT SHILLING
#   ECE 112 Homework Helper
#
# . . . . . . . . . . . . . . . .


import webbrowser
import random

#
# numbered problem sets
#
cv_prob = [1,2,3,4,5,6,7,7,18,19,21,22,25,26,27,28,34]
rn_prob = [1,2,4,5,8,9,10,14]
sol_prob = [1,2,3,10,11,13,14,15,16,17,25,26,28]
kvl_prob = [1,3,4,7,8,9,11,13,15,17,18,20,22]

#
# hw prob url
#
p_ccv = "http://web.engr.oregonstate.edu/~traylor/ece112/hw_prob_pdf/ccv"
p_rn = "http://web.engr.oregonstate.edu/~traylor/ece112/hw_prob_pdf/rn"
p_sol = "http://web.engr.oregonstate.edu/~traylor/ece112/hw_prob_pdf/sol"
p_kvl = "http://web.engr.oregonstate.edu/~traylor/ece112/hw_prob_pdf/kvl"

#
# hw ans url
#
a_ccv = "http://web.engr.oregonstate.edu/~traylor/ece112/hw_ans_pdf/ccv"
a_rn = "http://web.engr.oregonstate.edu/~traylor/ece112/hw_ans_pdf/rn"
a_sol = "http://web.engr.oregonstate.edu/~traylor/ece112/hw_ans_pdf/sol"
a_kvl = "http://web.engr.oregonstate.edu/~traylor/ece112/hw_ans_pdf/kvl"

choice = ''

#
# opens appropriate answer p_num in p_set
# 
def answer(p_set, p_num):
    
    print("Show answer?")
    print("1.) Yes")
    print("2.) No")
    choice = input("Input: ")
    print("Opening Answer...")

    if(choice=='1'):
        if(p_set == '1'):
                url = a_ccv
                url += str(cv_prob[p_num])
                url += ".pdf"
                webbrowser.open(url)

        if(p_set == '2'):
                url = a_rn
                url += str(rn_prob[p_num])
                url += ".pdf"
                webbrowser.open(url)

        if(p_set == '3'):
                url = a_sol
                url += str(sol_prob[p_num])
                url += ".pdf"
                webbrowser.open(url)

        if(p_set == '4'):
                url = a_kvl
                url += str(kvl_prob[p_num])
                url += ".pdf"
                webbrowser.open(url)
        print("")
    else:
        print("OK")
        print("")

#
# lets user choose the category
# opens random question within that category
#
while(choice != '5'):
    
    print("What would you like to practice?")
    print("1.) Charge & Voltage Problems")
    print("2.) Resistor Network Problems")
    print("3.) Sources and Ohm's Law Problems")
    print("4.) KVL Problems")
    print("5.) QUIT")
    choice = input("Choose problem set: ")

    if(choice == '1'):
        print("Opening Random Charge & Voltage Problem...")
        sel = random.randint(0, len(cv_prob)-1)
        print("")
        url = p_ccv
        url += str(cv_prob[sel])
        url += ".txt"
        webbrowser.open(url)
        answer(choice, sel)

    if(choice == '2'):
        print("Opening Random Resistor Network Problem...")
        sel = random.randint(0, len(rn_prob)-1)
        print("")
        url = p_rn
        url += str(rn_prob[sel])
        url += ".pdf"
        webbrowser.open(url)
        answer(choice, sel)

    if(choice == '3'):
        print("Opening Random Sources and Ohm's Law Problem...")
        sel = random.randint(0, len(sol_prob)-1)
        print("")
        url = p_sol
        url += str(sol_prob[sel])
        url += ".pdf"
        webbrowser.open(url)
        answer(choice, sel)

    if(choice == '4'):
        print("Opening Random KVL Problem...")
        sel = random.randint(0, len(kvl_prob)-1)
        print("")
        url = p_kvl
        url += str(kvl_prob[sel])
        url += ".pdf"
        webbrowser.open(url)
        answer(choice, sel)

print("Have a good day!")

