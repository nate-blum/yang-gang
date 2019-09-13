import pandas
import matplotlib.pyplot as plt
import numpy as np
import discord


def list_map(func, itr):
    return list(map(func, itr))


def list_filter(func, itr):
    return list(filter(func, itr))


async def yangvstrump(ctx):
    raw = pandas.read_csv('https://projects.fivethirtyeight.com/polls-page/president_polls.csv')
    yang_id = raw['poll_id'][list(raw['candidate_name']).index('Andrew Yang')]
    poll = {}
    for cat in raw:
        poll[cat] = list_map(lambda i: i[1],
                             list_filter(lambda i: raw['poll_id'][i[0]] == yang_id, enumerate(list(raw[cat]))))

    labels = list_filter(lambda i: i != 'Donald Trump', list(poll['candidate_name']))
    dem_pcts = list_map(lambda i: i[1], list_filter(lambda i: poll['candidate_name'][i[0]] != 'Donald Trump',
                                                    enumerate(list(poll['pct']))))
    trump_pcts = list_map(lambda i: i[1], list_filter(lambda i: poll['candidate_name'][i[0]] == 'Donald Trump',
                                                      enumerate(list(poll['pct']))))

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, dem_pcts, width, label='Dem', color="#2196F3")
    rects2 = ax.bar(x + width / 2, trump_pcts, width, label='Trump', color="#F44336")

    ax.set_ylabel('Vote Percentage')
    ax.set_title('Individual Democrats vs. Trump In A General Election')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    fig.set_figheight(8)
    fig.set_figwidth(10)
    plt.savefig('plot.png')
    await ctx.message.channel.send(file=discord.File("plot.png"))
