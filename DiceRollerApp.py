from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
import random

class DiceRollerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Create an image widget for the dice
        self.dice_image = Image(source='Dice1.png', size_hint=(1,1))
        
        # Create a label to display the result
        self.result_label = Label(text='Roll the Dice!', font_size=50, size_hint=(1, 0.2))
        
        # Create a button to roll the dice
        self.roll_button = Button(text='Roll', font_size=30, size_hint=(1, 0.2))
        self.roll_button.bind(on_press=self.roll_dice)
        
        # Add the image and label to the layout
        self.layout.add_widget(self.dice_image)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.roll_button)

        return self.layout

    def roll_dice(self, instance):
        # Start flipping the dice through images
        self.current_flip_index = 0
        self.flip_count = 10  # Number of times to flip through the images
        self.roll_result = random.randint(1, 6)  # Final result of the roll
        self.flip_dice(0)  # Start flipping the dice images with a dummy argument

    def flip_dice(self, dt):
        # Flip through the dice images
        if self.current_flip_index < self.flip_count:
            # Cycle through dice images
            self.dice_image.source = f'Dice{random.randint(1, 6)}.png'  # Random image for flipping
            self.dice_image.reload()
            self.current_flip_index += 1
            # Schedule the next flip
            Clock.schedule_once(self.flip_dice, 0.1)  # Change image every 0.1 seconds
        else:
            # Show the final result after flipping
            self.dice_image.source = f'Dice{self.roll_result}.png'  # Show final rolled value
            self.dice_image.reload()
            self.result_label.text = f'You rolled: {self.roll_result}'  # Update the result label

if __name__ == '__main__':
    DiceRollerApp().run()
