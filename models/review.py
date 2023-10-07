#!/usr/bin/python3
""" Module containing the class Review """
# Michael 2:00 PM 10/7
import BaseModel


class Review(BaseModel):
    """
    A class called Review with a public attributes.

    Attributes
    ~~~~~~~~~~
        place_id (string):
            ID of place
        user_id (string):
            ID of user
        text (string):
            The review itself
    """
    place_id = ""
    user_id = ""
    text = ""
