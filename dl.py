import sys, os
from skillshare import Skillshare
from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print(r"""	 

  ___  ______ ___________    _____ _____ _____ _____  ___  _    _  ___   _   _ 
 / _ \ | ___ \_   _| ___ \  /  ___|  ___|_   _|_   _|/ _ \| |  | |/ _ \ | \ | |
/ /_\ \| |_/ / | | | |_/ /  \ `--.| |__   | |   | | / /_\ \ |  | / /_\ \|  \| |
|  _  ||    /  | | |  __/    `--. \  __|  | |   | | |  _  | |/\| |  _  || . ` |
| | | || |\ \ _| |_| |      /\__/ / |___  | |  _| |_| | | \  /\  / | | || |\  |
\_| |_/\_| \_|\___/\_|      \____/\____/  \_/  \___/\_| |_/\/  \/\_| |_/\_| \_/
                                                                               
                                                                               
                                                                                                                                                                    


				Visit Us for more Cool Stuff: https://thetechrim.com/

                """)


if __name__ == "__main__":
    info()
    main()
