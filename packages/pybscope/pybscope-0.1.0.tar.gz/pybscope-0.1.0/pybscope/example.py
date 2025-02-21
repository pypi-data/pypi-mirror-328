# pybscope/example.py

def say(text):
    """Prints a message."""
    print(f"Pybscope says: {text}")

def boost_motor():
    """Controls LEGO BOOST Motor A."""
    from pylgbst.hub import MoveHub
    from pylgbst.comms import get_connection_bluepy

    hub = MoveHub(get_connection_bluepy())
    hub.motor_A.timed(1, 0.5)
    print("Motor A ran for 1 second!")
