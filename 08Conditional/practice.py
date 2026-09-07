Gender = input("Enter your gender (Male/Female/Other): ")
#insted of using "or" we can use .lower() method to convert the input to lowercase and use .strip() method to remove any leading or trailing whitespace from the input.
if Gender == "Male" or Gender == "male" or Gender == "MALE":
    print("You are a male")
    Job = input("Are you employed? (Yes/No): ")
    if Job == "Yes" or Job == "yes" or Job == "YES":
        print("You are employed")
        Prefernce = input("Are you a engineer or doctor? (Engineer/Doctor): ")
        if Prefernce == "Engineer" or Prefernce == "engineer" or Prefernce == "ENGINEER":
            print("You are lying, you are unemployed")
        if Prefernce == "Doctor" or Prefernce == "doctor" or Prefernce == "DOCTOR":
            print("You are a successful doctor, now go and steal money from poor people")    
    if Job == "No" or Job == "no" or Job == "NO":
        print("You are an engineer")


if Gender == "Female" or Gender == "female" or Gender == "FEMALE":
    print("You are a female")
    Job = input("Are you employed? (Yes/No): ")
    if Job == "Yes" or Job == "yes" or Job == "YES":
        print("You are a Housewife")
        Prefernce = input("Do you prefer rice or Roti? (Rice/Roti): ")
        if Prefernce == "Rice" or Prefernce == "rice" or Prefernce == "RICE":
            print("Sasural jake roti banana sikho")
        if Prefernce == "Roti" or Prefernce == "roti" or Prefernce == "ROTI":
            print("You are a good cook and never take alimony from your husband")
    if Job == "No" or Job == "no" or Job == "NO":
        print("You need to marry")
        prefer = input("Do you want to marry a rich or poor person? (Rich/Poor): ")
        if prefer == "Rich" or prefer == "rich" or prefer == "RICH":
            print("You are a Gold Digger")
        if prefer == "Poor" or prefer == "poor" or prefer == "POOR":
            print("You are a good person")    


if Gender == "Other" or Gender == "other" or Gender == "OTHER":
    print("Congratulations! You are eligible to go to USA.")
    travel = input("Do you want to travel to USA? (Yes/No): ")
    if travel == "Yes" or travel == "yes" or travel == "YES":
        vehicle = input("Do you want to travel with ship or plane? (Ship/Plane): ")
        if vehicle == "Plane" or vehicle == "plane" or vehicle == "PLANE":
            class_type = input("Want Regular or Business class? (Regular/Business): ")
            if class_type == "Regular" or class_type == "regular" or class_type == "REGULAR":
                print("Chalo Donald Trump ke saath milte hai")
            if class_type == "Business" or class_type == "business" or class_type == "BUSINESS":
                print("Kya majbori hogi ki tu abhi bhi chakka ha")    
        if vehicle == "Ship" or vehicle == "ship" or vehicle == "SHIP":
            print("Itna khali time hai to train me jake bhik mang le")
    if travel == "No" or travel == "no" or travel == "NO":
        print("Epstine k sath nahi mil na ha kya?")        

