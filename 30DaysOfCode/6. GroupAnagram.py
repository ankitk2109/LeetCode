class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Desired ouput data structure: {('a','e','t'):['ate','eat','tea'],('a','n','t'):['nat', 'tan']}
        default_dict = {}
        
        for str_ in strs :
            key = tuple(sorted(str_))
            if key not in default_dict:
                default_dict[key]= [str_]
            else:
                default_dict[key].append(str_)
        
        return(default_dict.values())
            