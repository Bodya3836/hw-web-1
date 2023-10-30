import os
from abc import ABC, abstractmethod
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

class AbstractOutputHandler(ABC):
    @abstractmethod
    def clear_screen(self):
        pass

    @abstractmethod
    def format_output(self, message):
        pass

    @abstractmethod
    def print_message(self, message):
        pass

    @abstractmethod
    def input_prompt(self, prompt_text, completer=None):
        pass

    @abstractmethod
    def display_message(self, message):
        pass

class OutputHandler(AbstractOutputHandler):
    def __init__(self):
        self.screen_width = 80  # Ширина екрану для форматування виведення

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Очищення екрану

    def format_output(self, message):
       
        pass

    def print_message(self, message):
        self.clear_screen()
        formatted_message = self.format_output(message)
        print(formatted_message)

    def input_prompt(self, prompt_text, completer=None):
        return prompt(prompt_text, completer=completer)

    def display_message(self, message):
        self.clear_screen()
        self.print_message(message)

class CommandProcessor:
    def __init__(self, output_handler):
        self.output_handler = output_handler

    def process_command(self, user_input):
        
        pass

def main():
    # Створення об'єкта OutputHandler
    output_handler = OutputHandler()

    # Передача об'єкта OutputHandler в об'єкт CommandProcessor
    command_processor = CommandProcessor(output_handler)

    completer = WordCompleter(command_dict, ignore_case=True)

    try:
        while True:
            user_input = output_handler.input_prompt(
                "\nType 'help' to view available commands. Type 'exit' to exit.\n>>> ",
                completer=completer
            )

            result = command_processor.process_command(user_input)

            # Вивід результату обробки команди
            output_handler.display_message(result)

            # Умова завершення роботи. Користувач повинен ввести команду: close | exit | good bye
            if result == 'Good Bye!':
                break
    finally:
        # Завершення роботи
        pass

if __name__ == "__main__":
    main()
