import random
import time

# Sample flashcard data
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the result of 9 * 8?", "answer": "72"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What does HTML stand for?", "answer": "HyperText Markup Language"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
]

def run_flashcards():
    print("\n📚 Welcome to the Flash Card App! Type 'exit' to quit.\n")
    random.shuffle(flashcards)
    
    for card in flashcards:
        print(f"🧠 Question: {card['question']}")
        user_input = input("Your answer: ").strip()
        
        if user_input.lower() == 'exit':
            print("Thanks for playing! Goodbye.")
            break
        elif user_input.lower() == card['answer'].lower():
            print("✅ Correct!\n")
        else:
            print(f"❌ Incorrect. The correct answer was: {card['answer']}\n")
        time.sleep(1)

if __name__ == "__main__":
    run_flashcards()
