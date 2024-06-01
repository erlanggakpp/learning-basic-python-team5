'''
Menyederhanakan Antarmuka Sistem Kompleks:
Mengisolasi Klien dari Subsystem:
Meningkatkan Keterbacaan dan Pemeliharaan Kode:
Menyediakan Titik Masuk Tunggal:
'''
class DVDPlayer:
    def on(self):
        print("DVD Player is on.")
        
    def off(self):
        print("DVD Player is off.")
        
    def play(self, movie):
        print(f"DVD Player is playing '{movie}'.")

class Projector:
    def on(self):
        print("Projector is on.")
        
    def off(self):
        print("Projector is off.")
        
    def wide_screen_mode(self):
        print("Projector is set to wide screen mode.")

class SoundSystem:
    def on(self):
        print("Sound System is on.")
        
    def off(self):
        print("Sound System is off.")
        
    def set_volume(self, level):
        print(f"Sound System volume set to {level}.")

class Lights:
    def dim(self):
        print("Lights are dimmed.")
        
    def on(self):
        print("Lights are on.")

class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system, lights):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system
        self.lights = lights

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.lights.dim()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound_system.on()
        self.sound_system.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)
        
    def end_movie(self):
        print("Shutting movie theater down...")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()
        self.lights.on()


# Create subsystem objects
dvd_player = DVDPlayer()
projector = Projector()
sound_system = SoundSystem()
lights = Lights()

# Create the facade
home_theater = HomeTheaterFacade(dvd_player, projector, sound_system, lights)

# Use the facade to watch a movie
home_theater.watch_movie("Inception")

# Use the facade to end the movie
home_theater.end_movie()