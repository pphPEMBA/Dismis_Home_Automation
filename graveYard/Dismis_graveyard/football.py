#! /usr/bin/env python

import sys
import json
import datetime
import argparse

import colorama # requirement
import humanize #requirement
import dateutil.parser
import dateutil.tz

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


FUTURE = "future"
NOW = "now"
PAST = "past"
SCREEN_WIDTH = 68


def progress_bar(percentage, separator="o", character="-"):
    """
    Creates a progress bar by given percentage value
    """
    filled = colorama.Fore.GREEN + colorama.Style.BRIGHT
    empty = colorama.Fore.WHITE + colorama.Style.BRIGHT

    if percentage == 100:
        return filled + character * SCREEN_WIDTH

    if percentage == 0:
        return empty + character * SCREEN_WIDTH

    completed = int((SCREEN_WIDTH / 100.0) * percentage)

    return (filled + (character * (completed - 1)) +
            separator +
            empty + (character * (SCREEN_WIDTH - completed)))


def prettify(match):
    """
    Prettifies given match object
    """
    diff = (datetime.datetime.now(tz=dateutil.tz.tzlocal()) -
            dateutil.parser.parse(match['datetime']))

    seconds = diff.total_seconds()

    if seconds > 0:
        if seconds > 60 * 90:
            status = PAST
        else:
            status = NOW
    else:
        status = FUTURE

    if status in [PAST, NOW]:
        color = colorama.Style.BRIGHT + colorama.Fore.GREEN
    else:
        color = colorama.Style.NORMAL + colorama.Fore.WHITE

    home = match['home_team']
    away = match['away_team']

    if status == NOW:
        minute = int(seconds / 60)
        match_status = "Being played now: %s minutes gone" % minute
    elif status == PAST:
        if match['winner'] == 'Draw':
            result = 'Draw'
        else:
            result = "%s won" % (match['winner'])
        match_status = "Played %s. %s" % (humanize.naturaltime(diff),
                                                  result)
    else:
        match_status = "Will be played %s" % humanize.naturaltime(diff)

    if status == NOW:
        match_percentage = int(seconds / 60 / 90 * 100)
    elif status == FUTURE:
        match_percentage = 0
    else:
        match_percentage = 100

    return u"""
    {} {:<30} {} - {} {:>30}
    {}
    \u26BD  {}
    """.format(
        color,
        home['country'],
        home['goals'],
        away['goals'],
        away['country'],
        progress_bar(match_percentage),
        colorama.Fore.WHITE + match_status
    )


def group_list(country):
    """
    Lists a group member
    """
    return """
    {}{:<5} \t\t {}
    wins: {} | losses: {} | goals for: {} | goals against: {} | out? {}
    {}
    """.format(
        colorama.Fore.GREEN + colorama.Style.BRIGHT,
        country['country'],
        colorama.Fore.WHITE + colorama.Style.BRIGHT,
        country['wins'],
        country['losses'],
        country['goals_for'],
        country['goals_against'],
        country['knocked_out'],
        "-" * 81
    )


def is_valid(match):
    """
    Validates the given match object
    """
    return (
        isinstance(match, dict) and
        (
            isinstance(match.get('home_team'), dict) and
            'goals' in match.get('home_team')
        ) and
        (
            isinstance(match.get('away_team'), dict) and
            'goals' in match.get('away_team')
        ) or
        isinstance(match.get('group_id'), int)
    )


def fetch(endpoint):
    """
    Fetches match results by given endpoint
    """
    url = "http://worldcup.sfg.io/%(endpoint)s" % {
        "endpoint": endpoint
    }

    data = urlopen(url)
    matches = json.loads(data.read().decode("utf-8"))

    for match in matches:
        if is_valid(match):
            yield match


def main():
    colorama.init()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('endpoint', nargs='?', default='', help="Set a " +\
        "filter on matches to retrieve (current, today, tomorrow)")
    parser.add_argument('-c', '--country', help="Filter matches to a " +\
        "specific country code.")
    parser.add_argument('-g', '--group', help="Filter matches to a " +\
        "specific group.")
    parser.add_argument('options', nargs='*', default='')
    args = parser.parse_args()

    endpoint = 'matches/' + args.endpoint
    
    if (args.country \
        or args.endpoint.lower() == 'country' and len(args.options)):
        endpoint = 'matches/country?fifa_code=%(country)s' % {
            "country": args.country.upper() if args.country \
                else args.options[0].upper() 
        }
    elif (args.group or args.endpoint.lower() == 'group' and len(args.options)):
        endpoint = 'group_results'
        group_id = int(args.group or args.options[0])
        for match in fetch(endpoint):
            if (match.get('group_id') == group_id):
                print(group_list(match))
        return

    for match in fetch(endpoint):
        print(prettify(match))


if __name__ == "__main__":
    main()

