from Question import Question # imports the Question class from Question.py

question_prompts = [
    'What colour are oranges?\n (a) Orange\n (b) Blue\n (c) Red\n\n',
    'What colour are strawberries?\n (a) Pink\n (b) Yellow\n (c) Red\n\n',
    'What colour are lemons?\n (a) Green\n (b) Yellow\n (c) Purple\n\n'
]  # array of questions to ask the user

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
]  # array feeds 'question_prompts' and the right answer into the Question class in Question.py (see for loop below)

def run_test(questions):
    score = 0  # sets score to 0 each time test is run + creates variable to track score
    for question in questions:  # loops through 'questions' array one by one
        answer = input(question.prompt)  # creates variable 'answer' and waits input from user, while printing qPrompt
        if answer == question.answer:  # if statement checks if answer is the correct answer
            score += 1  # adds 1 to score if answer correct
    print('You got ' + str(score) + '/' + str(len(questions)) + ' questions right.')  # prints num correct

run_test(questions)  # calls run_test function and feeds the question array into it



