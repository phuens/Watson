import re
import os


def main():
    entries = os.listdir('./img/images')
    for item in entries:
        image = os.path.join('./img/images', item)  # path for the images
        name, extension = os.path.splitext(image)
        if (extension == '.jpeg' or extension == '.jpg' or extension == '.png' or extension == '.JPG' or extension == '.jpeg'):
            print(
                "<div class='col-md-3 col-sm-6' style='padding:0'>\
                    <div class='portfolio-item'>\
                        <a href='{0}' data-lightbox='image-1'>\
                            <div class='thumb' style='height: 300px'>\
                                <div class='hover-effect'>\
                                    <div class='hover-content'>\
                                        <h1>Biodiesel</h1>\
                                        <p>Awesome</p>\
                                    </div>\
                                </div>\
                                <div class='image'>\
                                    <img src='{0}'>\
                                </div>\
                            </div>\
                        </a>\
                    </div>\
                </div>".format(image)
            )


if __name__ == '__main__':
    main()
