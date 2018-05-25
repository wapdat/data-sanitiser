# Remove Personal and Private Information

Code (mostly regular expresssion and Stanford NTLK) to tokenise (remove) Private Personal Information (PPI) in python. 


Essentially, it's a waterfall of regular expressions that identify and replace any words (entities) that match the expected pattern of known personal and private information.

`My name is Julian Assange, call me on 07867182333` **becomes** `My name is PERSONNAME, call me on UKMOBILE`

"never feed secrets as training data"

## Inspiration - models memorise secrets 

The inspiration is this paper. https://arxiv.org/abs/1802.08232  which [The Register](https://www.theregister.co.uk/2018/03/02/secrets_fed_into_ai_models_as_training_data_can_be_stolen/) explains in its inimitable fashion.  Briefly, Google trained their models with credit card numbers and now the card numbers are stored in the model. Whoops!

The [paper](https://arxiv.org/abs/1802.08232) (appendix F) has a decent enough idea to overcome the vulnerability, but assumes secrets have a low log perplexity (appears infrequently). That isn't often a characteristic of some PPI.  There is some PPI with a high log perplexity, and there is PPI that is quite easily identified by pattern.  

>"Intuitively, if the defender can identify secrets in the training data, then they can be removed from the model before it is trained. Such an approach guarantees to prevent memorization if the secrets can be identified, since the secrets will not appear in the training data, and thus not be observed by the model during training."

>"The key challenge of this approach is how to identify the secrets in the training data. Several heuristics can be used. For example, if the secrets were known to follow some template (e.g., a regular expression), the defender may be able to remove all substrings matching the template from the training data in a preprocessing step. However, such heuristics cannot be exhaustive, and the defender never be aware of all potential templates that may exist in the training data. When the secrets cannot be captured by the heuristics, the defense will fail."

[The Secret Sharer: Measuring Unintended Neural Network Memorization & Extracting Secrets](https://arxiv.org/abs/1802.08232)

# What is PPI?

This code will not exhaustively sanitise all PPI because the definition of PPI is not a definitive list. GDPR language is intentionally descriptive not definitive. It's a truism - how can you exhaustively identify things you can't define.

However, it is possible to exhaustively test for some PPI. For example, there are 1.6m postcodes in the UK. The regex used here has been tested against all 1.6m with 100% accuracy. For some PPI, it's trickier, in particular names and addresses. However, it is conceivable to exhaustively test your rules against every name and address in the UK Electoral Register.

As someone said to me -

>... there is no definitive list of attributes, indeed the challenge is with modern technology/data sources is that new attributes are continually being created, e.g. Geolocation data, timestamp data, descriptive data that can identify an individual – male, Kiwi accent, blue jeans with turnups, blue open neck sweater, black Doc Martin boots, MildMay pub, Islington 5.30pm Friday May 25

### Current sanitisation capabilities 

  * postcode
  * social security number
  * email address
  * UK phones mumber
  * US and Canada phone number

### To do 

  * person (name, title, initial)
  * organisation
  * address (Street)
  * city
  * account number
  * date (eg DOB but any date)
  * time
  * money amount
  * product name
  * card number
  * merchant name
  * zip code
  * state name
  * state Code

## Use Cases

* Sanitising training data before you feed it in to a Machine Learning model
* Sanitising data if you want to move a copy of data out of Production for test purposes
* Sanitising logs - re-write logs in-situ to remove PPI as an Infosec control 
* Data Loss Prevention - script it into your email server to sanitise outbound emails. Could definitley be done in Postfix without too many headaches

_NB There is no guarantee that this (or any thing) will remove all PPI information._

## Stanford NER 
When I get time I'll plug in the Stanford NER, https://www.nltk.org/_modules/nltk/tag/stanford.html and see what happens with names. It will just be an inline check for names and organisations, and tokenise these.

## Credit to all the various sources for the Regex

There are probably Stack Overflow posts I've missed, happy to be corrected.

Credit Cards
* https://stackoverflow.com/questions/9315647/regex-credit-card-number-tests
* https://www.safaribooksonline.com/library/view/regular-expressions-cookbook/9781449327453/ch04s20.html

Various phone number formats
* http://phoneregex.com/

UK Postcodes
* https://stackoverflow.com/questions/164979/uk-postcode-regex-comprehensive

Social Securty Numbers
* http://rion.io/2013/09/10/validating-social-security-numbers-through-regular-expressions-2/

Email Addresses
* http://emailregex.com/

This project is interesting.
* https://github.com/dssg/ushine-learning/wiki/Identify-private-information-in-report-text

