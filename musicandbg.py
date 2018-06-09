import vlc
import time

class Ｍusic:
    def bg(self):
        self.sbg = vlc.MediaPlayer("./music/gai.mp3")
        self.sbg.play()
        time.sleep(1)
        while(True):
            if(self.sbg.is_playing() == 1):
                continue
            else:
                self.bg()

    def gai(self):
        self.sgai = vlc.MediaPlayer("./music/gai.mp3")
        self.sgai.play()
        return self.sgai

    def gai_stop(self):
        self.sgai.stop()

    def tiangi(self):
        self.stiangi = vlc.MediaPlayer("./music/tiangi.mp3")
        self.stiangi.play()
    def tiangi_stop(self):
        self.stiangi.stop()

    def sungoku(self):
        self.ssungoku = vlc.MediaPlayer("./music/sungoku.mp3")
        self.ssungoku.play()
    def ssungoku_stop(self):
        self.ssungoku.stop()

    def ydl(self):
        self.sydl = vlc.MediaPlayer("./music/yodianluan.mp3")
        self.sydl.play()
    def sydl_stop(self):
        self.sydl.stop()

    def thunder(self):
        self.sthunder = vlc.MediaPlayer("./music/thunder.mp3")
        self.sthunder.play()
    def sthunder_stop(self):
        self.sthunder.stop()

