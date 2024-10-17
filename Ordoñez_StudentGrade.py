name = input("Input your name: ")
section = input("Input your section: ")

# Grades

pre = float(input("Enter your Prelims Period Grade: "))
mid = float(input("Enter your Midterm PeriodGrade: "))
fin = float(input("Enter your Finals  Period Grade: "))

# Calculating the average grade

avg = ((pre/100) * 33.33) + ((mid/100) * 33.33) + ((fin/100) * 33.33)
ravg = round(avg, 0)
print ("Your average grade is: ", ravg)

# GPA

if ravg > 100 :
    print("Error")
elif  ravg >= 99 and ravg <= 100 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 1.00, Excellent!")
elif  ravg >= 96 and ravg <= 98 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 1.25, Outstanding!")   
elif  ravg >= 93 and ravg <= 95 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 1.50, Superior")
elif  ravg >= 90 and ravg <= 92 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 1.75, Very Good")
elif  ravg >= 87 and ravg <= 89 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 2.00, Good")
elif  ravg >= 84 and ravg <= 86 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 2.25, Satisfactory")   
elif  ravg >= 81 and ravg <= 83 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 2.50, Fairly Satisfactory")
elif  ravg >= 78 and ravg <= 90 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 2.75, Fair") 
elif  ravg >= 75 and ravg <= 77 :
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 3.00, Passed")  
elif  ravg >= 75 and ravg <= 40:
    print("Hello,", name, "from",  section + ". Your Final Grade is", ravg, "and your  GPA is 5.00, Failed")
else :
    print("Error")






