# artificial_intelligence_assignments
Repository for Artificial Intelligence projects
First two projects are on Expert Systems with an attempt to make them more robust further on. 

Creating an AI expert system that uses PyKnow to answer a question. 

Hockey teams spend millions of dollars trying to determine if they should draft an 18 year old based on an attempt to project their future skill and impact in the NHL. This expert system will allow you to determine which round you should draft a player based on 5 different criteria. Hockey drafts are typically much more complicated, but this will provide a starting point, because these are the 5 most important criteria for a hockey player. In the NHL there are 7 rounds of drafting.

As this is just a basic expert system all leagues that prospects play in will be viewed as equal. 

The 5 criteria will be as follows:
 1. Hockey IQ (high medium low)
 2. Skating (high medium low)
 3. Best player on their line (Yes/No) - this is important for determining if players are being carried
 4. Offensive Driver (high medium low)
 5. Defensive Awareness (high medium low)

While it makes sense that you would want to draft a player with the highest stats this in all rounds this is implied by telling it to draft in the first round. 

This expert system allows you to put in the stats for the players, but states where players should be drafted based on priority of skills. For example the player could have "High" ratings in points 2 through 5, but if he has a low hockey IQ the program will tell you not to draft this player, as it views Hockey IQ as the most important stat for future success. Alternatively if the player has Medium hockey IQ, and low scores in every other category it will still tell you to try drafting them in the seventh round. Again it does this, because it believes that hockey IQ is the single most important trait. In fact if the player has a hockey IQ of medium they will not be suggested to be drafted until the sixth round at the earliest. Conversely a players ability to drive offense and/or defensive awareness is not as important and therefore a player with a medium skill set in both of these aspects (while having high scores in the remaining three categories) will be considered in the second or third round. 

This program also differentiates the skillset based on if it is a forward or a defenseman. The first question asked is therefore for positioning. The above description of the priorities will therefore be affected by the position of the player. 
Goalies will not be considered due to the unpredictably of drafting goalies.
