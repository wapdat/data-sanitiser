# PPI Sanitise (Personal and Private Information)
Regex to tokenise Private Personal Information in python. The design is basically a waterfall of regular expressions that are identifying and replacing any words (entities) that match the expected pattern. The value add is to pull all these into one script, and identify the regex that work the best. 

"never feed secrets as training data"

The inspiration was this paper. https://arxiv.org/abs/1802.08232  which The Register explains here https://www.theregister.co.uk/2018/03/02/secrets_fed_into_ai_models_as_training_data_can_be_stolen/

However the recommended approach in that assumes secrets have a low log perplexity (appears infrequently) but that isn't really a characteristic of much PPI, and the PPI that is unique and probably has a low log perpelxity (eg SSN) are quite easily identified by pattern.  

*Intuitively, if the defender can identify secrets in the training data, then they can be removed from the model before it is trained. Such an approach guarantees to prevent memorization if the secrets can be identified, since the secrets will not appear in the training data, and thus not be observed by the model during training.
The key challenge of this approach is how to identify the secrets in the training data. Several heuristics can be used. For example, if the secrets were known to follow some template (e.g., a regular expression), the defender may be able to remove all substrings matching the template from the training data in a preprocessing step. However, such heuristics cannot be exhaustive, and the defender never be aware of all potential templates that may exist in the training data. When the secrets cannot be captured by the heuristics, the defense will fail.* (The Secret Sharer: Measuring Unintended Neural Network Memorization & Extracting Secrets)

# What is PPI

This code will not exhaustively sanitise all PPI. Notably the definition of PPI is not a definitive list. GDPR langauge is intentionally descriptive not definitive. As someoe said to me -

*... there is no definitive list of attributes, indeed the challenge is with modern technology/data sources is that new attributes are constantly being created e.g. Geolocation data, timestamp data, descriptive data that can identify an individual – male, Kiwi accent, blue jeans with turnups, blue open neck sweater, black Doc Martin boots, MildMay pub, Islington 5.30pm Friday May 25* (that would be me)

## Credit to all the various sources for the Regex

There are probably Stack Overflow posts I've missed, happy to be corrected.

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

