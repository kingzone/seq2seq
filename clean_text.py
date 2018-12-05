#! -*- coding: utf-8 -*-
import re


def clean_text(comment_text):
    comment_list = []
    for text in comment_text:
        # 将单词转换为小写
        text = text.lower()
        # 删除非字母、数字字符
        text = re.sub(r"[^A-Za-z0-9(),!?@&$\'\`\"\_\n]", " ", text)
        text = re.sub(r"\n", " ", text)

        # 恢复常见的简写
        text = re.sub(r"what's", "what is ", text)
        text = re.sub(r"\'s", " ", text)
        text = re.sub(r"\'ve", " have ", text)
        text = re.sub(r"can't", "can not ", text)
        text = re.sub(r"cannot", "can not ", text)
        text = re.sub(r"n't", " not ", text)
        text = re.sub(r"i'm", "i am ", text)
        text = re.sub(r"\'re", " are ", text)
        text = re.sub(r"\'d", " would ", text)
        text = re.sub(r"\'ll", " will ", text)

        # 恢复特殊符号的英文单词
        text = text.replace('&', ' and')
        text = text.replace('@', ' at')
        text = text.replace('$', ' dollar')

        comment_list.append(text)
    return comment_list


# train["clean_comment_text"] = clean_text(train['comment_text'])
# test['clean_comment_text'] = clean_text(test['comment_text'])

s1 = u'When someone commits a murder they typically go to extreme lengths to cover up their brutal crime. The harsh prison sentences that go along with killing someone are enough to deter most people from ever wanting to be caught, not to mention the intense social scrutiny they would face.\nOccasionally, however, there are folks who come forward and admit guilt in their crime. This can be for any number of reasons, like to gain notoriety or to clear their conscience, though, in other instances, people do it to come clean to the people they care about.\nWhen Rachel Hutson was just 19 years old, she murdered her own mother in cold blood. As heinous and unimaginable as her crime was, it was what she did after that shocked people the most\u2026\n\nRachel was just a teenager when she committed an unthinkable act against her own other\u2026\nWhile that in and of itself was a heinous crime, it\u2019s what Rachel did in the aftermath of her own mother\u2019s murder that shook people to their core. You\u2019re not going to believe what strange thing she decided to do next\u2026\nIt\u2019s hard to understand what drove Rachel to commit this terrible act, but sending the photo afterward seems to make even less sense.\nShare this heartbreaking story with your friends below.'
s2 = u"James Milner may not be one of the most exciting players in world football but he is one of the most effective, as underlined by the fact that the Liverpool ace is on the verge of making Champions League history.\nAhead of his side's semi-final first-leg meeting with Roma at Anfield, the England international needs just one more assist to break the tournament's all-time record for a single season.\n\nIndeed, Milner has already created eight goals during the Reds' remarkable run to the last four \u2013 three more than his nearest rivals, team-mate Roberto Firmino and Luis Suarez of the already-eliminated Barcelona.\nShould the 32-year-old midfielder turn provider again against Roma, he will claim outright possession of the record from Neymar and Wayne Rooney, both of whom racked up seven assists, in 2016-17 and 2013-14, respectively.\nMilner's achievement is made all the more remarkable for the fact that he has played only 611 minutes \u2013 fewer than both Neymar (797) and Rooney (765).\nHe actually started Liverpool's Champions League campaign on the bench, failing to see any game time in the draws with Sevilla and Spartak Moscow.\nHowever, as soon as he was added to Jurgen Klopp's starting line-up, the Reds began winning, with Milner racking up an assist in both the away and home wins over Maribor. Milner set up three goals in the 7-0 demolition of Spartak, which saw Liverpool progress to the knockout stage as winners of Group E.\nMilner teed Firmino up for Liverpool's fourth in their 5-0 win at Porto in the last 16 before doing likewise for Alex Oxlade-Chamberlain in the rousing 3-0 victory over Manchester at Anfield in the quarter-finals.\n\nAs a result, the Reds' unlikely hero is now poised to do something no player has ever done before in Champions League history!\n"
s1 = clean_text([s1])[0]
s2 = clean_text(s2)
print s1
print s2
