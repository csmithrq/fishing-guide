# fishing-guide
Successful fishers keep journals, season-by-season, spot-by-spot, fish-by-fish of what they're doing and where they're doing it. On top of that incoming information, there's a ton of fish, locations, legalities, fishing rigs, strategies and triggers that experienced fishers build up. Fishing reports are available, but they're available on that fishery's website and aren't aggregated anywhere or stored anywhere which makes visiting all the different sites annoying.

This project aims to consolidate that information and provide simple means of exposing it, and eventually suggesting options based on dates, fishing reports and local triggers. I want to answer this question when I wake up and have a fishing itch: what can I go fish for today?

From a technical perspective, I'm looking to get my feet under me in Python and get more exposure to Mongo DB, API's and end-to-end web development. 

As of 12/18:
-> write json data via persistence service to mongoDb.
-> fetch fish profiles and fishing options from a rest API
-> mapped two fishing report feeds to cover ~10 locations
-> persist fishing reports to the database by source, without duplicates
-> java background is showing as code is not very pythonic... duck typing + asking forgiveness than permission
