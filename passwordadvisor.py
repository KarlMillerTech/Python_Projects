import re

def CheckPassword(password):
    strength = ['Blank','Very Weak','Weak','Medium','Strong','Very Strong']
    score = 1

    if len(password) < 1:
        return strength[0]
    if len(password) < 4:
        return strength[1]

    if len(password) >= 8:
        score = score + 1
    if len(password) >= 10:
        score = score + 1

    if re.search('\d+', password):
        score = score + 1
    if re.search('[a-z]', password) and re.search('[A-Z]', password):
        score = score + 1
    if re.search('.,[,!,@,#,$,%,^,&,*,(,),_,~,-,]', password):
        score = score + 1

    return strength[score]

def main():

    user_input = raw_input("Check: ")

    while(user_input != 'quit'):
        print CheckPassword(user_input)
        user_input = raw_input("Check: ")

if __name__ == "__main__":
    main()
