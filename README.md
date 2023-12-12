# Binary-Sentiment-Classification

## Setup

Cd to the `backend` directory and install the requirements 

```
conda create -n "demo" python=3.9
conda activate demo
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
In the backend, you will also want to swap out the .env's API token with your own API token from HuggingFace. 
It is free to make an account and easy to make a token, should you need help use this link [HuggingFace Model](https://huggingface.co/facebook/bart-large-cnn?text=The+tower+is+324+metres+%281%2C063+ft%29+tall%2C+about+the+same+height+as+an+81-storey+building%2C+and+the+tallest+structure+in+Paris.+Its+base+is+square%2C+measuring+125+metres+%28410+ft%29+on+each+side.+During+its+construction%2C+the+Eiffel+Tower+surpassed+the+Washington+Monument+to+become+the+tallest+man-made+structure+in+the+world%2C+a+title+it+held+for+41+years+until+the+Chrysler+Building+in+New+York+City+was+finished+in+1930.+It+was+the+first+structure+to+reach+a+height+of+300+metres.+Due+to+the+addition+of+a+broadcasting+aerial+at+the+top+of+the+tower+in+1957%2C+it+is+now+taller+than+the+Chrysler+Building+by+5.2+metres+%2817+ft%29.+Excluding+transmitters%2C+the+Eiffel+Tower+is+the+second+tallest+free-standing+structure+in+France+after+the+Millau+Viaduct.)
and click deploy, then inference API and it will let you see in the top right of the pop up box, that you can sign up and make a token.
With that token you can modify the .env enviroment with your token to use.

## Running
Now from here you can open the `index.html` on the front end to get access to it - as long as the server is up (the uvicorn part in the setup).

Now here, you can give a title, the text contained in it and it will tell you how positive or negative it thinks it is.
You can also ask it questions but please note *it will return errors for the first minute after clicking **submit question***.
This is just because the model is a bit big so it needs to load first and then it will let you ping it.

Here is an example:

Title
```
The Last Great Mayan City: Mayapan, how it rose and fell
```

Content
```
The role of climate change on civil conflict and social instability in various historical societies has been the subject of much debate, partially because of the limited disciplinary and temporal scope of many case studies.
The cause of the collapse of Mayapan (the last great Maya city) has been the subject of just such a debate. It is known that internal conflict among the city’s elite eventually brought about societal collapse, but what brought about this internal conflict? Kennet et al. argue that prolonged drought escalated the rivalry among elite factions, ultimately leading to political demise and the city’s abandonment.
History of Mayapan
Location of Mayapan Credit: Kennet et al. 2022

The first large Maya cities appeared along the region’s western edge ca. 1000–800 cal BCE. By 500 BCE, numerous monumental centres existed, connected by a series of villages. These states existed in a cyclical nature, where states formed, became consolidated powers, expanded and fragmented, only for a new state to take their place.

Mayapan first came into being around 1100 cal CE, around the time that Chichen Itza’s power was failing. It was an impressive city surrounded by defensive walls, twelve formal gates, temples, shrines and columned halls decorated with murals and sculptures. At its height, it was home to 15,000–20,000 people. The city ensured its population had ample food by nurturing orchards, tending to their maize fields, hunting game, raising turkey and deer and cultivating household gardens. While Mayapan did engage in trade, it was predominantly a military state which raided its enemies and took captives as slaves and sacrifices.

The Mayapan rulers wielded power through a joint government. Three households, the Cocom, Xiu and Canuls, were the principal houses of nobility. The great houses were attended by their retinues and called on their town to supply them with food and goods. Of the three, the Cocom wielded the most power, bolstered by the support from the Canul mercenaries. The Xiu were the second most powerful, and the two houses effectively controlled the Mayapan state.
Building in Mayapan Credit: Eddie Bugajewski on Unsplash
Mayapan’s Demise

Mass excavations at Mayapan revealed three mass burials. MB 1 and MB 2, dated between 1360 and 1400cal CE, which coincided with a period of population decline and regional drought. Some buildings also show evidence of abandonment and destruction during this time. Researchers postulate that droughts led to population decline and impacted trade and agricultural productivity. Especially the incredibly drought-sensitive maize, which the Mayapan people relied on. The increased stress on the population likely led to increased internal violence, which escalated into the Xiu massacre of the Cocom between 1382 and 1401. The mass burial MB 3 was probably the result of this massacre; mtDNA indicated that the individuals buried there had strong matrilineal relations. Between 1440 and 1460CE, the Xiu ruled supreme before succumbing to disagreements among its vassals and looting, burning and abandoning the city.

Friar Diego de Landa provided the first European account of the rise and fall of Mayapan in 1566, over a century after the state’s demise. Though the city perished, much of its economic and political structures endured until European contact in the early 16th century.

Ultimately, the stress and rivalry that resulted from decades of drought brought about the collapse of Mayapan. Its surviving population dispersed into the surrounding area and took with them the culture of the Mayapan.
```

Question
```
What caused the fall of Mayapan?
```
