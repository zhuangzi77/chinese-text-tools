#regexes_Chinese.py
'''Some regexes (regular expressions) useful for working with Chinese texts.
Most can be used with the find and replace function OpenOffice,
but the Use Regular Expressions box must be checked.
Remove the r before the quotations when using in OpenOffice'''

import re

#Select all Chinese characters.
all_chars = r'[\u4E00-\u9FA5]+'

#Select all Chinese characters and newlines.
#\n indicates a newline.  The pipe character | means 'or'.
all_chars_and_new_lines =  r'[\u4E00-\u9FA5|\n]+'

all_chars_and_punc = r'[\u4E00-\u9FA5|，|。|：|(|)|《|》|】|【|〞|〝|\d|‘|’]+'

#Select everything but Chinese characters.
not_chars = r'[^\u4E00-\u9FA5]+'

#Select everything but Chinese characters or new lines.
not_chars_or_new_lines = r'[^\u4E00-\u9FA5|\n]+'

#Select chunks of text in brackets.
#This can be used to mark up text and generate a vocab list.
#It saves a lot of cutting and pasting.
in_brackets = '<.*>'

#Select the main commentary of a text, from character 注 to next newline. 
main_commentary = r'【注】.*'

#Select subcommentary of a text, from character 疏 to next newline.
sub_commentary = r'【疏】.*'

#Select names, followed Chinese characters, and a date.
names = r'[A-Za-z]+\s[A-Za-z]+’?s?\s?[\u4E00-\u9FA5]{1,4} \(.{1,24}\)'

#These functions can be used to get or delete any of the above regexes.
def get_regex (regex, string):
    """Returns all instances of a certain regex as a string."""
    regex_obj = re.compile(regex) 
    result = regex_obj.findall(string)
    result = ''.join(result)
    return result

def delete_regex(regex, string):
    """Deletes all instances of a regex in a string."""
    regex_obj = re.compile(regex)
    result = re.sub(regex,'',string)
    return result




#Section below is for testing.
#NB: Because of the new lines in the string, the matches will be short.
test_str = '''  According to the exegete and poet Wang Yi’s 王逸 (fl. 89–158)
Eastern Han commentary on the Chuci,
the transmitted versions of the “Nine Songs” included a symbolic element,
with gods acting as celestial models for ideal rulers.
These songs (or lost songs like them) were the basis for the “Li sao” 離騷
(The Sorrow of Exile)1 attributed to the tragic figure Qu Yuan 屈原(c. 347-c. 277),
perhaps the best known of all the loyal and
talented yet frustrated ministers in the whole of the Chinese tradition.'''

test_str_Chinese ='''{化而為鳥，其名為<鵬, peng2, large mythical bird> 。}@
【注】鵬鯤之實，吾所未詳也。夫莊子之大意，在乎逍遙遊放，無為而自得，故極小大之致以明性分之適。達觀之士，
宜要其會歸而遺其所寄，不足事事曲與生說。自不害其弘旨，皆可略之耳。@
【疏】夫四序風馳，三光電卷，是以負山岳而捨故，揚舟壑以趨新。故化魚為鳥，欲明變化之大理也。@
【釋文】《鵬》步登反。徐音朋。郭甫登反。崔音鳳，云：鵬即古鳳字，非來儀之鳳也。說文云：
朋及鵬，皆古文鳳字也。朋鳥象形。鳳飛，群鳥從以萬數，故以朋為朋黨字。字林云：鵬，朋黨也，古以為鳳字。◎盧文弨曰：
以朋舊作以鵬，今案文義（政）〔改〕正。◎慶藩案廣川書跋寶龢鍾銘、通雅四十五並引司馬云：鵬者鳳也。釋文闕。
《夫莊》音符。發句之端皆同。《性分》符問反。下皆同。《達觀》古亂反。《宜要》一遙反。'''

all_regexes = [all_chars,
               all_chars_and_new_lines,
               all_chars_and_punc,
               not_chars,
               not_chars_or_new_lines,
               in_brackets,
               names,
               main_commentary,
               sub_commentary]

#This loop test each regex.
##for i in all_regexes:
##    print (get_regex(i, test_str))
##    print (delete_regex(i, test_str))
##for i in all_regexes:
##    print (get_regex(i, test_str_Chinese))
##    print (delete_regex(i, test_str))


