class Sound:
    CLICK = 0

    def __init__(self, pygame):
        pygame.mixer.music.set_volume(0.8)

        self.sounds = []
        self.sounds.append(pygame.mixer.Sound("sound/filename.mp3"))

    def play(self, num):
        self.sounds[num].play()
