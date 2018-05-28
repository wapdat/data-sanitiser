from sanitise import sanitise

def test_ukphone():
    assert sanitise.replacePPI('test 02071831573') == 'test UKPHONE'
    assert sanitise.replacePPI('test 07837182113') == 'test UKPHONE'
    assert sanitise.replacePPI(' 07837182113 test') == ' UKPHONE test'
