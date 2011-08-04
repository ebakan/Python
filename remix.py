import echonest.audio as audio
from echonest.selection import fall_on_the
from echonest.sorting import duration

song=audio.LocalAudioFile("sleepyhead.mp3")
tempo=song.analysis.tempo
beats=song.analysis.beats
duration=song.analysis.duration
print "tempo: %s"% tempo
print "beats/duration: %s" % len(beats)/duration*60
