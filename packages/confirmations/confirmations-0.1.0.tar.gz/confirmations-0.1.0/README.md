# confirmations - fetch and analyze votes from US Senate confirmation hearings

## Usage

`python3 -m venv venv && source venv/bin/activate`
`pip install confirmations`
`confirmations --congress 119 --session 1`

If, for example, you just want to see the democrats voting records for Trump's
second term, you can do

`confirmations -c 119 -s 1 | grep ' (D-'`

The first time you run it for a given congress/session it will take awhile;
it's fetching the various roll call files one by one. Subsequent runs will
use cached data if it hasn't changed.

## TODO

It would be nice to report various interesting things; sort by how party-aligned
various senators are, show individual nominees results by party, etc..
