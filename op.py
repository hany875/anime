name = input("Enter your name: ")
print("Hello, " + name)
print("This is a Quiz of the One Piece And Naruto")
print("One Piece Quiz")
print("Copy and Paste From Options")

# Initialize counters for correct and wrong answers
correct_count = 0
correct2_count = 0
correct3_count = 0
wrong_count = 0
wrong2_count = 0
wrong3_count = 0

# Question 1
print("------ Question 1 ------")
print("Options:")
print("- Joy Boy")
print("- Whitebeard")
print("- Big Mom")

quiz1 = input("Q1: Who had a portion of the One Piece before Gol D. Roger? ")
if quiz1 == "Joy Boy":
    print("Correct answer!")
    correct2_count += 1
    correct_count += 1
else:
    print("Wrong Answer, The Answer is Joy Boy")
    wrong2_count += 1
    wrong_count += 1

# Question 2
print("------ Question 2 ------")
print("Options:")
print("- Dressrosa")
print("- Laughtale")
print("- Alabasta")

quiz2 = input("Q2: What is the final island of the Grand Line? ")
if quiz2 == "Laughtale":
    print("Correct answer!")
    correct2_count += 1
    correct_count += 1
else:
    print("Wrong Answer, The Answer is Laughtale")
    wrong2_count += 1
    wrong_count += 1

# Question 3
print("------ Question 3 ------")
print("Options:")
print("- Manji")
print("- Naruto")
print("- Zolo")

quiz3 = input("Q3: What was Sanji originally supposed to be named? ")
if quiz3 == "Naruto":
    print("Correct answer!")
    correct2_count += 1
    correct_count += 1
else:
    print("Wrong Answer, The Answer is Naruto")
    wrong2_count += 1
    wrong_count

# Question 4
print("------ Question 4 ------")
print("Options:")
print("- Rayleigh")
print("- Garp")
print("- Shanks")

quiz4 = input("Q4: Who taught Luffy to use Haki? ")
if quiz4 == "Rayleigh":
    print("Correct answer!")
    correct2_count += 1
    correct_count += 1
else:
    print("Wrong Answer, The Answer is Rayleigh")
    wrong2_count += 1
    wrong_count += 1

# Question 5
print("------ Question 5 ------")
print("Options:")
print("- Guffy")
print("- Rugy")
print("- Lucy")

quiz5 = input("Q5: What is the name Luffy uses to enter the Colosseum in Dressrosa? ")
if quiz5 == "Lucy":
    print("Correct answer!")
    correct2_count += 1
    correct_count += 1
else:
    print("Wrong Answer, The Answer is Lucy")
    wrong2_count += 1
    wrong_count += 1

    print("\nOne Piece Quiz Complete!")
print(f"Correct Answers: {correct2_count}")
print(f"Wrong Answers: {wrong2_count}")

print(f"Total Correct Answers: {correct_count}")
print(f"Total Wrong Answers: {wrong_count}")
print("Write in One Number, For Example - 1, 2, 3, 4, 5")
result1 = input("How Much Did You Get? Correct Answers Only ")
if result1 == "5":
    print("You Love One Piece")
if result1 == "4":
    print("You Got One Wrong, Not A Big Deal")
if result1 == "3":
    print("You Watch One Piece But You're In The Early Episodes")
if result1 == "2":
    print("You Gotta Watch One Piece Faster")
if result1 == "1":
    print("You Don't Watch One Piece, Only Shorts")
print("Naruto Quiz")

# Question 1
print("------ Question 1 ------")
print("Options:")
print("- Sasuke")
print("- Sakura")
print("- Rock Lee")

quiz6 = input("Q1: Name the character that can only use Taijutsu? ")
if quiz6 == "Rock Lee":
    print("Correct answer!")
    correct3_count += 1
    correct_count += 1
else:
    print("Wrong Answer, The Answer is Rock Lee")
    wrong3_count += 1
    wrong_count += 1

# Question 2
print("------ Question 2 ------")
print("Options:")
print("- Team 5")
print("- Team 6")
print("- Team 7")

quiz7 = input("Q2: What is Naruto's team known as? ")
if quiz7 == "Team 7":
    print("Correct answer!")
    correct3_count += 1
    correct_count += 1
else:
    print("Wrong Answer, The Answer is Team 7")
    wrong3_count += 1
    wrong_count += 1

# Question 3
print("------ Question 3 ------")
print("Options:")
print("- A Rank ")
print("- S Rank ")
print("- B Rank ")

quiz8 = input("Q3: Which rank criminal is every member of Akatsuki? ")
if quiz8 == "S Rank":
    print("Correct answer!")
    correct_count += 1
    correct3_count += 1
else:
    print("Wrong Answer, The Answer is S Rank")
    wrong_count += 1
    wrong3_count += 1

# Question 4
print("------ Question 4 ------")
print("Options:")
print("- Genin ")
print("- Jonin ")
print("- Chunin ")

quiz9 = input("Q4: To what level of Shinobi, D-rank missions are given? ")
if quiz9 == "Genin":
    print("Correct answer!")
    correct_count += 1
    correct3_count += 1
else:
    print("Wrong Answer, The Answer is Genin")
    wrong_count += 1
    wrong3_count += 1

# Question 5
print("------ Question 5 ------")
print("Options:")
print("- Sushi ")
print("- Takoyaki ")
print("- Ramen ")

quiz10 = input("Q5: Name Naruto's favorite food ")
if quiz10 == "Ramen":
    print("Correct answer!")
    correct_count += 1
    correct3_count += 1
else:
    print("Wrong Answer, The Answer is Ramen")
    wrong_count += 1
    wrong3_count += 1
    
    print("\nNaruto Quiz Complete")
print(f"Correct Answers: {correct3_count}")
print(f"Wrong Answers: {wrong3_count}")

print(f"Total Correct Answers: {correct_count}")
print(f"Total Wrong Answers: {wrong_count}")

print("Write in One Number, For Example - 1, 2, 3, 4, 5")
result2 = input("How Much Did You Get? Correct Answers Only ")
if result2 == "5":
    print("You Love Naruto")
if result2 == "4":
    print("You Got One Wrong, Not A Big Deal")
if result2 == "3":
    print("You Watch Naruto But You're In The Early Episodes")
if result2 == "2":
    print("You Gotta Watch Naruto Faster")
if result2 == "1":
    print("You Don't Watch One Naruto, Only Shorts")

print("Thank You For Doing My Quiz")
