# Project 1: Single-Ticker Data Fetch and Explore

First project in a 33-project quant trading roadmap.
Fetch AAPL daily prices, print summary stats, plot the close.

## Status
- [x] Project skeleton
- [ ] Fetch script
- [ ] Plot script
- [ ] Full README

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Assumptions & biases
- Single ticker only — no survivorship bias introduced yet (that comes in Project 2+)
- No lookahead concern because we only summarize historical data
- auto_adjust=False so raw Close and Adjusted Close are both preserved (used in Project 3)
- Not investment advice; not a strategy — just data plumbing
