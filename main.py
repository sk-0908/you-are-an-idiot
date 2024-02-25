from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QTimer, Qt  # ここでQtもインポート
from voice import VoicePlayer
import random  # VoicePlayerクラスをインポート
import sys

class FunnyWindow(QMainWindow):
    def __init__(self, sound_player):
        super().__init__()
        self.sound_player = sound_player  # VoicePlayerインスタンスを保持
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('YOU ARE AN IDIOT')
        self.setGeometry(100, 100, 240, 120)
        self.move_randomly()

        # QLabelを使用してテキストを表示
        self.label = QLabel('YOU ARE AN IDIOT!!!a ☺☺☺', self)
        self.label.setAlignment(Qt.AlignCenter)  # テキストを中央揃えにする
        self.label.setGeometry(10, 10, 220, 100)  # ラベルの位置とサイズを設定

        # ウィンドウをランダムに動かすタイマーを設定
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_randomly)
        self.timer.start(800)  # 800ミリ秒ごとに更新

    def move_randomly(self):
        self.move(random.randint(0, 800), random.randint(0, 600))
        self.sound_player.play_sound()  # ウィンドウが動くたびに音声を再生

def main():
    app = QApplication(sys.argv)
    sound_player = VoicePlayer('voice.wav')  # 音声ファイルを指定
    ex = FunnyWindow(sound_player)
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
