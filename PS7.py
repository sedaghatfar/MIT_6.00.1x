#PART I: DATA STRUCTURE DESIGN  

class NewsStory(object):
    def __init__(self,guid,title,subject,summary,link):
        self.guid = guid
        self.title = title
        self.subject = subject        
        self.summary = summary
        self.link = link
    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):
        return self.summary
    def getLink(self):
        return self.link

#PART II: WORD TRIGGERS

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError
        
# Enter your code for WordTrigger, TitleTrigger, 
# SubjectTrigger, and SummaryTrigger in this box

class WordTrigger(Trigger):
 
    def __init__(self, word):
        self.word = word
        
    def isWordIn(self, text):
        text = [a.strip(string.punctuation).lower() for a in text.split(" ")]
        for word in text:
            if self.word.lower() in word.split("'"):
                return True
        return False
        
 
class TitleTrigger(WordTrigger):
 
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
 
class SubjectTrigger(WordTrigger):
 
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
 
 
class SummaryTrigger(WordTrigger):
 
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
 
#PART II: COMPOSITE TRIGGERS
# NotTrigger, AndTrigger, and OrTrigger

class NotTrigger(Trigger):
 
    def __init__(self, t1):
        self.t1 = t1
 
    def evaluate(self, story):
        return not self.t1.evaluate(story)
 
 
class AndTrigger(Trigger):
 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
 
    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)
 
        
class OrTrigger(Trigger):
 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
 
    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)
        
        
#PART II: PHRASE TRIGGERS
class PhraseTrigger(Trigger):
 
    def __init__(self, phrase):
        self.phrase = phrase
 
    def isPhraseIn(self,text):
        return self.phrase in text
 
    def evaluate(self, story):
        if self.isPhraseIn(story.getTitle()):
            return True
        if self.isPhraseIn(story.getSummary()):
            return True
        if self.isPhraseIn(story.getSubject()):
            return True
        return False

#PART III: FILTERING

'''
Write a function, filterStories(stories, triggerlist) that takes in a list of news stories and a list of triggers, 
and returns a list of only the stories for which any of the triggers fires on. The list of stories should be unique
- that is, do not include any duplicates in the list. For example, if 2 triggers fire on StoryA, only include StoryA 
in the list one time.
'''

def filterStories(stories, triggerlist):
    output = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                output.append(story)
                break
    return output

#PART IV: USER-SPECIFIED TRIGGERS

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.
 
    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")
 
    Modifies triggerMap, adding a new key-value pair for this trigger.
 
    Returns: None
    """
    # TODO: Problem 11
    if triggerType == "TITLE":
        triggerMap[name] = TitleTrigger(params[0])
 
    elif triggerType == "SUBJECT":
        triggerMap[name] = SubjectTrigger(params[0])
 
    elif triggerType == "SUMMARY":
        triggerMap[name] = SummaryTrigger(params[0])
 
    elif triggerType == "NOT":
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
 
    elif triggerType == "AND":
        triggerMap[name] = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
 
    elif triggerType == "OR":
        triggerMap[name] = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
 
    elif triggerType == "PHRASE":
        triggerMap[name] = PhraseTrigger(' '.join(params))
 
    return triggerMap[name]

