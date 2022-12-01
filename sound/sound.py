class Sound:
    START = 0
    CLICK = 1
    CLICK_BAD = 2
    HELP = 3
    UP_OR_DOWN = 4
    COMPLEXITY = 5
    START_PLAY_GAME = 6

    def __init__(self, pygame):
        pygame.mixer.music.set_volume(0.8)

        self.sounds = []
        self.sounds.append(pygame.mixer.Sound("sound/start.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/click_good.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/click_bad.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/help.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/up_or_down.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/complexity.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/start_play_game.mp3"))

    def play(self, num):
        self.sounds[num].play()
