def update_records(dictionary_record, id, property, value):
       if dictionary_record.get(id):
              if property != 'tracks' and value != '':
                     dictionary_record[id].update({property : value})
              elif property == 'tracks' and not dictionary_record[id].get('tracks'): 
                     dictionary_record[id].update({property : [value]})
              elif property == 'tracks' and value != '': 
                     dictionary_record[id][property].append(value)
              elif value == '':
                     del dictionary_record[id][property]
       return dictionary_record
record_collection = {2548: {'albumTitle': 'Slippery When Wet',
                            'artist': 'Bon Jovi',
                            'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
                     2468: {'albumTitle': '1999',
                            'artist': 'Prince',
                            'tracks': ['1999', 'Little Red Corvette']},
                     1245: {'artist': 'Robert Palmer','tracks': []},
                     5439: {'albumTitle': 'ABBA Gold'}}
print(update_records(record_collection, 2548, 'artist', ''))