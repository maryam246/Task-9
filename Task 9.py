import json
import bardapi

class Note:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class BardAssistant:
    def __init__(self, token):
        self.bard = bardapi.Bard(token=token)
        self.notes = []

    def get_answer(self, question, length):
        answer = self.bard.get_answer(question)

        if answer is None:
            answer = "I don't know the answer to that question."

        if length == "short":
            answer = answer[:100]
        elif length == "medium":
            answer = answer[:200]
        elif length == "long":
            answer = answer
        else:
            raise ValueError("Invalid length")

        return answer

    def save_note(self, question, answer):
        note = Note(question, answer)
        self.notes.append(note)

    def load_notes(self):
        with open("notes.py", "r") as file:
            notes = json.load(file)
            self.notes = notes

    def save_notes_to_file(self):
        with open("notes.py", "w") as file:
            json.dump(self.notes, file)

def get_api_token_from_file():
    with open("api_token.txt", "r") as file:
        api_token = file.read()

    return api_token

def main():
    # Get the API token from a file.
    api_token = get_api_token_from_file()

    # Create a Bard assistant object.
    assistant = BardAssistant(token='bQhliM21tBxFJCItTNzf2TunvIuG4wfVOcjb-JNTzLWnAOSCvOJd3xZJ-hxTGsoqki0o0g.')

    # Print a welcome message.
    print("Welcome to the Bard note-taking app!")

    while True:
        # Ask the user if they want to ask a question.
        ask_question = input("Do you want to ask a question? (y/n): ")

        # If the user does not want to ask a question, exit the program.
        if ask_question != "y":
            break

        # Ask the user a question.
        question = input("Ask a question: ")

        # Ask the user for the length of the answer.
        length = input("What length of answer do you want? (short, medium, or long): ")

        # Get the answer from the assistant.
        answer = assistant.get_answer(question, length)

        # Print the answer to the user.
        print(answer)

        # Save the question and answer to a note.
        assistant.save_note(question, answer)

        # Ask the user if they want to save the question and answer.
        save_question_and_answer = input("Do you want to save the question and answer? (y/n): ")

        # If the user wants to save the question and answer, save it to the file.
        if save_question_and_answer == "y":
            assistant.save_notes_to_file()

    # Print a goodbye message.
    print("Good bye!")

if __name__ == "__main__":
    main()
