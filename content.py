# -*- coding: utf-8 -*-
"""Content model for The Viral Veer. Edit this file, then run build.py."""

SITE = {
    "name": "The Viral Veer",
    "tagline": "Smart advice for modern life.",
    "subline": "Relationships. Career. Technology. Life.",
    "description": "Viral Veer is an Indian content creator, technology and corporate professional, and commentator on relationships, careers, technology and modern life. Practical, experience-based answers to the questions people actually ask.",
    "handle": "@theviralvir",
    "instagram": "https://www.instagram.com/theviralvir/",
    "youtube": "https://www.youtube.com/@theviralvir",
    "facebook": "https://www.facebook.com/theviralvir",
    "email": "TheViralVir@gmail.com",
    "person": "V Jain",
    "stats": [("253k", "Instagram followers"), ("1B+", "views"), ("363", "posts"), ("36+", "Zindagi ke Smart Tips episodes")],
    "featured": ["Times of India", "BW Businessworld", "IIT Bombay"],
    "show": "The Viral Vir Show",
}

# Real Instagram tiles captured from instagram.com/theviralvir (assets/img/ig1-6.jpg)
IG_POSTS = [
    ("ig1.jpg", "Zindagi Ke Smart Tips, Episode 36: Muskurana"),
    ("ig2.jpg", "Zindagi Ke Smart Tips, Episode 35"),
    ("ig3.jpg", "Best comeback: a Viral Vir reaction"),
    ("ig4.jpg", "Zindagi Ke Smart Tips, talk show clip"),
    ("ig5.jpg", "The Viral Vir Show: conversations on love and life"),
    ("ig6.jpg", "The last word people say before death"),
]

# Recent YouTube uploads from youtube.com/@theviralvir (thumbnails in assets/img)
YT_VIDEOS = [
    ("sCaNPoA2f8g", "Healthy food is slowly poisoning your body, with Dr Shreya"),
    ("4mB-cBLVniQ", "Mental health conversations with The Viral Vir"),
    ("xAQaeq7ItF0", "How to become a fashion influencer on Instagram"),
    ("iT2Wn0NTrh8", "The most controversial film of 2025, with Tushar Amrish Goel"),
    ("UgHh87CcjEo", "Bhoot tantra or science, with Dr Sidhant Joshi"),
]

# Pillars -> sub-topics. Each sub-topic carries the question bank for its hub.
PILLARS = [
    {
        "slug": "relationships", "name": "Relationships", "emoji": "❤️",
        "lede": "Dating, love, marriage, breakups and the conversations in between. What actually happens, not what the movies promised.",
        "subs": [
            {"slug": "dating", "name": "Dating", "lede": "Reading signals, first moves, modern dating and the mistakes that cost people years.",
             "questions": [
                "How do you know if someone genuinely likes you?",
                "What are the signs someone is losing interest?",
                "How do you approach someone you like without being awkward?",
                "How important is physical attraction, really?",
                "Can a friendship turn into love?",
                "What are the biggest mistakes people make in modern dating?",
                "Dating after 30: what actually changes?",
                "How many dates before you know if it is serious?",
             ]},
            {"slug": "love", "name": "Love", "lede": "Attraction, chemistry, compatibility and the difference between them.",
             "questions": [
                "Love vs attraction: what is the difference?",
                "Why do intelligent people choose the wrong partner?",
                "What makes someone attractive beyond looks?",
                "How do you know if what you feel is love or loneliness?",
                "Is chemistry enough to build a relationship on?",
                "Why do people fall out of love?",
             ]},
            {"slug": "marriage", "name": "Marriage", "lede": "Deciding, committing, and staying married on purpose.",
             "questions": [
                "How do you know you are ready to get married?",
                "Arranged vs love marriage: what matters more than the label?",
                "What should couples discuss before marriage?",
                "What makes long marriages actually work?",
                "How do you handle in-laws without wrecking your marriage?",
                "Is it normal to have doubts before the wedding?",
             ]},
            {"slug": "men-and-women", "name": "Men & Women", "lede": "How men and women read the same situation differently, and what to do about it.",
             "questions": [
                "Why do men and women argue about the same things?",
                "What do women notice first about a man?",
                "What do men actually find attractive in a woman?",
                "Why do men go quiet when stressed?",
                "What does emotional intelligence look like in a man?",
             ]},
            {"slug": "breakups", "name": "Breakups", "lede": "Ending it, surviving it, and not repeating it.",
             "questions": [
                "How do you know when it is time to move on?",
                "How do you recover from a breakup properly?",
                "Should you stay friends with an ex?",
                "Why does the person who left seem fine?",
                "How long does it take to get over someone?",
                "Should you get back with an ex?",
             ]},
            {"slug": "communication", "name": "Communication", "lede": "Saying the hard thing without starting a war.",
             "questions": [
                "How often should couples communicate?",
                "How do you tell your partner something is bothering you?",
                "Why do small fights become big fights?",
                "What should you never say in an argument?",
                "How do you ask for what you want without sounding needy?",
             ]},
        ],
    },
    {
        "slug": "career", "name": "Career", "emoji": "💼",
        "lede": "Interviews, bosses, promotions, politics and pay. From someone who has sat on both sides of the table for decades.",
        "subs": [
            {"slug": "interviews", "name": "Interviews", "lede": "What interviewers are actually checking, and how to pass it.",
             "questions": [
                "What should you say when asked about your weakness?",
                "How do you answer 'why do you want to leave your current job'?",
                "What do senior interviewers notice in the first five minutes?",
                "How do you prepare for a leadership interview?",
                "What questions should you ask at the end of an interview?",
             ]},
            {"slug": "leadership", "name": "Leadership", "lede": "Managing people, being managed, and becoming someone people follow.",
             "questions": [
                "How do you become a better leader?",
                "What separates a good boss from a bad boss?",
                "How do you manage someone older or more experienced than you?",
                "How do you give feedback that people actually use?",
                "What does a CTO actually do all day?",
             ]},
            {"slug": "office-politics", "name": "Office Politics", "lede": "Why it exists, how it works, and how to play clean.",
             "questions": [
                "Why does office politics exist?",
                "How do you deal with a toxic boss?",
                "How do you handle a colleague who takes credit for your work?",
                "Should you be friends with your colleagues?",
                "How do you stay visible without being loud?",
             ]},
            {"slug": "job-search", "name": "Job Search", "lede": "When to leave, how to look, and how to land.",
             "questions": [
                "When should you leave your job?",
                "How do you job hunt while employed?",
                "What should you do in the first 90 days of a new job?",
                "How do you recover from a layoff?",
                "Is it bad to switch jobs too often?",
             ]},
            {"slug": "salary", "name": "Salary", "lede": "Asking for more without losing the job.",
             "questions": [
                "How do you negotiate your salary without losing the offer?",
                "How do you ask for a raise?",
                "Should you tell a recruiter your current salary?",
                "Why do job switchers get paid more than loyal employees?",
                "How do you negotiate a counter-offer?",
             ]},
            {"slug": "ai-and-careers", "name": "AI & Careers", "lede": "What AI changes about work, and what to do this year.",
             "questions": [
                "How will AI change jobs?",
                "Which jobs are most vulnerable to AI?",
                "Will AI replace programmers?",
                "How should professionals use ChatGPT at work?",
                "What should students learn in the AI era?",
             ]},
        ],
    },
    {
        "slug": "life", "name": "Life", "emoji": "🧠",
        "lede": "People, confidence, growth and the lessons that only show up after a few decades of living.",
        "subs": [
            {"slug": "life-advice", "name": "Life Advice", "lede": "The big questions, answered plainly.",
             "questions": [
                "What are the biggest mistakes people make in their 30s?",
                "What should you stop doing after 40?",
                "Why does success sometimes make people lonely?",
                "Why am I unhappy despite being successful?",
                "How do you know when it is time to move on from anything?",
             ]},
            {"slug": "zindagi-ke-smart-tips", "name": "Zindagi Ke Smart Tips", "lede": "Short, sharp, practical. The series that started it all.",
             "questions": [
                "Why do people lose friends as they get older?",
                "How do you deal with people who don't respect you?",
                "How do you stop caring what people think?",
                "What is the smartest way to handle an insult?",
                "How do you say no without guilt?",
             ]},
            {"slug": "people", "name": "People", "lede": "Reading people, trusting people, and knowing when not to.",
             "questions": [
                "How do you know if someone can be trusted?",
                "Why do people ghost?",
                "How do you spot a manipulator early?",
                "Why do people change after they get what they want?",
             ]},
            {"slug": "confidence", "name": "Confidence", "lede": "The real thing, not the performance.",
             "questions": [
                "What makes a person genuinely confident?",
                "Confidence vs arrogance: how do you tell them apart?",
                "Why is confidence attractive?",
                "How do you build confidence after a failure?",
             ]},
            {"slug": "personal-growth", "name": "Personal Growth", "lede": "Getting better at being you.",
             "questions": [
                "Why do intelligent people overthink?",
                "How do you stop overthinking?",
                "Why do smart people procrastinate?",
                "How do you become more disciplined without hating your life?",
             ]},
        ],
    },
    {
        "slug": "technology", "name": "Technology", "emoji": "🤖",
        "lede": "Technology for real life. AI, apps, gadgets and digital habits, explained by someone who has built and run technology for a living.",
        "subs": [
            {"slug": "ai", "name": "AI", "lede": "What it is, what it is not, and how a normal person should use it.",
             "questions": [
                "How can a non-technical person use AI?",
                "AI vs human intelligence: what is the real difference?",
                "Should you learn AI in 2026?",
                "What are the most useful AI tools for everyday life?",
                "Is it safe to share personal information with AI chatbots?",
             ]},
            {"slug": "apps", "name": "Apps", "lede": "Features most people never find.",
             "questions": [
                "10 Google Maps features most people don't use",
                "5 WhatsApp tricks you should know",
                "How to organise your digital life in one weekend",
                "Which apps are actually worth paying for?",
             ]},
            {"slug": "gadgets", "name": "Gadgets", "lede": "What to buy, what to skip, and what I actually use.",
             "questions": [
                "How do you choose a phone without overpaying?",
                "Is a smartwatch worth it?",
                "What gadgets make travel easier?",
             ]},
            {"slug": "digital-life", "name": "Digital Life", "lede": "Privacy, habits and sanity in a connected world.",
             "questions": [
                "How do you reduce screen time without a digital detox?",
                "How do you protect yourself from online scams?",
                "Should you keep your relationship off social media?",
                "How do you travel internationally without paying excessive roaming charges?",
             ]},
        ],
    },
    {
        "slug": "travel-and-living", "name": "Travel & Living", "emoji": "✈️",
        "lede": "Cities, countries, food, books and the lessons that living abroad teaches you about home.",
        "subs": [
            {"slug": "travel", "name": "Travel", "lede": "Hacks and habits from a lot of airports.",
             "questions": [
                "20 things travelling taught me",
                "How do you travel well on a modest budget?",
                "What should every Indian know before their first international trip?",
             ]},
            {"slug": "living-abroad", "name": "Living Abroad", "lede": "What different countries teach you about people.",
             "questions": [
                "What living abroad teaches you about India",
                "10 things I learned after working in different countries",
                "Should you move abroad for your career?",
             ]},
            {"slug": "the-viral-veer-life", "name": "The Viral Veer Life", "lede": "Food, books, cities, failures, and the people I have met.",
             "questions": [
                "Things I wish I knew at 30",
                "What 30 years of working taught me about people",
                "Books that changed how I think",
             ]},
        ],
    },
]

# Flagship articles in the Viral Veer Answer format.
ARTICLES = [
    {
        "slug": "how-to-know-if-someone-likes-you", "pillar": "relationships", "sub": "dating",
        "title": "How do you know if someone genuinely likes you?",
        "description": "Seven consistent signs someone genuinely likes you, the mistakes people make reading them, and Viral Veer's take on why attention is the only real tell.",
        "short": "Someone who genuinely likes you shows consistent interest through their time, attention, communication and actions. Not occasional flirting. Consistency is the tell.",
        "signs_heading": "7 signs someone genuinely likes you",
        "signs": [
            ("They initiate contact.", "Not every time, but regularly. If you are always the one starting the conversation, you are the one carrying the interest."),
            ("They remember details.", "Your exam date, your mother's surgery, the name of the colleague who annoys you. Memory follows attention."),
            ("They make time.", "Busy people make time for what matters. 'I'm busy' for three weeks is an answer, not a delay."),
            ("They ask about your life.", "Curiosity about your world, not just your availability."),
            ("Their actions match their words.", "A plan made is a plan kept. The gap between what someone says and does is the most honest thing about them."),
            ("They include you in the future.", "A concert next month. A wedding they want you at. People do not plan ahead with someone they are unsure about."),
            ("They are consistent.", "Warm on Monday and cold on Thursday is not mystery. It is ambivalence."),
        ],
        "take": [
            "Here is what I have watched happen for decades, in colleges, offices and families. People who like you do not make you decode them. The decoding itself is the signal that something is off.",
            "I have seen very intelligent people spend months building a theory about why someone is distant. The theory is always more complicated than the truth, which is usually this: interest is loud. Disinterest is quiet and polite.",
            "So stop reading tea leaves. Look at where their attention goes when nobody is making them put it anywhere. That is the Attention Test, and it has never lied to me.",
        ],
        "mistakes": [
            "Confusing politeness with interest. Many people, especially in Indian social settings, are warm by default. Warmth to everyone is a personality, not a signal.",
            "Reading one big gesture as proof. One grand birthday message means less than ten ordinary Tuesday conversations.",
            "Explaining away inconsistency. 'They are busy', 'they are shy', 'they have a lot going on'. Sometimes true. Usually not for three months.",
            "Asking friends to interpret screenshots. Your friends will tell you what you want to hear. Their behaviour will tell you the truth.",
        ],
        "faqs": [
            ("How do you know if someone likes you over text?", "Look at who initiates, how quickly they reply when they are free, and whether they ask questions back. Someone interested keeps the conversation alive. Someone polite just answers it."),
            ("Can someone like you and still not make a move?", "Yes, for a while. Fear and timing are real. But if there is no move in a reasonable time, assume the interest is not strong enough to act on, which is the same as not enough."),
            ("What if they are hot and cold?", "Hot and cold is a pattern, not a puzzle. It usually means they like the attention more than they like you, or they have not decided. Either way, you are not the priority."),
            ("Should I just ask them directly?", "Usually, yes. A direct question costs a moment of awkwardness and saves months of guessing. Adults can handle a clear answer."),
        ],
    },
    {
        "slug": "how-to-negotiate-salary-without-losing-the-offer", "pillar": "career", "sub": "salary",
        "title": "How do you negotiate your salary without losing the offer?",
        "description": "A practical salary negotiation method from someone who has made and received hundreds of offers: when to negotiate, what to say, and the lines that get offers pulled.",
        "short": "Negotiate after the offer, not during the interview. Ask once, with a number and a reason, in a friendly tone. Offers almost never get pulled for a polite ask. They get pulled for ultimatums, lies and repeated haggling.",
        "signs_heading": "The 6-step method",
        "signs": [
            ("Wait for the written offer.", "Before the offer you have no leverage. After it, the company has already decided it wants you and spent money getting there."),
            ("Say thank you first, honestly.", "Enthusiasm is leverage. A hiring manager pushes for a candidate who clearly wants to join."),
            ("Ask with a number, not a feeling.", "'I was hoping for something closer to 18 lakh' beats 'is there any flexibility?'. Vague asks get vague answers."),
            ("Give one clean reason.", "A competing offer, the market band for the role, or a specific skill you bring. One reason. Not a list of expenses."),
            ("Ask about the whole package.", "Joining bonus, variable pay, notice-period buyout and review timing are often easier to move than base."),
            ("Ask once, then decide.", "One round, maybe two. People who come back a fourth time look like they will be a difficult employee."),
        ],
        "take": [
            "I have been the person on the other side of the table for a long time. Here is the thing nobody tells candidates: the hiring manager usually wants you to negotiate a little. It confirms their judgment that they picked someone who knows their value.",
            "What I have seen get offers pulled is not the ask. It is the fake competing offer that gets checked, the 'I need an answer in 24 hours' ultimatum, and the candidate who agreed, then came back for more after the paperwork started.",
            "Negotiate like someone who will be working with these people next month. Because you will.",
        ],
        "mistakes": [
            "Negotiating in the first interview. You are not an offer yet. You are a risk.",
            "Anchoring on your current salary. The company does not care what you earn now. It cares about the band for this role and the alternatives it has.",
            "Using personal expenses as the reason. EMIs and school fees are real, but they are your problem, not a reason the company should pay more.",
            "Bluffing. HR teams in India talk to each other more than you think.",
            "Winning the negotiation and losing the relationship. A hard-won extra lakh is not worth a manager who starts you on the back foot.",
        ],
        "faqs": [
            ("Is it rude to negotiate salary in India?", "No. It is expected at mid and senior levels, and increasingly at entry level. Tone matters more than the act."),
            ("How much more should I ask for?", "Ten to twenty percent above the offer is a normal ask if you have a reason. Beyond that you need a competing offer or a rare skill."),
            ("Should I tell them my current CTC?", "You can decline politely. Say you would rather discuss the band for this role. If they insist, give the full number including variable, and move on."),
            ("Can an offer really be withdrawn for negotiating?", "Rarely, and almost always because of how it was done, not that it was done."),
        ],
    },
    {
        "slug": "why-intelligent-people-choose-the-wrong-partner", "pillar": "relationships", "sub": "love",
        "title": "Why do intelligent people sometimes choose the wrong partner?",
        "description": "Smart people are not immune to bad relationship choices. Here is why intelligence can make it worse, and the 3C rule that keeps it honest.",
        "short": "Intelligence helps you solve problems. It does not stop you from choosing one. Smart people rationalise red flags faster, confuse chemistry with compatibility, and are often too proud to admit the early mistake.",
        "signs_heading": "5 reasons intelligence does not protect you",
        "signs": [
            ("Smart people are better at rationalising.", "An intelligent mind can build an airtight explanation for any behaviour. That skill is a liability when the behaviour is a red flag."),
            ("They mistake chemistry for compatibility.", "Chemistry is about how the person makes you feel today. Compatibility is about how the two of you handle a bad Tuesday in year three."),
            ("They choose a project.", "Capable people are drawn to fixing things. A partner is not a thing to fix."),
            ("They under-rate character.", "Looks, success and wit get noticed in the first hour. Character shows up in the first crisis."),
            ("Pride delays the exit.", "Admitting a mistake is harder for people whose identity is built on being right."),
        ],
        "take": [
            "I have watched brilliant engineers, doctors and founders marry people who everyone around them could see were wrong for them. Not because they could not see it. Because they could explain it.",
            "This is why I use a simple filter, the 3C rule: Chemistry, Compatibility, Character. Most people only check the first one, and the first one is the only one that fades.",
            "If you are smart, be smart about this too. Ask yourself: if a friend described this relationship to me, what would I tell them?",
        ],
        "mistakes": [
            "Treating attraction as evidence. It is a starting condition, not a verdict.",
            "Believing you can change someone. You can influence a person who wants to change. You cannot change one who does not.",
            "Ignoring how they treat waiters, drivers and parents. That is the person you will live with once the courtship ends.",
            "Staying because of sunk cost. Three years invested is not a reason to invest a fourth.",
        ],
        "faqs": [
            ("What is the 3C rule?", "Chemistry, Compatibility, Character. A relationship needs all three. Chemistry gets you in. Compatibility keeps the daily life workable. Character keeps you safe when things go wrong."),
            ("Can chemistry grow over time?", "Attraction can deepen with respect and shared life. But if there is zero spark at the start, that is worth taking seriously."),
            ("Is it shallow to care about looks?", "No. It is shallow to care only about looks."),
        ],
    },
    {
        "slug": "how-to-deal-with-a-toxic-boss", "pillar": "career", "sub": "office-politics",
        "title": "How do you deal with a toxic boss?",
        "description": "A step-by-step playbook for surviving and exiting a toxic boss, from someone who has managed, been managed and cleaned up after a few of them.",
        "short": "Document everything, make allies, deliver visibly, and start your exit quietly. Toxic bosses rarely change. Your job is to protect your record and your reputation until you move.",
        "signs_heading": "The 6-step playbook",
        "signs": [
            ("Confirm it is toxic, not just tough.", "A demanding boss raises your standard. A toxic one lowers your self-respect. Yelling, credit theft, humiliation and moving goalposts are toxic."),
            ("Write things down.", "Dates, instructions, outcomes. Email summaries after verbal instructions. This is not paranoia. It is insurance."),
            ("Make your work visible beyond them.", "Share updates with stakeholders, present your own work, keep a relationship with the skip-level manager."),
            ("Build allies, not a rebellion.", "Peers and seniors who have seen your work are your reference letters. A coup is a career risk."),
            ("Decide your line and your deadline.", "What behaviour you will not accept, and how long you will give it. Without a deadline, people stay for years."),
            ("Exit on your terms.", "Start looking before you must. Leave with a good last project, not a resignation written in anger."),
        ],
        "take": [
            "In my experience, a toxic boss is almost never fixed by HR, by feedback or by time. They are usually fixed by the organisation when the damage becomes expensive, which can take years. You do not have years.",
            "The mistake I see most often is good people waiting for justice. The smarter play is to treat the situation as a problem to be managed and exited, not a wrong to be righted.",
            "And one more thing. Do not become the story. The person who complains loudly about their boss is remembered as the complainer, not the victim.",
        ],
        "mistakes": [
            "Confronting them publicly. You will lose, even if you are right.",
            "Going to HR without documentation. HR protects the company, and the company has already bet on your boss.",
            "Dropping your performance to protest. The only record that follows you is your work.",
            "Venting to colleagues. It will reach them, usually with embellishments.",
        ],
        "faqs": [
            ("Should I complain to HR about my boss?", "Only with a clear, documented pattern and a specific ask. And only after you have thought about what happens if nothing changes."),
            ("Should I quit without another job?", "Only if your health is at risk or you have real savings. Otherwise, a quiet search while employed is almost always better."),
            ("How do I explain leaving in an interview?", "Keep it about growth, not grievance. 'I had learned what I could in that role' works. Bad-mouthing a former boss is a red flag to any interviewer."),
        ],
    },
    {
        "slug": "why-people-lose-friends-as-they-get-older", "pillar": "life", "sub": "zindagi-ke-smart-tips",
        "title": "Why do people lose friends as they get older?",
        "description": "Losing friends in your 30s and 40s is normal and partly healthy. Here is why it happens, which friendships are worth keeping, and how to make new ones after 35.",
        "short": "Friendship runs on proximity, repetition and shared stage of life. Adulthood removes all three. Most friendships were built on circumstance, and when the circumstance ends, so does the friendship. The ones built on character survive.",
        "signs_heading": "5 reasons friendships fade",
        "signs": [
            ("Proximity disappears.", "College friends saw each other every day. Now you need a calendar invite."),
            ("Life stages split.", "The friend with twins and the friend who is single have very different Saturdays."),
            ("Energy gets rationed.", "Work, marriage, parents and children take the hours friendship used to get."),
            ("People grow in different directions.", "Values shift. Some friendships were held together by who you used to be."),
            ("Nobody initiates.", "Both people assume the other is busy. Silence becomes the default."),
        ],
        "take": [
            "I have moved cities and countries several times. Each move taught me the same thing: most friendships are rented, not owned. That sounds harsh. It is actually freeing.",
            "A handful of people stayed through every move, every job, every phase. What they had in common was not history. It was character. They showed up when it was inconvenient.",
            "So do not mourn the hundred. Invest in the five. And be the one who sends the message first, because the other person is thinking the same thing you are.",
        ],
        "mistakes": [
            "Keeping score. Friendship is not a ledger of who called last.",
            "Expecting the college version of a friend to still exist. People change. Meet the current version.",
            "Not making new friends after 35 because 'it is awkward'. It is awkward for everyone. Do it anyway.",
            "Confusing acquaintances on social media with friends. Likes are not presence.",
        ],
        "faqs": [
            ("Is it normal to have very few friends in your 40s?", "Yes. Research on social networks consistently shows the number of close friends shrinks with age. Quality matters more than count."),
            ("How do you make friends after 35?", "Through repetition. Join something that meets weekly: a sport, a class, a volunteer group. Friendship is a side effect of showing up repeatedly."),
            ("Should I reconnect with old friends?", "If you miss them, yes. A simple 'thought of you today' message is enough. The worst case is a polite reply."),
        ],
    },
    {
        "slug": "how-will-ai-change-jobs", "pillar": "career", "sub": "ai-and-careers",
        "title": "How will AI change jobs?",
        "description": "A technology leader's plain-language view on how AI changes jobs: which tasks go first, which roles grow, and the three moves every professional should make this year.",
        "short": "AI will not replace most jobs this decade. It will replace the parts of jobs that are repeatable, written and checkable. The people at risk are not in any one profession. They are the people who do only the repeatable part of their profession.",
        "signs_heading": "What actually changes",
        "signs": [
            ("Tasks go before jobs.", "Drafting, summarising, first-pass analysis, routine code and customer replies are already being handed to AI. The job remains. Its shape changes."),
            ("Junior work gets squeezed.", "The entry-level tasks that trained people for twenty years are the easiest to automate. Companies will have to rethink how juniors learn."),
            ("Judgment becomes the premium.", "Knowing which answer is right, which client to call, and which risk to take. AI gives you options. Someone still has to choose."),
            ("Generalists with tools beat specialists without them.", "A marketer who can use AI for analysis outperforms a pure analyst who refuses to."),
            ("New roles appear quietly.", "Nobody announces them. Someone in a team starts doing it, and two years later it has a title."),
        ],
        "take": [
            "I have run technology teams through several waves: outsourcing, cloud, mobile. Every wave had the same two groups. People who learned the new tool early and became more valuable, and people who waited for it to blow over.",
            "This wave is faster and wider, but the pattern holds. The question is not 'will AI take my job?'. It is 'will someone using AI take my job?'. That is a question you can actually act on.",
            "Three moves this year: use AI daily for real work, not demos. Get better at the human parts, which means judgment, relationships and taste. And move closer to where money is made in your company, because those roles are protected last.",
        ],
        "mistakes": [
            "Waiting for the hype to settle. It will not, and the skill gap compounds.",
            "Learning AI as theory. Courses on machine learning are not the same as using the tools in your actual job.",
            "Assuming your profession is safe because it needs a licence. Licences protect the signature, not the hours of work behind it.",
            "Panicking. Fear makes people freeze. Curiosity makes them useful.",
        ],
        "faqs": [
            ("Which jobs are most vulnerable to AI?", "Roles built mostly on producing text, summaries, routine code, basic analysis or scripted customer support. The vulnerability is in the task mix, not the title."),
            ("Will AI replace programmers?", "It will replace a lot of programming. Programmers who understand systems, users and trade-offs will be more valuable, not less."),
            ("What should students learn in the AI era?", "Fundamentals of their field, how to use AI tools fluently, and how to communicate and persuade. The last one is the most under-taught."),
            ("Should a non-technical person learn AI?", "Yes, as a user, not a builder. Learn to ask good questions, verify answers and build small workflows. That is enough to be ahead of most colleagues."),
        ],
    },
]

# Viral Veer Explains
EXPLAINS = [
    ("why-people-ghost", "Why people ghost", "Ghosting is rarely about you. It is about the ghoster's inability to handle a small, uncomfortable conversation. Avoidance is a habit, not a verdict."),
    ("why-people-cheat", "Why people cheat", "Opportunity, unmet needs and low character, in varying mixes. Most cheating starts as an ego fix, not a love story."),
    ("why-people-fall-out-of-love", "Why people fall out of love", "Love does not usually die in a fight. It dies in a thousand ordinary evenings where nobody made an effort."),
    ("why-smart-people-procrastinate", "Why smart people procrastinate", "Smart people can see all the ways a task could go wrong, so they delay starting. Perfectionism dressed up as planning."),
    ("why-office-politics-exists", "Why office politics exists", "Because organisations have limited rewards and unlimited ambition. Politics is how humans allocate scarce things. You can refuse to play, but you cannot refuse to be affected."),
    ("why-people-hate-their-jobs", "Why people hate their jobs", "Usually three things: no control, no progress, or a bad manager. Pay is rarely the first reason, though it is the most common excuse."),
    ("why-confidence-is-attractive", "Why confidence is attractive", "Confidence signals that someone can handle themselves, so you will not have to. It is attractive for the same reason competence is."),
    ("why-money-does-not-always-make-people-happy", "Why money does not always make people happy", "Money removes certain miseries. It does not add meaning. People who expect it to do both are disappointed on schedule."),
]

# Viral Veer vs
VERSUS = [
    ("love-vs-attraction", "Love vs Attraction", "Attraction is what pulls you in. Love is what keeps you in when the pull fades.", "Attraction is fast, physical and involuntary. Love is slow, chosen and built. Confusing the two is how people end up married to a feeling."),
    ("confidence-vs-arrogance", "Confidence vs Arrogance", "Confidence does not need you to be smaller. Arrogance does.", "Confident people are comfortable being wrong. Arrogant people cannot afford it. Watch how someone handles correction and you will know which one you are dealing with."),
    ("chemistry-vs-compatibility", "Chemistry vs Compatibility", "Chemistry is the first date. Compatibility is the fourth year.", "Chemistry is how you feel together. Compatibility is how you function together. A long relationship needs both, but only one of them can be built on purpose."),
    ("career-vs-job", "Career vs Job", "A job pays you for your hours. A career pays you for your direction.", "A job is a transaction. A career is a sequence of jobs chosen with intent. Most people have a job and call it a career. The difference shows up at 45."),
    ("experience-vs-qualifications", "Experience vs Qualifications", "Qualifications open the door. Experience decides what you do in the room.", "Early in a career, qualifications matter more because there is nothing else to judge. After ten years, nobody asks about your degree. They ask what you have done."),
    ("ai-vs-human-intelligence", "AI vs Human Intelligence", "AI is very good at answering. Humans are still better at asking.", "AI recombines what exists, fast and tirelessly. Humans decide what matters, take responsibility and act under uncertainty. The combination is the point."),
    ("friendship-vs-relationship", "Friendship vs Relationship", "A relationship without friendship is a transaction with feelings.", "The best relationships are friendships with attraction added. The worst are attractions with friendship missing. If you cannot sit in silence with someone, be careful."),
    ("dating-vs-courtship", "Dating vs Courtship", "Dating explores. Courtship decides.", "Dating is open-ended and low-commitment by design. Courtship has a destination. Problems start when one person is dating and the other is courting."),
]

# Viral Veer Dictionary
DICTIONARY = [
    ("the-3c-rule", "The 3C Rule", "Chemistry + Compatibility + Character.", "The three things a relationship needs. Chemistry gets you in, compatibility keeps daily life workable, character keeps you safe when things go wrong. Most people only check the first one."),
    ("the-3r-rule", "The 3R Rule", "Respect + Reliability + Reciprocity.", "The minimum standard for any relationship worth keeping, romantic or professional. Remove any one and the relationship becomes a slow-motion exit."),
    ("the-career-ceiling", "The Career Ceiling", "The point where technical competence stops producing career growth.", "Usually arrives around the senior-manager level. Beyond it, growth comes from judgment, relationships and the ability to make others successful. Many excellent engineers hit it without realising why."),
    ("the-attention-test", "The Attention Test", "Where someone's attention goes when nobody is directing it reveals their priorities.", "People can say anything. Attention is expensive and finite, so where it goes is honest. Works for partners, bosses and friends."),
    ("the-exit-test", "The Exit Test", "A relationship, job or situation has reached its natural end when you are staying for reasons that have nothing to do with it.", "Sunk cost, fear of the unknown, what people will say. If every reason to stay is about the leaving and none is about the staying, the answer is already in."),
    ("rented-friendships", "Rented Friendships", "Friendships held together by circumstance rather than character.", "College, a job, a neighbourhood. When the circumstance ends, the friendship goes with it. Not a tragedy. Just a lease that expired."),
    ("the-tuesday-test", "The Tuesday Test", "Judge a relationship by an ordinary Tuesday, not by birthdays and holidays.", "Anyone can perform on a special day. The real relationship is how two people treat each other on a tired weekday with nothing to celebrate."),
    ("quiet-exit", "Quiet Exit", "Leaving a bad situation on your own terms, without drama, with your record intact.", "The opposite of the dramatic resignation or the public breakup. Takes more discipline and leaves fewer scars."),
]

# Media appearances (placeholders until real coverage is added).
MEDIA = [
    {"slug": "modern-dating-podcast", "title": "Viral Veer on why modern dating is getting harder", "outlet": "Podcast appearance", "date": "2026", "topic": "Relationships", "summary": "A long-form conversation on dating apps, attention and why intelligent people struggle with modern dating.", "url": "#"},
    {"slug": "ai-and-executive-careers", "title": "Viral Veer on how AI is changing executive careers", "outlet": "Business media", "date": "2026", "topic": "Career", "summary": "What senior professionals should do this year, and which roles are protected last.", "url": "#"},
    {"slug": "living-abroad-india", "title": "Viral Veer on what living in different countries teaches you about people", "outlet": "Lifestyle feature", "date": "2026", "topic": "Life", "summary": "Lessons from working across countries and what they reveal about India.", "url": "#"},
]

ASK_CATEGORIES = [
    ("❤️", "Relationships"), ("💼", "Career"), ("🧠", "Life"), ("🤖", "Technology"),
    ("💰", "Money"), ("✈️", "Travel"), ("👨‍👩‍👧", "Family"), ("🔥", "Dating"),
]

ASK_SAMPLES = [
    ("I'm 35 and afraid I'll never find the right partner. What should I do?", "Relationships",
     "Fear is doing the choosing for you. At 35 you have more clarity, more money and more self-knowledge than at 25. Use them. Stop treating every date as an audition for marriage, widen where you meet people, and be honest early about what you want. The right partner is usually found by people who are living a full life, not by people who are waiting."),
    ("My manager keeps taking credit for my work. Do I confront him?", "Career",
     "Not publicly, and not emotionally. Make your work visible before it reaches him: send the deck yourself, copy the stakeholder, present your own numbers. Credit theft only works in the dark. Then decide your deadline. If visibility does not fix it in six months, it will not fix it at all."),
    ("Should I learn AI or is it too late?", "Technology",
     "It is not too late. Most people have not started. You do not need a course. Pick one real task from your job this week and do it with an AI tool. Repeat daily for a month. That puts you ahead of most of your colleagues."),
]

EPISODES = []
