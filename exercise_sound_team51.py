#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: int, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)


dotted_quarter: float = 0.552  # seconds
quarter: float = 0.368
eighth: float = 0.184
sixteenth: float = 0.092

C2: int = 65
Csharp2: int = 69
D2: int = 73
Dsharp2: int = 78
E2: int = 82
F2: int = 87
Fsharp2: int = 93
G2: int = 98
Gsharp2: int = 104
A2: int = 110
Asharp2: int = 117
B2: int = 123

C3: int = 131
Csharp3: int = 139
D3: int = 147
Dsharp3: int = 156
E3: int = 165
F3: int = 175
Fsharp3: int = 185
G3: int = 196
Gsharp3: int = 208
A3: int = 220
Asharp3: int = 233
B3: int = 247

C4: int = 262
Csharp4: int = 277
D4: int = 294
Dsharp4: int = 311
E4: int = 330
F4: int = 349
Fsharp4: int = 370
G4: int = 392
Gsharp4: int = 415
A4: int = 440
Asharp4: int = 466
B4: int = 494

C5: int = 523
Csharp5: int = 554
D5: int = 587
Dsharp5: int = 622
E5: int = 659
F5: int = 698
Fsharp5: int = 740
G5: int = 784
Gsharp5: int = 831
A5: int = 880
Asharp5: int = 932
B5: int = 988




print("Playing frequency (Hz):")

playtone(E4, dotted_quarter)
playtone(D4, quarter)
playtone(G4, quarter)
playtone(Fsharp4, quarter)
playtone(D4, quarter)
playtone(E4, quarter)
playtone(B3, quarter)
playtone(B3, eighth)
playtone(D4, quarter)
playtone(A3, quarter)
playtone(B3, eighth)
playtone(G3, quarter)
playtone(G3, quarter)
playtone(Fsharp3, quarter)
playtone(G3, quarter)
playtone(G3, quarter)
playtone(B3, sixteenth)
playtone(C4, sixteenth)
playtone(D4, dotted_quarter)
playtone(G3, dotted_quarter)
playtone(Fsharp3, dotted_quarter)
playtone(G3, quarter)
playtone(G3, quarter)
playtone(B3, sixteenth)
playtone(C4, sixteenth)
playtone(D4, dotted_quarter)
playtone(G3, dotted_quarter)
playtone(Fsharp3, dotted_quarter)

print("done")
# Turn off the PWM
quiet()