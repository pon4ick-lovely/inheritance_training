def test_pegasus_initialization():
    p1 = Pegasus()
    assert p1.get_pos() == (0, 0)
    
    
def test_pegasus_movement():
    p1 = Pegasus()
    p1.move(10, 15)
    assert p1.get_pos() == (10, 15)
    p1.move(-5, 20)
    assert p1.get_pos() == (5, 35)
    
    
def test_pegasus_no_movement():
    p1 = Pegasus()
    initial_pos = p1.get_pos()
    p1.move(0, 0)
    assert p1.get_pos() == initial_pos
    
    
def test_pegasus_negative_movement():
    p1 = Pegasus()
    p1.move(-10, -15)
    assert p1.get_pos() == (-10, -15)
    p1.move(5, -20)
    assert p1.get_pos() == (-5, -35)
    
    
def test_pegasus_get_pos():
    p1 = Pegasus()
    p1.move(10, 15)
    assert p1.get_pos() == (10, 15)
    p1.move(-5, 20)
    assert p1.get_pos() == (5, 35)
    p1.move(0, 0)
    assert p1.get_pos() == (5, 35)
    
    
def test_pegasus_voice():
    p1 = Pegasus()
    expected_sound = 'Frrr'  # Default sound of the Horse class
    p1.voice()
    assert p1.sound == expected_sound
    
    
def test_pegasus_multiple_voice_calls():
    p1 = Pegasus()
    expected_sound = 'Frrr'  # Default sound of the Horse class
    p1.voice()
    assert p1.sound == expected_sound
    p1.voice()
    assert p1.sound == expected_sound
    p1.voice()
    assert p1.sound == expected_sound