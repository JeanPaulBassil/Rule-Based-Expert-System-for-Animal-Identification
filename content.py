class Content:
    def __init__(self, content_data):
        # Initialize with content data (rule or condition).
        self.content_data = content_data

class If(Content):
    # The If class represents a conditional statement in the expert system.
    pass

class And(Content):
    # The And class represents a logical AND operation in the rules.
    pass

class Or(Content):
    # The Or class represents a logical OR operation in the rules.
    pass
