'''

This module contains a utility function that converts audio files into spectrograms.

'''


import os
import pylab
import wave

# Utility function to get sound and frame rate info
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.frombuffer(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

MAIN_INPUT_DIR = #set the main folder which contains different subfolders containing 'wav' audio files

OUTPUT_DIR = #set the folder where you want to save the spectogram images

#function to create spectogram images using pylab by extracting 'wav' audio files
#from subfolders which denote classes and creating subfolders in similar pattern for 
#the spectogram images

def audio_to_spectograms(MAIN_INPUT_DIR,OUTPUT_DIR): 
    for INPUT_DIR in os.listdir(MAIN_INPUT_DIR):
        temp = MAIN_INPUT_DIR + '/' + INPUT_DIR
        for filename in os.listdir(temp):
            if "wav" in filename:
                file_path = os.path.join(temp, filename)
                file_stem = Path(file_path).stem
                target_dir = str(x)
                dist_dir = os.path.join(OUTPUT_DIR, target_dir)
                file_dist_path = os.path.join(dist_dir, file_stem)
                if not os.path.exists(file_dist_path + '.png'):
                    if not os.path.exists(dist_dir):
                        os.mkdir(dist_dir)
                    file_stem = Path(file_path).stem
                    sound_info, frame_rate = get_wav_info(file_path)
                    pylab.specgram(sound_info, Fs=frame_rate)
                    
                    pylab.savefig(f'{file_dist_path}'+str(os.listdir(Main_INPUT_DIR).index(INPUT_DIR))+'.png')
                    pylab.close()

audio_to_spectograms(MAIN_INPUT_DIR, OUTPUT_DIR)