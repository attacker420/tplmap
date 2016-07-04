import unittest
import requests
import os
import sys
import random

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from plugins.engines.velocity import Velocity
from core.channel import Channel

class VelocityTest(unittest.TestCase):
    
    def test_reflection(self):
        
        template = '%s'
        
        channel = Channel({
            'url' : 'http://127.0.0.1:15001/velocity?inj=*'
        })
        Velocity(channel).detect()
        self.assertEqual(channel.data, {
            'reflect_tag': '#set($p=%s)\n$p',
            'language': 'java',
            'engine': 'velocity'
        })

    
    def test_reflection_within_text(self):
        template = 'AAAA%sAAAA'
        
        channel = Channel({
            'url' : 'http://127.0.0.1:15001/velocity?inj=*'
        })
        Velocity(channel).detect()
        self.assertEqual(channel.data, {
            'reflect_tag': '#set($p=%s)\n$p',
            'language': 'java',
            'engine': 'velocity'
        })
        