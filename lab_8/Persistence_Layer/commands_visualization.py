from Business_Layer.commands import Command

class BasicVisualizationCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.basic_visualization()

class ExtendedVisualizationCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.extended_visualization()