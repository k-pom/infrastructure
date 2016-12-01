
### Infrastructure

    * Countermeasures protect from attackers
        - IDS (protects vs everything)
        - Firewall (protects vs phishing)
        - Antivirus (protects vs malware)
        - Load Balancer (protects vs DDOS)

    * Servers - The more users you have, the more users you can support

    * Databases - Databases are where you keep your data (points)

    * Engineers - Increases your resources/reputation

### Actors

    * Users - Require server space, result in data (points)

    * Attackers - Cause you to lose resources, reputation and points

### Resources

    * [] Resources - how you pay for infrastructure

    * *  Reputation - How many visitors you get each round

    * (x) Data - Points

### Setup

Each player receives a player board. Each players places their marker on 3 resources and 1 reputation.

Shuffle the infrastructure tiles, users and attackers.

Fill each purchasing space on the board with a infrastructure tile.

##Each round:

The game is played over 4 rounds. Each turn players will be able to buy up to 
3 infrastructure tiles before moving to the production phase

    Planning
        - Each player gains +1 Resource and Reputation (+ any engineer bonuses)

    Implementation:
        - Each player gets 3 turns to:
            - Buy an infrastructure tile, paying Resources costs (1 - 5)
            - After a tile is purchased, all tiles slide right one space
            - Any empty spaces on the track are refilled from the top of the deck
            - A player who can not or does not want to buy a tile may gain +1 resource instead

    Beta:
        - Each player draws up to attackers equal to their reputation.
        - Lose resources/data/reputation, modified by any countermeasures you have

    Production:
        - Each player
            - Draws a number user cards up to their reputation
            - Discard user cards until the number of users does not exceed total server value.
            - Score the bottom number of points on each kept user card.
            - Each database can only hold a limited number of points
            - Each database is limited in the number of points is can gain in a single round
            - scores USER points(DATA), up to DATABASE_SPACE
