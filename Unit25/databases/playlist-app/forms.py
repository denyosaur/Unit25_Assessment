'''Forms for playlist app.'''

from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, Optional
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    '''Form for adding playlists.'''
    name = StringField('Playlist Name', validators=[InputRequired(message='Playlist name required.')])
    description = StringField('Description', validators=[Optional()])


class SongForm(FlaskForm):
    '''Form for adding songs.'''
    title = StringField('Song Title', validators=[InputRequired(message='Title required.')])
    artist = StringField('Artist',validators=[InputRequired(message='Artist name required.')])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    '''Form for adding a song to playlist.'''

    song = SelectField('Song To Add', coerce=int)
