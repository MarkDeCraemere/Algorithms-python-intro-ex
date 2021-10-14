from led import Led

def test_isOn():
  led = Led(1)
  assert(led.on())

def test_isFalse():
  led = Led(2)
  assert(led.off() == False)

def test_toggle():
  led = Led(3)
  assert(led.getState() == False)
  assert(led.toggle())
  assert(led.toggle() == False)