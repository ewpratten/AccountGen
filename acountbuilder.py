import random
import string

def _randChr():
    return random.choice(string.ascii_lowercase)

def _buildPrefix(n=4):
    return "".join(_randChr() for _ in range(n))

def _buildSuffix(n=4):
    return "".join(_randChr() for _ in range(n))

def _buildSID():
    """Generate a random SID prefix with a possible range of 100-999"""
    return random.randint(100, 999)

def buildUID():
    return f"{_buildPrefix()}{_buildSuffix()}{_buildSID()}"

if __name__ == "__main__":
    print(buildUID())