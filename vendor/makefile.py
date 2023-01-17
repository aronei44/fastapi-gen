
class MakeFile:
    def __init__(self, name):
        self.name = name

    def controller(self):
        try:
            namefile = 'app/controllers/' + self.name + '.py'
            f = open(namefile, 'x')
            f.write("""from fastapi import HTTPException

async def main(data, session):
    pass""")
            f.close()
        except Exception as e:
            print(e)