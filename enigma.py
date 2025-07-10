
class Enigma:
    def __init__(self, hash_map, wheels, reflector_map):
        self.hash_map = hash_map
        self.wheels = wheels
        self.reflector_map = reflector_map

    def encrypt(self, message):
        incryptedmessage = ""
        count = 0
        for char in message:
            if char not in self.hash_map:
                continue 
            else:
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
                i = self.hash_map[c2]
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

if __name__ == "__main__":
    try:
        import sys
        args = sys.argv
        path = args[args.index("-c") + 1]
        input = args[args.index("-i") + 1]
        if "-o" in args:
            output = args[args.index("-o") + 1]
        enigma = load_enigma_from_path(path)
        with open(input,'r') as f:
            lines = f.readlines()
        encrypted = [enigma.encrypt(line) for line in lines]
        if "-o" in args:
            with open(output, 'w') as f:
                for line in encrypted:
                    f.write(line + '\n')
        else:
            for line in encrypted:
                print(encrypted)
        
    except JSONFileException:
        print("The enigma script has encountered an error")
        exit(1)
