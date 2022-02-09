import json 


class Profile :
    
    def __init__(self, username : str, id : int, join : str, birthday : str, color : str, secret_id : int):
        self.username  = username
        self.id        = id
        self.join      = join
        self.birthday  = birthday
        self.color     = color 
        self.secret_id = secret_id
    
    def to_json(self, file = "data/profile.json") :
        with open(file, 'r', encoding='utf8') as r_file :
            r_file = json.load(r_file)
            r_file[self.username] = {}
            
            for key in self.__dict__ :
                r_file[self.username][key] = self.__dict__[key]
        
            with open(file, 'w', encoding='utf8') as w_file :
                json.dump(r_file, w_file)


def get_profile(username : str, file = "data/profile.json")->Profile :
    with open(file, 'r', encoding='utf8') as r_file :
        r_file  = json.load(r_file)
        try :
            profile = r_file[username]        
            return Profile(profile['username'], profile['id'], profile['join'], profile['birthday'], profile['color'], profile['secret_id'])
        except KeyError :
            return None