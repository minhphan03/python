async def reply_bot():
    print("retrieving mentions")
    search_query = '@thevocabbot'
    for tweet in api.search(q=search_query, count=2):
        try:
            if (datetime.datetime.now() - tweet.created_at).total_seconds() < 3600 * 24:
                text = re.search(r'\s*(?<=(@thevocabbot)).*', tweet.text)
                result = "@" + tweet.user.screen_name + " " + webscraping(text.group().strip().split())
                api.update_status(result)
            else:
                print("false")
        except tweepy.TweepError as e:
            print(e)


def webscraping(word):
    try:
        link = "https://www.merriam-webster.com/dictionary/" + "+".join(word)
        r = requests.get(link)
        c = r.content

        soup = BeautifulSoup(c, 'html.parser')
        allcontent = soup.find('div', attrs={'class': 'vg'})

        content = allcontent.findAll('span', attrs={'class': 'dtText'})
        if len(content) > 3:
            content = content[:3]
        strings = []

        for i in content:
            text = re.search(":\s.*", i.get_text()).group().strip()[2:]
            if re.search(r"sense \w+", i.get_text()) is not None:
                print(re.search(r"sense \w+", i.get_text()).group())
                text = re.sub(re.search(r"sense \w+", i.get_text()).group(), "", text)
            strings.append(text)

        return " ".join(word) + ": " + "; ".join(strings) + ". See more at " + link

    except requests.exceptions:
        return "This word does not exist in Merriam Webster. Please look up manually or check your grammar. DM me if you have any request."

