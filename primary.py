from bs4 import BeautifulSoup
import requests
import re
import matplotlib.pyplot as plt
import numpy as np
import discord


def list_map(func, itr):
    return list(map(func, itr))


def list_filter(func, itr):
    return list(filter(func, itr))


async def primary_polls(ctx):
    r = requests.get('https://www.realclearpolitics.com/epolls/2020/president/us/2020_democratic_presidential_nomination-6730.html')
    soup = BeautifulSoup(r.text, features='html.parser')
    avgs = list_map(lambda i: i.text, soup.select('tr.rcpAvg td'))
    pcts = list_map(lambda i: float(i), avgs[2:avgs.index(list_filter(lambda i: re.match(r"^[a-zA-Z]", i), avgs)[1])])
    cands = list_map(lambda i: i.text, soup.select('tr.header th'))
    names = cands[2:cands.index('Spread')]
    y_pos = np.arange(len(names))
    fig, ax = plt.subplots(figsize=(11, 7))
    bar = plt.bar(y_pos, pcts, align='center', color="#2196F3")
    plt.xticks(y_pos, names)
    plt.ylabel('Dem Vote Share')
    plt.title('Democratic primary polls')
    fig.tight_layout()
    for rect in bar:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
    plt.savefig("plot.png")
    await ctx.message.channel.send(file=discord.File("plot.png"))
