# Interactive Prison Break Quiz

# Function to ask a question and get the user's answer
def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}) {option}")
    
    # Get a valid answer from the user
    while True:
        try:
            answer = int(input("Enter the number of your choice: "))
            if 1 <= answer <= len(options):
                return options[answer - 1]
            else:
                print(f"Please choose a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Questions and options
questions = [
    {
        "question": "Who do you choose to break out of prison with?",
        "options": ["Michael", "Sucre", "Lincoln", "T-Bag"]
    },
    {
        "question": "Which prison do you choose to break out from?",
        "options": ["Fox River", "Sona", "Ogygia"]
    },
    {
        "question": "Who do you trust with your information?",
        "options": ["Alex Mahone", "Agent Kellerman", "The General"]
    },
    {
        "question": "Where do you run away to?",
        "options": ["Panama", "Mexico", "Yemen"]
    }
]

# Store the user's choices
choices = []

# Ask each question and store the user's answer
for q in questions:
    answer = ask_question(q["question"], q["options"])
    choices.append(answer)
    print(f"You chose: {answer}\n")

# Display a summary of the user's choices
print("Summary of your choices:")
print(f"1. Partner: {choices[0]}")
print(f"2. Prison: {choices[1]}")
print(f"3. Trusted person: {choices[2]}")
print(f"4. Runaway destination: {choices[3]}")

# Provide some feedback based on the user's choices
if choices[0] == "Michael":
    print("\nGood choice! Michael always has a plan.")
elif choices[0] == "T-Bag":
    print("\nT-Bag? Really? Good luck trusting him!")

if choices[1] == "Fox River":
    print("\nClassic choice! Fox River is tough, but doable.")
elif choices[1] == "Sona":
    print("\nSona is a dangerous place... better be prepared.")

if choices[3] == "Panama":
    print("\nPanama sounds like a good place to lay low.")
elif choices[3] == "Yemen":
    print("\nYemen? That's a risky choice, especially with all the chaos.")