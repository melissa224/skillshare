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


   _____        .__           _________       __  .__                              
  /  _  \_______|__|_____    /   _____/ _____/  |_|__|____ __  _  _______    ____  
 /  /_\  \_  __ \  \____ \   \_____  \_/ __ \   __\  \__  \\ \/ \/ /\__  \  /    \ 
/    |    \  | \/  |  |_> >  /        \  ___/|  | |  |/ __ \\     /  / __ \|   |  \
\____|__  /__|  |__|   __/  /_______  /\___  >__| |__(____  /\/\_/  (____  /___|  /
        \/         |__|             \/     \/             \/             \/     \/ 
                                                                                                                                                                    


				Stay at Home     Contact me @MrTamvan

                """)


if __name__ == "__main__":
    info()
    main()