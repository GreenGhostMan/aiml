#!/usr/bin/env python
import os
import rospy

from std_msgs.msg import String
from pocketsphinx import LiveSpeech, get_model_path


class GreenHat(object):
    """Class to add keyword spotting functionality"""

    def __init__(self):
        self.pub_ = rospy.Publisher("/chatter", String, queue_size=10)
        rospy.init_node("psa_control")
        

        self.model_path = get_model_path()
        self.speech = LiveSpeech()
        # Call custom function on node shutdown


        """Created by pyae soan aung"""
        self.speech = LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(self.model_path, 'en-us'),
            lm=os.path.join(self.model_path, 'en-us.lm.bin'),
            dic=os.path.join(self.model_path, 'cmudict-en-us.dict')
        )   

        # All params satisfied. Starting recognizer
        self.start_recognizer()

    def start_recognizer(self):
        for phrase in self.speech:
            print(phrase)
            self.pub_.publish(str(phrase))
            self.speech.end_utt()

    def stop_recognizer(self):
        pass
    

if __name__ == "__main__":
    a = GreenHat()
    rospy.spin()
    
