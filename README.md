<h1>Ability Power Parity - API Challenge 2.0</h1>

<p>Ability Power Parity is a website designed to demonstrate the changes to all the AP items that recieved changes in patch 5.13.
It utilizes python to execute exactly 400,000 requests to the Riot API, returning 400,000 unique dictionaries to then be broken
down and analyzed for information. This information is then displayed on the working demo website, </p>
www.abilitypowerparity.com
<br>
<p>You can find full documentation of my progress on my blog, www.davidskudra.ca/blog/Riot-API-Challenge-2.0 </p>
<p>For further details on the website and it's navigation, refer to the final entry of my blogpost. </p>

<h1>Tech Used</h1>
<ul>
<li>Python 3.4.3 (Data mining, processing)</li>
<li>Microsoft Excel (Data organization & summation)</li>
<li>HTML, CSS (Website structure)</li>
<li>Javascript, JQuery (Website accent)</li>
</ul>

<h1>Production</h1>
<h2>Data Provided</h2>
<p>Riot provided 400,000 unique gameIDs, spread apart in two different patches, 5.11 and 5.14. Each patch had 2 seperate game modes,
normal 5x5 and ranked solo. Each different game mode then contained 10 json files, 1 for each region, while each contained a list of
10,000 gameIDs in a list. You can find these 40 files organized in the <i>provided dataset</i> tree in the master branch. It also contains two
additional json files, champ.json and item.json, which help find the ID of various champions and items.</p>

<h2>Data Acquisition</h2>
<p>The files for parsing these jsons can be found in the <i>request execution files</i> tree. The first thing you'll notice is
the RiotConstants.py and RiotAPI.py files. I've covered both of these in a previous blog post of mine where I gave a demo on
interfacing with the Riot API in python. You can find that post at www.davidskudra.ca/blog/Riot-API-Demo </p>
<p>Reading the demo isn't necessary, as the most important thing here is to note that the request module for python is installed
and used for this project as well. Credit to Raznick for the original RiotConstants and RiotAPI concept that I modified.</p>
https://www.youtube.com/watch?v=0NycEiHOeX8&ab_channel=SNAP
<br>
<p>The default method of making API calls in Python is very messy and less efficient, so using the request module is the best way
to go. Use pip to install it easily under cmd.</p>
<p>The remaining 4 files in the request execution files tree are the files that open & parse the Riot provided gameIDs json files.
Once the files are loaded and imported as a list, each unique gameID is used for an API call to the Riot API. The API then returns
a dictionary from the match by matchID call. Each request is organized into a master dictionary, where the key is the gameID and
the value is the returned dictionary from the API.<p>
<p>Riot provided a production key in order to have much higher rate limits. This made executing all 400,000 requests fairly easy.
My key was temporary for the duration of the competition but once I finished executing all of my requests I no longer needed it.
If you put together a working app that demands a higher rate limit, Riot will provided a non-temporary key for usage.</p>
<p>Once each dictionary is completed, the files are then dumped into a new json file for local storage. I decided to create my
library in the exact same format that the Riot provided dataset was organized. You can find a dummy version of the library
in the <i>executed request dump</i> tree. Obviously the actual library is too huge to upload and unnecessary, clocking in at
about 10GB in size.</p>

<h2>Data Processing</h2>
<p>Once all data is stored locally it is very easily to manipulate for information. The master branch includes the 3 main files
used to process the library. Using the library is very easy thanks to the full documentation found at the Riot Developers website.
The included python files have comments all over to help describe the process.</p>
<p>The three files had the following functions:</p>
<ul>
<li>Itemcount.py - This file found the wins, losses, and total purchases of all 12 significant AP items from patch 5.13, for each dictionary.
Good for finding item popularity and winrate before and after the updates.</li>
<li>GameLength-Item.py - This file found the average length of a game won with each item and also a game lost with each item.
This helped find what items had shorter and longer gametimes, before and after the updates.</li>
<li>Champ-Itemcount.py - This file found how often certain AP items were built by certain champions. Good for checking on how
changes to certain items affected their popularity with champions that often picked them up.</li>
</ul>
<br>
<p>Once all the data had been obtained, I used Microsoft Excel to organize it and search for trends, anomalies, and other information.
Excel obviously made it easy to find averages, max/mins, standard deviation, etc. I thought about incorporating some graphs into
the website demo but opted to stick with individualized data for each item.</p>

<h1>Front End</h1>
<p>I opted to create the website using twitter bootstrap to keep things nice and organized. You'll also notice some basic
JS and JQuery used to keep the pages nice and organized. Again, I included a full explanation of the website's basic functions
on my blog.<p>
http://www.davidskudra.ca/blog/Riot-API-Challenge-2.0-4
<p>I originally thought of doing the application all on one page in a matrix reduction-esque format, but ultimately decided that
navigation would be both clearer and more user friendly to isolate each item to it's own page, and narrow things down from there.</p>
<p>The website supports all major browsers, with JQuery limiting IE to versions 9 & 10. The radial gradient background I used is
limited to IE 10 but supports all other browsers, so the website will function for IE9 but won't support the background. Mobile
and desktop are both fully supported.</p>

<h1>Additional Notes</h1>
<p>I found some additional information that didn't fit the "AP item changes" category so I didn't elect to put it on the website.</p>
<ul>
<li>Games that included any of the 12 AP items analyzed had an average length of 22.86 minutes in patch 5.11. After the updates,
they had an average length of 23.33 minutes in patch 5.14.</li>
<li>Games on the Korean server had by far the quickest games, at an average length of 22.09 minutes. As seen on the website, some
items even had a sub-20 minute average win time.</li>
<li>The EUW server was about as average as average gets from all the regions - the standard deviation being negligible in almost
all cases, for both patch 5.11 and patch 5.14.</li>
</ul>

<h1>Addendum</h1>
<p>You can find out more about me at my homepage at www.davidskudra.ca</p>
<p>You can find the working demo of my entry at www.abilitypowerparity.com</p>
<p>I hope you take the time to explore both websites and learn more about my entry. If you have any questions, thoughts, or
concerns you can contact me at my email: dskudra@gmail.com </p>
<h4>Thanks for reading!</h4>
