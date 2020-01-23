#!/usr/bin/python3

import csv
import json

words = {}
sources = {}

with open('metaWords.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        word_id = int(row[0])
        words[word_id] = {
            "na'vi": row[1],
            "ipa": row[2],
            "infixes": row[3],
            "type": row[4],
            "translations": {}
        }

def mapTranslated(code):
    if code == "eng":
        return "en"
    elif code == "est":
        return "et"
    else:
        return code

with open('localizedWords.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        word_id = int(row[0])
        words[word_id]["translations"][mapTranslated(row[1])] = row[2]

def getWordType(word, t):
    if word == "si":
        return "v:si"
    
    if word.endswith(" si"):
        return "n:si"
    
    if t == "n.":
        return "n"
    if t == "prop.n.":
        return "n:pr"
    if t == "pn.":
        return "pn"
    if t == "adj.":
        return "adj"
    if t == "num.":
        return "num"
    if t == "adv.":
        return "adv"
    if t == "adj., adv.":
        return ["adj", "adv"]
    if t == "n., adv." or t == "adv., n.":
        return ["n", "adv"]
    if t == "adp.":
        return "adp"
    if t == "intj.":
        return "intj"
    if t == "n., intj.":
        return ["n", "intj"]
    if t == "adv., intj.":
        return ["adv", "intj"]
    if t == "part." or t == "part., intj.":
        return "part"
    if t == "conj.":
        return "conj"
    if t == "pn., sbd.":
        return "ctr"
    elif t == "v.":
        return "v:?"
    elif t == "vin." or t == "svin.":
        return "v:in"
    elif t == "vtr." or t == "vtr., vin." or t == "vin., vtr.":
        return "v:tr"
    elif t == "vim.":
        return "v:m"
    elif t == "vtrm.":
        return ["v:tr", "v:m"]
    elif t == "ph.":
        return "phr"
    
    raise ValueError("word type {} of {} unknown".format(t, word))

def getPronunciation(word, ipa):
    wordDashed = ''
    stressed = 1
    infixes = ''
    
    if word.endswith(" si"):
        word = word[:-3]
        ipa = "".join(ipa.split(" ")[:-1])
    if " " in word:
        # ignore multi-word entries
        raise ValueError("multi-word entry")
    if '] or [' in ipa:
        # those have several stress patterns
        raise ValueError("several pronunciations allowed")
    elif word == 'Jakesully':
        # ... seriously?
        raise ValueError("Jakesully lu skxawng")
    elif word == 'fìtseng':
        # has weird parentheses fitseng(e)
        wordDashed = 'fì-tseng'
        stressed = 2
    elif word == 'fìtsenge':
        wordDashed = 'fì-tse-nge'
        stressed = 2
    elif word == 'srak':
        wordDashed = 'srak'
        stressed = 1
    elif word == 'srake':
        wordDashed = 'sra-ke'
        stressed = 1
    elif word == 'talun':
        wordDashed = 'ta-lun'
        stressed = 2
    elif word == 'taluna':
        wordDashed = 'ta-lun-a'
        stressed = 2
    elif word == 'taweyk':
        wordDashed = 'ta-weyk'
        stressed = 2
    elif word == 'taweyka':
        wordDashed = 'ta-wey-ka'
        stressed = 2
    elif word == 'tseng':
        wordDashed = 'tseng'
        stressed = 1
    elif word == 'tsenge':
        wordDashed = 'tse-nge'
        stressed = 1
    elif word == 'stxenutìng':
        # has , as syllable marker :o
        wordDashed = 'stxe-nu-tìng'
        stressed = 1
        infixes = 'stxenut..ìng'
    elif word == 'tompakel':
        wordDashed = 'tom-pa-kel'
        stressed = 1
    elif word == 'swaynivi':
        wordDashed = 'sway-ni-vi'
        stressed = 1
    elif word == 'ningyen':
        wordDashed = 'ning-yen'
        stressed = 1
    elif word == 'tìreyn':
        # has a + in front of the ipa :O
        wordDashed = 'tì-reyn'
        stressed = 2
    elif word == 'lì\'uvi':
        # has a spurious ' :O!
        wordDashed = 'lì-\'u-vi'
        stressed = 1
    elif word == 'fkxara':
        # has a weird character instead of k' :O!!
        wordDashed = 'fkxa-ra'
        stressed = 1
    elif word == 'fkxaranga\'':
        wordDashed = 'fkxa-ra-nga\''
        stressed = 1
    elif word == 'txeptun':
        wordDashed = 'txep-tun'
        stressed = 1
    elif word == 'tsyänel':
        # no stress marker :O!!!
        wordDashed = 'tsyä-nel'
        stressed = 1
    elif word == 'tìtxantslusam':
        # is just plain wrong :O!!!!
        wordDashed = 'tì-txan-tslu-sam'
        stressed = 2
    elif word == 'kintrram':
        wordDashed = 'kin-trr-am'
        stressed = 1
    elif word == 'kintrray':
        wordDashed = 'kin-trr-ay'
        stressed = 1
    else:
        syllable = 1
        i = 0
        for letter in ipa:
            if letter == 'ˈ':
                # this is the stressed syllable
                stressed = syllable
            elif letter == '.':
                # start of a new syllable
                syllable += 1
                wordDashed += '-'
            elif letter in '·':
                # infix position
                infixes += '.'
            elif letter in '\u0361\u031A¦\u02CC':
                # IPA nonsense, ignore
                pass
            elif letter == 'ŋ':
                # can correspond to two letters ('ng') but not in e.g. 'zenke'
                wordDashed += word[i]
                infixes += word[i]
                i += 1
                if word[i] == 'g':
                    wordDashed += word[i]
                    infixes += word[i]
                    i += 1
            else:
                wordDashed += word[i]
                infixes += word[i]
                i += 1
    
    if infixes.count('.') == 1:
        infixes = infixes.replace('.', '..')
    return (wordDashed, stressed, infixes)

with open('sources.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        if len(row) == 2:
            word_id = int(row[0])
            sources[word_id] = row[1]

typeErrors = 0
ipaErrors = 0

for w in words:
    word = words[w]["na'vi"]
    ipa = words[w]["ipa"]
    infixes = words[w]["infixes"]
    word_type = words[w]["type"]
    translations = words[w]["translations"]
    
    word_output = {
        "na'vi": word,
        "translations": [translations]
    }
    
    try:
        word_output["pronunciation"], stressed, infixes = getPronunciation(word, ipa)
        word_output["pronunciation"] = [word_output["pronunciation"], stressed]
        if "." in infixes:
            word_output["infixes"] = infixes
    except (IndexError, ValueError) as e:
        print("IPA of {} ({}) confuses our parser: {}".format(word, ipa, str(e)))
        ipaErrors += 1
    
    try:
        word_type = getWordType(word, word_type)
    except ValueError as e:
        print(str(e))
        typeErrors += 1
        word_type = "?"
        
    if not isinstance(word_type, list):
        word_type = [word_type]
    
    if word.endswith(" si"):
        word = word[:-3]
        
    word_output["na'vi"] = word
    try:
        word_output["source"] = sources[w]
    except KeyError as e:
        print('no source for ' + word)
    
    for t in word_type:
        filename = "output/{}-{}.json".format(word, t)
        if t != "?":
            word_output["type"] = t
        with open(filename, "w") as f:
            json.dump(word_output, f, ensure_ascii=False, indent=4)

print('{} type errors encountered'.format(typeErrors))
print('{} IPA errors encountered'.format(ipaErrors))
