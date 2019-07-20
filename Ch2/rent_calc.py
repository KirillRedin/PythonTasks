"""
Program: rent_calc.py
Author: Kirill Redin
Last modified: 10.11.2018
This program calculate the total charge for a customer's video rentals

Pseudocode:
new video amount = Input amount of new videos
old video amount = Input amount of old videos
total cost = new video amount * 3 + old video amount * 2
print total cost
"""

NEW_VIDEO_COST = 3
OLD_VIDEO_COST = 2

new_video_amount = int(input("Enter amount of new videos: "))
old_video_amount = int(input("Enter amount of old videos: "))
total_cost = new_video_amount * NEW_VIDEO_COST + \
             old_video_amount * OLD_VIDEO_COST
print("The total cost is:", total_cost)
