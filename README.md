# Sanitise (by removal, tokenisaction, or redaction) Personal and Private Data

Code (regular expresssions and NTLK) to tokenise (remove) Private Personal Data in unstructured data. 

Essentially, it cleans data of personal information, using NTLK Named Entity Recognition, along with a waterfall of regular expressions that identify and replace any words (entities) that match the expected pattern of known personal and private information. It does this in a way to retain some level of readability, and semantic meaning in the data.

It turns this...

`My email address is  dummy@gmail.com and lindsay.smith@telrock.com  N16 9Ln I like bank holidays and speaking french. my ssn is  078-06-1120 call me on 078371827735 or 0207 183 1573  - your sincerely  Lindsay Smith and by the way  I work at Telrock`

into this. (something you could pass to a 3rd party and they wouldn't need to be classed a GDPR Processor)

`My email address is  NAME@EMAIL.COM and NAME@EMAIL.COM  UKPOSTCODE I like bank holidays and speaking french. my ssn is  SSN call me on UKPHONE or UKPHONE  - your sincerely  PERSON and by the way  I work at ORGANIZATION`



## Inspiration - models memorise secrets 

"never feed secrets as training data"

The inspiration for this project is from this paper. https://arxiv.org/abs/1802.08232  which [The Register](https://www.theregister.co.uk/2018/03/02/secrets_fed_into_ai_models_as_training_data_can_be_stolen/) explains in its inimitable fashion.  Briefly, Google trained their models with credit card numbers and now the card numbers are stored in the model. Whoops!

The [paper](https://arxiv.org/abs/1802.08232) has a decent suggestion to overcome the vulnerability, but assumes secrets have a low log perplexity (appears infrequently). That isn't often a characteristic of some PPI.  There is some PPI with a high log perplexity, and there is PPI that is quite easily identified by pattern.  What do you do if your training data is full of PPI?

>"Intuitively, if the defender can identify secrets in the training data, then they can be removed from the model before it is trained. Such an approach guarantees to prevent memorization if the secrets can be identified, since the secrets will not appear in the training data, and thus not be observed by the model during training."

>"The key challenge of this approach is how to identify the secrets in the training data. Several heuristics can be used. For example, if the secrets were known to follow some template (e.g., a regular expression), the defender may be able to remove all substrings matching the template from the training data in a preprocessing step. However, such heuristics cannot be exhaustive, and the defender never be aware of all potential templates that may exist in the training data. When the secrets cannot be captured by the heuristics, the defense will fail."

[The Secret Sharer: Measuring Unintended Neural Network Memorization & Extracting Secrets](https://arxiv.org/abs/1802.08232)

# What is Personal and Private Data?

Here's the thing - there is no difinitive list, at one level it is intuitively obvious, but there is no "Periodic Table" of personal data. 

This code will not exhaustively sanitise all Personal and Private Data because the definition of Personal and Private Data is not a definitive list. GDPR language is intentionally descriptive not definitive. It's a truism - how can you exhaustively identify things you can't define.

However, it is possible to exhaustively test for some PPI. For example, there are 1.6m postcodes in the UK. The regex used here has been tested against all 1.6m with 100% accuracy. For some PPI, it's trickier, in particular names and addresses. However, it is conceivable to exhaustively test your rules against every name and address in the UK Electoral Register.

As someone said to me -

>... there is no definitive list of attributes, indeed the challenge is with modern technology/data sources is that new attributes are continually being created, e.g. Geolocation data, timestamp data, descriptive data that can identify an individual – male, Kiwi accent, blue jeans with turnups, blue open neck sweater, black Doc Martin boots, Mildmay pub, Islington 5.30pm Friday May 25

## What about US, US and everyother countries defintion of Personal and Private data?

>U.S. and EU privacy law diverge greatly. At the foundational level, they differ in their underlying philosophy: In the United States, privacy law focuses on redressing consumer harm and balancing privacy with efficient commercial transactions. In the European Union, privacy is hailed as a fundamental right that can trump other interests. [Paul M. Schwartz and Danie J. Solove, Reconciling Personal Information in the United States and European Union, 102 Calif. L. Rev. 877 (2014).](https://scholarship.law.berkeley.edu/californialawreview/vol102/iss4/7/)

European data protection law does not utilise the concept of PII, and its scope is instead determined by non-synonymous, wider concept of "personal data". Good overview found on [wikipedia - Personally_identifiable_information](https://en.wikipedia.org/wiki/Personally_identifiable_information)

### Current Data Cleaning capabilities 

Refer to the tests to understand exactly what these data items mean and how wide the matcing works.

  * UK postcode
  * US social security number
  * email address
  * UK phones number
  * US and Canada phone number
  * Payment cards (Amex, BCGlobal, Carte Blanche Card, Diners Club Card, Discover Card, Insta Payment Card, JCB Card, KoreanLocalCard, Laser Card, Maestro Card, Mastercard, Solo Card, Switch Card, Union Pay Card, Visa Card, Visa Master Card)
  * US Zipcodes
  * Canadian Postcodes
  * account number (any 5 -12 length of digits - do this last so not to pick up more specific matches)
  * person (name, title, initial)
  * organisation - merchant name
  * city
  * Locations (GPE)
  * state name
  * state Code
  
### To do 

  * address (Street)
  * date (eg DOB but any date)
  * time
  * money amount
  * product name
  * and for fun lets do profanities

## Use Cases

* Sanitising training data before you feed it in to a Machine Learning model
* Sanitising data if you want to move a copy of data out of Production for test purposes
* Sanitising logs - re-write logs in-situ to remove PPI as an Infosec control 
* Data Loss Prevention - script it into your email server to sanitise outbound emails. Could definitley be done in Postfix without too many headaches

_NB There is no guarantee that this (or any thing) will remove all PPI information._

## NLTK 
It uses the default implementation of NER available in NLTK. It does ok at recognising names. GPE stands for "Geo-political entity", ie location.

## Credit to all the various sources for the Regex

There are probably Stack Overflow posts I've missed, happy to be corrected.

Go here first
 * http://cldr.unicode.org/

Credit Cards
* https://stackoverflow.com/questions/9315647/regex-credit-card-number-tests
* https://www.safaribooksonline.com/library/view/regular-expressions-cookbook/9781449327453/ch04s20.html
* http://www.richardsramblings.com/2012/12/the-perfect-credit-card-number-regex/

Various phone number formats
* http://phoneregex.com/

UK Postcodes
* https://stackoverflow.com/questions/164979/uk-postcode-regex-comprehensive

US & Canadian zipcodes
* http://geekswithblogs.net/MainaD/archive/2007/12/03/117321.aspx
* http://html5pattern.com/Postal_Codes

Social Securty Numbers
* http://rion.io/2013/09/10/validating-social-security-numbers-through-regular-expressions-2/

Email Addresses
* http://emailregex.com/

Profanity & Censorship
UK List from OfCom
* https://www.ofcom.org.uk/__data/assets/pdf_file/0023/91625/OfcomQRG-AOC.pdf
Various lits of various provenance
* https://code.google.com/archive/p/badwordslist/downloads
* https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/
* http://www.bannedwordlist.com/
Discusion on censorship in different counties
* https://en.wikipedia.org/wiki/Censorship_by_Google


These projects are interesting. Scrubadub is similar to this but I prefer the simplicity of a waterfall of Regex.
* https://github.com/dssg/ushine-learning/wiki/Identify-private-information-in-report-text
* https://github.com/datascopeanalytics/scrubadub

# FAQ

Why do I get requests from NTLK to download stuff the first time I run it?

NTLK needs some basic models to run, and it decides the first times it is run which ones it needs. In the error messages it will tell you what you need to do and how to do it. There are a few nltk.download('punkt'), nltk.download('averaged_perceptron_tagger'), nltk.download('maxent_ne_chunker'), nltk.download('words'). Read this https://github.com/nltk/nltk/wiki/Frequently-Asked-Questions-(Stackoverflow-Edition)

# Interesting Papers

Out of date in terms of legal status of PPI but good list of techniques.
* http://www.orafaq.com/papers/data_sanitization.pdf

Guide to Protecting the Confidentiality of Personally Identifiable Information (PII) - Recommendations of the National Institute of Standards and Technology
* https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-122.pdf


