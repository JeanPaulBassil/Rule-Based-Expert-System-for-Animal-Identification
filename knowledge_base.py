from ask import Ask
from content import If, And, Or

class KnowledgeBase:
    def __init__(self, rules):
        # Initialize with a set of rules and an empty memory for caching.
        self.rules = rules
        self.memory = {}

    def get(self, name):
        # Handle composite names (name:value).
        if ':' in name:
            key, value = name.split(':')
            actual_value = self.get(key)
            return 'y' if value == actual_value else 'n'

        # Retrieve from memory if already known.
        if name in self.memory:
            return self.memory[name]

        # Evaluate the rules.
        for rule in self.rules:
            if rule == name or rule.startswith(name + ":"):
                value = 'y' if rule == name else rule.split(':')[1]
                result = self.evaluate(self.rules[rule], field=name)
                if result not in ['y', 'n'] and value == 'y':
                    self.memory[name] = result
                    return result
                if result == 'y':
                    self.memory[name] = value
                    return value

        # Use default rule if field is not found.
        result = self.evaluate(self.rules['default'], field=name)
        self.memory[name] = result
        return result
                
    def evaluate(self, expression, field=None):
        # Evaluate the expression based on its type.
        if isinstance(expression, Ask):
            print(field)
            return expression.ask()
        elif isinstance(expression, If):
            return self.evaluate(expression.content_data)
        elif isinstance(expression, And) or isinstance(expression, list):
            items = expression.content_data if isinstance(expression, And) else expression
            for item in items:
                if self.evaluate(item) == 'n':
                    return 'n'
            return 'y'
        elif isinstance(expression, Or):
            for item in expression.content_data:
                if self.evaluate(item) == 'y':
                    return 'y'
            return 'n'
        elif isinstance(expression, str):
            return self.get(expression)
        else:
            print(f"Unknown expression: {expression}")
