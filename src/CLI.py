import subprocess

class CLI:
    @staticmethod
    def run(self, command: str, args: dict):
        process = subprocess.Popen(command.format(**args).split(), stdout = subprocess.PIPE);
        output, error = process.communicate();
        return output;