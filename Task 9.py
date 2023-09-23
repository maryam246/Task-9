import bardapi
import os

def save_question_and_answer(question, answer, feedback):
  """Saves the question, answer, and feedback to a file."""

  # Get the path to the PyCharm project directory.
  project_directory = os.path.dirname(os.path.abspath(__file__))

  # Create the filename for the questions and answers file.
  filename = os.path.join(project_directory, 'questions_and_answers.txt')

  # Open the file in append mode.
  with open(filename, 'a') as f:
    # Write the question, answer, and feedback to the file.
    f.write(f'{question}\n{answer}\n{feedback}\n')

bard = bardapi.Bard(token='bQhliBCrsGd3ATAuACHNiH5Tc2fOqDRHxHJAyHIqj8aysIHhp63Jndd1GDCnOSiXGZjYsg.')

while True:
  print("Welcome Ask anything!")
  # Ask the user for the desired answer size.
  answer_size = int(input('Enter the desired answer size: '))

  # Get the user's question.
  q = input('ask question:')

  if q:
    # Get the answer from Bard.
    r = bard.get_answer(q)

    # If the answer is longer than the desired answer size, truncate it.
    if len(r) > answer_size:
      r = r[:answer_size]

    # Print the answer to the console.
    print(r)

    # Get the user's feedback on the answer.
    feedback = input('Feedback on answer: ')

    # Save the question, answer, and feedback to a file.
    save_question_and_answer(q, r, feedback)

    # Ask the user if they want to exit.
    exit_confirmation = input('Do you want to exit? (y/n): ')

    # If the user enters "y" or "Y", exit the loop.
    if exit_confirmation.lower() == 'y':
      print("Good by!")
      break

  else:
    # If the user enters an empty string, break out of the loop.
    break
