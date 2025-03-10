##
##Luke Herron
##Theory of Computation
##Professor Obando
##Project 1
##3/7/2025
##


import random  ##for CFG choices
import mido  ##midi file handling
from mido import Message, MidiFile, MidiTrack  ##create midifiles and track object

note_to_midi = { ##dictionary to map midi numbers to notes
    "C4": 60, "D4": 62, "E4": 64, "F4": 65, "G4": 67, "A4": 69, "B4": 71
}


def generate_melody(): ##function to create melody using context free grammar 
    grammar = { ##dictionary for CFG language
        "S": ["Phrase Phrase X"],  ##melody will have 2 "phrases"
        "X": ["S", ""], ##either S or empty
        "Phrase": ["Note Note Note"],  ##phrase has 3 notes
        "Note": ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]  ##possible notes
        
        
        ##without X, it would result in
        ##[["note","note","note"],["note", "note", "note"]]
        
        
        
    }
    

    def expand(symbol): ##recursive function for creating melody
        if symbol in grammar: ##if non-terminal symbol
            expansion = random.choice(grammar[symbol]).split() ##randomly chose a rule in the dictionary
            return sum([expand(s) for s in expansion], []) ##calls sum to "flatten" the lists and combine them into one list
            ##return [expand(s) for s in expansion] ##recursivly call expand with new terminal or non terminal symbol
        else:
            return [symbol]  ##return the note if it is terminal symbol

    melody_structure = expand("S") ##begin recrusion from S

    ##melody = [item for sublist in melody_structure for item in (sublist if isinstance(sublist, list) else [sublist])] ##"flattens" nested list into list
    ##[['note'], ['note'], ['note'], ['note'], ['note'], ['note']] 

        
    return melody_structure  



def create_midi(melody, filename="melody.mid"):
    midi_file = MidiFile()  ##create midi file
    track = MidiTrack()  ##create track object
    midi_file.tracks.append(track)  ##add track object to midi file
    time_per_note = 480  ##speed of melody

    for note_name in melody:  ##loop through the notes in the melody list
        midi_note = note_to_midi.get(note_name, 60)  ##convert note to midi number (C4 or 60 as default)

        track.append(Message("note_on", note=midi_note, velocity=64, time=0))  ##start the note
        track.append(Message("note_off", note=midi_note, velocity=64, time=time_per_note))  ##stop the note after the time for that note

    midi_file.save(filename)  ##save melody as midi file
    print(f"MIDI file saved as {filename}")



##run the code


melody = generate_melody() ##call generate_melody function
print("Generated Melody:", melody)  
create_midi(melody) ##call create_midi to create midi file
