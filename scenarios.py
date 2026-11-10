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

MY_WRITING = [
    # 1
    "I’m definitely not in the best place of my whole life right now since it's daylight savings time, this is the first time I feel like that this is winter.",
    # 2
    "Recently, I have been really hard on myself. I refused to spend any money eating out and has been taking a toll on my mental health.",
    # 3 (plain)
    "I drive to work and I'm kind of regretting choosing this apartment because it's around 20 minutes of a drive to my office.",
    # 4 (plain)
    "I really wish I could achieve my goal of learning Spanish next year because learning language is a very fulfilling experience.",
    # 5
    "I sign up for the Finnish dinner date, hoping that I can have a chance to visit Finland with expenses covered.",
    # 6
    "Seeing a therapy doesn't necessarily make your life easier, sometimes it's stress people's last result because they have nobody else to talk about problems in their lives.",
    # 7
    "The joy of making food and tasting it slowly fades away as life gets busier.",
    # 8
    "My life is a swirl of things full of unexpected side quests and unforeseen challenges.",
    # 9 (plain)
    "I really like Natalie Lynn because I think she is a really cool YouTuber and filmmaker.",
    # 10 (plain)
    "I'm trying to learn chess, but I don't think I'm smart enough.",
]

AI_CLEAR = [
    "Time management is an essential skill for students and professionals alike. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can significantly improve their productivity. Additionally, taking regular breaks helps maintain focus and prevents burnout. Ultimately, effective time management leads to better outcomes and a healthier work-life balance.",
    "Climate change is one of the most pressing challenges facing our world today. Rising temperatures, melting ice caps, and extreme weather events are having a significant impact on ecosystems and communities. To address this issue, governments, businesses, and individuals must work together to reduce emissions and invest in sustainable solutions.",
    "Regular exercise offers numerous benefits for both physical and mental health. It strengthens the heart, improves sleep quality, and boosts overall energy levels. Furthermore, physical activity has been shown to reduce stress and anxiety. Incorporating even a small amount of exercise into your daily routine can make a meaningful difference.",
    "Social media has transformed the way people communicate and share information. While it offers opportunities for connection and creativity, it also presents challenges such as misinformation and privacy concerns. It is important for users to approach social media thoughtfully and to be mindful of the content they consume and share.",
    "Reading is a valuable habit that can enrich your life in many ways. It expands your knowledge, improves your vocabulary, and enhances your critical thinking skills. In addition, reading can be a great way to relax and reduce stress. Whether you prefer fiction or nonfiction, making time to read is a worthwhile investment.",
]

# Lightly edited AI: 2–3 changes each (word swap, a typo, or one short added sentence)
AI_EDIT = [
    # "can open many doors" -> "a lot of doors"; "Moreover" -> "Also"; typo "consistant"
    "Learning a new language can open a lot of doors, both personally and professionally. It allows you to connect with people from different cultures and broadens your perspective. Also, studies suggest that bilingualism can improve memory and cognitive flexibility. With consistant practice and the right resources, anyone can make progress.",
    # "foundation" -> "basis"; typo "procesed"; added last sentence
    "Healthy eating is the basis of a balanced lifestyle. A diet rich in fruits, vegetables, whole grains, and lean proteins provides the nutrients your body needs. It is also important to stay hydrated and limit procesed foods. Small, sustainable changes are often more effective than drastic diets. I'm still bad at this part.",
    # "crucial" -> "a really big"; typo "eachother's"; "difficult times" -> "hard weeks"
    "Teamwork plays a really big role in the success of any organization. When team members communicate openly and respect eachother's ideas, they can solve problems more effectively. Strong teams also share responsibility and support one another during hard weeks. Building trust is key to creating a positive team environment.",
    # "essential" -> "super important"; "Establishing" -> "Having"; added "I never get that much."
    "Sleep is super important for overall health and well-being. During sleep, the body repairs itself and the brain processes information from the day. Adults should aim for seven to nine hours of sleep each night. I never get that much. Having a consistent bedtime routine can help improve sleep quality.",
    # "rewarding" -> "nice"; typo "comunity"; "countless" -> "lots of"
    "Volunteering is a nice way to give back to your comunity. It allows you to develop new skills, meet new people, and make a positive impact. Many volunteers also report feeling happier and more fulfilled. There are lots of opportunities available, so it is easy to find a cause that matters to you.",
]

# Clearly human: my own thesis abstract, split into five consecutive pieces (verbatim)
HUMAN_CLEAR = [
    "Green development is one of the important agendas for China's current development, and green finance, as a combination of finance and the real economy, has been the focus of economists. Green credit is an important part of green finance, which means that banks and other financial institutions encourage enterprises to green their transformation and reduce pollution emissions by means of preferential lending rates and other means.",
    "By assessing whether the export resilience of Chinese regions after the implementation of the green credit policy is related to the share of environmental credit programs, it can better provide certain suggestions for the future development of local enterprises, and can enrich the research in the field of cross-study between finance and international economics and trade. This paper combs through the past literature related to green credit, export resilience and export competitiveness in the study of green finance, and reviews them.",
    "In order to study the relationship between green credit and export resilience, this paper constructs a green credit index by selecting the credit share data of environmental protection projects at the prefecture and municipal levels from 2010 to 2022, draws on the variable construction method of Jin Zehu (2024), and constructs regional export resilience indexes by using a comprehensive index evaluation system from the aspects of export resistance and resilience and reconstruction capacity, and after many screening and extrapolating, adds the population After several screenings and refinements, adding population size, level of economic development and other control variables, and using the double fixed effects model and the moderating effects model, the study explores the impact of green credit on export resilience.",
    "It is found that green credit has a significant positive impact on export toughness, and this impact affects export toughness through the moderating effect of the degree of financial development, and this result passes the robustness test.",
    "In the heterogeneity test analysis, this paper finds that there are inter-regional differences in the causal relationship between green credit and export toughness, and the differences are more obvious.",
]

SCENARIOS = [
    {
        "name": "c1 own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },
    {
        "name": "c2 spread",
        "criterion": 2,
        # first 5 are AI, last 5 are human
        "texts": AI_CLEAR + HUMAN_CLEAR,
    },
    {
        "name": "c3 coverage",
        "criterion": 3,
        # 1-5 clearly AI, 6-10 clearly human, 11-15 lightly edited AI
        "texts": AI_CLEAR + HUMAN_CLEAR + AI_EDIT,
    },
    {
        "name": "c4 bad input",
        "criterion": 4,
        "bodies": [
            {"creator_id": "eval_bad_missing"},                       # no text field
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t ", "creator_id": "eval_bad_space"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": "Hi", "creator_id": "eval_bad_short"},            # under 3 tokens -> 422
            {"text": "word " * 4001, "creator_id": "eval_bad_huge"},  # 20,005 chars -> 413
        ],
    },
    # Criterion 5 (appeals) is tested by hand with a separate script,
    # because run_eval.py can't submit and then appeal the content_id it got back.
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
