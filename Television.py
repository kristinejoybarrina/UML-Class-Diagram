# Create a class 

class Television:
    
    # Create constructor and instance variables
    def __init__(self, name, channel, volume_level, power):
        self.name = str(name)
        self.channel = int(channel)
        self.volume_level = int(volume_level)
        self.power = bool(power)
    
    def show_name (self):
        return "Television " + str(self.name) + "'s"
    
    # Create a turn on method
    def turn_on (self):
        return 
    
    # Create a turn off method
    def turn_off (self):
        return
    
    # Create a get channel method
    def get_channel (self):
        channel_number = self.channel
        return "channel is " + str(channel_number)
    
    # Create a set channel method
    def set_channel (self):
        return 
    
    # Create get volume method
    def get_volume (self):
        volume_number = self.volume_level
        return "volume is " + str(volume_number)
     
    # Create set volume method
    def set_volume (self):
        return
    
    # Create channel up method
    def channel_up (self):
        return
    
    # Create channel down method
    def channel_down (self):
        return
    
    # Create volume up method
    def volume_up (self):
        return
    
    # Create volume down method
    def volume_down (self):
        return
 