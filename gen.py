import sys
import asyncio
from vendor.makefile import MakeFile

class Generator:
    def __init__(self, args):
        self.args = args

    def is_valid(self):
        if len(self.args) == 0:
            raise ValueError("Must give at least 1 argument. check 'py gen.py help' for hints.")
    
    async def make_file(self, command, name):
        makefile = MakeFile(name=name)
        if command == 'controller':
            makefile.controller()
        elif command == 'model':
            pass
        elif command == 'route':
            pass
        else: 
            raise ValueError("Undefined command. check 'py gen.py help' for hints.")

    async def generate(self):
        try:
            self.is_valid()
            command = self.args[0].split(':')
            if command[0] == 'make':
                if len(command) >=2:
                    if len(self.args) >= 2:
                        await self.make_file(command = command[1], name= self.args[1])
                    else:
                        raise ValueError("Command 'make:{}' need at least 2 argument. 1 passed. check 'py gen.py help' for hints.".format(command[1]))
                else:
                    raise ValueError("Command 'make' need subcommand. check 'py gen.py help' for hints.")

            elif command[0] == 'help':
                available = [
                    """make:controller controllerName   : for generating new controller file""",
                    """make:model modelName             : for generating new model file""",
                    """make:route routeName             : for generating new route file""",
                    """help                             : for hints""",
                ]
                print('Available command')
                for i in available:
                    print(i)
            else:
                raise ValueError("Undefined command. check 'py gen.py help' for hints.")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    args = sys.argv
    generator = Generator(args[1:])
    asyncio.run(generator.generate())