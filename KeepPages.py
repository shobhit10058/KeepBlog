import os, click, validators, webbrowser, shutil, string
from pathlib import Path

@click.group()
def main():
    """
    Simple CLI for saving your favourite webpages like blogs 
    under different topics and then seeing them whenever you wish
    """
    global dic, topics, dic_top_pag, confDir
    home = str(Path.home())
    os.chdir(home)
    confDir = '.blogs'
    if not os.path.exists(confDir):
        os.makedirs(confDir)     
    topics = set(os.listdir(confDir))
    dic = {}
    dic_top_pag = {}
    os.chdir(confDir)
    for Topic in topics:
        for r, d, files in os.walk(Topic):
            dic_top_pag[Topic] = set()
            for f in files:
                file = open(Topic + "/" + f, 'r')
                name, url = file.readline()[:-1], file.readline()[:-1]
                dic_top_pag[Topic].add(name)
                dic[name] = [url, Topic]
                file.close()
    pass


@main.command()
@click.argument('topic')
@click.argument('name')
@click.argument('url')
def AddBlog(topic, name, url):
    """ Add your favourite Page"""
    make = True
    topic,name= (s.lower() for s in [topic, name])
    """Keep the name and topic descriptive"""
    if(validators.url(url)):
        if(topic in topics):
            if(name in dic):
                click.echo("Try other name, this name is already used")
                make = False
            else:
                dic[name] = [url, topic]
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
        webbrowser.open_new_tab(dic[name][0])    
    else:
        click.echo("No such pages are saved, try first saving it")

@main.command()
@click.option('--topic', '-f', help="Shows the saved pages under a topic(lower or upper case)")
def SeePages(topic):
    """See all saved pages of a topic"""
    click.echo('There are '+ str(len(topics)) + ' topics')
    click.echo("\n".join(list(topics)))
    if(len(topics) == 0):
        return
    if(topic == None):
        topic = click.prompt("Input a topic(lower or upper case) to see all the pages within it")
    
    topic = topic.lower()

    if(not topic in topics):
        click.echo('No such topic exists')
        return

    for pages in dic_top_pag[topic]:
        click.echo("Name-> " + pages + ", Link-> " + dic[pages][0])

@main.command()
@click.confirmation_option(help='This will delete all saved pages')
@click.option('--topic', '-rt', help="Removes all saved pages under the topic")
@click.option('--page', '-r', help="Removes specified saved page with specified name")
def remove(topic, page):
    """without any options this delete all saved pages, see with --help"""
    if((topic == None) and (page == None)):
        os.chdir('../')
        shutil.rmtree(confDir)
    if(topic != None):
        topic = topic.lower() 
        if(topic in topics):
            shutil.rmtree(topic)
        else:
            click.echo("failed to remove the topic as it does not exist")
    if(page != None):
        page = page.lower()
        if(page in dic):
            os.chdir(dic[page])
            os.remove(page)
        else:
            click.echo("failed to remove the page as it does not exist")

if __name__ == "__main__":
    main()