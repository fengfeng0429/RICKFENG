## Welcome to Learning note
week 1 筆記:<br>
[linked list](https://hackmd.io/@Zq6oiEB9Ty-KvUdV9n7vOw/ryfRSqEPB)<br>
week 1 練習/作業:<br>
[leetcode-linked list](https://github.com/fengfeng0429/RICKFENG-DSA/tree/master/leetcode/week%201)<br>
week 2 筆記:<br>
[Stack and Queue](https://www.csie.ntu.edu.tw/~r95116/CA200/slide/C8_StackQueue.pdf)<br>
[Markdown](https://blog.csdn.net/zhaokaiqiang1992/article/details/41349819)<br>
week 3 練習/作業:<br>
[Stack and Queue](https://github.com/fengfeng0429/RICKFENG-DSA/tree/master/leetcode/week%202)<br>
week 4 筆記:<br>
week 4 練習/作業:<br>


## Something about me:
Name:馮正毅<br>
Major:<br>
SCU English<br>
SCU Big Data<br>
## Why am I double-majoring:<br>
1. I am interesting in NLP and machine translation.<br>
2. I want to know whether human translation be replaced by machine.<br>
3. I want to learn how machine can speak and respond like us.<br>
Links about NLP and Machine translation:<br>
a.[斷開中文的鎖鍊！自然語言處理](http://research.sinica.edu.tw/nlp-natural-language-processing-chinese-knowledge-information/)<br>
b.[自然語言處理實驗室](http://nlg.csie.ntu.edu.tw/)<br>
c.[從ACL 2017 看到四個在自然語言處理(NLP)的趨勢](https://medium.com/@cyeninesky3/%E5%BE%9Eacl-2017-%E7%9C%8B%E5%88%B0%E5%9B%9B%E5%80%8B%E5%9C%A8%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86-nlp-%E7%9A%84%E8%B6%A8%E5%8B%A2-3163c6a91c50)<br>
d.[Natural Language Processing & Machine Translation Labs](http://nlp.csie.ncnu.edu.tw/~shin/)<br>
Natural language processing:<br>
Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data.<br>

Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation.<br>
Rule-based vs. statistical NLP:<br>
In the early days, many language-processing systems were designed by hand-coding a set of rules:such as by writing grammars or devising heuristic rules for stemming.<br>

Since the so-called "statistical revolution" in the late 1980s and mid 1990s, much natural language processing research has relied heavily on machine learning. The machine-learning paradigm calls instead for using statistical inference to automatically learn such rules through the analysis of large corpora (the plural form of corpus, is a set of documents, possibly with human or computer annotations) of typical real-world examples.<br>

Many different classes of machine-learning algorithms have been applied to natural-language-processing tasks. These algorithms take as input a large set of "features" that are generated from the input data. Some of the earliest-used algorithms, such as decision trees, produced systems of hard if-then rules similar to the systems of handwritten rules that were then common. Increasingly, however, research has focused on statistical models, which make soft, probabilistic decisions based on attaching real-valued weights to each input feature. Such models have the advantage that they can express the relative certainty of many different possible answers rather than only one, producing more reliable results when such a model is included as a component of a larger system.<br>

Systems based on machine-learning algorithms have many advantages over handproduced rules:<br>

The learning procedures used during machine learning automatically focus on the most common cases, whereas when writing rules by hand it is often not at all obvious where the effort should be directed.<br>
Automatic learning procedures can make use of statistical-inference algorithms to produce models that are robust to unfamiliar input (e.g. containing words or structures that have not been seen before) and to erroneous input (e.g. with misspelled words or words accidentally omitted). Generally, handling such input gracefully with handwritten rules, or, more generally, creating systems of handwritten rules that make soft decisions, is extremely difficult, error-prone and time-consuming.<br>
Systems based on automatically learning the rules can be made more accurate simply by supplying more input data. However, systems based on handwritten rules can only be made more accurate by increasing the complexity of the rules, which is a much more difficult task.<br> In particular, there is a limit to the complexity of systems based on handcrafted rules, beyond which the systems become more and more unmanageable. However, creating more data to input to machine-learning systems simply requires a corresponding increase in the number of man-hours worked, generally without significant increases in the complexity of the annotation process.<br>
Major evaluations and tasks:<br>
Syntax:<br>
Grammar induction<br>
Generate a formal grammar that describes a language's syntax.<br>
Lemmatization<br>
The task of removing inflectional endings only and to return the base dictionary form of a word which is also known as a lemma.<br>
Morphological segmentation<br>
Separate words into individual morphemes and identify the class of the morphemes. The difficulty of this task depends greatly on the complexity of the morphology (i.e. the structure of words) of the language being considered. English has fairly simple morphology, especially inflectional morphology, and thus it is often possible to ignore this task entirely and simply model all possible forms of a word (e.g. "open, opens, opened, opening") as separate words. In languages such as Turkish or Meitei, a highly agglutinated Indian language, however, such an approach is not possible, as each dictionary entry has thousands of possible word forms.<br>
Part-of-speech tagging<br>
Given a sentence, determine the part of speech (POS) for each word. Many words, especially common ones, can serve as multiple parts of speech. For example, "book" can be a noun ("the book on the table") or verb ("to book a flight"); "set" can be a noun, verb or adjective; and "out" can be any of at least five different parts of speech. Some languages have more such ambiguity than others.[dubious – discuss] Languages with little inflectional morphology, such as English, are particularly prone to such ambiguity. Chinese is prone to such ambiguity because it is a tonal language during verbalization. Such inflection is not readily conveyed via the entities employed within the orthography to convey intended meaning.<br>
Parsing<br>
Determine the parse tree (grammatical analysis) of a given sentence. The grammar for natural languages is ambiguous and typical sentences have multiple possible analyses. In fact, perhaps surprisingly, for a typical sentence there may be thousands of potential parses (most of which will seem completely nonsensical to a human). There are two primary types of parsing, Dependency Parsing and Constituency Parsing. Dependency Parsing focuses on the relationships between words in a sentence (marking things like Primary Objects and predicates), whereas Constituency Parsing focuses on building out the Parse Tree using a Probabilistic Context-Free Grammar (PCFG).<br> 
Sentence breaking (also known as sentence boundary disambiguation)<br>
Given a chunk of text, find the sentence boundaries. Sentence boundaries are often marked by periods or other punctuation marks, but these same characters can serve other purposes (e.g. marking abbreviations).<br>
Stemming<br>
The process of reducing inflected (or sometimes derived) words to their root form. (e.g. "close" will be the root for "closed", "closing", "close", "closer" etc.).<br>
Word segmentation<br>
Separate a chunk of continuous text into separate words. For a language like English, this is fairly trivial, since words are usually separated by spaces. However, some written languages like Chinese, Japanese and Thai do not mark word boundaries in such a fashion, and in those languages text segmentation is a significant task requiring knowledge of the vocabulary and morphology of words in the language. Sometimes this process is also used in cases like Bag of Words (BOW) creation in data mining.<br>
Terminology extraction<br>
The goal of terminology extraction is to automatically extract relevant terms from a given corpus.
Semantics<br>
Lexical semantics<br>
What is the computational meaning of individual words in context?<br>
Distributional semantics<br>
How can we learn semantic representations from data?<br>
Machine translation<br>
Automatically translate text from one human language to another. This is one of the most difficult problems, and is a member of a class of problems colloquially termed "AI-complete", i.e. requiring all of the different types of knowledge that humans possess (grammar, semantics, facts about the real world, etc.) in order to solve properly.<br>
Named entity recognition (NER)<br>
Given a stream of text, determine which items in the text map to proper names, such as people or places, and what the type of each such name is (e.g. person, location, organization). Although capitalization can aid in recognizing named entities in languages such as English, this information cannot aid in determining the type of named entity, and in any case is often inaccurate or insufficient. For example, the first letter of a sentence is also capitalized, and named entities often span several words, only some of which are capitalized. Furthermore, many other languages in non-Western scripts (e.g. Chinese or Arabic) do not have any capitalization at all, and even languages with capitalization may not consistently use it to distinguish names. For example, German capitalizes all nouns, regardless of whether they are names, and French and Spanish do not capitalize names that serve as adjectives.<br>
Natural language generation<br>
Convert information from computer databases or semantic intents into readable human language.<br>
Natural language understanding<br>
Convert chunks of text into more formal representations such as first-order logic structures that are easier for computer programs to manipulate. Natural language understanding involves the identification of the intended semantic from the multiple possible semantics which can be derived from a natural language expression which usually takes the form of organized notations of natural language concepts. Introduction and creation of language metamodel and ontology are efficient however empirical solutions. An explicit formalization of natural language semantics without confusions with implicit assumptions such as closed-world assumption (CWA) vs. open-world assumption, or subjective Yes/No vs. objective True/False is expected for the construction of a basis of semantics formalization.<br>
Optical character recognition (OCR)<br>
Given an image representing printed text, determine the corresponding text.<br>
Question answering<br>
Given a human-language question, determine its answer. Typical questions have a specific right answer (such as "What is the capital of Canada?"), but sometimes open-ended questions are also considered (such as "What is the meaning of life?"). Recent works have looked at even more complex questions.<br>
Recognizing Textual entailment<br>
Given two text fragments, determine if one being true entails the other, entails the other's negation, or allows the other to be either true or false.<br>
Relationship extraction<br>
Given a chunk of text, identify the relationships among named entities (e.g. who is married to whom).<br>
Sentiment analysis (see also multimodal sentiment analysis)<br>
Extract subjective information usually from a set of documents, often using online reviews to determine "polarity" about specific objects. It is especially useful for identifying trends of public opinion in the social media, for the purpose of marketing.
Topic segmentation and recognition<br>
Given a chunk of text, separate it into segments each of which is devoted to a topic, and identify the topic of the segment.<br>
Word sense disambiguation<br>
Many words have more than one meaning; we have to select the meaning which makes the most sense in context. For this problem, we are typically given a list of words and associated word senses, e.g. from a dictionary or from an online resource such as WordNet.<br>
Discourse<br>
Automatic summarization<br>
Produce a readable summary of a chunk of text. Often used to provide summaries of text of a known type, such as research papers, articles in the financial section of a newspaper.<br>
Coreference resolution<br>
Given a sentence or larger chunk of text, determine which words ("mentions") refer to the same objects ("entities"). Anaphora resolution is a specific example of this task, and is specifically concerned with matching up pronouns with the nouns or names to which they refer. The more general task of coreference resolution also includes identifying so-called "bridging relationships" involving referring expressions. For example, in a sentence such as "He entered John's house through the front door", "the front door" is a referring expression and the bridging relationship to be identified is the fact that the door being referred to is the front door of John's house (rather than of some other structure that might also be referred to).<br>
Discourse analysis<br>
This rubric includes a number of related tasks. One task is identifying the discourse structure of connected text, i.e. the nature of the discourse relationships between sentences (e.g. elaboration, explanation, contrast). Another possible task is recognizing and classifying the speech acts in a chunk of text (e.g. yes-no question, content question, statement, assertion, etc.).<br>
Speech<br>
Speech recognition<br>
Given a sound clip of a person or people speaking, determine the textual representation of the speech. This is the opposite of text to speech and is one of the extremely difficult problems colloquially termed "AI-complete" (see above). In natural speech there are hardly any pauses between successive words, and thus speech segmentation is a necessary subtask of speech recognition (see below). In most spoken languages, the sounds representing successive letters blend into each other in a process termed coarticulation, so the conversion of the analog signal to discrete characters can be a very difficult process. Also, given that words in the same language are spoken by people with different accents, the speech recognition software must be able to recognize the wide variety of input as being identical to each other in terms of its textual equivalent.<br>
Speech segmentation<br>
Given a sound clip of a person or people speaking, separate it into words. A subtask of speech recognition and typically grouped with it.<br>
Text-to-speech<br>
Given a text, transform those units and produce a spoken representation. Text-to-speech can be used to aid the visually impaired.<br>
Dialogue<br>
The first published work by an artificial intelligence was published in 2018, 1 the Road, marketed as a novel, contains sixty million words.<br>
