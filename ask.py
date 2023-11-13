class Ask:
    def __init__(self, choices=['y', 'n']):
        # Initialize with a list of choices, default is ['y', 'n'].
        self.choices = choices

    def ask(self):
        # Check if the longest choice string is more than one character.
        if max(len(choice) for choice in self.choices) > 1:
            # Display the choices with indices if choices are longer than one character.
            for index, choice in enumerate(self.choices):
                print(f"{index}. {choice}", flush=True)

            # Get user input as an integer index.
            user_input_index = int(input())

            # Return the choice corresponding to the input index.
            return self.choices[user_input_index]
        else:
            # For single-character choices, display them joined by "/".
            print("/".join(self.choices), flush=True)

            # Return the user's input directly.
            return input()
