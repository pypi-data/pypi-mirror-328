from argparse import ArgumentParser
from collections import defaultdict
import logging
import sys

import requests_cache
import bs4

log = logging.getLogger(__name__)
req_session = requests_cache.CachedSession('votes_cache', backend='filesystem')

def roll_call_url(congress, session, vote):
    url = f'https://www.senate.gov/legislative/LIS/roll_call_votes/vote%s%s/vote_%s_%s_%s.xml' % (congress, session, congress, session, vote)
    return url

def fetch_roll_call(congress, session, vote):
    r = req_session.get(roll_call_url(congress, session, vote))
    return bs4.BeautifulSoup(r.text, 'xml')

def process_roll_call(tally, roll_call):
    # <vote_document_text>Howard Lutnick, of New York, to be Secretary of Commerce</vote_document_text>

    if roll_call.vote_question_text.text.startswith('On the Nomination'):
        for m in roll_call.find_all('member'):
            tally[m.member_full.text][m.vote_cast.text] += 1

def vote_menu_url(congress, session):
    url = f'https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_%s_%s.xml' % (congress, session)
    return url

def fetch_confirmation_votes(congress, session):
    r = req_session.get(vote_menu_url(congress, session))
    menu = bs4.BeautifulSoup(r.text, 'xml')
    votes = [vote.vote_number.text for vote in menu.votes.find_all('vote') if vote.question.text.startswith('On the Nomination') and vote.vote_number is not None]
    return votes

#if __name__ == '__main__':
def main():
    parser = ArgumentParser(prog='confirmations',
                            description='Download and collate senate confirmation voting information')

    parser.add_argument('-c', '--congress', default='119')
    parser.add_argument('-s', '--session', default='1')
    opts = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    tally = defaultdict(lambda: defaultdict(int))

    log.info(f'Fetching and processing confirmations from the %s congress, session %s...' % (opts.congress, opts.session))
    for vote in fetch_confirmation_votes(opts.congress, opts.session):
        soup = fetch_roll_call(opts.congress, opts.session, vote)
        for member in soup.members.find_all('member'):
            tally[member.member_full.text][member.vote_cast.text] += 1

    for full_member in tally:
        opts = ['Yea', 'Nay', 'Not Voting']
        counts = ', '.join([f'%s %4d' % (opt, tally[full_member].get(opt, 0)) for opt in opts])
        print(f'%25s, ' % full_member, counts)
