import time
import random

def main():

    scale = {}
    scale['C'] = ['C','D','E','F','G','A','B']
    scale['C#'] = ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#']
    scale['Db'] = ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C']
    scale['D'] = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
    scale['Eb'] = ['Eb','F','G','Ab','Bb','C','D']
    scale['E'] = ['E','F#','G#','A','B','C#','D#']
    scale['F'] = ['F','G','A','Bb','C','D','E']
    scale['F#'] = ['F#','G#','A#','B','C#','D#','E#']
    scale['Gb'] = ['Gb','Ab','Bb','Cb','Db','Eb','F']
    scale['G'] = ['G','A','B','C','D','E','F#']
    scale['Ab'] = ['Ab','Bb','C','Db','Eb','F','G']
    scale['A'] = ['A','B','C#','D','E','F#','G#']
    scale['Bb'] = ['Bb','C','D','Eb','F','G','A']
    scale['B'] = ['B','C#','D#','E','F#','G#','A#']
    scale['Cb'] = ['Cb','Db','Eb','Fb','Gb','Ab','Bb']

    sharp_flap = {}
    sharp_flap['C'] = ['C','C#','Cb']
    sharp_flap['D'] = ['D','D#','Db']
    sharp_flap['E'] = ['E','E#','Eb']
    sharp_flap['F'] = ['F','F#','Fb']
    sharp_flap['G'] = ['G','G#','Gb']
    sharp_flap['A'] = ['A','A#','Ab']
    sharp_flap['B'] = ['A','A#','Ab']
    sharp_flap['C#'] = ['C#','Cx','C']
    sharp_flap['D#'] = ['D#','Dx','D']
    sharp_flap['E#'] = ['E#','Ex','E']
    sharp_flap['F#'] = ['F#','Fx','F']
    sharp_flap['G#'] = ['G#','Gx','G']
    sharp_flap['A#'] = ['A#','Ax','A']
    sharp_flap['Db'] = ['Db','D','Dbb']
    sharp_flap['Eb'] = ['Eb','E','Ebb']
    sharp_flap['Gb'] = ['Gb','G','Gbb']
    sharp_flap['Ab'] = ['Ab','A','Abb']
    sharp_flap['Bb'] = ['Bb','B','Bbb']
    sharp_flap['Cb'] = ['Cb','C','Cbb']

    key_arr = ['C','C#','Db','D','Eb','E','F','F#','Gb','G','Ab','A','Bb','B']
    same_key = {'Db':'C#','Eb':'D#','Gb':'F#','Ab':'G#','Bb':'A#'}
    # chord_arr = ['','m','aug','dim','M7','7','mM7','m7','m7-5']
    chord_arr = ['','m']
    chord_formations = {
        '':[0, 2, 4],
        'm':[0, 2, 4]
    }
    chord_sharp_flap = {
        '': [0, 0, 0],
        'm': [0, -1, 0]
    }

    while(True):
        # 生成根音和弦
        base_key = key_arr[random.randint(0, len(key_arr) - 1)]
        chord = chord_arr[random.randint(0, len(chord_arr) - 1)]
        # 获得和弦构成音
        chord_keys = []
        for i in range(len(chord_formations[chord])):
            key = scale[base_key][chord_formations[chord][i]]
            adjusted_key = sharp_flap[key][chord_sharp_flap[chord][i]]
            chord_keys.append(adjusted_key)
        chord_str = base_key + chord
        # 生成低音
        low_key = chord_keys[random.randint(0, len(chord_keys) - 1)]
        # 打印
        if low_key != base_key:
            print(chord_str + '/' + low_key)
        else:
            print(chord_str)
        time.sleep(10)

if __name__ == '__main__':
    main()
