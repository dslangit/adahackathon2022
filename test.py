import re

if __name__ == '__main__':
    post = "Reform health care to serve www.baidu.com patients, not corporate medicine http://t.co/WMKJKU4hl7 @PNHP #SinglePayerSunday https://t.co/i4bNrruUNS wty"
    #post=re.sub(r'\s*(?:https?://)?www\.\S*\.[A-Za-z]{2,5}\s*', ' ', post).strip()
    s = "@ClareDalyMEP  Strategic Psychobabble (Andrei Martyanov) | The Vineyard of the Saker https://t.co/YjOQPk6HTJ"
    post = re.sub(r'http://\S+ ', '', post)
    post = re.sub(r'http://\S+\n', '', post)
    post = re.sub(r'http://\S+', '', post)
    post = re.sub(r'https://\S+ ', '', post)
    post = re.sub(r'https://\S+\n', '', post)
    post = re.sub(r'https://\S+', '', post)
    s = re.sub(r'www\.\S+\.com', '', s)
    #print(' '.join(item for item in post.split() if not (item.startswith('http://') and item.endswith(' ') and len(item) > 7)))
    print(s)
