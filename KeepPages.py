import os, click, validators, webbrowser, shutil, string
import pandas as pd
from fuzzywuzzy import fuzz
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


def Search(Iterator, query):
    strings = [s for s in Iterator]

    tar = [strings[0] for _ in range(5)]
    ini = [0 for _ in range(5)]

    for s in strings:
        ps = fuzz.partial_ratio(s, query)
        for i in range(len(ini)):
            if(ps > ini[i]):
                ini[i + 1: ] = ini[i: -1]
                tar[i + 1: ] = tar[i: -1]
                tar[i] = s
                ini[i] = ps
                break

    click.echo("\nThe most similar are:")
    for i in range(len(ini)):
        if(ini[i] > 0):
            click.echo(tar[i])


@main.command()
def AddBlog():
    """ Add your favourite Page"""
    make = True
    topic = click.prompt("Enter the topic").lower()
    name = click.prompt("Enter the name (Keep it unique under the topic)").lower()
    url = click.prompt("Enter the correct url").lower()
    """Keep the name and topic descriptive"""
    if(validators.url(url)):
        if(topic in topics):
            if(name in dic):
                click.echo("Try other name, this name is already used")
                make = False
            else:
                dic[name] = [url, topic]
                click.echo("Your webpage is saved, you can open it using the open command")
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
    name = name.lower()
    if(name in dic):
        click.echo('Opening in your browser')
        webbrowser.open_new_tab(dic[name][0])    
    else:
        click.echo("No such pages are saved.")
        Search(dic, name)

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
        Search(topics, topic)
        return

    List = pd.DataFrame(columns=["Name", "Link"])

    for pages in dic_top_pag[topic]:
        d = {}
        d["Name"] = pages
        d["Link"] = dic[pages][0]
        List = List.append(d, ignore_index=True)
    click.echo(List)

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
            Search(topics, topic)
    if(page != None):
        page = page.lower()
        if(page in dic):
            os.chdir(dic[page][1])
            os.remove(page+".txt")
        else:
            click.echo("failed to remove the page as it does not exist")
            Search(dic, page)

if __name__ == "__main__":
    main()