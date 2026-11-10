"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "False Positives: At most 1 in 10 Human-written posts are falsely labeled as AI.",
        "criterion": 1,
        "texts": [
            "When I attended high school, I was introduced to Computer Science classes. It was there where I started learning how to code, and where I realized how much I love the Computer Science field and enjoy coding. During high school, I took classes in which I gained experience in the Java and Python programming languages. During those years, I realized that a professional career in a tech-related field is a goal that I would like to pursue in my life. Ever since then and up to now, I have taken various Computer Science courses to hone my technological skills.",
            "My coursework at both NJIT and CodePath have given me knowledge and intriguing hands-on experiences in cybersecurity. In NJIT's CS 351 Cybersecurity course, I wrote a simple program for decoding simple substitution ciphers, and used tools for sniffing packets, and performing reconnaissance. In CodePath's Intermediate Cybersecurity course, which was two hours per week of live virtual sessions for ten weeks that I took on my own time, I learned to use tools such as Splunk, VirusTotal, Google Colab, and Catalyst in order to perform and report threat investigations. These projects are interesting to me because I used real-world tools to do meaningful work, connect the dots, and present the findings.",
            "Similarly, I have also gained knowledge and valuable direct experience with AI in my CodePath Foundations of AI Engineering course, which was another two hours per week of live virtual sessions for ten weeks of my own time that I recently completed this month. This course gave me experience working on small-scale AIs by implementing guard rails and confidence checks, as well as exercising responsible AI usage when using chatbots to help with work. I see these Cybersecurity and AI course projects as good experiences for paving my path in the cybersecurity/AI field and preparing me to use such skills in critical lines of work.",
            "Bottom-Up DP goes through each sum from 0 to amount, and it finishes when it reaches that final amount.",
            "Top-Down DP basically does the same thing, going through sums from 0 to amount, but returning back to previous calls whenever a coin amount for a number is obtained. It also computes every possible sum for amount in order to search for the smallest sum.",
            "BFS finishes when it first finds the sum to amount, because at that first point, the sum is already the smallest number of coins. It finishes early instead of calculating large amounts of sums that are potentially needed later.",
            "BFS finishes faster than DP when the gap between different coins is large, but the amount can be found with a small number of coins, such as with a coins list of [1, 99] and an amount of 101. Bottom-Up DP calculates every sum from 1 to 100, and Top-Down DP dedicates its first recursive branch to subtracting 1 100 times. BFS, meanwhile, only makes 4 calculations (0+1 and 0+99 in the first breadth, 1+1 and 1+99 in the second breadth).",
            "The tails array preserves the correct length by writing a new subsequence into the array where it would continue from a previous number, while overlapping all previous subsequences. If a new sub is longer, it fully covers the shorter subs. If a new sub is shorter, the older, longer subs stay uncovered at their endpoint, and can even continue to be expanded from there. Thus, the length of the array maintains as the length of the longest subsequence, even if some shorter subsequences overwrite the numbers.",
            "My thoughts on AI are that its extensive thinking capabilities can help people find solutions to tough challenges that we can't conceive of. However, it has concerns such as ethical issues and bias if the data it was trained on is biased. Generative AI enables laziness with users turning to AI to do their work, and is sometimes wrong.",
            "A file management system is like digital filing cabinets, neatly storing docs in folders. It's a DBMS that allows access to single files or tables at a time. In a File System, data is directly stored in a set of files. It contains flat files that have no relation to other files. On a computer, the file system includes virtual space for storing info.",
        ],
    },
    {
        "name": "False Negatives: No more than 1 in 3 AI posts are falsely labeled as Human.",
        "criterion": 2,
        "texts": [
            # Generated by Claude
            "The old lighthouse on the northern point hasn't guided a ship in decades, but the town still repaints it every spring. Volunteers show up with ladders, buckets of white paint, and thermoses of coffee. Children get to do the bottom few feet, which always ends up a little streaky. By noon someone has usually started a radio, and the work slows down to match the music. Nobody really remembers when the tradition started.",
            "Octopuses have three hearts and blue blood, which sounds made up but isn't. Two of the hearts pump blood through the gills, and the third sends it to the rest of the body. Oddly, that third heart stops beating while the octopus swims. This may be part of why they'd usually rather crawl than swim. Their blood is blue because it carries oxygen with copper instead of iron.",
            "My neighbor has been building a canoe in his garage for almost three years now. Every few weekends the door rolls up and the smell of cedar drifts down the street. He tells anyone who stops by that it's nearly done, though it never looks much different. Last month he finally put on the first coat of varnish. I'm starting to think he'll miss the project more than he'll enjoy the boat.",
            # Generated by ChatGPT
            "The rain began just as the afternoon sunlight disappeared behind the clouds. Drops tapped against the windowsill, forming tiny streams that wandered down the glass. Somewhere outside, a dog barked twice before everything settled into a comfortable quiet. The smell of wet pavement drifted through the slightly open window.",
            "A small wooden boat rested near the edge of the lake, gently rocking with each passing ripple. Its faded blue paint had begun to peel, revealing patches of pale wood underneath. A dragonfly landed on the bow, stayed for a moment, and disappeared into the tall grass. Across the water, the trees stood perfectly still.",
            "The refrigerator hummed softly in the kitchen while an old clock ticked on the wall. A bowl of oranges sat beside a folded newspaper, and a single spoon had been left in the sink. The room was ordinary, but the warm light made everything seem a little softer. Outside, evening slowly turned into night.",
            # Generated by Gemini
            "A steady rain tapped rhythmically against the glass, blurring the vibrant neon signs of the city street below. Inside the quiet café, the rich aroma of freshly ground coffee beans provided a comforting shield against the chilly autumn air. A lone patron sat by the corner booth, slowly turning the pages of an old, leather-bound novel. Every few minutes, steam would rise lazily from their ceramic mug, dissipating into the warm overhead light. It was the kind of slow, ordinary afternoon where time seemed to stretch out and lose its urgency.",
            "High above the clouds, a satellite silently orbited the earth, capturing crisp data from the swirling oceans below. Engineers thousands of miles away monitored the incoming signals on glowing, multi-screen consoles. The deep blue expanse of the planet looked entirely serene from this distant, mechanical vantage point. Back on the ground, automated systems quietly processed the data to update global weather models overnight. Science often operates in this quiet background, weaving technology into the fabric of daily life without fanfare.",
            "Deep in the heart of an ancient forest, moss-covered roots anchored giant trees that had stood for centuries. Sunlight filtered through the dense green canopy in sharp, dramatic shafts, illuminating tiny particles of dust dancing in the air. A small stream gurgled softly as it wound its way over smooth, gray pebbles and fallen branches. Somewhere in the distance, the sharp call of a blue jay echoed across the otherwise silent wilderness. Nature moved at its own deliberate pace here, completely indifferent to the bustling world beyond its borders.",
        ],
    },
    {
        "name": "False Positives: The percentage of False Positives (out of all Human posts) is less than each of the other 'confusion matrix fields'.",
        "criterion": 3,
        "texts": [
            # The above human posts
            "When I attended high school, I was introduced to Computer Science classes. It was there where I started learning how to code, and where I realized how much I love the Computer Science field and enjoy coding. During high school, I took classes in which I gained experience in the Java and Python programming languages. During those years, I realized that a professional career in a tech-related field is a goal that I would like to pursue in my life. Ever since then and up to now, I have taken various Computer Science courses to hone my technological skills.",
            "My coursework at both NJIT and CodePath have given me knowledge and intriguing hands-on experiences in cybersecurity. In NJIT's CS 351 Cybersecurity course, I wrote a simple program for decoding simple substitution ciphers, and used tools for sniffing packets, and performing reconnaissance. In CodePath's Intermediate Cybersecurity course, which was two hours per week of live virtual sessions for ten weeks that I took on my own time, I learned to use tools such as Splunk, VirusTotal, Google Colab, and Catalyst in order to perform and report threat investigations. These projects are interesting to me because I used real-world tools to do meaningful work, connect the dots, and present the findings.",
            "Similarly, I have also gained knowledge and valuable direct experience with AI in my CodePath Foundations of AI Engineering course, which was another two hours per week of live virtual sessions for ten weeks of my own time that I recently completed this month. This course gave me experience working on small-scale AIs by implementing guard rails and confidence checks, as well as exercising responsible AI usage when using chatbots to help with work. I see these Cybersecurity and AI course projects as good experiences for paving my path in the cybersecurity/AI field and preparing me to use such skills in critical lines of work.",
            "Bottom-Up DP goes through each sum from 0 to amount, and it finishes when it reaches that final amount.",
            "Top-Down DP basically does the same thing, going through sums from 0 to amount, but returning back to previous calls whenever a coin amount for a number is obtained. It also computes every possible sum for amount in order to search for the smallest sum.",
            "BFS finishes when it first finds the sum to amount, because at that first point, the sum is already the smallest number of coins. It finishes early instead of calculating large amounts of sums that are potentially needed later.",
            "BFS finishes faster than DP when the gap between different coins is large, but the amount can be found with a small number of coins, such as with a coins list of [1, 99] and an amount of 101. Bottom-Up DP calculates every sum from 1 to 100, and Top-Down DP dedicates its first recursive branch to subtracting 1 100 times. BFS, meanwhile, only makes 4 calculations (0+1 and 0+99 in the first breadth, 1+1 and 1+99 in the second breadth).",
            "The tails array preserves the correct length by writing a new subsequence into the array where it would continue from a previous number, while overlapping all previous subsequences. If a new sub is longer, it fully covers the shorter subs. If a new sub is shorter, the older, longer subs stay uncovered at their endpoint, and can even continue to be expanded from there. Thus, the length of the array maintains as the length of the longest subsequence, even if some shorter subsequences overwrite the numbers.",
            "My thoughts on AI are that its extensive thinking capabilities can help people find solutions to tough challenges that we can't conceive of. However, it has concerns such as ethical issues and bias if the data it was trained on is biased. Generative AI enables laziness with users turning to AI to do their work, and is sometimes wrong.",
            "A file management system is like digital filing cabinets, neatly storing docs in folders. It's a DBMS that allows access to single files or tables at a time. In a File System, data is directly stored in a set of files. It contains flat files that have no relation to other files. On a computer, the file system includes virtual space for storing info.",

            #The above AI posts
            # Generated by Claude
            "The old lighthouse on the northern point hasn't guided a ship in decades, but the town still repaints it every spring. Volunteers show up with ladders, buckets of white paint, and thermoses of coffee. Children get to do the bottom few feet, which always ends up a little streaky. By noon someone has usually started a radio, and the work slows down to match the music. Nobody really remembers when the tradition started.",
            "Octopuses have three hearts and blue blood, which sounds made up but isn't. Two of the hearts pump blood through the gills, and the third sends it to the rest of the body. Oddly, that third heart stops beating while the octopus swims. This may be part of why they'd usually rather crawl than swim. Their blood is blue because it carries oxygen with copper instead of iron.",
            "My neighbor has been building a canoe in his garage for almost three years now. Every few weekends the door rolls up and the smell of cedar drifts down the street. He tells anyone who stops by that it's nearly done, though it never looks much different. Last month he finally put on the first coat of varnish. I'm starting to think he'll miss the project more than he'll enjoy the boat.",
            # Generated by ChatGPT
            "The rain began just as the afternoon sunlight disappeared behind the clouds. Drops tapped against the windowsill, forming tiny streams that wandered down the glass. Somewhere outside, a dog barked twice before everything settled into a comfortable quiet. The smell of wet pavement drifted through the slightly open window.",
            "A small wooden boat rested near the edge of the lake, gently rocking with each passing ripple. Its faded blue paint had begun to peel, revealing patches of pale wood underneath. A dragonfly landed on the bow, stayed for a moment, and disappeared into the tall grass. Across the water, the trees stood perfectly still.",
            "The refrigerator hummed softly in the kitchen while an old clock ticked on the wall. A bowl of oranges sat beside a folded newspaper, and a single spoon had been left in the sink. The room was ordinary, but the warm light made everything seem a little softer. Outside, evening slowly turned into night.",
            # Generated by Gemini
            "A steady rain tapped rhythmically against the glass, blurring the vibrant neon signs of the city street below. Inside the quiet café, the rich aroma of freshly ground coffee beans provided a comforting shield against the chilly autumn air. A lone patron sat by the corner booth, slowly turning the pages of an old, leather-bound novel. Every few minutes, steam would rise lazily from their ceramic mug, dissipating into the warm overhead light. It was the kind of slow, ordinary afternoon where time seemed to stretch out and lose its urgency.",
            "High above the clouds, a satellite silently orbited the earth, capturing crisp data from the swirling oceans below. Engineers thousands of miles away monitored the incoming signals on glowing, multi-screen consoles. The deep blue expanse of the planet looked entirely serene from this distant, mechanical vantage point. Back on the ground, automated systems quietly processed the data to update global weather models overnight. Science often operates in this quiet background, weaving technology into the fabric of daily life without fanfare.",
            "Deep in the heart of an ancient forest, moss-covered roots anchored giant trees that had stood for centuries. Sunlight filtered through the dense green canopy in sharp, dramatic shafts, illuminating tiny particles of dust dancing in the air. A small stream gurgled softly as it wound its way over smooth, gray pebbles and fallen branches. Somewhere in the distance, the sharp call of a blue jay echoed across the otherwise silent wilderness. Nature moved at its own deliberate pace here, completely indifferent to the bustling world beyond its borders.",
            # One more, for a round 10 AI posts, generated by DuckDuckGo
            "Rain tapped softly on the window while the kettle warmed. A small patch of sunlight slipped across the kitchen floor, then disappeared behind a cloud. Outside, a sparrow shook the water from its feathers and hopped along the fence. The room smelled faintly of tea and wet earth.",

            # 3 Clearly AI
            # Generated by Gemini
            "In today's fast-paced digital landscape, businesses must harness the power of innovation to remain competitive. Pivotal to this transition is the ability to delve into data-driven insights—not as a mere luxury, but as a core operational strategy. Seamlessly integrating these tools fosters growth, enhances collaboration, and drives transformative results. Notable works in the field underscore a single truth: it is not about working harder, it is about unlocking your true potential.",
            # Generated by ChatGPT
            "Hi! It looks like you're testing—everything's working. How can I help you today?",
            "Good question — and that's the key distinction between lea and mov. Let's compare them directly 👇",

            # 3 Clearly Human
            # (my own tweets from twitter, so hopefully these have enough of a human touch)
            "Sometimes when I think about stuff I really want but shouldnt buy, I consider making a graphic board with pics of every gift I want that I can think of, so that I can look at it and go ok if I buy one of these ill just keep wanting more. but I think thatd just keep my mind on them. also I wouldnt know the limit of what to put on the board. do I really want plushies of the ghosts from pac man? or figures of yakko or dot warner? or those tiny toons keychains? and there's actually so much merch out there for fraggle rock and pac man",
            "ok is it just me or is the cartoon thing of \"the prey actually *wants* to be chased! isnt that cute?\" a bit cliche by now? jerry likes the chase. tweety wants sylvester to chase him. bugs wants lebron to chase him. road runner wants to be chased. daffy wants to be hunted. ...yk?",
            "some video games have tumors. the grim reaper in Castlevania. the boobeam trap in mega man 2. The volleyball moons in Mario odyssey. they could just be removed from the game and everything would be alright. but they're not removed from the game. they're in there.",  
            
            
            # 2 that are Human but sound like AI
            "You know the ones — the em dash everywhere. It's not just excessive, it's exhausting. Moreover, furthermore, and indeed, we shall delve into this tapestry of linguistic patterns.",
            "Sorry, you're right. Mercury and gasoline are not real ingredients for super speed. My bad.",

            # 2 that are AI but sound like Human
            # Generated by Claude
            "ok so i went to the farmers market this morning bc i was out of eggs right. and theres this guy selling honey and he gives me a sample on this tiny wooden stick and its like the best thing ive ever tasted lol. so obviously i buy a jar and its $18 which is insane but whatever. then i get home and realize i never got the eggs. like the one thing i went there for. i literally just made toast with honey for breakfast instead lmao",
            "omg ok so i finally tried that ramen place downtown you told me about. we waited like 40 min for a table which almost killed me lol but it was so worth it. i got the spicy one and my nose was running the whole time but i couldnt stop eating it. my brother ordered the mild one and kept stealing bites of mine and then complaining it was too hot?? like dude just get ur own. we def have to go together next time, im already thinking about it",
        ],
    },
    {
        "name": "Label coverage: Correct labels >= Unsure labels >= Incorrect labels, across the whole set.",
        "criterion": 4,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            # The above human posts
            "When I attended high school, I was introduced to Computer Science classes. It was there where I started learning how to code, and where I realized how much I love the Computer Science field and enjoy coding. During high school, I took classes in which I gained experience in the Java and Python programming languages. During those years, I realized that a professional career in a tech-related field is a goal that I would like to pursue in my life. Ever since then and up to now, I have taken various Computer Science courses to hone my technological skills.",
            "My coursework at both NJIT and CodePath have given me knowledge and intriguing hands-on experiences in cybersecurity. In NJIT's CS 351 Cybersecurity course, I wrote a simple program for decoding simple substitution ciphers, and used tools for sniffing packets, and performing reconnaissance. In CodePath's Intermediate Cybersecurity course, which was two hours per week of live virtual sessions for ten weeks that I took on my own time, I learned to use tools such as Splunk, VirusTotal, Google Colab, and Catalyst in order to perform and report threat investigations. These projects are interesting to me because I used real-world tools to do meaningful work, connect the dots, and present the findings.",
            "Similarly, I have also gained knowledge and valuable direct experience with AI in my CodePath Foundations of AI Engineering course, which was another two hours per week of live virtual sessions for ten weeks of my own time that I recently completed this month. This course gave me experience working on small-scale AIs by implementing guard rails and confidence checks, as well as exercising responsible AI usage when using chatbots to help with work. I see these Cybersecurity and AI course projects as good experiences for paving my path in the cybersecurity/AI field and preparing me to use such skills in critical lines of work.",
            "Bottom-Up DP goes through each sum from 0 to amount, and it finishes when it reaches that final amount.",
            "Top-Down DP basically does the same thing, going through sums from 0 to amount, but returning back to previous calls whenever a coin amount for a number is obtained. It also computes every possible sum for amount in order to search for the smallest sum.",
            "BFS finishes when it first finds the sum to amount, because at that first point, the sum is already the smallest number of coins. It finishes early instead of calculating large amounts of sums that are potentially needed later.",
            "BFS finishes faster than DP when the gap between different coins is large, but the amount can be found with a small number of coins, such as with a coins list of [1, 99] and an amount of 101. Bottom-Up DP calculates every sum from 1 to 100, and Top-Down DP dedicates its first recursive branch to subtracting 1 100 times. BFS, meanwhile, only makes 4 calculations (0+1 and 0+99 in the first breadth, 1+1 and 1+99 in the second breadth).",
            "The tails array preserves the correct length by writing a new subsequence into the array where it would continue from a previous number, while overlapping all previous subsequences. If a new sub is longer, it fully covers the shorter subs. If a new sub is shorter, the older, longer subs stay uncovered at their endpoint, and can even continue to be expanded from there. Thus, the length of the array maintains as the length of the longest subsequence, even if some shorter subsequences overwrite the numbers.",
            "My thoughts on AI are that its extensive thinking capabilities can help people find solutions to tough challenges that we can't conceive of. However, it has concerns such as ethical issues and bias if the data it was trained on is biased. Generative AI enables laziness with users turning to AI to do their work, and is sometimes wrong.",
            "A file management system is like digital filing cabinets, neatly storing docs in folders. It's a DBMS that allows access to single files or tables at a time. In a File System, data is directly stored in a set of files. It contains flat files that have no relation to other files. On a computer, the file system includes virtual space for storing info.",

            #The above AI posts
            # Generated by Claude
            "The old lighthouse on the northern point hasn't guided a ship in decades, but the town still repaints it every spring. Volunteers show up with ladders, buckets of white paint, and thermoses of coffee. Children get to do the bottom few feet, which always ends up a little streaky. By noon someone has usually started a radio, and the work slows down to match the music. Nobody really remembers when the tradition started.",
            "Octopuses have three hearts and blue blood, which sounds made up but isn't. Two of the hearts pump blood through the gills, and the third sends it to the rest of the body. Oddly, that third heart stops beating while the octopus swims. This may be part of why they'd usually rather crawl than swim. Their blood is blue because it carries oxygen with copper instead of iron.",
            "My neighbor has been building a canoe in his garage for almost three years now. Every few weekends the door rolls up and the smell of cedar drifts down the street. He tells anyone who stops by that it's nearly done, though it never looks much different. Last month he finally put on the first coat of varnish. I'm starting to think he'll miss the project more than he'll enjoy the boat.",
            # Generated by ChatGPT
            "The rain began just as the afternoon sunlight disappeared behind the clouds. Drops tapped against the windowsill, forming tiny streams that wandered down the glass. Somewhere outside, a dog barked twice before everything settled into a comfortable quiet. The smell of wet pavement drifted through the slightly open window.",
            "A small wooden boat rested near the edge of the lake, gently rocking with each passing ripple. Its faded blue paint had begun to peel, revealing patches of pale wood underneath. A dragonfly landed on the bow, stayed for a moment, and disappeared into the tall grass. Across the water, the trees stood perfectly still.",
            "The refrigerator hummed softly in the kitchen while an old clock ticked on the wall. A bowl of oranges sat beside a folded newspaper, and a single spoon had been left in the sink. The room was ordinary, but the warm light made everything seem a little softer. Outside, evening slowly turned into night.",
            # Generated by Gemini
            "A steady rain tapped rhythmically against the glass, blurring the vibrant neon signs of the city street below. Inside the quiet café, the rich aroma of freshly ground coffee beans provided a comforting shield against the chilly autumn air. A lone patron sat by the corner booth, slowly turning the pages of an old, leather-bound novel. Every few minutes, steam would rise lazily from their ceramic mug, dissipating into the warm overhead light. It was the kind of slow, ordinary afternoon where time seemed to stretch out and lose its urgency.",
            "High above the clouds, a satellite silently orbited the earth, capturing crisp data from the swirling oceans below. Engineers thousands of miles away monitored the incoming signals on glowing, multi-screen consoles. The deep blue expanse of the planet looked entirely serene from this distant, mechanical vantage point. Back on the ground, automated systems quietly processed the data to update global weather models overnight. Science often operates in this quiet background, weaving technology into the fabric of daily life without fanfare.",
            "Deep in the heart of an ancient forest, moss-covered roots anchored giant trees that had stood for centuries. Sunlight filtered through the dense green canopy in sharp, dramatic shafts, illuminating tiny particles of dust dancing in the air. A small stream gurgled softly as it wound its way over smooth, gray pebbles and fallen branches. Somewhere in the distance, the sharp call of a blue jay echoed across the otherwise silent wilderness. Nature moved at its own deliberate pace here, completely indifferent to the bustling world beyond its borders.",
            # One more, for a round 10 AI posts, generated by DuckDuckGo
            "Rain tapped softly on the window while the kettle warmed. A small patch of sunlight slipped across the kitchen floor, then disappeared behind a cloud. Outside, a sparrow shook the water from its feathers and hopped along the fence. The room smelled faintly of tea and wet earth.",

            # 3 Clearly AI
            # Generated by Gemini
            "In today's fast-paced digital landscape, businesses must harness the power of innovation to remain competitive. Pivotal to this transition is the ability to delve into data-driven insights—not as a mere luxury, but as a core operational strategy. Seamlessly integrating these tools fosters growth, enhances collaboration, and drives transformative results. Notable works in the field underscore a single truth: it is not about working harder, it is about unlocking your true potential.",
            # Generated by ChatGPT
            "Hi! It looks like you're testing—everything's working. How can I help you today?",
            "Good question — and that's the key distinction between lea and mov. Let's compare them directly 👇",

            # 3 Clearly Human
            # (my own tweets from twitter, so hopefully these have enough of a human touch)
            "Sometimes when I think about stuff I really want but shouldnt buy, I consider making a graphic board with pics of every gift I want that I can think of, so that I can look at it and go ok if I buy one of these ill just keep wanting more. but I think thatd just keep my mind on them. also I wouldnt know the limit of what to put on the board. do I really want plushies of the ghosts from pac man? or figures of yakko or dot warner? or those tiny toons keychains? and there's actually so much merch out there for fraggle rock and pac man",
            "ok is it just me or is the cartoon thing of \"the prey actually *wants* to be chased! isnt that cute?\" a bit cliche by now? jerry likes the chase. tweety wants sylvester to chase him. bugs wants lebron to chase him. road runner wants to be chased. daffy wants to be hunted. ...yk?",
            "some video games have tumors. the grim reaper in Castlevania. the boobeam trap in mega man 2. The volleyball moons in Mario odyssey. they could just be removed from the game and everything would be alright. but they're not removed from the game. they're in there.", 
            
            
            # 2 that are Human but sound like AI
            "You know the ones — the em dash everywhere. It's not just excessive, it's exhausting. Moreover, furthermore, and indeed, we shall delve into this tapestry of linguistic patterns.",
            "Sorry, you're right. Mercury and gasoline are not real ingredients for super speed. My bad.",

            # 2 that are AI but sound like Human
            # Generated by Claude
            "ok so i went to the farmers market this morning bc i was out of eggs right. and theres this guy selling honey and he gives me a sample on this tiny wooden stick and its like the best thing ive ever tasted lol. so obviously i buy a jar and its $18 which is insane but whatever. then i get home and realize i never got the eggs. like the one thing i went there for. i literally just made toast with honey for breakfast instead lmao",
            "omg ok so i finally tried that ramen place downtown you told me about. we waited like 40 min for a table which almost killed me lol but it was so worth it. i got the spicy one and my nose was running the whole time but i couldnt stop eating it. my brother ordered the mild one and kept stealing bites of mine and then complaining it was too hot?? like dude just get ur own. we def have to go together next time, im already thinking about it",
        ],
    },
    {
        "name": "Score Spread: Clearly-AI text and Clearly-Human text should be at least 0.5 points apart, on the correct sides.",
        "criterion": 5,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            # 3 Clearly AI
            # Generated by Gemini
            "In today's fast-paced digital landscape, businesses must harness the power of innovation to remain competitive. Pivotal to this transition is the ability to delve into data-driven insights—not as a mere luxury, but as a core operational strategy. Seamlessly integrating these tools fosters growth, enhances collaboration, and drives transformative results. Notable works in the field underscore a single truth: it is not about working harder, it is about unlocking your true potential.",
            # Generated by ChatGPT
            "Hi! It looks like you're testing—everything's working. How can I help you today?",
            "Good question — and that's the key distinction between lea and mov. Let's compare them directly 👇",

            # 3 Clearly Human
            # (my own tweets from twitter, so hopefully these have enough of a human touch)
            "Sometimes when I think about stuff I really want but shouldnt buy, I consider making a graphic board with pics of every gift I want that I can think of, so that I can look at it and go ok if I buy one of these ill just keep wanting more. but I think thatd just keep my mind on them. also I wouldnt know the limit of what to put on the board. do I really want plushies of the ghosts from pac man? or figures of yakko or dot warner? or those tiny toons keychains? and there's actually so much merch out there for fraggle rock and pac man",
            "ok is it just me or is the cartoon thing of \"the prey actually *wants* to be chased! isnt that cute?\" a bit cliche by now? jerry likes the chase. tweety wants sylvester to chase him. bugs wants lebron to chase him. road runner wants to be chased. daffy wants to be hunted. ...yk?",
            "some video games have tumors. the grim reaper in Castlevania. the boobeam trap in mega man 2. The volleyball moons in Mario odyssey. they could just be removed from the game and everything would be alright. but they're not removed from the game. they're in there."  
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
