import base64
import sys
#The returned HTML code does not contain the media's path, instead it contains
#the base64 encoded string. This is done to prevent browser from displaying 
#cached media after the media has been updated.

#returns html code to display video on the browser
def get_video(src, width=480, height=300):
    try:
        video_file = open(src, 'rb')
        binary_data = video_file.read()
    except Exception as e:
        print(e, file=sys.stderr)
        return ''
    video_file.close()
    binary_data = base64.b64encode(binary_data)
    return f"""<br>
    <video width="{width}" height="{height}" autoplay controls>
        <source src="data:video/mp4;base64,{binary_data.decode('ascii')}" type="video/mp4">
    </video>
    """

#returns html code to display image on the browser
def get_image(src, width=480, height=300):
    try:
        image_file = open(src, 'rb')
        binary_data = image_file.read()
    except Exception as e:
        print(e, file=sys.stderr)
        return ''
    image_file.close()
    binary_data = base64.b64encode(binary_data)
    return f'<br><img width="{width}" height="{height}" src="data:image/png;base64,{binary_data.decode("ascii")}">'