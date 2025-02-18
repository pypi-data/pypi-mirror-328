import inspect

class CodeJump:
    def __init__(self):
        self.checkpoints = {}
        self.lines = []
        self.current_line = 0

    def checkpoint(self, name):
        """Registers a checkpoint with the current execution position."""
        self.checkpoints[name] = self.current_line

    def teleport_to(self, name):
        """Teleports to a checkpoint by changing execution pointer."""
        if name not in self.checkpoints:
            raise ValueError(f"Checkpoint '{name}' not found")
        self.current_line = self.checkpoints[name]

    def jumprun(self, func):
        """Extracts and executes function code step-by-step."""
        source_lines, _ = inspect.getsourcelines(func)
        self.lines = [line.strip() for line in source_lines if line.strip() and not line.startswith("def")]

        # Pre-registers checkpoints
        for i, line in enumerate(self.lines):
            if line.startswith("checkpoint("):
                checkpoint_name = line.split('"')[1]
                self.checkpoints[checkpoint_name] = i

        # Starts execution
        while self.current_line < len(self.lines):
            line = self.lines[self.current_line]
            if line.startswith("teleport_to("):
                checkpoint_name = line.split('"')[1]
                self.teleport_to(checkpoint_name)
            else:
                exec(line, globals(), locals())
                self.current_line += 1

# Create an instance of CodeJump
codejump = CodeJump()
checkpoint = codejump.checkpoint
teleport_to = codejump.teleport_to
jumprun = codejump.jumprun