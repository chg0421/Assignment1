import cmd
"""

class HelloWorld(cmd.Cmd):
    Comment this ------ Simple command processor example.
    prompt = 'prompt: '
    intro = "Simple command processor example."
    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'
    ruler = '-'
    def do_prompt(self, line):
        self.prompt = line + ': '
    def do_EOF(self, line):
        return True
if __name__ == '__main__':
    HelloWorld().cmdloop() 

import os
class ShellEnabled(cmd.Cmd):
    last_output = ''
    def do_shell(self, line):
        "Run a shell command"
        print ("running shell command:", line)
        output = os.popen(line).read()
        print (output)
        self.last_output = output
    def do_echo(self, line):
        "Print the input, replacing '$out' with the output of the last shell command"
        # Obviously not robust
        print (line.replace('$out', self.last_output))
    def do_EOF(self, line):
        return True
if __name__ == '__main__':
    ShellEnabled().cmdloop()"""


class InteractiveOrCommandLine(cmd.Cmd):
    """Accepts commands via the normal interactive prompt or on the command line."""
    def do_greet(self, line):
        print ('hello,', line)
    def do_EOF(self, line):
        return True
if __name__ == '__main__':
    import sys
if len(sys.argv) > 1:
    InteractiveOrCommandLine().onecmd(' '.join(sys.argv[1:]))
else:
    InteractiveOrCommandLine().cmdloop()