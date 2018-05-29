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

    
     