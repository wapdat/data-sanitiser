from sanitise import sanitise

def test_ukphone():
    assert sanitise.replacePPI('test 02071831573') == 'test UKPHONE'
    assert sanitise.replacePPI('test 0207 183 1573') == 'test UKPHONE'
    
    assert sanitise.replacePPI('test 07837182113') == 'test UKPHONE'
    assert sanitise.replacePPI(' 07837182113 test') == ' UKPHONE test'

def test_email():
    assert sanitise.replacePPI(' aaaaaaa@bbbbb.com test') == ' NAME@EMAIL.COM test'
    assert sanitise.replacePPI(' a@b.com test') == ' NAME@EMAIL.COM test'
    assert sanitise.replacePPI(' a@b.io test') == ' NAME@EMAIL.COM test'    
    assert sanitise.replacePPI(' 123@10.10.10.10 test') == ' NAME@EMAIL.COM test'  
    assert sanitise.replacePPI('1a@2.com test') == 'NAME@EMAIL.COM test'
    assert sanitise.replacePPI(' test 1a@2.com test') == ' test NAME@EMAIL.COM test'
    assert sanitise.replacePPI('1a@2.com test') == 'NAME@EMAIL.COM test' 
    assert sanitise.replacePPI('test 1a@2.com test 1a@2.com test') == 'test NAME@EMAIL.COM test NAME@EMAIL.COM test'        

# http://rion.io/2013/09/10/validating-social-security-numbers-through-regular-expressions-2/
def test_ssn():
    assert sanitise.replacePPI('test 123-12-1234') == 'test SSN'   
    
    assert sanitise.replacePPI('test 123 12 1234') != 'test SSN'
    assert sanitise.replacePPI('test 666-12-1234') != 'test SSN'
    assert sanitise.replacePPI('test 123-12-0000') != 'test SSN'
    assert sanitise.replacePPI('test 123-00-1234') != 'test SSN'
    assert sanitise.replacePPI('test 000-12-1234') != 'test SSN'   
    assert sanitise.replacePPI('test 900-00-1234') != 'test SSN' 
    assert sanitise.replacePPI('test 078-05-1120') != 'test SSN' 
    assert sanitise.replacePPI('test 219-09-9999') != 'test SSN'   

def test_canada_postcode():
    assert sanitise.replacePPI('test V9A 7N2') == 'test POSTCODECA'

def test_us_zipcode():
    assert sanitise.replacePPI('test 77801') == 'test ZIPCODEUS'
       
def test_cardnum():
    # Consumer Amex
    assert sanitise.replacePPI('test 371449635398431') == 'test CARDNUM'
    # Commercial Amex
    assert sanitise.replacePPI('test 378734493671000') == 'test CARDNUM'
    # Australina Bankcard  
    assert sanitise.replacePPI('test 5610591081018250') == 'test CARDNUM'
    


    
    
    