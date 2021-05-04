#Question 1:
print(": Use R to create the following two matrices and do the indicated matrix multiplication.")

X = matrix(
    c(7,9,12,2,4,13),
    nrow = 2,
    ncol = 3,
    byrow = TRUE)
print(X)

Y = matrix(
    c(1,7,12,19,2,8,13,20,3,9,14,21),
    nrow = 3,
    ncol = 4,
    byrow = TRUE)
print(Y)

#Resulting Matrix:
print(X %*% Y)

#Question 2:
#a. data frame:

Data_Frame <- data.frame (
  id = c(1,2,3,4,5),
  name = c("Peter", "Amy", "Ryan", "Gary", "Michelle"),
  salary = c(623.30, 515.20, 611.00, 729.00, 843.25)
)

Data_Frame

#b. adding department column
Data_Frame$department <- c("sales", "accounting", "accounting", "sales", "finance")

Data_Frame

#c. extracting specific rows and columns:
Data_Frame[c(1,3,5), c(2,3)]


#d. bar chart:
y <- Data_Frame[c(1,4,5), c(3)]

x <- Data_Frame[c(1,4,5), c(2)]

barplot(y, names.arg = x)

#e. pie chart:
Data_Frame
summary(Data_Frame)

z <- Data_Frame[c(1,2,5), c(3)]
mylabel <- c("Peter", "Amy", "Michelle")
pie(z, label = mylabel, main = "Employee Salaries")

#Question 3: Python to R
    #Function 1: "if else"
    #Python code
#def valid_function():
#   def result_function():
#    if user_action == computer_action:
#        print(f"Both players selected {user_action}. It's a tie!")
#    elif user_action == "rock":
#        if computer_action == "scissors":
#            print("Rock smashes scissors! You win!")
#        else:
#            print("Paper covers rock! You lose.")
#    elif user_action == "paper":
#        if computer_action == "rock":
#            print("Paper covers rock! You win!")
#        else:
#            print("Scissors cuts paper! You lose.")
#    elif user_action == "scissors":
#        if computer_action == "paper":
#            print("Scissors cuts paper! You win!")
#        else:
#            print("Rock smashes scissors! You lose.")

game = function(){
    user.input <- readline(prompt="Enter a choice (rock, paper, scissors): ")
    options = c("rock", "paper", "scissors")
          comp.move = sample(options, size = 1)

    if (user.input == comp.move) {
    print("Tie!")
    } else if (user.input == "rock" & comp.move == "paper") {
    print("You chose rock, computer chose paper: you lose")
    } else if (user.input == "rock" & comp.move == "scissors") {
    print("You chose rock, computer chose scissors: you win! ")
    } else if (user.input == "scissors" & comp.move == "rock") {
    print("You chose scissors, computer chose rock: you lose")
    } else if (user.input == "scissors" & comp.move == "paper") {
    print("You chose scissors, computer chose paper: you win!")
    } else if (user.input == "paper" & comp.move == "rock") {
    print("you chose paper, computer chose rock: you win!")
    } else if (user.input == "paper" & comp.move == "scissors") {
    print("you chose paper, computer chose scissors: you lose")
    } else
    print("error, invalid selection")
    }

game()

#Question 3:
    #Function 2: "while loop"
#def play_function():
#    print("Play another game?")
#    t=True
#    while t:
#        choice = input("Enter y or n: ")
#        if choice == 'y' or choice == 'Y':
#            random_function()
#            valid_function()
#            result_function()
#            score_function()
#            play_function()
#            t=False
#        else:
#            t=False

play = function(){
t = TRUE
while (t == TRUE){
    user.choice <- readline(prompt="Play another game? Enter y or n:")
    if (user.choice == "y" | user.choice == "Y") {
    game()
    play()
    t = FALSE
    } else 
    t = FALSE
}
}

play()

main = function(){
    game()
    play()
}

main()
