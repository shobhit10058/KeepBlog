import os, click, validators, webbrowser
from pathlib import Path

@click.group()
def main():
    """
    Simple CLI for saving your favourite webpages like blogs 
    under different topics and then seeing them whenever you wish
    """
    home = str(Path.home())
    os.chdir(home)
    if not os.path.exists("blogs"):
        os.makedirs('blogs')    
    global dic
    global topics
    topics = set(os.listdir('blogs'))
    dic = {}
    os.chdir('blogs')
    for Topic in topics:
        for r, d, files in os.walk(Topic):
            for f in files:
                file = open(Topic + "/" + f, 'r')
                name, url = file.readline()[:-1], file.readline()[:-1]
                dic[name] = url
                file.close()
    pass


@main.command()
@click.argument('topic')
@click.argument('name')
@click.argument('url')
def AddBlog(topic, name, url):
    """ Add your favourite Page"""
    #click.echo(" ".join([topic,name,url]))
    make = True
    """Keep the name and topic descriptive"""
    if(validators.url(url)):
        if(topic in topics):
            if(name in dic):
                click.echo("Try other name, this name is already used")
                make = False
            else:
                dic[name] = url
                click.echo("Your webpage is saved, you can open it using the openyourpage command")
        else:
            os.makedirs(topic)
        if(make):
            os.chdir(topic)
            file = open(name+".txt", 'w')
            file.write(name+'\n')
            file.write(url+'\n')
    else:
        click.echo('Your url is not correct, you can try using http:// in front of the url you are saving')    

@main.command()
@click.argument('name')
def Open(name):
    """Open the webpage in your browser"""
    if(name in dic):
        click.echo('Opening in your browser')
        webbrowser.open_new_tab(dic[name])    
    else:
        click.echo("No such pages are saved, try first saving it")

@main.command()
def SeePages():
    """See all saved pages of a topic"""
    click.echo('There are '+ str(len(topics)) + ' topics')
    print(topics)

if __name__ == "__main__":
    main()