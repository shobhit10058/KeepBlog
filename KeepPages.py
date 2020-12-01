import os, click
from pathlib import Path
home = str(Path.home())
os.chdir(home)
if not os.path.exists("blogs"):
    os.makedirs('blogs')

dic = {}

@click.group()
def main():
    """
    Simple CLI for saving your favourite webpages like blogs 
    under different topics and then seeing them whenever you wish
    """
    dic = {topic:{} for topic in os.listdir('blogs')}
    os.chdir('blogs')
    for Topic, pages in dic.items():
        os.chdir(Topic)
        for r, d, f in os.walk(Topic):
            file = open(f, 'r')
            dic[Topic][file.readline()] = file.readline()
            file.close()
        os.chdir('blogs')
    pass


@main.command()
@click.argument()
def AddBlog():
    """Add your favourite blog"""
    click.echo('Hello World!')


@main.command()
@click.argument()
def OpenYourPage():
    """Open the webpage in your browser"""
    click.echo('Hello World!')    


if __name__ == "__main__":
    main()