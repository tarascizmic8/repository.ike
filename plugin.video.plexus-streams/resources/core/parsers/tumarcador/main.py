# -*- coding: utf-8 -*-

"""
This plugin is 3rd party and not part of plexus-streams addon

TuGoleada.com

"""
import sys,os,requests
current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir =  current_dir.replace(basename,'').replace('parsers','')
sys.path.append(core_dir)
import re
from utils.webutils import *
from utils.pluginxbmc import *
from utils.directoryhandle import *
from utils.parsers import parser_resolver

parserName = "tumarcador"
base_url = "http://tumarcador.xyz"

def module_tree(name,url,iconimage,mode,parser,parserfunction):
    if not parserfunction: menu()
    elif parserfunction == "resolve_and_play": parser_resolver(name,url, os.path.join(current_dir,'icon.png'))


def menu():
    try:
        source = get_page_source(base_url)
    except:
        xbmcgui.Dialog().ok(translate(40000),translate(40128))
        return

    aceLinks = re.search("Canales AceStream.+?<ul[^>]*>(.+?)</ul>", source, re.MULTILINE | re.DOTALL)
    if aceLinks:
        channels = re.findall('href="([^"]+)[^>]+>([^<]+)', aceLinks.group(1))
        for chURL, chName in channels:
            addDir("[B] {0}[/B]".format(chName), "{0}/{1}".format(base_url, chURL), 401, os.path.join(current_dir,"icon.png"), 1, False, parser=parserName, parserfunction="resolve_and_play")

    else:
        for i in range(1, 10):
            addDir("[B] Channel {0}[/B]".format(i), "{0}/canal{1}a.php".format(base_url, i), 401, os.path.join(current_dir,"icon.png"), 1, False, parser=parserName, parserfunction="resolve_and_play")
