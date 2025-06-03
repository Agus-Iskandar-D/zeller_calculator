# zeller_calculator
Here we go, It is simple command prompt program by using zeller's congruence to know the day of certain date.
before taking step further let's take a peek to the Zeller's congruence
Zeller's congruence is an algorithm devised by Christian Zeller in the 19th century to calculate the day of the week for any Julian or Gregorian calendar date.

##Let's get started!
###Well here are the requarements:
1. The system must be able to validate the input number
2. The system must be able to identify whetere it is leap year or not, including 2 years before and after the input year
3. The system must be able to identify the day of the input date
   
###to know the system, first I picture the system in usecase diagram and activity diagram to know the flow

![usecase diagram](https://github.com/Agus-Iskandar-D/zeller_calculator/blob/main/Usecase%20diagram.png)

![activity diagram](https://github.com/Agus-Iskandar-D/zeller_calculator/blob/main/Activity%20diagram.png)

Now, Let's roll the drum to code!
I devide every requarement into function

###to validate the input number, I use while and if. I also use break to make the iteration focus on each input number
![input_validation](https://github.com/Agus-Iskandar-D/zeller_calculator/blob/main/input%20validation.png)
##NOTE:the validation date still validate within 1 and 31 for each month (sorry, I am still newbe tho, next it will be better ;))

###to identify leap year, I use condtional if with the formula of leap year 
![leap year](https://github.com/Agus-Iskandar-D/zeller_calculator/blob/main/leap%20year.png)

##to identify the day, I use conditioal elif because teh condition more than one. and the condition use Zeller's congruence formula:
![zeller's](https://github.com/Agus-Iskandar-D/zeller_calculator/blob/main/zeller's.png)
Here is the code:
![Zeller](https://github.com/Agus-Iskandar-D/zeller_calculator/blob/main/zeller's%20congruense.png)

###Last but not least, I call all the function as the main program
![progam](https://github.com/Agus-Iskandar-D/zeller_calculator/blob/main/main%20program.png)

###Voala! here is the output:
![output](https://github.com/Agus-Iskandar-D/zeller_calculator/blob/main/output.png)

We can identify the day and its kind of year, whether it is leap year or not.

See you later, Danke!
