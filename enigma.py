
class Enigma:
    def __init__(self, hash_map, wheels, reflector_map):
        self.hash_map = hash_map
        self.wheels = wheels
        self.reflector_map = reflector_map

    def encrypt(self, message):
        incryptedmessage = ""
        count = 0
        for char in message:
            i =  self.hash_map.get(char)
            toAdd = ((self.wheels[0] * 2) - self.wheels[1] + self.wheels[2]) % 26 
            if toAdd == 0:
                i = i + 1
            else:
                i = i + toAdd
            i = i % 26
            for k in self.hash_map.keys():
                if self.hash_map[k] == i:
                    c1 = k
            c2 = self.reflector_map[c1]
            i = self.reflector_map[c2]
            if toAdd == 0:
                i = i - 1
            else:
                i = i - toAdd
            i = i % 26
            for j in self.hash_map.keys():
                if self.hash_map[j] == i :
                    c3 = j
            incryptedmessage += c3
            self.wheels[0] = (self.wheels[0] + 1) % 9
            count += 1 
            if count % 2 == 0:
                self.wheels[1] *= 2
            else:
                self.wheels[1] -= 1
            if count % 10 == 0:
                self.wheels[2] = 10
            elif count % 3 == 0:
                self.wheels[2] = 5
            else:
                self.wheels[2] = 0

        return incryptedmessage

class JSONFileException(Exception):

    pass
 
def load_enigma_from_path(path):
    import json
    try:
        with open(path,'r') as f:
            data = json.load(f)
        wheels = data["wheels"]
        hash_map = data["hash_map"]
        reflector_map = data["reflector_map"]
    except Exception as e:
        raise JSONFileException
    enigma = Enigma(hash_map,wheels,reflector_map)
    return enigma


