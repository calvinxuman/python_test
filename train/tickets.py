# coding: utf-8

"""命令行火车票查看器

Usage:
    tickets [-dgktz] <from> <to> <date>

Options:
    -h, --help 查看帮助
    -d         动车
    -g         高铁
    -k         快速
    -t         特快
    -z         直达

Examples:
    tickets 上海 北京 2018-01-10
    tickets -dg 成都 南京 2018-01-10
"""

import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init, Fore

from stations import stations
from stations2 import stations2


init()

class TrainsCollection:

    header = '车次 车站 时间 历时 商务座 一等 二等 软卧 硬卧 硬座 无座 备注'.split()

    def __init__(self, available_trains, options):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        self.options = options

    def _get_duration(self, list_train):
        duration = list_train[10].replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for raw_train in self.available_trains:
            list_train=raw_train.split('|')
            train_no = list_train[3]
            for i in range(len(list_train)):
                if list_train[i] == '':
                    list_train[i] = '--'
            initial = train_no[0].lower()
            if (not self.options or initial in self.options) and list_train[1]=='预订':
                train = [
                    train_no,
                    '\n'.join([Fore.GREEN + stations2[list_train[6]] + Fore.RESET,
                               Fore.RED + stations2[list_train[7]] + Fore.RESET]),
                    '\n'.join([Fore.GREEN + list_train[8] + Fore.RESET,
                               Fore.RED + list_train[9] + Fore.RESET]),
                    self._get_duration(list_train),
                    list_train[32],
                    list_train[31],
                    list_train[30],
                    list_train[23],
                    list_train[28],
                    list_train[29],
                    list_train[26],
                    list_train[1]
                ]
                yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


def cli():
    """Command-line interface"""
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
                date, from_station, to_station
           )
    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    r = requests.get(url)
    available_trains = r.json()['data']['result']
    TrainsCollection(available_trains, options).pretty_print()


if __name__ == '__main__':
    cli()



