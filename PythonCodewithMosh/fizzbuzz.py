def fizzbuzz(value):
    # if value % 3 == 0 and value % 5:
    #     result="FizzBuzz"
    # elif value % 5 == 0 :
    #     result="Buzz"
    # elif value% 3 == 0 :
    #     result="Fizz"
    # else :
    #     result=value

    return "FizzBuzz" if value % 3 == 0 and value % 5 == 0 else "Buzz" if value % 5 == 0 else "Fizz" if value % 3 == 0 else value


print(fizzbuzz(int(input("Enter a number : "))))

# stack
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.pop()
print(browsing_session)
if browsing_session:
    print(browsing_session[-1])
