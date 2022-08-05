
import wave
import pyaudio



def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels= wf.getnchannels(),
        rate= wf.getframerate(),
        output= True
    )
    print('jjjjjjj')

    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

play_audio('./audio/mixkit-sci-fi-reject-notification-896.wav')