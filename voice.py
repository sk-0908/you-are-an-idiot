import pygame

class VoicePlayer:
    def __init__(self, sound_file):
        self.sound_file = sound_file
        # Pygame ミキサーの初期化
        pygame.mixer.init()
        # 音声ファイルのロード
        self.sound = pygame.mixer.Sound(sound_file)
    
    def play_sound(self):
        self.sound.play()
